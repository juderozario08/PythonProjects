import gzip
from math import ceil


def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)


# print(factorial(5))


def oddBananza(ls):
    # If the list length is 0 then return 0 (exit clause 1)
    if len(ls) == 0:
        return 0
    # If the list length is 1 then return the condition provided by the problem
    if len(ls) == 1:
        return 10-(ls[0] % 10)
    # Else do the recursive call and multiply the condition with it
    return (10-(ls.pop() % 10))*oddBananza(ls)


# print(oddBananza([1, 3, 5]))


def oddBananzaComp(ls):
    # If the list length is 0 then return 0 (exit clause 1)
    if len(ls) == 0:
        return 0
    # If the list length is 1 then return the condition provided by the problem
    if len(ls) == 1:
        return 10-(ls[0] % 10)
    # Else do the recursive call and multiply the condition with it
    secondHalf = [ls.pop() for i in range(len(ls)//2)]
    return oddBananzaComp(ls)*oddBananzaComp(secondHalf)


# x = "sara"
# print("   x    x\nx xx x\nx   x   x".replace("x", x))
# for i in range(5):
#     print(" "*i+x+" "*(9-i*2), x)
# print(" "*6, x)
def bowTie(h):
    print(
        ''.join(['*'*(2*i + 1) + ' '*2*(h - (2*i + 1)) + '*'*(2*i + 1)+'\n' for i in range(h//2 + 1)]) + ''.join(
            ['*'*(2*i + 1) + ' '*2*(h - (2*i + 1)) + '*'*(2*i + 1)+'\n' for i in range(h//2 - 1, -1, -1)]))


R = []
vowels = 'aeiou'
for verse in [[input() for j in range(4)] for i in range(int(input()))]:
    for line in verse:
        lastWord = line.split(" ")[-1].lower()
        result = ''
        for character in range(len(lastWord)-1, -1, -1):
            result += lastWord[character]
            if lastWord[character] in vowels:
                break
        R.append(result)
    if R[0] == R[1] == R[2] == R[3]:
        print('perfect')
    elif R[0] == R[1] and R[2] == R[3]:
        print('even')
    elif R[0] == R[3] and R[1] == R[2]:
        print('shell')
    elif R[0] == R[2] and R[1] == R[3]:
        print('cross')
    else:
        print('free')
    R.clear()

if __name__ == '__main__':
    bowTie(int(input()))
