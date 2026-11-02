class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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