class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1
        """
        :type num: int
        :rtype: bool
        """
        