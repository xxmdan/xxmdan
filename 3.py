p=input("words?")
def frame(words):
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))
frame(p.split(" "))

