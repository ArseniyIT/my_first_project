text = input("введите текст можешь мешать рус и англ яз-->")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
counter = 0

for letter in text:
    if letter in alphabet:
        counter += 1

print(counter)