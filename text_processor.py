import spacy
import re
from typing import List, Dict, Tuple

class TextProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.loophole_keywords = [
            "loophole", "exemption", "exception", "exclude", "exclusion",
            "notwithstanding", "except", "unless", "provided that",
            "subject to", "in accordance with", "as per"
        ]
        self.benefit_keywords = [
            "benefit", "advantage", "entitlement", "right", "privilege",
            "eligible", "qualify", "qualification", "shall", "must",
            "required", "obligation", "duty"
        ]

    def simplify_text(self, text: str) -> str:
        """Simplify complex text to make it more readable"""
        # Replace complex words with simpler alternatives
        simplifications = {
            "notwithstanding": "despite",
            "pursuant to": "according to",
            "in accordance with": "following",
            "prior to": "before",
            "subsequent to": "after",
            "commence": "start",
            "terminate": "end",
            "utilize": "use",
            "implement": "use",
            "facilitate": "help",
            "endeavor": "try",
            "pursuant": "according",
            "herein": "in this document",
            "thereof": "of this",
            "therein": "in that",
            "whereby": "by which",
            "wherein": "where",
            "vis-a-vis": "compared to",
            "henceforth": "from now on"
        }
        
        for complex_word, simple_word in simplifications.items():
            text = re.sub(r'\b' + complex_word + r'\b', simple_word, text, flags=re.IGNORECASE)
        
        return text

    def preprocess_text(self, text: str) -> str:
        """
        Clean and preprocess the input text.
        
        Args:
            text (str): Input text to preprocess
            
        Returns:
            str: Preprocessed text
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters but keep basic punctuation
        text = re.sub(r'[^\w\s.,;:?!()]', '', text)
        
        return text.strip()

    def detect_loopholes_and_benefits(self, text: str) -> Dict[str, List[str]]:
        """
        Detect potential loopholes and benefits in the text.
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            Dict[str, List[str]]: Dictionary containing detected loopholes and benefits
        """
        doc = self.nlp(text)
        results = {
            "loopholes": [],
            "benefits": []
        }
        
        # Split text into sentences
        sentences = [sent for sent in doc.sents]
        
        for sentence in sentences:
            # Check for loopholes
            if any(keyword in sentence.text.lower() for keyword in self.loophole_keywords):
                # Simplify and shorten the text
                phrase = self.simplify_text(sentence.text.strip())
                phrase = phrase[:100]  # Limit length
                if len(phrase) == 100:
                    phrase = phrase[:phrase.rfind(' ')] + '...'
                results["loopholes"].append(phrase)
            
            # Check for benefits
            if any(keyword in sentence.text.lower() for keyword in self.benefit_keywords):
                # Simplify and shorten the text
                phrase = self.simplify_text(sentence.text.strip())
                phrase = phrase[:100]  # Limit length
                if len(phrase) == 100:
                    phrase = phrase[:phrase.rfind(' ')] + '...'
                results["benefits"].append(phrase)
        
        # Limit to top 5 items for each category
        results["loopholes"] = results["loopholes"][:5]
        results["benefits"] = results["benefits"][:5]
        
        return results

    def extract_key_phrases(self, text: str, max_phrases: int = 5) -> List[str]:
        """
        Extract key phrases from the text using spaCy.
        
        Args:
            text (str): Input text
            max_phrases (int): Maximum number of phrases to extract
            
        Returns:
            List[str]: List of key phrases
        """
        doc = self.nlp(text)
        key_phrases = []
        
        # Extract important phrases
        for chunk in doc.noun_chunks:
            if len(chunk.text.split()) >= 2:  # Only include multi-word phrases
                # Simplify the phrase
                simple_phrase = self.simplify_text(chunk.text)
                key_phrases.append(simple_phrase)
        
        # Extract names and important terms
        for ent in doc.ents:
            if len(ent.text.split()) >= 2:  # Only include multi-word terms
                # Simplify the phrase
                simple_phrase = self.simplify_text(ent.text)
                key_phrases.append(simple_phrase)
        
        return key_phrases[:max_phrases] 