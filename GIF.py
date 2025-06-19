from PIL import Image
import os

# Image file list (make sure these images exist in the same folder)
image_files = ["img1.png", "img2.png", "img3.png", "img4.png", "img5.png"]

# Open all images and convert to RGB
images = [Image.open(img).convert("RGB") for img in image_files]

# Resize all images to the size of the first one
base_size = images[0].size
images = [img.resize(base_size) for img in images]

# Save as GIF
images[0].save(
    'output.gif',
    save_all=True,
    append_images=images[1:],
    duration=500,  # milliseconds
    loop=0         # infinite loop
)

print("GIF created successfully!")
