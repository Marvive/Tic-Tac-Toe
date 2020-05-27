height = int(input())
count = 1
for i in range(0, height):
    print((" " * (height - i - 1)) + "#" * count + (" " * (height - i)))
    count += 2
