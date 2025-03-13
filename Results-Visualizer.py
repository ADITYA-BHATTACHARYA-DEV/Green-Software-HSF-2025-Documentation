import os
import cv2
import time
import psutil
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from codecarbon import EmissionsTracker

# For Removing CodeCarbon lock file if it exists to prevent potential errors
lock_file = "/tmp/.codecarbon.lock"
if os.path.exists(lock_file):
    os.remove(lock_file)


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# CodeCarbon initializes
tracker = EmissionsTracker(
    output_dir=log_dir,
    output_file="carbon_emission.csv",
    measure_power_secs=1,
    tracking_mode="process",
    allow_multiple_runs=True
)

# Creating a dummy grayscale image for processing
image = np.ones((512, 512, 3), dtype=np.uint8) * 255
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Function to retrieve CPU and memory usage before and after processing
def get_system_usage():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
    }


# Function to process an image with either low or high efficiency
def process_image(image, efficiency="low"):
    start_time = time.time()
    system_usage_before = get_system_usage()
    height, width = image.shape[:2]

    if efficiency == "low":
        for _ in range(200):
            blurred = cv2.GaussianBlur(image, (5, 5), 0)
            rotated = cv2.rotate(blurred, cv2.ROTATE_90_CLOCKWISE)
            rotated = cv2.resize(rotated, (width, height))
            if len(blurred.shape) == 2:
                blurred = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
                rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
            blended = cv2.addWeighted(blurred, 0.5, rotated, 0.5, 0)
    else:
        blurred = cv2.GaussianBlur(image, (5, 5), 0)
        edges = cv2.Canny(blurred, 100, 200)

    end_time = time.time()
    system_usage_after = get_system_usage()

    return {
        "time": round(end_time - start_time, 4),
        "cpu_before": system_usage_before["cpu"],
        "cpu_after": system_usage_after["cpu"],
        "memory_before": system_usage_before["memory"],
        "memory_after": system_usage_after["memory"],
    }


# Codecarbon Initializes tracking
print("Starting energy tracking...")
tracker.start()


print("Processing image using low efficiency...")
low_efficiency_metrics = process_image(gray_image, "low")

print("Processing image using high efficiency...")
high_efficiency_metrics = process_image(gray_image, "high")

# haults after processing
tracker.stop()
print("Energy tracking stopped.")

# Load CodeCarbon log file data extraction
log_file_path = os.path.join(log_dir, "carbon_emission.csv")
if os.path.exists(log_file_path):
    df = pd.read_csv(log_file_path)
    energy_consumed = df["energy_consumed"].iloc[-1] if "energy_consumed" in df.columns else 0
    emissions = df["emissions"].iloc[-1] if "emissions" in df.columns else 0
    cpu_power = df.get("cpu_power", pd.Series([None])).iloc[-1]
    gpu_power = df.get("gpu_power", pd.Series([None])).iloc[-1]
    ram_power = df.get("ram_power", pd.Series([None])).iloc[-1]
else:
    print("No CodeCarbon log file found.")
    energy_consumed = emissions = cpu_power = gpu_power = ram_power = None

# Estimating energy loss assuming 85% efficiency
energy_lost = energy_consumed * 0.15 if energy_consumed else 0

print("\nEnergy & Performance Metrics:")
print(f"Energy Consumed: {energy_consumed:.5f} kWh")
print(f"Carbon Emissions: {emissions:.5f} kg CO₂")
print(f"Estimated Energy Lost: {energy_lost:.5f} kWh")
print(f"Processing Time - High Efficiency: {high_efficiency_metrics['time']} sec")
print(f"Processing Time - Low Efficiency: {low_efficiency_metrics['time']} sec")


sns.set(style="darkgrid")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Energy Consumption & Subsequent Emissions Plotting
axes[0, 0].bar(["Emissions (kg CO₂)", "Energy Consumed (kWh)", "Energy Lost (kWh)"],
               [emissions, energy_consumed, energy_lost], color=["blue", "purple", "red"])
axes[0, 0].set_title("Carbon Footprint & Energy Consumption")
axes[0, 0].set_ylabel("Value")
axes[0, 0].tick_params(axis='x', rotation=20)

# CPU Usage Processing Before & After Plotting
cpu_usage = [low_efficiency_metrics["cpu_before"], low_efficiency_metrics["cpu_after"],
             high_efficiency_metrics["cpu_before"], high_efficiency_metrics["cpu_after"]]
labels = ["Low Eff Before", "Low Eff After", "High Eff Before", "High Eff After"]
axes[0, 1].bar(labels, cpu_usage, color=["gray", "black", "green", "orange"])
axes[0, 1].set_title("CPU Usage Before & After")
axes[0, 1].set_ylabel("CPU %")

# Memory Usage Processing Before and After Plotting
memory_usage = [low_efficiency_metrics["memory_before"], low_efficiency_metrics["memory_after"],
                high_efficiency_metrics["memory_before"], high_efficiency_metrics["memory_after"]]
axes[1, 0].bar(labels, memory_usage, color=["gray", "black", "blue", "purple"])
axes[1, 0].set_title("Memory Usage Before & After")
axes[1, 0].set_ylabel("Memory %")

# Processing time Comparison Plotting
axes[1, 1].bar(["Low Efficiency", "High Efficiency"],
               [low_efficiency_metrics["time"], high_efficiency_metrics["time"]],
               color=["red", "green"])
axes[1, 1].set_title("Processing Time Comparison")
axes[1, 1].set_ylabel("Time (seconds)")

# The Generated Plots are displayed
plt.tight_layout()
plt.show()
