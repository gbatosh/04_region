def polindrome(word):
    word1=word[::-1]
    #or we can use reverse function
    if word1 == word:
        print("YES")
    else: print("NO")
polindrome("madap")
    