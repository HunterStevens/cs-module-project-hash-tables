# Your code here
import operator
with open("robin.txt") as r:
    words = r.read()

def histo(s):
    count = {}
    s = s.lower()
    word = ''

    for i in s:
        if i.isalnum():
            word += i
        elif i == "'":
            word += i
        elif i == "\r" or i == "\n" or i == "\t" or i == " ":
            if word in count:
                count[word] += '#'
                word = ''
            else:
                count[word] = '#'
                word = ''
    if '' in count:
        count.pop("")
    if word != '':
        if word in count:
            count[word] += '#'
        else:
            count[word] = '#'
    sorted_histo = sorted(count.items(), key = operator.itemgetter(1), reverse = True)
    for i in sorted_histo:
        print(i)

histo(words)
