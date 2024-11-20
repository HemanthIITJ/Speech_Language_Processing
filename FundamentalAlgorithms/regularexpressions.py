"""
Advanced NLP Research Guide to Regular Expressions in Python
============================================================

This Python script outlines the core principles of Regular Expressions (RegEx) in Python and provides 
a detailed explanation with examples catered to advanced NLP researchers. It covers the basics and 
gradually moves to more advanced concepts such as disjunctions, negations, wildcards, and usage best 
practices in Python. Particular attention is given to Python's handling of backslashes in 
strings, underlining the need for raw string notation with examples.

"""

import re  # For working with regular expressions in Python
from typing import List, Tuple, Optional


def find_word_the(text: str) -> List[str]:
    """
    Find all instances of the word 'the' in a given text, considering both lower and upper cases,
    and ensuring not to match substrings of other words.

    Steps in design process:
    - Initial regex `the` misses uppercased examples.
    - New regex `[tT]he` includes both cases but also matches 'theology'.
    - Fix: Add word boundaries to avoid matching substrings within words.
    
    Args:
        text: Input text where we need to find occurrences of 'the'.
        
    Returns:
        List of strings where 'the' or 'The' occurs, bounded by non-word characters.

    example pattern: r'\b[tT]he\b'
    """
    pattern = r'\b[tT]he\b'
    matches = re.findall(pattern, text)
    return matches


def regex_disjunction(text: str) -> List[str]:
    """
    Demonstrates the use of disjunction in regular expressions. Finds either 'cat', 'dog', or 'rabbit'
    in the text, but avoids substrings of larger words (like 'category').

    Args:
        text: Input text where we want to perform a disjunction search.

    Returns:
        List of matched strings: 'cat', 'dog', or 'rabbit'.
    """
    pattern = r'\b(cat|dog|rabbit)\b'
    return re.findall(pattern, text)


def regex_with_negation_disjunction(text: str) -> List[str]:
    """
    Demonstrates negation in disjunction: find words that are not 'cat', 'dog', or 'rabbit'.

    Args:
        text: Input text for which matches excluding 'cat', 'dog', or 'rabbit' are found.

    Returns:
        List of words excluding 'cat', 'dog', and 'rabbit'.
    """
    # We'll split the text into words and then filter out 'cat', 'dog', and 'rabbit'
    words = re.findall(r'\b\w+\b', text)
    return [word for word in words if word not in {"cat", "dog", "rabbit"}]


def convenient_aliases_examples(text: str) -> List[str]:
    """
    Demonstrates the use of common regex aliases like `\d`, `\w`, and `\s`.
    This function extracts all sequences of digits, word characters, and whitespace in the text.

    Args:
        text: Input text.

    Returns:
        List of matched strings for digit sequences, word sequences, and whitespace.
    """
    digit_pattern = r'\d+'  # Alias for digits
    word_pattern = r'\w+'   # Alias for word characters (alphanumeric + underscore)
    space_pattern = r'\s+'  # Alias for space characters (spaces, tabs, newlines)

    digits = re.findall(digit_pattern, text)
    words = re.findall(word_pattern, text)
    spaces = re.findall(space_pattern, text)

    return {
        'digits': digits,
        'words': words,
        'spaces': spaces
    }


def advanced_regex_wildcards(text: str) -> List[str]:
    """
    Demonstrates use of wildcards, optionality, and repetition in regex:
    - `.` matches any character except newline;
    - `?` matches 0 or 1 occurrence of the previous expression;
    - `*` matches 0 or more occurrences of the previous expression;
    - `+` matches 1 or more occurrences of the previous expression.

    This function returns instances of patterns like "a", "an", "any" (optional 'n'), and
    repeated characters.

    Args:
        text: Input text.

    Returns:
        List of matched examples based on wildcards and repetition patterns.
    """
    pattern = r'a[n]?\w*'  # Matches 'a', 'an', 'any', etc.
    return re.findall(pattern, text)


def regex_anchors_examples(text: str) -> List[str]:
    """
    Demonstrates use of regex anchors: `^` for start of line, `$` for end of line.
    Finds lines that start with 'The' and end with a period.

    Args:
        text: Input text to search for anchored patterns.

    Returns:
        List of sentences that match the anchored pattern.
    """
    pattern = r'^The.*\.$'  # Sentences starting with "The" and ending with period
    return re.findall(pattern, text, re.MULTILINE)  # MULTILINE to handle line-by-line matching


def iterative_regex_process_example(text: str) -> Tuple[List[str], List[str]]:
    """
    Demonstrates the iterative design process of regular expressions to reduce
    false positives and false negatives. We aim to extract the word "the" in a text,
    ensuring we neither miss valid instances nor incorrectly match invalid strings.

    Args:
        text: Input text.

    Returns:
        Tuple consisting of:
        - List of valid matches ('the' or 'The').
        - List of invalid matches (e.g., 'there', 'then', 'other').
    """
    # Initial attempt: 
    rough_pattern = r'[tT]he'                          # Matches too much, not filtered for boundaries
    valid_pattern = r'\b[tT]he\b'                      # Correct usage with boundaries to avoid substrings

    # Valid matches
    valid_matches = re.findall(valid_pattern, text)

    # Invalid matches from the rough pattern
    invalid_matches = list(set(re.findall(rough_pattern, text)) - set(valid_matches))

    return valid_matches, invalid_matches


def main():
    """
    Main function to run all regular expression examples with sample text for demonstration purposes.
    This function allows NLP researchers to see how regular expressions apply to real-world examples,
    allowing them to review each case demonstration separately.
    """
    sample_text = (
        "The quick brown fox jumps over the lazy dog. Then, the thief ran away. Now, theology "
        "and other subjects are being discussed. Can cats, dogs, and rabbits coexist? What about cats2 or dog3?"
    )

    # Example of finding "the"/"The" in text
    print("Find all 'The/the':", find_word_the(sample_text))

    # Example of disjunction
    print("Disjunction Example (cat/dog/rabbit):", regex_disjunction(sample_text))

    # Example of negation in disjunction
    print("Negation in Disjunction (exclude cat/dog/rabbit):", regex_with_negation_disjunction(sample_text))

    # Example of convenient aliases for digits, words, and space
    print("Convenient Aliases:", convenient_aliases_examples(sample_text))

    # Example of wildcards, optionality, repetition
    print("Wildcard Examples:", advanced_regex_wildcards(sample_text))

    # Example of anchor usage
    print("Anchors Examples (start with 'The', end with '.'): ", regex_anchors_examples(sample_text))

    # Demonstrating the process of iterative regex refining
    valid, invalid = iterative_regex_process_example(sample_text)
    print("Iterative Regex Process - Valid Matches:", valid)
    print("Iterative Regex Process - Invalid Matches:", invalid)


if __name__ == "__main__":
    main()