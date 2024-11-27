class FiniteStateAutomaton:
    def __init__(self):
        # Define the states
        self.states = {'q0', 'q1', 'q2'}
        self.start_state = 'q0'
        self.accept_states = {'q2'}
        self.current_state = self.start_state

        # Define the transition function as a dictionary
        self.transition = {
            ('q0', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q1', 'a'): 'q1',  # Allow repetition of 'a'
            ('q2', 'a'): 'q1',  # Reset if 'a' follows 'ab'
            ('q2', 'b'): 'q0'   # Reset on other patterns
        }

    def reset(self):
        """Reset the automaton to the start state."""
        self.current_state = self.start_state

    def process_input(self, input_string):
        """Process an input string to determine if it's accepted."""
        self.reset()
        for char in input_string:
            # Transition to the next state if the transition exists
            if (self.current_state, char) in self.transition:
                self.current_state = self.transition[(self.current_state, char)]
            else:
                # If no valid transition exists, move to an invalid state
                self.current_state = None
                break

        # Check if the current state is an accept state
        return self.current_state in self.accept_states


# Example usage
if __name__ == "__main__":
    fsa = FiniteStateAutomaton()

    # Test strings
    test_strings = ["a", "ab", "aaab", "xyz", "abab", "aabbab"]

    for string in test_strings:
        if fsa.process_input(string):
            print(f"'{string}' is ACCEPTED by the automaton.")
        else:
            print(f"'{string}' is REJECTED by the automaton.")
