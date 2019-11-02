filename = "KJV.txt"

def get_file(filename):
    with open(filename) as f:
        for line in f.readlines():
            yield line[0:-1]


data = get_file(filename)

def get_word_count(data):
    count = 0
    for line in data:
        word = line.replace("\t", " ").split(" ")
        count += len(word)
    return count
print(get_word_count(data))
