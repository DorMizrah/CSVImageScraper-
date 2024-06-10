# CSVImageScraper

CSVImageScraper is a Python project designed to automate the downloading of images from URLs listed in a CSV file. This project leverages Google Drive to store the CSV files and downloads images to a specified local directory.

## Features

- Mounts Google Drive to access CSV files.
- Downloads CSV files from Google Drive.
- Reads URLs from the CSV file and downloads the images.
- Allows limiting the number of images to download and display.
- Organizes downloaded images into a structured folder hierarchy.

## Installation

1. **Mount Google Drive:**

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. **Install Required Libraries:**

!pip install pandas requests gdown

3. **Clone the Repository:**

git clone https://github.com/yourusername/CSVImageScraper.git
cd CSVImageScraper
```

