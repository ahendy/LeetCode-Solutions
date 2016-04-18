    def subsets(coins, pos, set):
        if pos == len(coins):
            doSomeWithSubset(set)
            return
        
        subsets(coins, pos+1, set)
        subsets( coins, pos+1, set+[coins[pos]])


subsets(lists, 0, [])


