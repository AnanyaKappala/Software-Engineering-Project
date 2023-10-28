from PIL import Image, ImageFilter

# Open an image
img = Image.open("/COLLEGE/SE/Group activity 02/dog.jpg")

# Apply median filter with a larger size
smoothed_img = img.filter(ImageFilter.MedianFilter(size=9))

# Apply the filter multiple times for stronger smoothing
for _ in range(5):
    smoothed_img = smoothed_img.filter(ImageFilter.MedianFilter(size=9))

# Save the smoothed image
smoothed_img.save("/COLLEGE/SE/Group activity 02/smoothed_dog2.png")