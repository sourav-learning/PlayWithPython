sentence = input("Enter a sentence :")
vowels = ['a','e','i','o','u']
result = {}
for character in sentence:
    if character in vowels:
        result[character] = result.get(character,0) + 1

for k,v in result.items():
    print('The vowel ', k, ' appears ', v, ' times in the sentence')