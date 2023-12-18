s1 = input()
s2 = input()
bulls = 0
cows = 0
for i in set(s1) & set(s2):
    if len(s1) == len(s2):
        if s1.index(i) == s2.index(i):
            bulls +=1
        else: cows += 1
    else:
        print("неравное количество символов")
print('bulls:',bulls,'cows:',cows)
