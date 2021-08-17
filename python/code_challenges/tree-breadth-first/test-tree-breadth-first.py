def test_tree_breadth_first():
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
    expected = [2,7,5,2,6,9,5,11,4]
    actual = bt.tree_breadth_first()
    assert actual == expected
