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

```!pip install pandas requests gdown```

3. **Clone the Repository:**
```
git clone https://github.com/yourusername/CSVImageScraper.git
cd CSVImageScraper
```

## Usage
      
1. **Set Up Variables:**
Change the variables for each new CSV file:

```
csv_file_id = 'your_csv_file_id'  # Google Drive file ID of the CSV
csv_file_name = 'your_csv_file_name'  # Desired name for the CSV file without .csv extension
max_images = 10  # Maximum number of images to download and display
```

2. **Run the Script:**


       
