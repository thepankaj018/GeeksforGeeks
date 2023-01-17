def PalinArray(arr ,n):
    empty_list = []
    for i in range(n):
        if str(arr[i]) == str(arr[i])[::-1]:
            empty_list.append(1)
        else:
            empty_list.append(0)
    return min(empty_list)
print(PalinArray([121,131,20],3))                            

        

