def no_dups(s):
    # Your code here
    new_s = []
    word = ''
    s = s.lower()

    for i in s:
        if i.isalnum():
            word += i
        elif i== "'":
            word += i
        elif i == "\n" or i == " ":
            if word in new_s:
                word = ''
            else:
                new_s.append(word)
                word = ''
    if '' in new_s:
        new_s.pop('')
    if word != '':
        if word in new_s:
            word = ''
        else:
            new_s.append(word)
        complete = " "
        return (complete.join(new_s))
    else:        
        complete = " "
        return (complete.join(new_s))

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))