from codecarbon import EmissionsTracker
import cv2
import numpy as np
import time


tracker =EmissionsTracker( output_file="carbon_emissions.csv")
tracker.start()


print("Loading Image.....")

image =cv2.imread("Tom_Cruise.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

print("Converting to grayscale.....")
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Applying Canny edge detection..")

edges =cv2.Canny(gray_image,100,200)

print("Running workload...")

for _ in range(100):
    blurred =cv2.GaussianBlur(edges, (5,5), 0)
    rotated =cv2.rotate(blurred, cv2.ROTATE_90_CLOCKWISE)

    if blurred.shape == rotated.shape:
        blended=cv2.addWeighted(blurred, 0.5, rotated, 0.5,0)

    else:
        print("Error: Image shapes do not match for addWeighted")


tracker.stop()

print("Profiling complete! Check logs for energy usage")