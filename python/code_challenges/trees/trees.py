class Node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

class binary_tree():
    def __init__(self):
        self.root = None

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
      
  
class binary_search_tree(binary_tree):
    def add(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return
        current = self.root
        while current:
            if current.value > value: 
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return
            if current.value < value:
                if current.left:
                   current = current.left
                else:
                    current.left = node
                    return

    def contains(self, value):
        if value == self.root:
            return True
        current = self.root
        while current:
            if current.value > value: 
                if current.right:
                   current = current.right
                else:
                    return False
            if current.value < value:
                if current.left:
                   current = current.left 
                else:
                    return False
            if current.value == value:
                return True  
        return False 

if __name__=="__main__":
    bt = binary_tree()
    bt.root = Node('_')
    bt.root.left = Node('M')
    bt.root.left.left = Node('H')
    bt.root.left.left.left = Node('A')
    bt.root.left.right = Node('A')
    bt.root.left.right.right = Node('D')
    bt.root.right = Node('L')
    bt.root.right.left = Node('A')
    bt.root.right.left.left = Node('H')
    bt.root.right.left.left.left = Node('S')
    bt.root.right.right = Node('I')
    bt.root.right.right.left = Node('E')
    bt.root.right.right.right = Node('N')
    print(bt.in_order(bt.root))
    bst = binary_search_tree()
    bst.add(11)
    bst.add(22)
    bst.add(33)
    bst.add(44)
    bst.add(55)
    print(bst.contains(11))
    print(bst.contains(5))
    print(bst.contains(30))
    print(bst.contains(55))
    print(bst.contains(22))
