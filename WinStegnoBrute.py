import os
import subprocess
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# Paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "stegno images")
WORDLIST_DIR = os.path.join(BASE_DIR, "wordlists")
RESULTS_FILE = os.path.join(BASE_DIR, "results.txt")
STEGOHIDE_PATH = os.path.join(BASE_DIR, "steghide", "steghide.exe")
EXTRACTED_DATA_DIR = os.path.join(BASE_DIR, "extracted_data")

# Ensure necessary directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(WORDLIST_DIR, exist_ok=True)
os.makedirs(EXTRACTED_DATA_DIR, exist_ok=True)

# Banner
BANNER = f"""
{Fore.LIGHTCYAN_EX}****************************************************
{Fore.LIGHTCYAN_EX}*                                                  *
{Fore.LIGHTCYAN_EX}*      Windows StegnoBrute - Steganography Tool    *
{Fore.LIGHTCYAN_EX}*          Author: Ozz961                          *
{Fore.LIGHTCYAN_EX}*          Version: 1.0                            *
{Fore.LIGHTCYAN_EX}*                                                  *
{Fore.LIGHTCYAN_EX}****************************************************
"""

def log_result(message):
    """Log messages to results.txt."""
    with open(RESULTS_FILE, "a") as f:
        f.write(message + "\n")

def extract_data_steghide(image_file, passphrase):
    """Attempt to extract data using steghide."""
    try:
        # Ensure the path is correct and steghide is accessible
        if not os.path.exists(STEGOHIDE_PATH):
            print(f"{Fore.LIGHTRED_EX}[ERROR]{Style.RESET_ALL} steghide executable not found at {STEGOHIDE_PATH}")
            log_result(f"[ERROR] steghide executable not found at {STEGOHIDE_PATH}")
            return False

        # Create a unique output file for each extraction attempt
        output_file = os.path.join(EXTRACTED_DATA_DIR, f"{os.path.splitext(os.path.basename(image_file))[0]}_{passphrase}.txt")

        # Construct steghide command
        command = [
            STEGOHIDE_PATH,
            "extract",
            "-sf", image_file,
            "-p", passphrase,
            "-xf", output_file
        ]

        # Run the command
        print(f"{Fore.LIGHTYELLOW_EX}Running steghide command for {image_file} with passphrase: {passphrase}...{Style.RESET_ALL}")
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"{Fore.LIGHTGREEN_EX}[SUCCESS]{Style.RESET_ALL} Data extracted from {image_file} with passphrase: {passphrase}")
            log_result(f"[SUCCESS] {image_file} | Passphrase: {passphrase}")
            return True
        else:
            print(f"{Fore.LIGHTRED_EX}[FAILED]{Style.RESET_ALL} {image_file} | Passphrase: {passphrase}")
            log_result(f"[FAILED] {image_file} | Passphrase: {passphrase}")
            return False

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}[ERROR]{Style.RESET_ALL} Error during extraction: {e}")
        log_result(f"[ERROR] {e}")
        return False

def main():
    try:
        print(BANNER)

        # Tool Description
        print(f"{Fore.LIGHTMAGENTA_EX}Welcome to StegnoBrute!{Style.RESET_ALL}")
        print("This tool is designed to help you extract hidden data from .jpg/.jpeg images using steghide.")
        print("\nRequirements:")
        print(f"{Fore.LIGHTYELLOW_EX}1. Place your .jpg/.jpeg images in the 'stegno images' folder.")
        print(f"{Fore.LIGHTYELLOW_EX}2. Place your password wordlist textfile inside the 'wordlists' folder.")
        print("\nThe tool will attempt to brute force the hidden data using the passwords provided in the wordlist.")

        # Check for necessary files and directories
        if not os.path.exists(IMAGES_DIR):
            print(f"{Fore.LIGHTRED_EX}Error: 'stegno images' folder not found. Please create the folder and add images.")
            input(f"{Fore.LIGHTRED_EX}Press Enter to exit the program.{Style.RESET_ALL}")
            return

        if not os.path.exists(WORDLIST_DIR):
            print(f"{Fore.LIGHTRED_EX}Error: 'wordlists' folder not found. Please create the folder and add a wordlist.")
            input(f"{Fore.LIGHTRED_EX}Press Enter to exit the program.{Style.RESET_ALL}")
            return

        if not os.path.exists(STEGOHIDE_PATH):
            print(f"{Fore.LIGHTRED_EX}Error: 'steghide' executable not found at {STEGOHIDE_PATH}. Please ensure steghide is placed in the correct folder.")
            input(f"{Fore.LIGHTRED_EX}Press Enter to exit the program.{Style.RESET_ALL}")
            return

        images = [f for f in os.listdir(IMAGES_DIR) if f.lower().endswith(('.jpg', '.jpeg'))]
        if not images:
            print(f"{Fore.LIGHTRED_EX}No .jpg or .jpeg files found in the 'stegno images' folder.")
            input(f"{Fore.LIGHTRED_EX}Press Enter to exit the program.{Style.RESET_ALL}")
            return

        wordlist_files = [f for f in os.listdir(WORDLIST_DIR) if f.lower().endswith('.txt')]
        if not wordlist_files:
            print(f"{Fore.LIGHTRED_EX}No wordlist files found in the 'wordlists' folder.")
            input(f"{Fore.LIGHTRED_EX}Press Enter to exit the program.{Style.RESET_ALL}")
            return

        # Confirm from the user
        input(f"{Fore.LIGHTCYAN_EX}Press Enter to continue if you have placed all required files correctly...{Style.RESET_ALL}")

        # Clear results file at the start
        with open(RESULTS_FILE, "w") as f:
            f.write("")

        # Process images
        print(f"{Fore.LIGHTGREEN_EX}Starting extraction process...{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}Processing {len(images)} images and {len(wordlist_files)} wordlists...{Style.RESET_ALL}")

        success_count = 0
        total_count = 0

        for image in images:
            image_path = os.path.join(IMAGES_DIR, image)
            print(f"{Fore.LIGHTCYAN_EX}Processing image: {image}...{Style.RESET_ALL}")

            for wordlist_file in wordlist_files:
                wordlist_path = os.path.join(WORDLIST_DIR, wordlist_file)
                print(f"{Fore.LIGHTYELLOW_EX}Using wordlist: {wordlist_file}...{Style.RESET_ALL}")

                try:
                    with open(wordlist_path, "r") as wf:
                        for line in wf:
                            passphrase = line.strip()
                            total_count += 1
                            print(f"{Fore.LIGHTMAGENTA_EX}Trying passphrase: {passphrase}...{Style.RESET_ALL}")

                            # Try extraction using steghide
                            if extract_data_steghide(image_path, passphrase):
                                success_count += 1

                except Exception as e:
                    print(f"{Fore.LIGHTRED_EX}[ERROR]{Style.RESET_ALL} Error reading wordlist {wordlist_file}: {e}")
                    log_result(f"[ERROR] Error reading wordlist {wordlist_file}: {e}")

        # Summary
        print(f"{Fore.LIGHTGREEN_EX}Extraction process completed. {success_count} successful extractions out of {total_count} attempts.{Style.RESET_ALL}")
        print(f"Results are saved in {RESULTS_FILE}.")
        print(f"{Fore.LIGHTYELLOW_EX}Log file {RESULTS_FILE} has been updated with the results of the extraction attempts.{Style.RESET_ALL}")

        input(f"{Fore.LIGHTCYAN_EX}Press Enter to exit the program...{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}[ERROR]{Style.RESET_ALL} Unexpected error occurred: {e}")
        log_result(f"[ERROR] Unexpected error: {e}")
        input(f"{Fore.LIGHTRED_EX}Press Enter to exit the program and check for errors.{Style.RESET_ALL}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.LIGHTRED_EX}[EXIT]{Style.RESET_ALL} Exiting gracefully. Goodbye!")
        exit()
