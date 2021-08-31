class Node:
    def __init__(self,val):
        self.left = None
        self.val = val
        self.right = None 
    def print_node(self):
        print(self.val)

class MyBinTree:
    def __init__(self):
        self.root:Node = None

    def insert(self, val): 
        self.root = self.insert_recursive(self.root, val)

    def insert_recursive(self,current:Node,val:int): 
        if current == None:
            return Node(val)
        else:
            if current.val == val:
                return current
            elif val < current.val:
                current.left = self.insert_recursive(current.left,val)
            else:
                current.right = self.insert_recursive(current.right,val)

        return current

    def print_inorder(self,curr:Node):
        if curr != None:
            self.print_inorder(curr.left)
            print(" ",curr.val)
            self.print_inorder(curr.right)

    def print_asc(self):
        self.print_inorder(self.root)



my_bst = MyBinTree()
my_bst.insert(10)
my_bst.insert(6)
my_bst.insert(12)
my_bst.insert(200)
my_bst.print_asc()
