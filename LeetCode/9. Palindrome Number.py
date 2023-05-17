class Solution:
    def isPalindrome(self, x: int) -> bool:
        answer = True
        temp = list(str(x))
        if temp[0:] == temp[::-1]:
            answer = True
        else:
            answer = False
        return answer
