class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructFromPrePost(preorder,postorder):
    def makeTree():            
        node = TreeNode(postorder.pop())

        if node.val != preorder[-1]:
            node.right = makeTree()

        if node.val != preorder[-1]:
            node.left = makeTree()

        preorder.pop()
        return node

    return makeTree()