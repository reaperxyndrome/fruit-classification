from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = Image.open('testfile.jpg')

# Get pixel data
pixels = np.array(image)

# Save pixel data to a .npy file
np.save('output.npy', pixels)

# Load pixel data from .npy file
data = np.load('output.npy')

# Display the image
plt.imshow(data)
plt.show()