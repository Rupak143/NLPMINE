# Define a simple grammar as a dictionary
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["the"], ["a"]],
    "N": [["dog"], ["cat"], ["ball"]],
    "V": [["chases"], ["sees"], ["eats"]],
}

def parse(tokens, non_terminal, pos=0):
    """
    Recursive function to perform top-down parsing.
    
    Parameters:
        tokens: list of input tokens (e.g., ["the", "dog", "chases", "a", "cat"])
        non_terminal: current non-terminal to expand
        pos: current position in the tokens list
    
    Returns:
        (success: bool, new_pos: int): whether parsing was successful and the new token position
    """
    if non_terminal not in grammar:
        # If the non-terminal is a terminal, match it directly
        if pos < len(tokens) and [tokens[pos]] == [[non_terminal]]:
            return True, pos + 1
        return False, pos

    # For each production of the non-terminal
    for production in grammar[non_terminal]:
        temp_pos = pos
        success = True

        for symbol in production:
            success, temp_pos = parse(tokens, symbol, temp_pos)
            if not success:
                break

        if success:
            return True, temp_pos

    return False, pos

def top_down_parser(input_string):
    """
    Wrapper function to parse an input string using the defined grammar.
    
    Parameters:
        input_string: a sentence (string) to parse
    
    Returns:
        success: whether the input string is valid according to the grammar
    """
    tokens = input_string.split()
    success, final_pos = parse(tokens, "S")
    return success and final_pos == len(tokens)

if __name__ == "__main__":
    # Input string to test
    test_sentences = [
        "the dog chases a cat",
        "a cat sees the ball",
        "the ball eats a dog",
        "dog chases the cat",
    ]

    # Parse each test sentence
    for sentence in test_sentences:
        print(f"Input: '{sentence}'")
        if top_down_parser(sentence):
            print("Result: Accepted\n")
        else:
            print("Result: Rejected\n")
