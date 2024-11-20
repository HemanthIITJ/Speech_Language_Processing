"""
Advanced Concepts in NLP: Error Characterization and Regular Expressions with ELIZA Example

This script provides an in-depth explanation of error characterization in Natural Language Processing (NLP),
focusing on the trade-offs between coverage (recall) and accuracy (precision). It also delves into
advanced regular expression techniques in Python, such as substitutions, capture groups, non-capturing groups,
and lookahead assertions. Finally, it demonstrates these concepts by implementing a simple ELIZA-like chatbot.

Author: Kandimalla Hemanth
Date: November 2024
"""

import re
from typing import List, Pattern, Callable, Tuple

# Section 1: Characterizing Errors in NLP
"""
In NLP applications, reducing error rate involves balancing recall and precision:
1. **Recall**: Ensures relevant instances are captured (minimizing false negatives).
2. **Precision**: Ensures irrelevant instances are avoided (minimizing false positives).
Trade-offs are made depending on the application, e.g., medical systems prioritize recall over precision.
"""

# Section 2: Advanced Regular Expressions
"""
We explore advanced regex concepts like substitutions, capture groups, and lookahead assertions.
"""

def convert_colour_to_color(text: str) -> str:
    """
    Converts occurrences of 'colour' to 'color' in the given text.
    """
    return re.sub(r'colour', 'color', text)

def add_angle_brackets_around_numbers(text: str) -> str:
    """
    Encloses all numbers in angle brackets within the given text.
    """
    return re.sub(r'(\d+)', r'<\1>', text)

def match_repetitive_structure(text: str) -> bool:
    """
    Matches sentences of the form:
    'the [adjective]er they [verb], the [same adjective]er we [same verb]'
    """
    pattern = re.compile(r'the (.*)er they (.*), the \1er we \2', re.IGNORECASE)
    return bool(pattern.fullmatch(text.strip()))

def match_without_capturing(text: str) -> bool:
    """
    Matches phrases like 'some cats like some cats' but not 'some cats like some some'.
    """
    pattern = re.compile(r'^(?:some|a few) (people|cats) like some \1$', re.IGNORECASE)
    return bool(pattern.match(text.strip()))

def match_lines_not_starting_with_volcano(text: str) -> List[str]:
    """
    Extracts words at the beginning of each line that do not start with 'Volcano'.
    """
    pattern = re.compile(r'^(?!Volcano)([A-Za-z]+)', re.MULTILINE)
    return pattern.findall(text)

# Section 3: ELIZA Chatbot
"""
A simplified ELIZA chatbot uses regex patterns for matching user inputs and responding.
"""

reflections = {
    "am": "are", "was": "were", "i": "you", "i'd": "you would", "i'll": "you will",
    "i've": "you have", "i'm": "you are", "my": "your", "are": "am", "were": "was",
    "you've": "I have", "you'll": "I will", "you'd": "I would", "your": "my",
    "yours": "mine", "you": "I", "me": "you"
}

def reflect(fragment: str) -> str:
    """
    Reflects words in the fragment using the reflections mapping.
    """
    tokens = fragment.lower().split()
    return ' '.join(reflections.get(token, token) for token in tokens)

patterns: List[Tuple[Pattern[str], Callable[[re.Match], str]]] = [
    (re.compile(r'I need (.+)', re.IGNORECASE),
     lambda match: f"Why do you need {reflect(match.group(1))}?"),
    (re.compile(r'Why don\'t you (.+)\??', re.IGNORECASE),
     lambda match: f"Do you really think I don't {reflect(match.group(1))}?"),
    (re.compile(r'Why can\'t I (.+)\??', re.IGNORECASE),
     lambda match: f"Maybe you could {reflect(match.group(1))} if you tried."),
    (re.compile(r'I can\'t (.+)', re.IGNORECASE),
     lambda match: f"What makes you think you can't {reflect(match.group(1))}?"),
    (re.compile(r'I am (.+)', re.IGNORECASE),
     lambda match: f"How long have you been {reflect(match.group(1))}?"),
    (re.compile(r'I\'m (.+)', re.IGNORECASE),
     lambda match: f"Why are you {reflect(match.group(1))}?"),
    (re.compile(r'I feel (.+)', re.IGNORECASE),
     lambda match: f"Tell me more about feeling {reflect(match.group(1))}."),
    (re.compile(r'(.*)', re.IGNORECASE),
     lambda match: "Please tell me more.")
]

def get_eliza_response(user_input: str) -> str:
    """
    Generates a response based on the user's input using predefined patterns.
    """
    for pattern, response_function in patterns:
        match = pattern.fullmatch(user_input.strip())
        if match:
            return response_function(match)
    return "I'm not sure I understand. Can you elaborate?"

def eliza_chatbot():
    """
    A simple ELIZA-like chatbot that interacts with the user.
    """
    print("ELIZA: Hello. How are you feeling today?")
    try:
        while True:
            user_input = input("> ").strip()
            if user_input.lower() in {'quit', 'exit', 'bye'}:
                print("ELIZA: Goodbye. Take care!")
                break
            print(f"ELIZA: {get_eliza_response(user_input)}")
    except (KeyboardInterrupt, EOFError):
        print("\nELIZA: Goodbye. Take care!")

if __name__ == "__main__":
    eliza_chatbot()
