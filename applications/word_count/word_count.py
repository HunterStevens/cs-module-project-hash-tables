def word_count(s):
    # Your code here
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
                count[word] += 1
                word = ''
            else:
                count[word] = 1
                word = ''
    if '' in count:
        count.pop("")
    if word != '':
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
        return count
    else: 
        return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))