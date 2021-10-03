a="jahnavi"
res=[a[i:j] for i in range(len(a))
        for j in range(i+1,len(a)+1)]
print(res)
"""
['j', 'ja', 'jah', 'jahn', 'jahna', 'jahnav', 'jahnavi', 'a', 'ah', 'ahn', 'ahna', 'ahnav', 'ahnavi', 'h', 'hn', 'hna', 'hnav', 'hnavi', 'n', 'na', 'nav', 'navi', 'a', 'av', 'avi', 'v', 'vi', 'i']
"""
