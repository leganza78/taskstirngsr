nekot = int(input())
baza = []
for _ in range(nekot):
    baza.append(input())

for i, line in enumerate(baza):
    index = line.find("кот")
    if index != -1:
        print(i+1, index+1)
