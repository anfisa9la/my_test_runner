class File:

    def __init__(self, file_dir):
        self.file_dir = file_dir

    def open_file(self):
        with open(self.file_dir, mode='r', encoding='latin1') as file:
            return file.read()

    def rtf_to_text(self):
        from striprtf.striprtf import rtf_to_text
        rtf = self.open_file()
        text = rtf_to_text(rtf)
        print(text)
