class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for str_ in ransomNote:
            if not str_ in magazine:
                break
            else:
                magazine = magazine.replace(str_, '', 1)
        else:
            return True
        return False