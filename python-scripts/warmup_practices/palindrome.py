class Solution(object):
    def isPalindrome_string(self, x):
        """
        :type x: str
        :rtype: bool
        """
        if len(x) < 0:
            return False
        l = len(x) - 1
        for i in range(1, int(len(x) / 2) + 1):
            if x[i - 1] != x[-i]:
                return False
        return True

    def isPalindrome_int(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        x_origin = x
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            x = x // 10
        if rev != x_origin:
            return False
        return True

    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        c = int(len(x) / 2)
        if len(x) % 2 == 1:
            return x[0:c] == x[c + 1 : len(x)][::-1]
        else:
            return x[0:c] == x[c : len(x)][::-1]


if __name__ == "__main__":
    s = Solution()
    input_str = "sartas"
    print(s.isPalindrome_string(input_str))
    input_int = 12621
    print(s.isPalindrome_int(input_int))
