class Node():
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None
    
  def __str__(self):
    return str(self.value)

 
class binary_tree():
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
      pre_order_output = pre_order_output + self.in_order(root.right)
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
    pass

  def contains(self,value):
    pass
 

if __name__ = '__main__':
