class Solution:
    def checkRecord(self, s: str) -> bool:
        if "LLL" not in s and s.count("A") < 2:
            return True
        else:
            return False