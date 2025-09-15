#!/bin/bash
# setup.sh
# A script to set up the environment for the Product Feature Extraction project.

echo "--- Setting up Project Environment ---"

# 1. Update package lists
echo "1. Updating system package lists..."
sudo apt-get update
if [ $? -ne 0 ]; then
    echo "Error: Failed to update apt-get. Exiting."
    exit 1
fi

# 2. Install Tesseract OCR and its language packs
echo "2. Installing Tesseract OCR and language packs..."
sudo apt-get install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-osd
if [ $? -ne 0 ]; then
    echo "Error: Failed to install Tesseract OCR. Exiting."
    exit 1
fi
echo "Tesseract OCR installed successfully."

# 3. Create and activate a Python virtual environment
echo "3. Setting up Python virtual environment..."
PYTHON_VENV_DIR="venv"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: python3 could not be found. Please install Python 3."
    exit 1
fi

if [ -d "$PYTHON_VENV_DIR" ]; then
    echo "Virtual environment '$PYTHON_VENV_DIR' already exists. Skipping creation."
else
    python3 -m venv "$PYTHON_VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment. Exiting."
        exit 1
    fi
    echo "Virtual environment '$PYTHON_VENV_DIR' created."
fi

# Activate the virtual environment
# Check if running in bash/zsh or similar for 'source'
if [ -n "$ZSH_VERSION" ] || [ -n "$BASH_VERSION" ]; then
    source "$PYTHON_VENV_DIR"/bin/activate
    if [ $? -ne 0 ]; then
        echo "Error: Failed to activate virtual environment. Exiting."
        exit 1
    fi
    echo "Virtual environment activated."
else
    echo "Please activate the virtual environment manually: source $PYTHON_VENV_DIR/bin/activate"
fi


# 4. Update pip and install Python dependencies
echo "4. Updating pip and installing Python dependencies from requirements.txt..."
pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo "Warning: Failed to upgrade pip. Continuing with installation."
fi

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install Python dependencies. Please check requirements.txt."
        exit 1
    fi
    echo "Python dependencies installed successfully."
else
    echo "Error: requirements.txt not found. Please create it."
    exit 1
fi

echo "--- Setup Complete ---"
echo "To deactivate the virtual environment later, run: deactivate"
echo "You can now run your Jupyter Notebook: jupyter notebook notebooks/Product_Feature_Analysis.ipynb"