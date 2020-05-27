text = input()
words = text.split()

out = [word for word in words if "http" in word.lower() or "www." in word.lower()]
for i in out:
    print(i)
# for word in words:
    # finish the code here