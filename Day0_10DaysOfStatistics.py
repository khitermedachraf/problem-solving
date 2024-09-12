# Read the first line (number of elements, although we might not need to use it directly)
import math
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


# Calculate the weighted mean
def weightedMean(x, w):
    # Element-wise multiplication
    result = [a * b for a, b in zip(x, w)]
    return round(sum(result) / sum(w), 1)


# Day1: Standard Deviation
def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    sum = 0
    for number in arr:
        sum += number

    mean = round(sum / len(arr), 1)
    newArr = [math.pow(element - mean, 2) for element in arr]
    sum = 0
    for number in newArr:
        sum += number

    return round(math.sqrt(sum / len(newArr)), 1)


# Day1 find the Quartiles
# Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.
def getMedian(arr):
    # Sort the list in ascending order
    n = len(arr)
    # Step 3 & 4: Calculate the median
    if n % 2 == 1:  # Odd number of elements
        return arr[n // 2]
    else:  # Even number of elements
        return (arr[(n // 2) - 1] + arr[n // 2]) / 2


def quartiles(arr):
    # Write your code here
    n = len(arr)
    arr.sort()
    q2 = getMedian(arr)
    q1 = q3 = 0
    if len(arr) % 2 == 1:  # Odd number of elements
        q1 = getMedian(arr[0: n // 2])
        q3 = getMedian(arr[n // 2 + 1:])
    else:
        q1 = getMedian(arr[0: n // 2])
        q3 = getMedian(arr[n // 2:])
    return [q1, q2, q3]


# Day1: Find Interquartile Range
def interQuartile(values, freqs):
    # Define the values and their frequencies
    s = [value for value, freq in zip(values, freqs) for _ in range(freq)]
    s.sort()
    [a, b, c] = quartiles(s)
    return c - a
