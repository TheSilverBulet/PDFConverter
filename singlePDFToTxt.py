from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
import sys

def convert_pdf_to_clean_text(pdf_path, text_path):
    """
    Converts a PDF file to a text file, removing superfluous spaces and newlines.

    Args:
        pdf_path (str): The path to the input PDF file.
        text_path (str): The path to the output text file.
    """
    try:
        with open(pdf_path, 'rb') as pdf_file, open(text_path, 'w', encoding='utf-8') as text_file:
            laparams = LAParams()
            text = extract_text_to_fp(pdf_file, text_file, laparams=laparams)

        # Read the generated text file and clean it
        with open(text_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        cleaned_lines = [line.strip() for line in lines if line.strip()]
        cleaned_text = " ".join(cleaned_lines)

        # Write the cleaned text back to the output file
        with open(text_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

        print(f"Successfully converted '{pdf_path}' to '{text_path}' with cleaned text.")

    except FileNotFoundError:
        print(f"Error: PDF file not found at '{pdf_path}'.")
    except Exception as e:
        print(f"An error occurred while processing '{pdf_path}': {e}")

if __name__ == "__main__":
    pdf_file_path = input("Enter the path to the PDF file: ")
    output_text_path = input("Enter the path for the output text file: ")
    convert_pdf_to_clean_text(pdf_file_path, output_text_path)
