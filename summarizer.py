from transformers import BartForConditionalGeneration, BartTokenizer
import torch
from typing import Optional

class DocumentSummarizer:
    def __init__(self):
        self.model_name = "facebook/bart-large-cnn"
        self.tokenizer = BartTokenizer.from_pretrained(self.model_name)
        self.model = BartForConditionalGeneration.from_pretrained(self.model_name)
        
        # Move model to GPU if available
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def summarize(self, text: str, max_length: int = 150, min_length: int = 40) -> Optional[str]:
        """
        Generate a summary of the input text using BART.
        
        Args:
            text (str): Input text to summarize
            max_length (int): Maximum length of the summary
            min_length (int): Minimum length of the summary
            
        Returns:
            Optional[str]: Generated summary or None if summarization fails
        """
        try:
            # Tokenize the input text
            inputs = self.tokenizer.encode(
                "summarize: " + text,
                return_tensors="pt",
                max_length=1024,
                truncation=True
            ).to(self.device)
            
            # Generate summary
            summary_ids = self.model.generate(
                inputs,
                max_length=max_length,
                min_length=min_length,
                length_penalty=2.0,
                num_beams=4,
                early_stopping=True
            )
            
            # Decode the summary
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            return summary
            
        except Exception as e:
            print(f"Error during summarization: {str(e)}")
            return None 