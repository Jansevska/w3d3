# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:				
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

def solution(ransomeNote, magazine):
#loop through magazine string to find characters
    for char in ransomeNote:
        # for i in magazine:
        if char not in magazine:
            return False
        else:
            magazine = magazine.replace(char, ' ', 1)
    return True


from collections import Counter
def solution(ransom, magazine):
    ransom_count = Counter(ransom)
    magazine_count = Counter(magazine)
    for letter, count in ransom_count.items():
        if magazine_count.get(letter, 0) < count:
            return False
    return True

def solution(ransomeNote, magazine):
    note = dict(Counter(ransomeNote))
    mag = dict(Counter(magazine))
    res = True
    for char, val in note.items():
        if not mag.get(char, 0) >= note[char]:
            res = False
    return res