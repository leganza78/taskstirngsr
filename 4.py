slovaк = input()
min = slovaк
max = slovaк
y = 'ДА'
n = 'НЕТ'
while True:
    slovaк = input()
    if slovaк == 'стоп':
        if len(set(min) - set(max)) == 0:
            print(y)
            break
        else :
            print(n)
            break

    if len(slovaк) > len(max):
        max = slovaк
    if len(slovaк) < len(min):
        min = slovaк
