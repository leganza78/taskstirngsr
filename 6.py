max = int(input())
n = int(input())

for i in range(n):
    title = input()
    if len(title) <= max:
        print(title)
    else:
        shortened_title = title[:max-3] + "..."
    print(shortened_title)
