#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value  # This calls the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):  # Check if NOT a string
            print("The value must be a string.")  # Print the error
            self._value = ""  # Reset value to empty string
        else:
            self._value = new_value



    def is_sentence(self):
        return self.value.endswith(".")
    

    def is_question(self):
        return self.value.endswith("?")
    
    def is_exclamation(self):
        return self.value.endswith("!")
    
    def count_sentences(self):
        import re
        # Split the string by sentence-ending punctuation followed by whitespace or end of string
        sentences = re.split(r'[.!?]+(?=\s|$)', self.value)
        # Filter out any empty strings resulting from the split
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
