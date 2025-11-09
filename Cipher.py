import string
alphabet = string.ascii_lowercase + string.ascii_lowercase
print("𝓐𝓵𝓱𝓪𝓶𝔃𝓪  𝓒𝓪𝓮𝓼𝓪𝓻 𝓒𝓲𝓹𝓱𝓮𝓻 𝓽𝓸𝓸𝓵")
input("Press Enter To Start ! ")
word = input("Enter the word you want to encrypt : ").lower()
key =int(input("Enter the key :"))
encrypted_word = ""
for letter in word :
    original_position = alphabet.index(letter)
    new_position = original_position+key
    encrypted_word += alphabet[new_position]

print(f"The encrypted word : {encrypted_word}")
