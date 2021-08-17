class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return " ".join(items)
    
    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
    
    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        
    def is_empty(self):
        if self.front:
            return False
        return True

class Node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

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
      
    def tree_breadth_first(self):
            output = []
            temp = None
            queue = Queue()
            queue.enqueue(self.root)
            # if not self.root:
            #     return
            while queue.front:
                temp = queue.dequeue()
                output.append(temp.value)
                if temp.left:
                    queue.enqueue(temp.left)
                if temp.right:
                    queue.enqueue(temp.right)
            return output

if __name__ == "__main__":
    bt = binary_tree()
    bt.root = Node(2)
    bt.root.left = Node(7)
    bt.root.right = Node(5)
    bt.root.left.right = Node(6)
    bt.root.left.left = Node(2)
    bt.root.right.right=Node(9)
    bt.root.right.right.left=Node(4)
    bt.root.left.right.left=Node(5)
    bt.root.left.right.right = Node(11)
    print(bt.tree_breadth_first()) #[2,7,5,2,6,9,5,11,4]
