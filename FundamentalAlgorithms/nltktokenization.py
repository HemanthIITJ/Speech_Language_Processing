import re
from typing import List, Tuple, Set
import nltk
from nltk.tokenize import regexp_tokenize
from collections import Counter
import math

# Ensure you have the NLTK data required
nltk.download('punkt')

def tokenize_text(text: str) -> List[str]:
    """
    Tokenizes input text using a regular expression pattern with NLTK's regexp_tokenize.

    Args:
    text (str): The text you want to tokenize.

    Returns:
    List[str]: A list of tokens extracted from the text.
    """
    # Regular expression pattern for tokenization
    pattern = r'''(?x) # set flag to allow verbose regexps
                   ([A-Z]\.)+         # abbreviations, e.g. U.S.A.
                   | \w+(-\w+)*       # words with optional internal hyphens
                   | \$?\d+(\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
                   | \.\.\.           # ellipsis
                   | [][.,;"'?():-_‘] # these are separate tokens; includes ], [
                '''

    tokens = regexp_tokenize(text, pattern)
    return tokens

def compute_vocabulary(tokens: List[str]) -> Tuple[int, Set[str]]:
    """
    Computes vocabulary size and returns unique vocabulary set with its size.

    Args:
    tokens (List[str]): A list of word tokens.

    Returns:
    Tuple[int, Set[str]]: A tuple containing the count of unique vocabulary (V) and a set of words.
    """
    vocabulary_set = set(tokens)
    return len(vocabulary_set), vocabulary_set

def heaps_law_estimation(num_tokens: int, beta: float = 0.7, k: float = 10.0) -> float:
    """
    Applies Heap's Law to estimate vocabulary size based on the number of tokens.

    Args:
    num_tokens (int): Number of tokens in the text corpus.
    beta (float): Constant characterizing the growth rate of vocabulary with the number of tokens.
    k (float): Constant scaling factor.

    Returns:
    float: Estimated vocabulary size according to Heap's Law.
    """
    estimated_vocab_size = k * (num_tokens ** beta)
    return estimated_vocab_size

def text_analysis_pipeline(text: str) -> None:
    """
    Performs complete analysis on a given text including tokenization, vocabulary size computation,
    and vocabulary size estimation using Heap's Law.

    Args:
    text (str): The text to be analyzed.

    Raises:
    ValueError: If the text is empty.
    """
    if not text:
        raise ValueError("Text input cannot be empty.")

    # Tokenization
    tokens = tokenize_text(text)
    num_tokens = len(tokens)
    
    # Compute Vocabulary
    vocab_size, vocabulary = compute_vocabulary(tokens)

    # Estimate Vocabulary Size using Heap's Law
    estimated_vocab_size = heaps_law_estimation(num_tokens)

    # Output the results
    print(f"Number of Tokens (N): {num_tokens}")
    print(f"Vocabulary Size (|V|): {vocab_size}")
    print(f"Vocabulary Set: {vocabulary}")
    print(f"Estimated Vocabulary Size (Heap's Law): {estimated_vocab_size:.2f}")

if __name__ == "__main__":
    # Example text input
    example_text = "That U.S.A. poster-print costs $12.40..."
    
    try:
        # Running the text analysis pipeline
        text_analysis_pipeline(example_text)
    except Exception as e:
        print(f"An error occurred during text analysis: {e}")