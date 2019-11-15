# by Xander Eagle
# November 15, 2019

# this program encodes or decodes a word or frase input by the user by shifting the alphabet...
# ...however many times the user wants


def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    user_shift = int(input("How many shifts do you want to make to the alphabet?"))  # user chooses the number of shifts
    first = alphabet[:user_shift]
    second = alphabet[user_shift:]
    second_alphabet = second + first
    user_word = input("What word or frase would you like to decode/encode?")  # user chooses the word to be encoded
    user_word = user_word.lower()
    encoded_word = ""
    for x in user_word:  # encodes the word
        if x not in alphabet:
            encoded_word += x
        else:
            position = alphabet.index(x)
            encoded_word += second_alphabet[position]

    decoded_word = ""
    for y in encoded_word:  # decodes the word
        if y not in alphabet:
            decoded_word += y
        else:
            position = second_alphabet.index(y)
            decoded_word += alphabet[position]
    print("Your encoded word is:", encoded_word)
    print("Your decoded word is:", decoded_word,)
    print("You are now on you way to becoming a hacker. Good luck and don't go to prison!")


main()
