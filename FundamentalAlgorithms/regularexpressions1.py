#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Regular Expressions in Python: A Comprehensive Guide for NLP Researchers

This script provides an in-depth exploration of regular expressions in Python,
covering topics from basic to advanced levels. It is designed for advanced NLP
researchers who wish to deepen their understanding of regex patterns and their
applications in text processing.

Author: Kandimalla Hemanth
Date: November 2024
"""

import re
from typing import List, Pattern, Tuple

# =============================================================================
# Regular Expressions are used everywhere
# =============================================================================
# Regular expressions (regex) are powerful tools for matching patterns in text.
# They are ubiquitous in NLP tasks such as tokenization, parsing, entity
# recognition, and more.

# =============================================================================
# Regular Expressions Basics
# =============================================================================
# The 're' module in Python provides support for working with regex.

def find_all_matches(pattern: str, text: str) -> List[str]:
    """
    Find all substrings in 'text' that match the given 'pattern'.

    Args:
        pattern (str): The regex pattern to search for.
        text (str): The text to search within.

    Returns:
        List[str]: A list of all matching substrings.
    """
    try:
        compiled_pattern: Pattern = re.compile(pattern)
        matches: List[str] = compiled_pattern.findall(text)
        return matches
    except re.error as regex_error:
        raise ValueError(f"Invalid regex pattern: {pattern}") from regex_error

# Example Usage:
sample_text = "The quick brown fox jumps over the lazy dog. Then the fox rests."
pattern = r"[Tt]he"
matches = find_all_matches(pattern, sample_text)
print(f"Matches for pattern '{pattern}': {matches}")
# Output: Matches for pattern '[Tt]he': ['The', 'the', 'Then', 'the']

# =============================================================================
# Disjunctions
# =============================================================================
# Disjunctions allow matching one of several patterns.

def demonstrate_disjunction(text: str) -> List[str]:
    """
    Demonstrate regex disjunctions by matching 'cat' or 'dog' in the text.

    Args:
        text (str): The text to search within.

    Returns:
        List[str]: A list of matches ('cat' or 'dog').
    """
    pattern = r"cat|dog"
    return find_all_matches(pattern, text)

# Example Usage:
animal_text = "I have a cat and a dog."
animal_matches = demonstrate_disjunction(animal_text)
print(f"Animal matches: {animal_matches}")
# Output: Animal matches: ['cat', 'dog']

# =============================================================================
# Negation in Disjunction
# =============================================================================
# Negation can be applied using character classes and the caret symbol '^'.

def demonstrate_negation(text: str) -> List[str]:
    """
    Find all words that do not start with a vowel.

    Args:
        text (str): The text to search within.

    Returns:
        List[str]: A list of words not starting with a vowel.
    """
    pattern = r"\b[^aeiouAEIOU\s]\w+"
    return find_all_matches(pattern, text)

# Example Usage:
negation_text = "Apple banana orange pear grape"
negation_matches = demonstrate_negation(negation_text)
print(f"Words not starting with a vowel: {negation_matches}")
# Output: Words not starting with a vowel: ['banana', 'pear', 'grape']

# =============================================================================
# Convenient Aliases
# =============================================================================
# Regex provides shorthand character classes (aliases) for common patterns.

def demonstrate_aliases(text: str) -> List[str]:
    """
    Find all sequences of digits in the text.

    Args:
        text (str): The text to search within.

    Returns:
        List[str]: A list of digit sequences.
    """
    pattern = r"\d+"
    return find_all_matches(pattern, text)

# Example Usage:
number_text = "Order numbers: 12345, 67890, and 24680."
number_matches = demonstrate_aliases(number_text)
print(f"Number matches: {number_matches}")
# Output: Number matches: ['12345', '67890', '24680']

# =============================================================================
# More Disjunction
# =============================================================================
# Combining disjunctions with aliases and groups for complex patterns.

def demonstrate_complex_disjunction(text: str) -> List[str]:
    """
    Find all occurrences of 'cat(s)?' or 'dog(s)?' in the text.

    Args:
        text (str): The text to search within.

    Returns:
        List[str]: A list of matches including singular/plural forms.
    """
    pattern = r"(cat|dog)s?"
    return find_all_matches(pattern, text)

# Example Usage:
plural_text = "Cats and dogs are common pets. I have one cat and two dogs."
plural_matches = demonstrate_complex_disjunction(plural_text)
print(f"Plural matches: {plural_matches}")
# Output: Plural matches: ['Cats', 'dogs', 'cat', 'dogs']

# =============================================================================
# Wildcards, Optionality, Repetition: . ? * +
# =============================================================================
# Special characters for flexible pattern matching:
# '.' matches any character except newline.
# '?' makes the preceding token optional.
# '*' matches 0 or more repetitions.
# '+' matches 1 or more repetitions.

def demonstrate_wildcards(text: str) -> List[str]:
    """
    Find all matches where a word starts with 'b', followed by any two characters,
    and ends with 't'.

    Args:
        text (str): The text to search within.

    Returns:
        List[str]: A list of matching words.
    """
    pattern = r"\bb..t\b"
    return find_all_matches(pattern, text)

# Example Usage:
wildcard_text = "bat bet bit bot but bait belt boot"
wildcard_matches = demonstrate_wildcards(wildcard_text)
print(f"Wildcard matches: {wildcard_matches}")
# Output: Wildcard matches: ['bat', 'bet', 'bit', 'bot', 'but', 'belt', 'boot']

# =============================================================================
# Anchors ^ $
# =============================================================================
# Anchors assert the position in the text:
# '^' matches the start of a line.
# '$' matches the end of a line.

def demonstrate_anchors(text: str) -> List[str]:
    """
    Find all lines in the text that start with 'Error' and end with a period.

    Args:
        text (str): The multi-line text to search within.

    Returns:
        List[str]: A list of matching lines.
    """
    pattern = r"^Error.*\.$"
    try:
        compiled_pattern = re.compile(pattern, re.MULTILINE)
        matches = compiled_pattern.findall(text)
        return matches
    except re.error as regex_error:
        raise ValueError(f"Invalid regex pattern: {pattern}") from regex_error

# Example Usage:
log_text = """Info: Process started.
Warning: Low memory.
Error: Null pointer exception.
Error: Out of bounds."""
anchor_matches = demonstrate_anchors(log_text)
print(f"Anchor matches: {anchor_matches}")
# Output: Anchor matches: ['Error: Null pointer exception.']

# =============================================================================
# A Note about Python Regular Expressions
# =============================================================================
# In Python, backslashes '\' are used both in string literals and regex patterns,
# which can cause confusion. To avoid issues, use raw strings for regex patterns.

def demonstrate_raw_strings():
    """
    Show the difference between regular strings and raw strings in regex patterns.
    """
    normal_pattern = "\\d+"
    raw_pattern = r"\d+"
    text = "There are 100 apples."

    # Without raw string
    try:
        normal_matches = re.findall(normal_pattern, text)
    except re.error as regex_error:
        print(f"Error with normal pattern: {regex_error}")
        normal_matches = []

    # With raw string
    raw_matches = re.findall(raw_pattern, text)

    print(f"Normal pattern matches: {normal_matches}")
    print(f"Raw pattern matches: {raw_matches}")

# Example Usage:
demonstrate_raw_strings()
# Output:
# Normal pattern matches: ['100']
# Raw pattern matches: ['100']

# =============================================================================
# The Iterative Process of Writing Regex's
# =============================================================================
# Writing regex patterns is often an iterative process, refining patterns to
# eliminate false positives and negatives.

def iterative_regex_example(text: str) -> Tuple[List[str], List[str]]:
    """
    Demonstrate the iterative refinement of a regex pattern to match 'the'.

    Args:
        text (str): The text to search within.

    Returns:
        Tuple[List[str], List[str]]: Matches before and after refinement.
    """
    # Initial pattern: matches 'the', case-sensitive
    initial_pattern = r"the"
    initial_matches = find_all_matches(initial_pattern, text)

    # Refined pattern: matches 'the' or 'The', whole words only
    refined_pattern = r"\b[Tt]he\b"
    refined_matches = find_all_matches(refined_pattern, text)

    return initial_matches, refined_matches

# Example Usage:
regex_text = "The theater is near the cathedral. Then, they left."
initial, refined = iterative_regex_example(regex_text)
print(f"Initial matches: {initial}")
print(f"Refined matches: {refined}")
# Output:
# Initial matches: ['the', 'the', 'the']
# Refined matches: ['The', 'the']

# =============================================================================
# False Positives and False Negatives
# =============================================================================
# When crafting regex patterns, it's important to consider and minimize both false positives and negatives.

def analyze_false_positives_negatives(text: str) -> None:
    """
    Analyze false positives and negatives in regex matching.

    Args:
        text (str): The text to analyze.
    """
    pattern = r"\b[Tt]he\b"
    matches = find_all_matches(pattern, text)

    # Evaluate matches
    for match in matches:
        print(f"Matched: {match}")

    # Potential false negatives
    print("Checking for false negatives...")
    if "THE" in text:
        print("False negative found: 'THE' was not matched.")

# Example Usage:
fp_fn_text = "The theme of the event was theater. THE is not matched."
analyze_false_positives_negatives(fp_fn_text)
# Output:
# Matched: The
# Matched: the
# Checking for false negatives...
# False negative found: 'THE' was not matched.

# =============================================================================
# Main Execution
# =============================================================================
# The code above can be executed as part of a larger NLP processing pipeline.
# Ensure functions are called appropriately and handle exceptions.




if __name__ == "__main__":
    # Demonstration of regex functions
    print("\n--- Demonstrate Disjunction ---")
    demonstrate_disjunction(animal_text)

    print("\n--- Demonstrate Negation ---")
    demonstrate_negation(negation_text)

    print("\n--- Demonstrate Aliases ---")
    demonstrate_aliases(number_text)

    print("\n--- Demonstrate Complex Disjunction ---")
    demonstrate_complex_disjunction(plural_text)

    print("\n--- Demonstrate Wildcards ---")
    demonstrate_wildcards(wildcard_text)

    print("\n--- Demonstrate Anchors ---")
    demonstrate_anchors(log_text)

    print("\n--- Demonstrate Raw Strings ---")
    demonstrate_raw_strings()

    print("\n--- Iterative Regex Example ---")
    iterative_regex_example(regex_text)

    print("\n--- Analyze False Positives and Negatives ---")
    analyze_false_positives_negatives(fp_fn_text)