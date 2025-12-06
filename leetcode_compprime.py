import math

class Solution(object):
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def completePrime(self, num):
        s = str(num)

        
        if not self.is_prime(num):
            return False

       
        for k in range(1, len(s)):
            if not self.is_prime(int(s[:k])):
                return False

        
        for k in range(1, len(s)):
            if not self.is_prime(int(s[k:])):
                return False

        return True
