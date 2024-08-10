import re


class TestDataEmptyArray:
    def get_array(self):
        return []


class TestDataUniqueValues:
    def get_array(self):
        return [1, 2]

    def get_expected_result(self):
        return 0


class TestDataExactlyTwoDifferentMinimums:
    def get_Array(self):
        return [4, 2, 1, 2]

    def get_expected_result(self):
        return 3

    # DAY 28: work with regex to match emails end with @gmail.com, return the users in alphabitic order

    N = int(input().strip())
    # Regex pattern to match the required email format
    pattern = r'^[a-z\.]+@gmail\.com$'
    firstNames = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]

        if re.match(pattern, emailID):
            firstNames.append(firstName)

    firstNames.sort()
    print("\n".join(firstNames))


# Betwise And: Task
# Given set {1,2,3,...N} Find two integers, A and B (where A< B), from set  such that the value of A&B is the maximum possible and also less than a given integer K. In this case, & represents the bitwise AND operator.
# Function Description
# Complete the bitwiseAnd function in the editor below.
# bitwiseAnd has the following paramter(s):
# - int N: the maximum integer to consider
# - int K: the limit of the result, inclusive


def bitwiseAnd(n, k):
    # Write your code here
    maximum_value = 0
    for i in range(1, n+1):
        for j in range(i + 1, n+1):
            if k > i & j > maximum_value:
                maximum_value = i & j

    return maximum_value
