def is_anagram(str1, str2):
    if len(str1) != len(str2):
        isAnagram = False
    elif (sorted(str1) == sorted(str2)):
        isAnagram = True
    else:
        isAnagram = False
    return isAnagram
is_anagram("apple", "Pear")
is_anagram("listen", "silent")
is_anagram("bad", "dad")
