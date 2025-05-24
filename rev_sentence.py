sentence = input("Enter a word or phrase or sentence : ")
rev_sentence = ''
pos = len(sentence) - 1
# the complex way
while pos >= 0:
    rev_sentence = rev_sentence + sentence[pos]
    pos-=1
print("The reversed sentence : ", rev_sentence)

#the easy way
print("The reversed sentence in the easy way : ", sentence[::-1])

#another easy way
print("Reversed using another easy way : ", ''.join(reversed(sentence)))