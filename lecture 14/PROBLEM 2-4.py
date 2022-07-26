def triple(n):
    for i in range(len(n)-2):
        if n[i] == n[i+1] and n[i] == n[i+2]:
            return True
    return False

file = open("words.txt", "r")
count = 0
for word in file:
    word = word.strip()
    if len(word) < 3:
        continue
    if triple(word):
        count += 1
        print word
print count
file.close()
print "no. of words = ", count
