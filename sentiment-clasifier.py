punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(string):
    for char in punctuation_chars:
        string = string.replace(char,"")
    return string
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(string):
    #print(string)
    count = 0
    string = string.lower()
    string = strip_punctuation(string)
    for i in positive_words:
            for j in string.split():
                if i == j:
                    count += 1
    #print(count)
    return count
