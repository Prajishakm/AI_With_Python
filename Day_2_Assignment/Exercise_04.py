def my_split(sentence, separator):
    result = []
    current = ""
    for char in sentence:
        if char == separator:
            result.append(current)
            current = ""
        else:
            current += char
    result.append(current)
    return result

def my_join(items, separator):
    result = ""
    for i in range(len(items)):
        result += items[i]
        if i != len(items) - 1:
            result += separator
    return result

sentence = input("Please enter sentence:")
words = my_split(sentence, " ")

comma_sentence = my_join(words, ",")
print(comma_sentence)

for word in words:
    print(word)