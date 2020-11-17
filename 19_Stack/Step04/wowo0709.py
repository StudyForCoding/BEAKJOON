import sys
input = sys.stdin.readline

stack = []
while 1:
    sentence = input().rstrip()
    if len(sentence) == 1: sys.exit(0)
    for letter in sentence:
        if letter == '(' or letter == '[':
            stack.append(letter)
        elif letter == ')' or letter == ']':
            if not stack:
                print('no')
                break
            last_bracket = stack.pop()
            if (letter == ')' and last_bracket == '[')\
               or (letter == ']' and last_bracket == '('):
                print('no')
                break
        elif letter == '.':
            if not stack:
                print('yes')
            else: 
                print('no')
        else:
            continue
    stack.clear()