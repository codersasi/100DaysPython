TEMPLATE_INPUT_PATH = "./Input/Letters/starting_letter.txt"
NAMES_FILE = "./Input/Names/names.txt"
OUTPUT_READY_PATH = ".\\Output\\ReadyToSend\\"


class MailMerger:
    def __init__(self):
        self.template = None
        self.names = []

    def read_template(self):
        with open(TEMPLATE_INPUT_PATH) as file:
            self.template = file.read()

    def read_names(self):
        with open(NAMES_FILE) as file:
            self.names = file.readlines()

    def generate_mail(self):
        for name in self.names:
            new_letter = self.template
            name = name.strip()
            new_letter = new_letter.replace("[name]", name)
            file_name = OUTPUT_READY_PATH + name
            print(file_name)
            with open(file_name, mode="w") as file:
                file.write(new_letter)


mail_merger = MailMerger()
mail_merger.read_template()
mail_merger.read_names()
mail_merger.generate_mail()
