# WinStegnoBrute - Steganography Brute-Force Tool

## Overview

**WinStegnoBrute** is a Python-based tool designed to brute-force hidden data in `.jpg` or `.jpeg` image files using **steghide**. This tool will attempt to extract hidden data from images by trying passphrases from a wordlist.

This tool is useful for **forensics**, **CTF challenges**, or any situation where you need to extract hidden data from images.

## Features

- Brute-forces hidden data in `.jpg` and `.jpeg` images.
- Uses the **steghide** tool for extraction.
- Can use a wordlist to attempt passphrases.
- Logs successful and failed extraction attempts.
- Saves extracted data in a separate folder.

## Requirements

- **Python 3.x** (Recommended Python 3.7+)
- **steghide** (Windows version)
- **Wordlist** text files for passphrase brute-forcing.
- **Images** in `.jpg` or `.jpeg` format.

## Installation

### 1. Clone or Download the Repository

Clone the repository using Git or download it directly as a ZIP file.

To clone via Git:
```bash
git clone https://github.com/Roger-Rached-ozz961/WinStegnoBrute.git
```

Alternatively, you can download the repository as a ZIP file from [WinStegnoBrute](https://github.com/Roger-Rached-ozz961/WinStegnoBrute).

### 2. Download and Set Up **steghide**

1. Download the Windows version of **steghide** from [here](http://steghide.sourceforge.net/).
2. Place `steghide.exe` in the `steghide` folder inside your project directory.

### 3. Organize Your Files

- Place `.jpg` or `.jpeg` images into the `stegno images` folder.
- Place wordlist text files (e.g., `wordlist.txt`) into the `wordlists` folder.

### 4. Install Python 3.x

If you don't have Python 3.x installed, download and install it from [python.org](https://www.python.org/downloads/). Ensure that Python is added to the system PATH during installation.

### 5. Install Dependencies (Optional)

If you have any additional dependencies, you can install them via `pip`. For example:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Running the Tool

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the following command:
   ```bash
   python stegnobrute.py
   ```

### 2. Tool Instructions

- The tool will display a banner and prompt you to confirm that all necessary files are in place.
- You will be asked to press **Enter** when ready to start.
- The tool will attempt to extract hidden data from each image using each wordlist passphrase.

### 3. Output and Results

- The tool will log results to `results.txt`.
- Successful extractions will be saved in the `extracted_data` folder.

Example Output in the terminal:

```
****************************************************
*                                                  *
*        WinStegnoBrute - Steganography Tool        *
*               Author: Roger Rached               *
*                  Version: 1.0                    *
*                                                  *
****************************************************

Starting extraction process...
Processing 5 images and 3 wordlists...
Trying passphrase: mypassword123...
[SUCCESS] Data extracted from image1.jpg with passphrase: mypassword123
...
```

## Folder Structure

```
WinStegnoBrute/
│
├── stegnobrute.py            # The main Python script
├── steghide/                 # Folder containing the steghide executable (steghide.exe)
├── wordlists/                # Folder containing wordlist text files
│   └── mywordlist.txt
├── stego images/             # Folder containing images to process
│   └── image1.jpg
└── extracted_data/           # Folder for saving extracted files
└── results.txt               # Log file with extraction results
```

## Troubleshooting

- **`steghide.exe` not found**: Ensure you have downloaded the correct version of **steghide** for Windows and placed it in the `steghide` folder.
- **No `.jpg` or `.jpeg` images found**: Ensure the images are placed in the `stegno images` folder.
- **No wordlist files found**: Ensure you have placed a `.txt` wordlist file in the `wordlists` folder.

## License

This tool is free to use for educational and ethical purposes. Feel free to modify it according to your needs.

## Author

- **Roger Rached (Ozz961)**
