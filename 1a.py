''' What do you mean by image filtering? Apply two different filtering techniques to make smoother the given 
character images using any suitable programs (like using Python, java, etc).
'''
from PIL import Image, ImageFilter

# Open an image
img = Image.open("/COLLEGE/SE/Group activity 02/dog.jpg")

# Apply Gaussian blur with a larger radius
smoothed_img = img.filter(ImageFilter.GaussianBlur(radius=10))

# Apply the filter multiple times for stronger smoothing
for _ in range(5):
    smoothed_img = smoothed_img.filter(ImageFilter.GaussianBlur(radius=10))

# Save the smoothed image
smoothed_img.save("/COLLEGE/SE/Group activity 02/smoothed_dog1.jpg")
