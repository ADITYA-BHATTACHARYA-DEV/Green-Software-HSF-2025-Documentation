import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import psutil
from codecarbon import EmissionsTracker

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Constants for Sustainability Computation Index (SCI) calculation
I = 0.4  # Marginal carbon emissions factor (kg CO₂/kWh), can vary based on location
M = 10   # Embodied emissions per functional unit (kg CO₂), represents manufacturing cost
R = 1    # Functional unit (e.g., one processed image)

def get_system_usage():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "ram_used": round(psutil.virtual_memory().used / (1024 ** 3), 2),
    }


tracker = EmissionsTracker(output_dir=log_dir, output_file="carbon_emission.csv")
tracker.start()

print("Processing image...")
image = np.ones((512, 512, 3), dtype=np.uint8) * 255
start_time = time.time()
system_usage_before = get_system_usage()

blurred = cv2.GaussianBlur(image, (5, 5), 0)
edges = cv2.Canny(blurred, 100, 200)

end_time = time.time()
system_usage_after = get_system_usage()
tracker.stop()

log_file = os.path.join(log_dir, "carbon_emission.csv")
if os.path.exists(log_file):
    df = pd.read_csv(log_file)
    energy_consumed = df["energy_consumed"].iloc[-1] if "energy_consumed" in df.columns else 0
    emissions = df["emissions"].iloc[-1] if "emissions" in df.columns else 0
else:
    energy_consumed = 0
    emissions = 0

SCI = ((energy_consumed * I) + M) / R

data = {
    "Metric": ["Energy Consumed (kWh)", "Carbon Emissions (kg CO₂)", "SCI Score", "Memory Usage (%)", "RAM Used (GB)"],
    "Value": [energy_consumed, emissions, SCI, system_usage_after["memory"], system_usage_after["ram_used"]],
}
df_metrics = pd.DataFrame(data)


def plot_graphs():
    sns.set(style="darkgrid")

    plt.figure(figsize=(10, 5))
    sns.barplot(x=df_metrics["Metric"], y=df_metrics["Value"], palette="coolwarm")
    plt.title("Carbon Footprint & Energy Consumption")
    plt.ylabel("Value")
    plt.xticks(rotation=30)
    plt.show()

    plt.figure(figsize=(10, 5))
    time_series = [system_usage_before["memory"], system_usage_after["memory"]]
    plt.plot(["Before Processing", "After Processing"], time_series, marker="o", linestyle="-", color="blue")
    plt.title("Memory Usage Over Time")
    plt.xlabel("Stage")
    plt.ylabel("Memory Usage (%)")
    plt.show()


plot_graphs()

df_metrics.to_csv(os.path.join(log_dir, "sci_results.csv"), index=False)
print("Results saved to sci_results.csv")
