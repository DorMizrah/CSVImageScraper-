# Step 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Step 2: Install required libraries
!pip install pandas requests gdown

# Step 3: Define the necessary code
import os
import pandas as pd
import requests
import gdown

# CHANGE THESE VARIABLES FOR EACH NEW CSV FILE
csv_file_id = ''  # Google Drive file ID of the CSV
csv_file_name = ''  # Desired name for the CSV file without .csv extension
max_images = 400  # Maximum number of images to download and display

# Define local paths
main_folder_path = '/content/drive/My Drive/Images'
csv_file_path = f'/content/{csv_file_name}.csv'

# Create the main folder if it doesn't exist
os.makedirs(main_folder_path, exist_ok=True)

# Download the CSV file from Google Drive using gdown
gdown.download(f'https://drive.google.com/uc?id={csv_file_id}', csv_file_path, quiet=False)

# Load the CSV file
data = pd.read_csv(csv_file_path)

# Create a subfolder within the main folder using the CSV file name (without extension)
subfolder_path = os.path.join(main_folder_path, csv_file_name)
os.makedirs(subfolder_path, exist_ok=True)

# Function to download an image from a URL
def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_path}")
    else:
        print(f"Failed to download {url}")

# Download images for a limited number of rows in the CSV file
for idx, row in data.head(max_images).iterrows():
    image_url = row['image_url']
    file_name = f"image_{idx+1}.jpg"
    file_path = os.path.join(subfolder_path, file_name)
    download_image(image_url, file_path)

# Verify if the images have been downloaded
!ls "{subfolder_path}"

# Display the images directly in the notebook (optional)
from IPython.display import Image, display

# Display all downloaded images
for idx in range(min(len(data), max_images)):
    image_path = os.path.join(subfolder_path, f"image_{idx+1}.jpg")
    display(Image(filename=image_path))
