class Soluion:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])

#This worked in leetcode idk if it would work in a IDE