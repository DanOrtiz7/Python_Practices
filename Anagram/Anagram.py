def is_anagram(str1, str2):
    if len(str1) != len(str2):
        print("False") 
    elif (sorted(str1) == sorted(str2)):
        print("True")
    else:
        print("False")
        
is_anagram("apple", "Pear")
is_anagram("listen", "silent")
is_anagram("bad", "dad")
word1 = input("Enter the first word to compare:")
word2 = input("Enter the second word to compare:")
is_anagram(word1, word2)