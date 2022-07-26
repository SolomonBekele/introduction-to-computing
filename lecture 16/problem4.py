from string import punctuation

text = open("emma.txt").read()


text = text.lower()
for p in punctuation:
    text = text.replace(p, '')
words = text.split()


d = {}
for w in words:
    if w in d and 3 <= len(w) <= 10:
        d[w] = d[w] + 1
    elif w not in d and 3 <= len(w) <= 10:
        d[w] = 1

adder = []
items = list(d.items())
items = [(i[1], i[0]) for i in items]
items.sort()
for i in items:
    adder = adder + [i]
    adder.sort(reverse=True)
for things in adder[:15]:
    print(things)

print("")
count = 0
for big in words:
    if len(big) > 20:
        count += 1
        print(big)

print("\nthere are", count, "words that are longer than 20 letters")
