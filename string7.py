alphabet = "abcdefghijklmnopqrstuvwxyz"
user_shift = int(input("How many shifts do you want to make to the alphabet?"))
first = alphabet[:user_shift]
second = alphabet[user_shift:]
second_alphabet = second + first
print(second_alphabet)

user_word = input("What word would you like to decode?")
for x in user_word:
    position = alphabet.index(x)
    print(second_alphabet[position])
