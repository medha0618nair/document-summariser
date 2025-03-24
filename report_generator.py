from fpdf import FPDF
from typing import Dict, List
import os
from datetime import datetime

class ReportGenerator:
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def _wrap_text(self, text: str, pdf: FPDF, max_width: float) -> List[str]:
        """Break text into lines that fit the page width"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            current_line.append(word)
            line_width = pdf.get_string_width(' '.join(current_line))
            
            if line_width > max_width:
                if len(current_line) > 1:
                    current_line.pop()
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    lines.append(word)
                    current_line = []
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines

    def create_report(self, 
                     filename: str,
                     summary: str,
                     analysis: Dict[str, List[str]],
                     key_phrases: List[str]) -> str:
        """Create an easy-to-read report of the document analysis"""
        pdf = FPDF()
        pdf.add_page()
        
        # Make wider margins for better readability
        margin = 25
        pdf.set_left_margin(margin)
        pdf.set_right_margin(margin)
        max_width = pdf.w - 2 * margin
        
        # Title at the top
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 15, "Simple Document Summary", ln=True, align="C")
        pdf.ln(5)
        
        # File information
        pdf.set_font("Helvetica", "", 12)
        pdf.cell(0, 10, f"File Name: {filename}", ln=True)
        pdf.cell(0, 10, f"Date: {datetime.now().strftime('%B %d, %Y')}", ln=True)
        pdf.ln(10)
        
        # Main summary
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "What This Document Says:", ln=True)
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 12)
        summary_lines = self._wrap_text(summary, pdf, max_width)
        for line in summary_lines:
            pdf.cell(0, 8, line, ln=True)
        pdf.ln(10)
        
        # Important points
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Important Points:", ln=True)
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 12)
        for phrase in key_phrases:
            phrase_lines = self._wrap_text(f"- {phrase}", pdf, max_width)
            for line in phrase_lines:
                pdf.cell(0, 8, line, ln=True)
            pdf.ln(3)
        pdf.ln(7)
        
        # Warnings section
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Watch Out For These:", ln=True)
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 12)
        for loophole in analysis["loopholes"]:
            loophole_lines = self._wrap_text(f"- {loophole}", pdf, max_width)
            for line in loophole_lines:
                pdf.cell(0, 8, line, ln=True)
            pdf.ln(3)
        pdf.ln(7)
        
        # Benefits section
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "Good Things to Know:", ln=True)
        pdf.ln(5)
        pdf.set_font("Helvetica", "", 12)
        for benefit in analysis["benefits"]:
            benefit_lines = self._wrap_text(f"- {benefit}", pdf, max_width)
            for line in benefit_lines:
                pdf.cell(0, 8, line, ln=True)
            pdf.ln(3)
        
        # Save the report with a simple name
        report_filename = f"summary_{os.path.splitext(filename)[0]}.pdf"
        report_path = os.path.join(self.output_dir, report_filename)
        pdf.output(report_path)
        
        return report_path 