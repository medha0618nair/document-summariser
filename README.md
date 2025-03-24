# Document Summarizer

A Python-based tool that makes complex documents easier to understand by:

- Extracting text from PDF documents
- Creating simple summaries
- Finding important points
- Identifying potential issues and benefits
- Generating easy-to-read reports

## Features

- PDF text extraction
- Simple document summarization
- Important point detection
- Warning and benefit identification
- Easy-to-read PDF report generation

## Prerequisites

- Python 3.8 or higher
- Tesseract OCR (for scanned PDFs)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/document-summarizer.git
   cd document-summarizer
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install Tesseract OCR:

   - macOS: `brew install tesseract`
   - Ubuntu: `sudo apt-get install tesseract-ocr`
   - Windows: Download from [GitHub Tesseract releases](https://github.com/UB-Mannheim/tesseract/wiki)

5. Download spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

1. Place your PDF documents in the `input` directory
2. Run the summarizer:
   ```bash
   python main.py
   ```
3. Find the generated reports in the `output` directory

## Project Structure

- `main.py`: Main script that runs the summarizer
- `pdf_processor.py`: Handles PDF text extraction
- `text_processor.py`: Processes and analyzes text
- `summarizer.py`: Creates document summaries
- `report_generator.py`: Generates easy-to-read reports
- `input/`: Directory for input PDFs
- `output/`: Directory for generated reports

## Example Report

The generated report includes:

- A simple summary of the document
- Important points to remember
- Things to watch out for
- Good things to know

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Commit your changes: `git commit -m 'Add your feature'`
5. Push to the branch: `git push origin feature/your-feature`
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- spaCy for natural language processing
- Transformers for text summarization
- FPDF for PDF generation
