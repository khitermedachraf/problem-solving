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
