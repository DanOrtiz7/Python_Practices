def compress(word):
    i = 0
    
    while( i < len(word)) :
        count = 1
        while word[i] == word[i - 1] :
            i += 1
            count += 1
            if i  == len(word):
                break
         
        print(str(word[i]) + str(count),  
                          end = " ")
        i += 1
    print()

compress("cool")
compress("Leonardo")