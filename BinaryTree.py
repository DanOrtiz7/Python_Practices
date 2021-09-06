#Node class to populate the Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
#Tree Class using the Node class
class Tree:
    #Privates Methods
    def __init__(self, data):
        self.root = Node(data)

    #Method to add a new node to the Tree
    def add_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.add_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.add_recursive(node.right, data)
    #Several methods on how you can travel/read the Tree
    def in_order_travel(self, node):
        if node is not None:
            self.in_order_travel(node.left)
            print(node.data, end=", ")
            self.in_order_travel(node.right)

    def pre_order_travel(self, node):
        if node is not None:
            print(node.data, end=", ")
            self.pre_order_travel(node.left)
            self.pre_order_travel(node.right)

    def post_order_travel(self, node):
        if node is not None:
            self.post_order_travel(node.left)
            self.post_order_travel(node.right)
            print(node.data, end=", ")

    #Method to search a Node
    def search_node(self, node, search):
        if node is None:
            return None
        if node.data == search:
            return node
        if search < node.data:
            return self.search_node(node.left,search)
        else:
            return self.search_node(node.right,search)
        
    def add_public(self, data):
        self.add_recursive(self.root, data)

    def in_order_public(self):
        print("Printing Tree in order: ")
        self.in_order_travel(self.root)
        print("")

    def preorder_public(self):
        print("Printing tree preorder: ")
        self.pre_order_travel(self.root)
        print("")

    def postorder_public(self):
        print("Printing tree postorder: ")
        self.post_order_travel(self.root)
        print("")

    def search_public(self, search):
        return self.search_node(self.root, search)

            
tree = Tree("Leo")
tree.add_public("Amelia")
tree.add_public("Caro")
tree.add_public("Nat")
tree.add_public("Cuphead")
tree.add_public("Ortiz")
tree.add_public("Dani")
tree.in_order_public()
tree.postorder_public()
# Search
searched = input("Search for something: ")
node = tree.search_public(searched)
if node is None:
    print(f"{searched} does not exist")
else:
    print(f"{searched} does exist")
        