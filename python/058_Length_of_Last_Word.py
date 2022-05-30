def lengthOfLastWord(s):
    s = s.strip()
    return len(s) - (s.rfind(" ") + 1)