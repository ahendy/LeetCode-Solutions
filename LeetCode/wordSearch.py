import copy

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # new = copy.deepcopy(board)
        def recurse(i, j, curr, newboard):
            if len(curr) == len(word):
                return curr == word
            
            if i not in range(len(board)) or j not in range(len(board[0])) or newboard[i][j] == '@' or\
                len(curr) > len(word):
                return False 
            
            currlen = len(curr)
            if board[i][j] == word[currlen]:
                tmp = newboard[i][j]
                newboard[i][j] = '@'
                if any((recurse(i+1, j, curr + tmp, newboard),
                   recurse(i-1, j, curr + tmp, newboard),
                   recurse(i, j+1, curr + tmp, newboard),
                   recurse(i, j-1, curr + tmp, newboard))):
                    return True
                    
                newboard[i][j] = tmp
            
            
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if word[0] == board[i][j]:
                    newboard = (board)
                    ans = recurse(i, j, "", newboard)
                    if ans:
                        return ans
        return False
                

                
            
            
            
            
            
