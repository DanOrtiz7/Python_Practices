def compress(word):
    i = 0
    list=[]
    while( i < len(word)) :
        count = 1
        while word[i] == word[i - 1] :
            i += 1
            count += 1
            if i  == len(word):
                break
         
        node= (str(word[i]) + str(count))
        list.append(node)
        i += 1
    print(list)
    print()

compress("cool")
compress("Leonardo")