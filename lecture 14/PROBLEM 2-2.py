
def check_palindrome(n):
    start = 0
    end = len(n) - 1
    for i in range(len(n)/2):
        if n[start] != n[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

file = open("words.txt", "r")
count = 0
for word in file:
    word = word.strip()
    if check_palindrome(word):
        count += 1
        print word
file.close()
print "no. of words = ", count
