class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        original = x
        reversed_num = 0

        while x > 0:
            last_digit = x % 10          # get the last digit
            reversed_num = reversed_num * 10 + last_digit   # build the reversed number
            x = x // 10                    # remove the last digit

        return original == reversed_num


        