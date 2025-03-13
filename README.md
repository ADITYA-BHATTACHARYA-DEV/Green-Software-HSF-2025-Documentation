## Energy Profiling of Image Processing Using CodeCarbon

## 📌 Overview
This project tracks the energy consumption of an image processing task using **CodeCarbon**, an open-source tool that estimates the carbon footprint of computational workloads. It utilizes **OpenCV** for image processing and performs various operations, including grayscale conversion, edge detection, Gaussian blur, and image rotation.

By monitoring energy usage and carbon emissions, this project helps in understanding the environmental impact of computationally expensive tasks such as AI/ML workloads and image processing.

---

## 🛠 Installation Guide

### 🔹 Prerequisites
Before running the project, ensure that you have the following dependencies installed:

- Python 3.7 or later
- pip (Python package manager)

### 🔹 Step-by-Step Installation

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/ADITYA-BHATTACHARYA-DEV/Green-Software-HSF-2025-Documentation.git
cd Green-Software-HSF-2025-Documentation
```

2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```bash
 python -m venv env
 source env/bin/activate  # On macOS/Linux
 env\Scripts\activate  # On Windows
```

3️⃣ **Install Required Dependencies**
```bash
pip install codecarbon opencv-python numpy

```

4️⃣ **Verify Installation**
```bash
 python CodeCarbon-Emission_Results.py  # Run the script
python Results-Visualizer.py
python SCI-Score -predictor.py
```
If everything is set up correctly, the script will begin execution and log energy usage in `carbon_emissions.csv`.

---

## ⚙️ How the Code Functions

### 🔸 **1. Importing Required Libraries**
The script starts by importing essential libraries:
- **CodeCarbon** to track energy consumption.
- **OpenCV (cv2)** for image processing.
- **NumPy** for handling arrays.
- **Time** for performance measurement.

### 🔸 **2. Initializing the Energy Tracker**
The **EmissionsTracker** is initialized, and tracking begins. This step ensures that energy usage is monitored from the very start of computations.
```python
 tracker = EmissionsTracker(output_file="carbon_emissions.csv")
 tracker.start()
```

### 🔸 **3. Loading and Preprocessing an Image**
The script reads an image (`Tom_Cruise.jpg`) and checks if it exists before proceeding.
```python
 image = cv2.imread("Tom_Cruise.jpg")
 if image is None:
     print("Error: Image not found!")
     exit()
```

### 🔸 **4. Performing Image Processing Tasks**
Several operations are applied:
- **Convert Image to Grayscale**: Reduces computational complexity.
- **Apply Canny Edge Detection**: Detects image edges.
- **Gaussian Blur and Rotation**: Simulate a heavy computational workload.

### 🔸 **5. Measuring Computational Impact**
After the image processing steps, CodeCarbon measures energy usage:
- **Monitors CPU, GPU, and RAM power consumption**.
- **Calculates total energy consumed in kWh**.
- **Estimates carbon emissions based on regional energy sources**.

### 🔸 **6. Logging and Stopping the Tracker**
At the end of execution, CodeCarbon stops tracking and logs the results in `carbon_emissions.csv`.
```python
 tracker.stop()
```

### 🔸 **7. Generating Reports and Visualizations (Optional)**
Users can analyze the `carbon_emissions.csv` file to visualize energy consumption trends.

---

## 📊 Expected Output
The script provides the following outputs:
✅ Image processing results (Grayscale & Edge Detection output images)
✅ CSV log containing:
- Energy consumption (kWh)
- Carbon emissions (kg CO₂)
- Hardware resource usage details



![download (1)](https://github.com/user-attachments/assets/e0ececc2-9440-4cfd-9ef2-ca984f1ddd72)
![download (2)](https://github.com/user-attachments/assets/62aa3064-9584-4bd5-8ded-8e8451e61dac)
![download (3)](https://github.com/user-attachments/assets/dc1bb6f0-868a-41c5-b152-5100020684dd)



## 📝 Conclusion

This project demonstrates how **CodeCarbon** can be integrated into an image processing pipeline to track energy usage and carbon emissions. By quantifying energy consumption, developers and researchers can optimize computations for better efficiency and sustainability. This approach can also be extended to deep learning and other high-performance computing tasks to promote **green AI** and **environmentally responsible computing**.

---

## 🤝 Detailed WorkBook
https://docs.google.com/document/d/1o3cYma2p-Uoemh5izaklWVyc_gOo6Z0QJTaGIBlEArM/edit?usp=sharing

---

## 📧 Contact
For any queries or suggestions, contact:
📩 Email: adityabhattacharya3002@gmail.com  
📌 GitHub: [ADITYA BHATTACHARYA:- ]([https://github.com/ADITYA-BHATTACHARYA-DEV])(https://github.com/ADITYA-BHATTACHARYA-DEV)

