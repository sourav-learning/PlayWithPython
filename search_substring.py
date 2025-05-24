sentence = input("Enter a sentence : ")
sub_string = input("Enter a substring to search in the above sentence : ")
pos = -1
length = len(sentence)
found = False
while True:
    pos = sentence.find(sub_string,pos+1,length)
    if(pos == -1):
        break
    else:
        print("The substring ", sub_string, " is found in position ", pos)
        found = True
if not found:
    print("No occurrence of substring : ", sub_string)