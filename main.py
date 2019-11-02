import time

def get_file(filename):
    with open(filename) as f:
        for line in f.readlines():
            yield line[0:-1]

def get_word_count(data):
    count = 0
    for line in data:
        word = line.replace("\t", " ").split(" ")
        count += len(word)
    return count

def get_line_list(line):
    return line.replace("\t", " ").split(" ")

def remove_char(word):
    result = ''
    for ch in word:
        if ch not in (",.:;!?~ "):
            result += ch
    return result

def get_unique_count(data):
    word_count = {}
    for line in data:
        for word in get_line_list(line):
            word = remove_char(word.lower())
            if word.isdigit():
                continue
            elif word not in word_count.keys():
                word_count[word] = 1
            else:
                word_count[word] += 1
    return word_count

start = time.time()
filename = "KJV.txt"
data = get_file(filename)
# print(get_word_count(data))
new_data = get_unique_count(data)
end = time.time()
time_taken = end - start
print(new_data)
print(time_taken)
