import matplotlib.pyplot as plt
import networkx as nx
import time

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.graph = nx.DiGraph()

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            self.graph.add_node(key)
            self.visualize(f"Inserted root: {key}")
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        self.visualize(f"Comparing {key} with {node.key}")
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
                self.graph.add_edge(node.key, key)
                self.visualize(f"Inserted {key} to the left of {node.key}")
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
                self.graph.add_edge(node.key, key)
                self.visualize(f"Inserted {key} to the right of {node.key}")
            else:
                self._insert_recursive(node.right, key)

    def visualize(self, message):
        pos = self._get_tree_layout(self.root)
        plt.clf()
        nx.draw(self.graph, pos, with_labels=True, node_size=800, node_color="skyblue", font_size=10, font_weight="bold")
        plt.title(f"BST Insertion Visualization\n{message}")
        plt.draw()
        plt.pause(1)

    def _get_tree_layout(self, root, pos=None, x=0, y=0, layer=1):
        if pos is None:
            pos = {}
        if root is not None:
            pos[root.key] = (x, y)
            spacing = 1.0 / layer
            pos = self._get_tree_layout(root.left, pos=pos, x=x - spacing, y=y - 1, layer=layer + 1)
            pos = self._get_tree_layout(root.right, pos=pos, x=x + spacing, y=y - 1, layer=layer + 1)
        return pos

# Example usage:
plt.ion()  # Turn on interactive mode
bst = BinarySearchTree()
values_to_insert = [50, 30, 70, 20, 90, 10, 40, 60, 80]
for value in values_to_insert:
    bst.insert(value)

plt.ioff()  # Turn off interactive mode
plt.show()


