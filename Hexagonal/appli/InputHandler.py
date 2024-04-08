class InputHandler:
    def __init__(self, prompt):
        self.prompt = prompt

    @staticmethod
    def get_input(prompt):
        return input(prompt).lower()
