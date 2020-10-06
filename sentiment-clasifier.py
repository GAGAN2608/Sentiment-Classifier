punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(string):
    for char in punctuation_chars:
        string = string.replace(char,"")
    return string
