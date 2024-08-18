# Read the first line (number of elements, although we might not need to use it directly)
from collections import Counter

n = int(input())

# Read the second line (space-separated integers)
numbers = list(map(int, input().split()))
sum = 0
for number in numbers:
    sum += number

mean = round(sum / n, 1)

# Sort the list in ascending order
numbers.sort()
# Step 3 & 4: Calculate the median
if n % 2 == 1:  # Odd number of elements
    median = numbers[n // 2]
else:  # Even number of elements
    median = (numbers[(n // 2) - 1] + numbers[n // 2]) / 2


# Count the frequency of each number
frequency = Counter(numbers)

# Find the maximum frequency
max_freq = max(frequency.values())

# Find all numbers with this maximum frequency (handling multiple modes)
modes = [key for key, value in frequency.items() if value == max_freq]

print(mean)
print(median)
print(modes[0])