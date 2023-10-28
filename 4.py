import cv2
import pandas as pd

# Load the thinned character image (64x64 binary)
thinned_character = cv2.imread("/COLLEGE/SE/Group activity 02/thinned_binary_smoothed_dog1.jpg", cv2.IMREAD_GRAYSCALE)

# Convert the thinned character to a Pandas DataFrame
df = pd.DataFrame(thinned_character)

# Save the DataFrame to an Excel file
df.to_excel("/COLLEGE/SE/Group activity 02/thinned_character_intensity.xlsx", index=False, header=False)