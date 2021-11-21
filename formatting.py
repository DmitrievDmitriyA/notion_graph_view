

# Helps to format text for node rendering in yEd
def beautify(text):
    words = text.split()

    line = []
    strings = []

    for i in range(len(words)):
        word = words[i]

        line.append(word)
        if len(line) == 5 or i == len(words)-1:
            new_string = ' '.join(line)
            new_string += '\n'
            strings.append(new_string)
            line = []

    width = max([len(string) for string in strings]) * 7
    height = len(strings) * 15

    content = ""
    for string in strings:
        content += string

    return (width, height, content)
