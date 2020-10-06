punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(string):
    for char in punctuation_chars:
        string = string.replace(char,"")
    return string

# lists of words to use
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
    for i in string.split():
        if i in positive_words:
            count += 1
    #print(count)
    return count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(string):
    #print(string)
    count = 0
    string = string.lower()
    string = strip_punctuation(string)
    for i in string.split():
        if i in negative_words:
            count += 1
    #print(count)
    return count


TwitterFile = open("project_twitter_data.csv","r")
resultant = open("resulting_data.csv","w")
resultant.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
resultant.write("\n")
lines = TwitterFile.readlines()
print(type(lines))
header_not_req= lines.pop(0)
print(header_not_req)
for line in lines:
    lists = line.strip().split(',')
    posc = get_pos(lists[0])
    negc = get_neg(lists[0])
    net = posc - negc
    row = "{}, {}, {}, {}, {}".format(lists[1], lists[2], posc, negc, net)
    resultant.write(row)
    resultant.write("\n")
    #sys.setExecutionLimit(20000)
TwitterFile.close()
resultant.close()
