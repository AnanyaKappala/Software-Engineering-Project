import cv2
from skimage import morphology
from skimage import io
import numpy as np

# Load the binary character image (make sure it's binary)
character_binary = io.imread("/COLLEGE/SE/Group activity 02/binary_smoothed_dog1.jpg")

# Perform skeletonization using skimage
skeleton = morphology.skeletonize(character_binary)

# Resize the skeleton image to 64x64 pixels
resized_skeleton = cv2.resize((skeleton * 255).astype(np.uint8), (64, 64))

# Save the thinned and resized image
cv2.imwrite("/COLLEGE/SE/Group activity 02/thinned_binary_smoothed_dog1.jpg", resized_skeleton)