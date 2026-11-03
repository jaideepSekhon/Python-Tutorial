# def increase(num):
#     return num+3

# result=increase(4)
# print(result*2)

def sum_positive(numbers):
    total=0
    for num in numbers:
        if num>0:
            total+=num

    return total

inputs=[[3, -1, 0, 8, -5, 2],[-4, -2]]

for input in inputs:
    print(sum_positive(input))