# put your python code here

list_ = input().split()
numb = input()
output = []
counter = 0
for each in list_:
    if each == numb:
        output.append(str(counter))
    counter += 1
if numb in list_:
    print(" ".join(output))
else:
    print("not found")
