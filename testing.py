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
