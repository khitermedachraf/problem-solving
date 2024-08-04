# Given an array, , of size  distinct elements, sort the array in ascending order using the Bubble Sort algorithm above.

def bubbleSorting(n, a):
    totalSwapsNumber = 0

    for i in range(0, n):
        swapsNumber = 0

        for j in range(0, n - 1):
            if a[j] > a[j + 1]:
                intermediate = a[j]
                a[j] = a[j + 1]
                a[j + 1] = intermediate
                # swap
                swapsNumber += 1

        totalSwapsNumber += swapsNumber
        if swapsNumber == 0:
            print(f"Array is sorted in {totalSwapsNumber} swaps.")
            print(f"First Element: {a[0]}")
            print(f"Last Element: {a[-1]}")
            break

    # test


bubbleSorting(4, [4, 3, 2, 1])
