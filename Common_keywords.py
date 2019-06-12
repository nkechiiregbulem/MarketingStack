def common_keywords(a,b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set): 
        print(set(a), set(b)) 
    else: 
        print("No common elements") 
        

#enter seperate lists for both 'a' and 'b'
common_keywords(a,b)
