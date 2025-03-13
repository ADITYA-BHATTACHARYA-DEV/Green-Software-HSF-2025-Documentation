[model.csv](https://github.com/user-attachments/files/19237034/model.csv)# Energy Profiling of Image Processing Using CodeCarbon

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

[Uploading model.cstimestamp,project_name,run_id,duration,emissions,emissions_rate,cpu_power,gpu_power,ram_power,cpu_energy,gpu_energy,ram_energy,energy_consumed,country_name,country_iso_code,region,cloud_provider,cloud_region,os,python_version,codecarbon_version,cpu_count,cpu_model,gpu_count,gpu_model,longitude,latitude,ram_total_size,tracking_mode,on_cloud,pue
2024-04-13T21:30:53,3CABTP,2012a217-6530-46c0-b1d2-9c3929fb2397,1.3259670734405518,1.5712467392432068e-07,1.1849817169035849e-07,12.5,0.0,2.7667794227600098,4.5959485901726615e-06,0,1.0156469071245054e-06,5.611595497297167e-06,France,FRA,,,,Linux-6.5.0-27-generic-x86_64-with-glibc2.38,3.11.7,2.3.4,4,Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz,,,2.3387,48.8582,7.378078460693359,machine,N,1.0
2024-04-13T21:31:07,3CABTP,2012a217-6530-46c0-b1d2-9c3929fb2397,16.53349208831787,1.962148159665233e-06,1.186771765567685e-07,12.5,0.0,2.7667794227600098,5.737896925873227e-05,0,1.2697750729311772e-05,7.007671998804404e-05,France,FRA,,,,Linux-6.5.0-27-generic-x86_64-with-glibc2.38,3.11.7,2.3.4,4,Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz,,,2.3387,48.8582,7.378078460693359,machine,N,1.0
2024-04-13T23:33:37,3CABTP,196f76fc-97c7-41a6-abb5-350b0e058284,0.7610042095184326,6.41139075801195e-08,8.424908401057481e-08,12.5,0.0,2.7667794227600098,2.6264281736479865e-06,0,5.792672053579887e-07,3.205695379005976e-06,France,FRA,,,,Linux-6.5.0-27-generic-x86_64-with-glibc2.38,3.11.7,2.3.4,4,Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz,,,2.3387,48.8582,7.378078460693359,machine,N,1.0
2024-04-13T23:34:33,3CABTP,196f76fc-97c7-41a6-abb5-350b0e058284,56.58539414405823,4.798543032859275e-06,8.480179568322665e-08,12.5,0.0,2.7667794227600098,0.0001964487127131,0,4.347843892977513e-05,0.0002399271516429,France,FRA,,,,Linux-6.5.0-27-generic-x86_64-with-glibc2.38,3.11.7,2.3.4,4,Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz,,,2.3387,48.8582,7.378078460693359,machine,N,1.0
2024-04-13T23:34:40,3CABTP,196f76fc-97c7-41a6-abb5-350b0e058284,64.24245166778564,5.4477924356356656e-06,8.480050642848456e-08,12.5,0.0,2.7667794227600098,0.0002230292881528,0,4.936033362892961e-05,0.0002723896217817,France,FRA,,,,Linux-6.5.0-27-generic-x86_64-with-glibc2.38,3.11.7,2.3.4,4,Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz,,,2.3387,48.8582,7.378078460693359,machine,N,1.0
2024-04-14T09:29:18,3CABTP,6188e52e-6489-41f4-8f19-235b7b07448a,3.8092644214630127,1.2012218521679646e-06,3.153422076450694e-07,42.5,0.0,2.9481554031372075,4.493276062938903e-05,0,3.1161134573295616e-06,4.8048874086718585e-05,France,FRA,,,,Windows-10-10.0.22631-SP0,3.11.8,2.3.5,4,Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz,,,2.3387,48.8582,7.861747741699219,machine,N,1.0
2024-04-14T09:49:48,3CABTP,db7c84ce-400c-487d-978a-8ecf0e3de370,41.1864070892334,4.402333538952775e-05,1.068880208320865e-06,42.5,0.0,2.9481554031372075,0.0004850785283578,0,3.358139211158857e-05,0.0005186599204694,France,FRA,,,,Windows-10-10.0.22631-SP0,3.11.8,2.3.5,4,Intel(R) Core(TM) i5-7300U CPU @ 2.60GHz,,,2.3387,48.8582,7.861747741699219,machine,N,1.0
2024-04-14T11:01:17,3CABTP,e1798a45-8078-41ff-a654-2ae084fd66ad,4.64962911605835,1.328087053669917e-06,2.856329011454105e-07,12.5,0.0,2.766777992248535,1.6136765480041505e-05,0,3.5707141707956684e-06,1.9707479650837172e-05,France,FRA,,,,Linux-6.5.0-27-generic-x86_64-with-glibc2.38,3.11.7,2.3.4,4,Intel(R) Core(TM) i3-10110U CPU @ 2.10GHz,,,2.3387,48.8582,7.378074645996094,machine,N,1.0
v…]()


## 📝 Conclusion

This project demonstrates how **CodeCarbon** can be integrated into an image processing pipeline to track energy usage and carbon emissions. By quantifying energy consumption, developers and researchers can optimize computations for better efficiency and sustainability. This approach can also be extended to deep learning and other high-performance computing tasks to promote **green AI** and **environmentally responsible computing**.

---

## 🤝 Detailed WorkBook
https://docs.google.com/document/d/1o3cYma2p-Uoemh5izaklWVyc_gOo6Z0QJTaGIBlEArM/edit?usp=sharing

---

## 📧 Contact
For any queries or suggestions, contact:
📩 Email: adityabhattacharya3002@gmail.com  
📌 GitHub: [Your GitHub Profile]([https://github.com/your-profile](https://github.com/ADITYA-BHATTACHARYA-DEV))

