import pdfplumber
import os
from typing import List, Optional

class PDFProcessor:
    def __init__(self, input_dir: str = "input"):
        self.input_dir = input_dir

    def extract_text(self, pdf_path: str) -> Optional[str]:
        """
        Extract text from a PDF file.
        
        Args:
            pdf_path (str): Path to the PDF file
            
        Returns:
            Optional[str]: Extracted text or None if extraction fails
        """
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() or ""
                return text.strip()
        except Exception as e:
            print(f"Error extracting text from {pdf_path}: {str(e)}")
            return None

    def process_directory(self) -> List[tuple]:
        """
        Process all PDF files in the input directory.
        
        Returns:
            List[tuple]: List of tuples containing (filename, extracted_text)
        """
        results = []
        for filename in os.listdir(self.input_dir):
            if filename.lower().endswith('.pdf'):
                pdf_path = os.path.join(self.input_dir, filename)
                text = self.extract_text(pdf_path)
                if text:
                    results.append((filename, text))
        return results 