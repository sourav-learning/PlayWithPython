word = input("Enter a word : ")
reverse_word = word[::-1]
#ignore case while comparing
if word.lower() == reverse_word.lower():
    print("The word is palindrome.")
else:
    print("The word is not palindrome.")