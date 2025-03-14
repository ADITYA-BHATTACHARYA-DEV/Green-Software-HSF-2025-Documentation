## Energy Profiling of Image Processing Using CodeCarbon

## 📌 Overview
This project tracks the energy consumption of an image processing task using **CodeCarbon**, an open-source tool that estimates the carbon footprint of computational workloads. It utilizes **OpenCV** for image processing and performs various operations, including grayscale conversion, edge detection, Gaussian blur, and image rotation.

By monitoring energy usage and carbon emissions, this project helps in understanding the environmental impact of computationally expensive tasks such as AI/ML workloads and image processing.

---

![dd1a3c80-258e-11eb-89dd-87fd3e35039c](https://github.com/user-attachments/assets/fd5ab1bc-a473-47a1-8f2d-f8de93a791c5)
![1_FTw5KFD6ApDigX1J1i4KhA](https://github.com/user-attachments/assets/57539772-34b4-4c49-b449-9d72bfe10e81)


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

## Experiment Results
<br>
## Experiment Results

| Timestamp           | Project Name | Run-ID                                  | Duration (s) | Emissions (kgCO₂eq) | Emissions-Rate (kgCO₂eq/s) | CPU Power (W) | GPU Power (W) | RAM Power (W) | CPU Energy (kWh) | GPU Energy (kWh) | RAM Energy (kWh) | Energy Consumed (kWh) | Country | Country Code | Region | Cloud Provider | Cloud Region | OS | Python Version | CodeCarbon Version | CPU Count | CPU Model | GPU Count | GPU Model | Longitude | Latitude | RAM Total Size (GB) | Tracking Mode | On Cloud | PUE |
|---------------------|-------------|-----------------------------------------|-------------|---------------------|--------------------------|--------------|--------------|--------------|----------------|----------------|----------------|-------------------|---------|--------------|--------|---------------|--------------|----|---------------|----------------|----------|------------|----------|------------|-----------|----------|------------------|--------------|---------|-----|
| 2024-04-13T21:30:53 | 3CABTP      | 2012a217-6530-46c0-b1d2-9c3929fb2397   | 1.325967073 | 1.57E-07            | 1.18E-07                 | 12.5         | 0            | 2.766779423  | 4.60E-06       | 0              | 1.02E-06       | 5.61E-06          | France  | FRA          |         |               |              | Linux | 3.11.7          | 2.3.4              | 4        | Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz | 0        | -          | 2.3387    | 48.8582  | 7.38               | Machine       | N       | 1   |
| 2024-04-13T21:31:07 | 3CABTP      | 2012a217-6530-46c0-b1d2-9c3929fb2397   | 16.53349209 | 1.96E-06            | 1.19E-07                 | 12.5         | 0            | 2.766779423  | 5.74E-05       | 0              | 1.27E-05       | 7.01E-05          | France  | FRA          |         |               |              | Linux | 3.11.7          | 2.3.4              | 4        | Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz | 0        | -          | 2.3387    | 48.8582  | 7.38               | Machine       | N       | 1   |
| 2024-04-13T23:33:37 | 3CABTP      | 196f76fc-97c7-41a6-abb5-350b0e058284   | 0.76100421  | 6.41E-08            | 8.42E-08                 | 12.5         | 0            | 2.766779423  | 2.63E-06       | 0              | 5.79E-07       | 3.21E-06          | France  | FRA          |         |               |              | Linux | 3.11.7          | 2.3.4              | 4        | Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz | 0        | -          | 2.3387    | 48.8582  | 7.38               | Machine       | N       | 1   |
| 2024-04-13T23:34:33 | 3CABTP      | 196f76fc-97c7-41a6-abb5-350b0e058284   | 56.58539414 | 4.80E-06            | 8.48E-08                 | 12.5         | 0            | 2.766779423  | 0.000196449    | 0              | 4.35E-05       | 0.000239927       | France  | FRA          |         |               |              | Linux | 3.11.7          | 2.3.4              | 4        | Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz | 0        | -          | 2.3387    | 48.8582  | 7.38               | Machine       | N       | 1   |
| 2024-04-13T23:34:40 | 3CABTP      | 196f76fc-97c7-41a6-abb5-350b0e058284   | 64.24245167 | 5.45E-06            | 8.48E-08                 | 12.5         | 0            | 2.766779423  | 0.000223029    | 0              | 4.94E-05       | 0.00027239        | France  | FRA          |         |               |              | Linux | 3.11.7          | 2.3.4              | 4        | Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz | 0        | -          | 2.3387    | 48.8582  | 7.38               | Machine       | N       | 1   |
| 2024-04-14T09:29:18 | 3CABTP      | 6188e52e-6489-41f4-8f19-235b7b07448a   | 3.809264421 | 1.20E-06            | 3.15E-07                 | 42.5         | 0            | 2.948155403  | 4.49E-05       | 0              | 3.12E-06       | 4.80E-05          | France  | FRA          |         |               |              | Windows 10 | 3.11.8          | 2.3.5              | 4        | Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz | 0        | -          | 2.3387    | 48.8582  | 7.86               | Machine       | N       | 1   |
| 2024-04-14T09:49:48 | 3CABTP      | db7c84ce-400c-487d-978a-8ecf0e3de370   | 41.18640709 | 4.40E-05            | 1.07E-06                 | 42.5         | 0            | 2.948155403  | 0.000485079    | 0              | 3.36E-05       | 0.00051866        | France  | FRA          |         |               |              | Windows 10 | 3.11.8          | 2.3.5              | 4        | Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz | 0        | -          | 2.3387    | 48.8582  | 7.86               | Machine       | N       | 1   |
| 2024-04-14T11:01:17 | 3CABTP      | e1798a45-8078-41ff-a654-2ae084fd66ad   | 4.649629116 | 1.33E-06            | 2.86E-07                 | 12.5         | 0            | 2.766777992  | 1.61E-05       | 0              | 3.57E-06       | 1.97E-05          | France  | FRA          |         |               |              | Linux | 3.11.7          | 2.3.4              | 4        | Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz | 0        | -          | 2.3387    | 48.8582  | 7.38               | Machine       | N       | 1   |




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

