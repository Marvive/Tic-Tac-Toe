# x = "lower camel case".split()
x = input().split()
counter = 0
for each in x:
    if each is not x[0]:
        x[counter] = each.title()
    counter += 1
out = "".join(x)
print(out)
