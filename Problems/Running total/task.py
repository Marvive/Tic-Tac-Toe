x = input()
int_list = [int(nums) for nums in x]
accum = [sum(int_list[:i + 1]) for i in range(len(int_list))]
print(accum)
