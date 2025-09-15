# **Product Feature Extraction from Images**

## **Project Overview**

This project aims to automate the extraction of product features, specifically **dimensions** and **units**, directly from product images. It leverages Optical Character Recognition (OCR) to convert text embedded in images into machine-readable format. Subsequently, custom natural language processing (NLP) rules are applied to identify, parse, and normalize relevant numerical values and their corresponding units.

This pipeline is designed to be modular and scalable, making it suitable for processing large datasets of product images and extracting structured feature data that can be used for e-commerce, cataloging, or data analysis.

**Key Features:**

* **Automated Text Extraction:** Utilizes Tesseract OCR to efficiently convert visual text from product images into raw string data.  
* **Robust Unit and Dimension Parsing:** Implements custom logic to accurately identify numerical values and their associated units (e.g., "10.5 cm", "2 meters"), handling various abbreviations and plural forms.  
* **Modular Code Structure:** Organized into distinct Python modules (data\_processing.py, feature\_extraction.py) for enhanced readability, maintainability, and reusability.  
* **Scalable Image Downloading:** Supports efficient downloading of images from provided URLs, including multiprocessing capabilities for faster data acquisition.  
* **Reproducible Environment Setup:** A setup.sh script is provided to streamline the installation of system-level dependencies (like Tesseract OCR) and Python package management via a virtual environment.

## **Project Structure**

The project is organized into a clear and logical directory structure:

product-feature-extraction/  
├── .gitignore             \# Specifies intentionally untracked files and directories to ignore by Git.  
├── LICENSE                \# Contains the licensing information for the project.  
├── README.md              \# This file; provides a comprehensive overview of the project.  
├── requirements.txt       \# Lists all required Python packages for the project.  
├── setup.sh               \# A shell script for setting up system dependencies (Tesseract OCR) and the Python virtual environment.  
├── src/                   \# Contains the core Python source code modules.  
│   ├── \_\_init\_\_.py        \# An empty file that marks the 'src' directory as a Python package.  
│   ├── data\_processing.py \# Handles functions for image downloading, processing, and text extraction using OCR.  
│   └── feature\_extraction.py \# Contains logic for parsing and normalizing dimensions and units from extracted text.  
└── notebooks/             \# Stores Jupyter Notebooks for experimentation, analysis, and demonstrating usage.  
    └── Product\_Feature\_Analysis.ipynb \# The main notebook demonstrating the end-to-end feature extraction pipeline.

## **Installation**

Follow these steps to set up the project environment on your local machine:

1. Clone the repository:  
   Open your terminal or command prompt and execute the following command to clone the project:  
   git clone https://github.com/pokhriyal-anmol/product-feature-extraction.git  
   cd product-feature-extraction

   *(Remember to replace YourUsername with your GitHub username and your-project-name with your actual repository name.)*  
2. Run the setup script:  
   This script automates the installation of system-level dependencies (specifically Tesseract OCR and its language packs) and sets up a dedicated Python virtual environment, then installs all required Python packages listed in requirements.txt.  
   bash setup.sh

   * **Note for Windows users:** The setup.sh script is designed for Unix-like environments (Linux, macOS, WSL, or Git Bash). If you are on Windows and do not use WSL or Git Bash, you will need to perform the installation steps manually:  
     * **Tesseract OCR:** Download and install Tesseract OCR from its [official GitHub releases page](https://github.com/tesseract-ocr/tesseract/wiki/Downloads). Make sure to add it to your system's PATH.  
     * **Python Virtual Environment & Dependencies:** Manually create a virtual environment (python \-m venv venv), activate it (.\\venv\\Scripts\\activate), and then install dependencies (pip install \-r requirements.txt).  
3. Activate the virtual environment (if not automatically activated):  
   The setup.sh script attempts to activate the virtual environment. However, if your terminal session doesn't show (venv) at the beginning of the prompt, you can activate it manually:  
   * **On Linux/macOS:**  
     source venv/bin/activate

   * **On Windows (Command Prompt):**  
     venv\\Scripts\\activate.bat

   * **On Windows (PowerShell):**  
     .\\venv\\Scripts\\Activate.ps1


## **Usage**

### **Running the Analysis Notebook**

The most straightforward way to interact with and run the feature extraction pipeline is through the provided Jupyter Notebook:

1. **Start Jupyter Notebook:**  
   Ensure your virtual environment is active, then from the project root directory, run:  
   ```bash
   jupyter notebook
   ```

2. Your default web browser will automatically open, displaying the Jupyter interface.  
3. Navigate to the `notebooks/` directory.  
4. Open the `Product_Feature_Analysis.ipynb` notebook.  
5. Execute all cells sequentially to load data, download images, extract text, and parse dimensions/units.

---

### **Using as a Library**

The core functionalities are encapsulated in the `src/` modules. You can import and use them in your own scripts:

```python
# Import core functions
from src.data_processing import download_images, extract_text_from_image
from src.feature_extraction import extract_dimensions, entity_unit_map, allowed_units, unit_abbreviation_map, irregular_plurals
```

#### Example 1: Downloading images
```python
import pandas as pd

df = pd.read_csv('../dataset/your_product_data.csv')  # Adjust path to your dataset
image_links = df['image_link'].tolist()
download_folder = '../images'
download_images(image_links, download_folder)
print(f"Images have been downloaded to: {download_folder}")
```

#### Example 2: Extracting text from an image
```python
image_path_example = '/path/to/your/downloaded_image.jpg'  # Replace with actual image path
extracted_text = extract_text_from_image(image_path_example)

if extracted_text:
    print(f"\nExtracted Text from {image_path_example}:")
    print(extracted_text)
else:
    print(f"\nCould not extract text from {image_path_example}.")
```

#### Example 3: Parsing dimensions and units
```python
sample_description = "The package contains a widget measuring 12.5 cm x 5 in and weighing 2 lbs. It needs 220V."
extracted_features = extract_dimensions(sample_description)

print("\nExtracted Dimensions and Units:")
print(extracted_features)
```

You can further process `extracted_features` based on your application's requirements.


## **License**

This project is licensed under the MIT License.

© 2024 Anmol Pokhriyal. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## **Acknowledgments**

* **Tesseract OCR:** The open-source OCR engine used for text extraction.  
* **Pillow (PIL Fork):** For robust image processing capabilities in Python.  
* **pytesseract:** The Python wrapper that allows seamless integration with Tesseract OCR.  
* **pandas:** An essential library for data manipulation and analysis.  
* **tqdm:** Provides elegant progress bars for loops and operations.  
* **requests:** (If you use this library for more advanced HTTP requests for image downloading in data\_processing.py).  
* **Jupyter:** For providing an interactive computing environment.  
* Special thanks to the open-source community for their invaluable tools and libraries.