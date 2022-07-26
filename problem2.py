file = open ("words.txt", "r")

Long = []

Palin = []


def palin(s):
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
        
print "Number of long words(more than 18 letters): ", count
for i in range(0, len(Long), 3):
    print Long[i], ",\t", Long[i+1], ",\t", Long[i+2], "\n"
