import collections

def step_one():
    with open('135-0.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        letter_freqs = {}
        for c in text:
            if c.isalnum():
                letter_freqs[c] = 1 + letter_freqs.get(c, 0)
        sorted_freqs = sorted(letter_freqs.items(), key=lambda x:x[1])
        list_freqs = []
        for i in sorted_freqs:
            list_freqs.append(Node(i[0], i[1]))
        return list_freqs

class Node:
    data = ""
    weight = 0
    parent = None
    left = None
    right = None

    def __init__(self, letter, freq) -> None:
        self.data = letter
        self.weight = freq
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.data + " " + str(self.weight)

    def __lt__(self, other):
        if self.weight < other.weight:
            return self.weight < other.weight

    def __gt__(self, other):
        if self.weight > other.weight:
            return self.weight > other.weight

class HuffmanTree:
    root = None
    
    def __init__(self, root) -> None:
        self.root = root

def step_two(sorted_nodes):
    while len(sorted_nodes) > 1:
        first, second = sorted_nodes.pop(0), sorted_nodes.pop(0)
        root_weight = first.weight + second.weight
        root_node = Node(None, root_weight)
        root_node.left = first
        first.parent = root_node
        root_node.right = second
        second.parent = root_node
        sorted_nodes.append(root_node)
        sorted_nodes.sort()
    huffman_tree = HuffmanTree(sorted_nodes.pop())
    return huffman_tree

def make_tree_test(sorted_nodes):
    while len(sorted_nodes) > 1:
        first, second = sorted_nodes.pop(0), sorted_nodes.pop(0)
        root_weight = first.weight + second.weight
        root_node = Node(None, root_weight)
        root_node.left = first
        first.parent = root_node
        root_node.right = second
        second.parent = root_node
        sorted_nodes.append(root_node)
        sorted_nodes.sort()
    huffman_tree = HuffmanTree(sorted_nodes.pop())
    return huffman_tree

def step_two_testing():
    #using this example to make the tree https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/Huffman.html
    test_list = []
    test_list.append(Node("C", 32))
    test_list.append(Node("D", 42))
    test_list.append(Node("E", 120))
    test_list.append(Node("K", 7))
    test_list.append(Node("L", 42))
    test_list.append(Node("M", 24))
    test_list.append(Node("U", 37))
    test_list.append(Node("Z", 2))
    test_list.sort()
    return make_tree_test(test_list)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)

        if root.data:
            print(root.data)

        inorder_traversal(root.right)

def step_three_test(tree):
    inorder_traversal(tree.root)
    #NEED TO MAKE LOOKUP TABLE
    
if __name__ == "__main__":
    step_two_tree = step_two_testing()
    step_three_test(step_two_tree)














