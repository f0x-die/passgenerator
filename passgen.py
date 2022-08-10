import random, string, pyperclip


n = int(256)

def passgen(n):
    all = list(string.ascii_letters)+ list(string.digits)+ list(string.punctuation)
    passph = []

    for i in range(n):
        tmp = random.choice(all)
        passph.append(tmp)
    res = "".join(passph)
    return res



pasgen = passgen(n)
pyperclip.copy(pasgen)
print('Your secure passphrase is: \n',pasgen, "\n \n The passphrase is automatically copied to the clipboard \n enjoy :) " )