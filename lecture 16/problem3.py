file = open ("words.txt", "r")

Long = []
Palin = []


def sel(s):
    start = 0
    end = len(s) - 1
    for i in range (len(s)/2):
        if s[start] != s[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

count = 0
c = 0
for word in file:
    word = word.strip()
    if (palin(word) == True):
        c += 1
        Palin.append(word)
    if (len(word) > 18):
        count += 1
        Long.append(word)
        
print "**************************************"
print "Number of long words(more than 18 letters): ", count
print "--------------------------------------\n"
for i in range(0, len(Long), 3):
    print Long[i], ",\t", Long[i+1], ",\t", Long[i+2], "\n"
print "**************************************\n"
print "Total Palindroms: ", c
print "--------------------------------------\n"
for x in range(0, len(Palin), 7):
    print Palin[x], ",   ", Palin[x+1], ",   ", Palin[x+2], ",   ", Palin[x+3], ",   ", Palin[x+4], ",   ", Palin[x+5], ",   ", Palin[x+6] 
print "**************************************\n"
raw_input("<Press Enter>")
