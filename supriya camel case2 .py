X=input("")
def cam(word):
        import re
        return ' '.join(x.capitalize() or ' ' for x in word.split(' '))
print(cam(X))
