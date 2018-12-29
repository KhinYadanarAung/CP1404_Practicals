'''word_to_count = {}
words = input("Text: ").split()

for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

    print(word)

for key, value in sorted(word_to_count.items()):
    print(key, " : ", value)
'''
d = {'a': 3, 'b': 2, 'c': 1}
for k in sorted(list(d.keys())):
    print(k, d[k], sep='', end='')
