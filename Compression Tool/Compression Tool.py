import collections
import struct

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
        if root.left:
            inorder_traversal(root.left)

        if root.data:
            print(root.data)
        
        if root.right:
            inorder_traversal(root.right)

def make_lookup_table(root, root_val, code, lookup_table):
    if root:
        if root.left:
            code.append("0")
            make_lookup_table(root.left, root_val, code, lookup_table)
            code.pop()

        if root.data:
            #print(root.data, code)
            lookup_table[root.data] = ''.join(code).encode('utf-8')
            #lookup_table.append([root.data, ''.join(code)])
        
        if root.right:
            code.append("1")
            make_lookup_table(root.right, root_val, code, lookup_table)
            code.pop()

def step_three(tree):
    root_val = tree.root.weight
    code = []
    lookup_table = {}
    make_lookup_table(tree.root, root_val, code, lookup_table)
    return lookup_table

def step_four():
    sorted_freqs = step_one()
    with open("compressed.txt", 'w') as f:
        f.write("--HEADER START--\n\n")
        for i in sorted_freqs:
            f.write(str(i))
            f.write("\n")
        f.write("\n--HEADER END--\n\n")

def step_5(lookup_table):
    compressed = b''
    with open('135-0.txt', 'r', encoding='utf-8') as f:
        full_text = f.read()
        for i in full_text:
            if i == " ":
                compressed += b" "
                continue
            if i in lookup_table:
                compressed += struct.pack(bytes(lookup_table[i]), 2)   
    with open("compressed.txt", 'ab') as c:
        c.write(compressed)
    c.close()
            
    #DO NEXT TIME figure out how to compress bit strings
    
if __name__ == "__main__":
    sorted_freqs = step_one()
    huffman_tree = make_tree_test(sorted_freqs)
    lookup_table = step_three(huffman_tree)
    step_four()
    step_5(lookup_table)
    '''test = []
    test.append(["C", 1110])
    test.append(["D", 101])
    test.append(["E", 0])
    test.append(["M", 11111])
    test.append(["Z", 111100])
    test.append(["K", 111101])
    test.append(["U", 100])
    test.append(["L", 110])
    test.sort()
    for i in test:
        print(i)'''














