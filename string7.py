user_sentence = input("Enter a sentence: ")
list_of_words = user_sentence.split(" ")
for x in range(len(list_of_words)):
    if len(list_of_words[x]) == 4:
        list_of_words[x] = "#$%@"
new_sentence = " ".join(list_of_words)
print(new_sentence)
