

def is_anagram(s, t):
    if sorted(s) == sorted(t):
        return True
    return False
