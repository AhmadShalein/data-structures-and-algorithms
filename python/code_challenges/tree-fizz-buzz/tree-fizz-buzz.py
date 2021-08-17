class Node():
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class binary_tree():
    def __init__(self):
        self.root = None
        self.output = []

    def pre_order(self, root):
        # root >> left >> right
        pre_order_output=[]
        if root:
            pre_order_output.append(root.value)
            pre_order_output = pre_order_output + self.pre_order(root.left)
            pre_order_output = pre_order_output + self.pre_order(root.right)
        return pre_order_output

    def in_order(self, root):
        # left >> root >> right
        in_order_output=[]
        if root:
            in_order_output = self.in_order(root.left)
            in_order_output.append(root.value)
            in_order_output = in_order_output + self.in_order(root.right)
        return in_order_output
  
    def post_order(self, root):
        # left >> right >> root
        post_order_output=[]
        if root:
            post_order_output = self.post_order(root.left)
            post_order_output = post_order_output + self.post_order(root.right)
            post_order_output.append(root.value)
        return post_order_output
        
def fizzBuzz(node):
    if node.value % 15 == 0:
        return'FizzBuzz'
    elif node.value %3 == 0:
        return'Fizz'
    elif node.value % 5 == 0:
        return'Buzz'
    else:
        return str(node.value)

def FizzBuzzTree(tree):
    if not tree.root:
        return []
    new_binary_tree = binary_tree()
    def traverser(node):
        new_binary_tree.output = new_binary_tree.output + [fizzBuzz(node)]
        if node.left:           
            traverser(node.left)
        if node.right:
            traverser(node.right)
        return new_binary_tree.output
    return traverser(tree.root) 

if __name__ == "__main__":
    bt = binary_tree()
    bt.root = Node(12)
    bt.root.left = Node(7)
    bt.root.right = Node(5)
    bt.root.left.right = Node(6)
    bt.root.left.left = Node(8)
    bt.root.right.right=Node(9)
    bt.root.right.right.left=Node(4)
    bt.root.left.left.right=Node(5)
    bt.root.left.right.left = Node(11)
    print (FizzBuzzTree(bt))
