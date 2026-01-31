# Safaricom Number Filter

## Overview
**Safaricom Number Filter** is a robust desktop application designed to efficiently extract, filter, and normalize Safaricom phone numbers from raw text files. Built with Python and PyQt5, this tool streamlines the process of data cleaning for marketing campaigns, contact management, and data analysis by isolating valid Safaricom contacts.

## Features
- **File Parsing**: Seamlessly import `.txt` files containing mixed raw data.
- **Intelligent Filtering**: Automatically identifies valid Safaricom numbers using regex patterns (Prefixes: 070-072, 079, etc.).
- **Data Normalization**: Cleans whitespace and standardizes formats.
- **Duplicate Removal**: Automatically removes duplicate entries to ensure a unique list of contacts.
- **Export Functionality**: Export the cleaned and sorted list of numbers to a new text file.
- **User-Friendly GUI**: Clean, responsive interface with status updates and visual feedback.

## Tech Stack
- **Language**: Python 3.x
- **GUI Framework**: PyQt5

## Prerequisites
Ensure you have Python installed on your system. You can verify this by running:
```bash
python --version
```

## Installation
1. Clone this repository or download the source code.
2. Navigate to the project directory:
   ```bash
   cd safaricomNumbersFilter
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python safNumFiltersTxt.py
   ```
2. Click **Browse** to select a `.txt` file containing mixed phone number data.
3. Click **Search** to process the file. The application will display the matching Safaricom numbers.
4. If matches are found, click **Export** to save the clean list to a new file.

## Project Structure
```
safaricomNumbersFilter/
├── safNumFiltersTxt.py    # Main application entry point
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules
```

## Credits
**Developed by:** Mufasa Tech

## Date Created
January 31, 2026
