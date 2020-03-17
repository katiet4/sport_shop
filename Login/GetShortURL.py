from random import randint
def generateSURL(SandFURL):
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    newSurl = (letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)]+
                letters[randint(0,len(letters)-1)])
    while (SandFURL.objects.filter(codeURL = newSurl).exists()):
        newSurl = (letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)]+
                    letters[randint(0,len(letters)-1)])
    return newSurl
