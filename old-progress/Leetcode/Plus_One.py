class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digt = ""
        for i in digits:
            str_digt += str(i)
        str_digt = int(str_digt) + 1
        return [int(i) for i in str(str_digt)]