import os
from pdf_processor import PDFProcessor
from text_processor import TextProcessor
from summarizer import DocumentSummarizer
from report_generator import ReportGenerator

def main():
    # Initialize components
    pdf_processor = PDFProcessor()
    text_processor = TextProcessor()
    summarizer = DocumentSummarizer()
    report_generator = ReportGenerator()
    
    # Process all PDFs in the input directory
    print("Processing PDF documents...")
    documents = pdf_processor.process_directory()
    
    if not documents:
        print("No PDF documents found in the input directory.")
        return
    
    # Process each document
    for filename, text in documents:
        print(f"\nProcessing: {filename}")
        
        # Preprocess text
        processed_text = text_processor.preprocess_text(text)
        
        # Generate summary
        print("Generating summary...")
        summary = summarizer.summarize(processed_text)
        
        if not summary:
            print(f"Failed to generate summary for {filename}")
            continue
        
        # Detect loopholes and benefits
        print("Analyzing text for loopholes and benefits...")
        analysis = text_processor.detect_loopholes_and_benefits(processed_text)
        
        # Extract key phrases
        print("Extracting key phrases...")
        key_phrases = text_processor.extract_key_phrases(processed_text)
        
        # Generate report
        print("Generating PDF report...")
        report_path = report_generator.create_report(
            filename=filename,
            summary=summary,
            analysis=analysis,
            key_phrases=key_phrases
        )
        
        print(f"Report generated: {report_path}")

if __name__ == "__main__":
    main() 