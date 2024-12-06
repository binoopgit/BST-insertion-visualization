
## BST insertion Visualization

A Binary Search Tree (BST) is a data structure that allows efficient insertion, deletion, and lookup of elements. It is a binary tree where each node has a value, and:

All nodes in the left subtree of a given node have values smaller than the node's value.

All nodes in the right subtree have values greater than the node's value.


## About This Code

This Python script provides a visualization of the BST insertion process using the matplotlib and networkx libraries. The script helps you understand how elements are added to the BST by displaying the insertion and comparison process step-by-step in an interactive window.

## Features

Step-by-Step Visualization: As each value is inserted into the BST, the current state of the tree is displayed, showing where the new value is placed.

Comparison Messages: During the insertion, messages are displayed to indicate the comparisons made and where the value is being inserted, helping users understand the decision-making process.

Interactive Visualization: The visualization updates dynamically after each insertion, allowing you to observe the evolution of the BST.

## How the Code Works

TreeNode Class: Represents a node in the BST with a value (key) and pointers to its left and right children.

BinarySearchTree Class: Contains methods to insert nodes and visualize the BST.

insert(key): Inserts a new value into the BST, starting from the root.

_insert_recursive(node, key): A helper method that recursively finds the correct position for the new value.

visualize(message): Displays the current state of the BST using matplotlib and networkx. The message parameter provides context about the current step in the insertion process.

Visualization: After each insertion, the current structure of the BST is displayed with a message indicating the comparison or insertion being made.

## Libraries Used

matplotlib: Used to create the visual representation of the BST.

networkx: Used to manage the graph structure of the BST and visualize the connections between nodes.

## Running the Code

Ensure you have Python installed (preferably version 3.6 or higher).

Install the required libraries:

```bash
  npm run deploy
```
Run the script to see the BST insertion visualization in action.

## Example Usage

The script inserts a sequence of values into the BST: [50, 30, 70, 20, 90, 10, 40, 60, 80]. During each insertion, the visualization updates to show how the BST grows, and messages explain the comparisons being made to find the correct position for each value.

## Code Snippet

```bash
plt.ion()  # Turn on interactive mode
bst = BinarySearchTree()
values_to_insert = [50, 30, 70, 20, 40, 60, 80]
for value in values_to_insert:
    bst.insert(value)

plt.ioff()  # Turn off interactive mode
plt.show()
```
## Output

The BST is visualized step-by-step as nodes are added.

Messages indicate whether the inserted value is compared with the current node, and if it is added to the left or right subtree.

## Learning Objectives

Understand the properties of a Binary Search Tree.

Learn how values are inserted into a BST.

Visualize how comparisons are made to find the correct insertion point.

## License

This project is open-source and free to use under  [MIT](https://choosealicense.com/licenses/mit/)

# BST-insertion-visualization
