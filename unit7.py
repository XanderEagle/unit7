# by Xander Eagle
# November 14, 2019
# this program encodes a would input by the user by shifted the alphabet however many times the user wants

alphabet = "abcdefghijklmnopqrstuvwxyz"
user_shift = int(input("How many shifts do you want to make to the alphabet?"))
first = alphabet[:user_shift]
second = alphabet[user_shift:]
second_alphabet = second + first

user_word = input("What word or frase would you like to decode/encode?")
user_word = user_word.lower()
encoded_word = ""
for x in user_word:
    if x not in alphabet:
        encoded_word += x
    else:
        position = alphabet.index(x)
        encoded_word += second_alphabet[position]

decoded_word = ""
for y in encoded_word:
    if y not in alphabet:
        decoded_word += y
    else:
        position = alphabet.index(y)
        decoded_word += second_alphabet[position]
print("Your decoded word is:", decoded_word,)
print("Your encoded word is:", encoded_word)
print("You are now on you way to becoming a hacker. Good luck and don't go to prison!")
