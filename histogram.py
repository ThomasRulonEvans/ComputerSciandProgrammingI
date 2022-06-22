def read_file_content(file):
    text_open = open("{}".format(file), "r")
    text = text_open.read().lower()
    return text

def build_letter_histogram():
