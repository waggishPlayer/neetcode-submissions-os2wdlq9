class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        check = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            check[char] = check.get(char, 0) + 1

        if(count == check):
            return True
        return False