import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1,100))
print(numbers)
left = 0
right = len(numbers) -1 

while left <= right:
    mid = (left + right) // 2
    if mid == 0 or numbers[mid] >= numbers[mid - 1] and mid == len(numbers) - 1 or numbers[mid] >= numbers[mid + 1]:
        print("We found a peak element at the position:", mid, " with value: ", numbers[mid])
        break
    elif mid>0 and numbers[mid] < numbers[mid -1]:
        right = mid -1
    else:
        left = mid +1
  
