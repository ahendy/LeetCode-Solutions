def binaryTreePaths(self, root):

    def recurser(result, root, list):
        
        if root is None:
            return
        
        recurser(result, root.left, list + [root.val])
        recurser(result, root.right, list + [root.val])
    
        if not root.left and not root.right:
            result.append("->".join(map(str, list + [root.val])))
            
    result = []
    recurser(result, root, [])
    return result



if __name__ == '__main__':

    assert("leetcode"), "Fail"