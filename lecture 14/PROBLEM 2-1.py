f = open("words.txt","r")
count = 0
for word in f:
    word = word.strip()
    if len(word) > 18:
        count += 1
        print word
print "no. of words = ", count
