class FiniteStateMachine:
    def __init__(self):
        # States and transitions
        self.start_state = 'q0'
        self.current_state = self.start_state
        self.transitions = {
            'q0': self.handle_base_case,
            'q1': self.handle_ends_with_y,
            'q2': self.handle_ends_with_special,
            'q3': self.handle_irregular_nouns
        }
        self.irregular_nouns = {
            'child': 'children',
            'man': 'men',
            'woman': 'women',
            'tooth': 'teeth',
            'foot': 'feet',
            'mouse': 'mice',
            'goose': 'geese'
        }
        self.special_endings = ['s', 'x', 'z', 'sh', 'ch']

    def handle_base_case(self, noun):
        """Handles default pluralization."""
        if noun in self.irregular_nouns:
            return 'q3'  # Transition to irregular handling
        elif any(noun.endswith(suffix) for suffix in self.special_endings):
            return 'q2'  # Transition to special endings
        elif noun[-1] == 'y' and not noun[-2] in 'aeiou':
            return 'q1'  # Transition to ends-with-y rule
        else:
            return None  # Stay in base case

    def handle_ends_with_y(self, noun):
        """Replace 'y' with 'ies' for nouns ending in consonant + 'y'."""
        return noun[:-1] + 'ies'

    def handle_ends_with_special(self, noun):
        """Add 'es' for nouns ending in s, x, z, sh, ch."""
        return noun + 'es'

    def handle_irregular_nouns(self, noun):
        """Handle irregular plural forms."""
        return self.irregular_nouns[noun]

    def process(self, noun):
        """Process the noun through the FSM."""
        while True:
            # Get the next state
            next_state = self.transitions[self.current_state](noun)

            # If there's no transition, assume default case
            if next_state is None:
                self.current_state = 'q0'
                return noun + 's'
            
            # If a specific transformation is returned, apply it
            if isinstance(next_state, str) and not next_state.startswith('q'):
                return next_state
            
            # Otherwise, move to the next state
            self.current_state = next_state


# Example usage
if __name__ == "__main__":
    fsm = FiniteStateMachine()
    test_nouns = ["cat", "dog", "baby", "class", "church", "box", "child", "man", "goose"]

    print("Plural Forms:")
    for noun in test_nouns:
        plural = fsm.process(noun)
        print(f"{noun} → {plural}")

