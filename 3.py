p=input("words?")
def frame(words):
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        (print('* {a:<{b}} *'.format(a=word, b=size)),'* {word} *')
    print('*' * (size + 4))
frame(p.split(" "))
