words = input()
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for alph in alpha :
    words = words.replace(alph,'.')
print(len(words))