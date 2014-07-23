class OptionalInstall(object):

    def __init__(self, prompt_text, skip_text, action):
        self.prompt_text = prompt_text
        self.skip_text = skip_text
        self.action = action

    def run(self):
        user_input = raw_input(self.prompt_text)
        if user_input == 'Y':
            self.action()
        else:
            print(self.skip_text)
