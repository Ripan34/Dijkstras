import cv2
import os

# Path to the directory containing your images
image_dir = 'pics'

# Output video file name
output_video = 'output_video.mp4'

# Slow down the video by reducing the frame rate
frame_rate = 3  # Adjust this value for the desired playback speed

# Get the list of image files in the directory
image_files = [f for f in os.listdir(image_dir) if f.startswith('pic') and f.endswith(('.jpg', '.jpeg', '.png'))]

# Sort the image files by extracting the numeric part and sorting numerically
image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

# Check if any images were found
if not image_files:
    print("No image files found in the directory.")
    exit()

# Get the first image to determine the size of the frames
first_image = cv2.imread(os.path.join(image_dir, image_files[0]))
frame_height, frame_width, _ = first_image.shape

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
out = cv2.VideoWriter(output_video, fourcc, frame_rate, (frame_width, frame_height))

# Iterate through the images and write each frame to the video
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    frame = cv2.imread(image_path)
    out.write(frame)

# Release the VideoWriter
out.release()

print(f"Video '{output_video}' created successfully.")
