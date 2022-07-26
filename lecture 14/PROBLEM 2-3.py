
def words_with_out_e(n):
    kira = True
    for i in range(len(n)):
        if n[i] == "e":
            flag = False
            break
    return kira

file = open("words.txt", "r")
count = 0
for word in file:
    word = word.strip()
    if words_with_out_e(word):
        count += 1

file.close()
print "no. of words = ", count
