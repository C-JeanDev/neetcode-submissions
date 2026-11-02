class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        anagramma: dict = {}

        for letter in s:
            if letter in anagramma:
                anagramma[letter] += 1
            else: anagramma [letter] = 1

        for letter in t:
            if letter in anagramma:
                anagramma[letter] -= 1
            else: return False
            if anagramma[letter] == 0: del anagramma[letter]

        return len(anagramma) == 0