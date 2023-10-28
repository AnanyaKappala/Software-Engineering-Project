'''
Differentiate between gray scale image and binary image. Convert the output images of Q1 into its corresponding 
binary images and then resize to 64x64 pixels using any suitable programs.
'''
from PIL import Image

# Open the previously smoothed images
smoothed_gaussian = Image.open("/COLLEGE/SE/Group activity 02/smoothed_dog1.jpg")
smoothed_median = Image.open("/COLLEGE/SE/Group activity 02/smoothed_dog2.png")

# Convert to grayscale
smoothed_gaussian_gray = smoothed_gaussian.convert("L")
smoothed_median_gray = smoothed_median.convert("L")

# Convert to binary using a threshold (128 in this example)
threshold = 128
smoothed_gaussian_binary = smoothed_gaussian_gray.point(lambda p: p > threshold and 255)
smoothed_median_binary = smoothed_median_gray.point(lambda p: p > threshold and 255)

# Resize to 64x64 pixels
resized_gaussian_binary = smoothed_gaussian_binary.resize((64, 64))
resized_median_binary = smoothed_median_binary.resize((64, 64))

# Save the binary and resized images
resized_gaussian_binary.save("binary_smoothed_dog1.jpg")
resized_median_binary.save("binary_smoothed_dog2.jpg")
