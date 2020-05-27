dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
words = input().split()
wrong_list = []
for word in words:
    if word not in dictionary:
        wrong_list.append(word)
        print(word)
if not wrong_list:
    print("OK")
