lines = int(input())

matches = [input().split() for n in range(lines)]
wins = [match[0] for match in matches if match[1] == "win"]


# output = []
# for inputs in range(lines):
#     entry = input()
#     if "win" in entry:
#         to_append = entry.split()
#         output.append(to_append[0])

print(wins)
print(len(wins))
