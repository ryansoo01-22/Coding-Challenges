import collections

def stepOne():
    with open('135-0.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        letter_freqs = {}
        for c in text:
            if c.isalnum():
                letter_freqs[c] = 1 + letter_freqs.get(c, 0)
        sorted_freqs = sorted(letter_freqs.items(), key=lambda x:x[1])
        return sorted_freqs

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
       
def make_tree_test(sorted_nodes):
    while len(sorted_nodes) > 1:
        first, second = sorted_nodes.pop(0), sorted_nodes.pop(0)
        root_weight = first.weight + second.weight
        root_node = Node(None, root_weight)
        root_node.left = first
        root_node.right = second
        sorted_nodes.append(root_node)
        sorted_nodes.sort()
    print("test")

def step_two_testing():
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
    make_tree_test(test_list)

step_two_testing()


