import nltk # add (natural language tool kit) via poetry
import string

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names
word_list = words.words()
name_list = names.words()

# ARGUMENTS THAT WE WILL PASS TO OUR ENCRYPTED FUNCTION
message1 = "hello"
message2 = "Go to sleep"
message3 = "The fox jumps over the red fence"
message4 = "#$$^&"

# IMPORT THE ALPHABET CHARACTERS STRING AND CONVERT TO A LIST
alphabet_string_upper = string.ascii_uppercase # bring in our alphabet string (uppercase)
alphabet_string_lower =  string.ascii_lowercase #bring in our alphabet string (lowercase)
alphabet_list_lower = list(alphabet_string_lower)  #convert the lowercase alphabet string to a list
alphabet_list_upper = list(alphabet_string_upper) # convert the uppercase alphabet string to a list
print(alphabet_list_lower)
print(alphabet_list_upper)


# CREATE A FUNCTION THAT WILL ENCRYPT OUR TEXT WITH A GIVEN KEY, AND RETURN THE ENCRYPTED TEXT AS A STRING
def encrypt(plain_text, key):
    encrypted_text = ''
    print(f'The plain text letter is: {encrypted_text}')

    for letter in plain_text: #iterate through word
        if letter not in alphabet_list_lower and letter not in alphabet_list_upper:
            plain_text += letter
        elif letter in alphabet_list_upper:
            x = alphabet_list_upper.index(letter)
            y = (x + key) % 26
            encrypted_text += alphabet_list_upper[y]
        else:
            x = alphabet_list_lower.index(letter)
            y = (x + key) %26
            encrypted_text += alphabet_list_lower[y]
    # print(encrypted_text)
    return encrypted_text
        
def decrypt(encoded, key):
    return encrypt(encoded, - key)

def crack(encoded):
    pass

if __name__ == "__main__":
    print(encrypt(message1, 6)) #89
    print(encrypt(message2, 4)) #67
    print(encrypt(message3, 7)) #90
    print(encrypt(message4, 5))
    print(decrypt('nkrru', 6))
    # print(decrypt(Ksxswpiit, 4))