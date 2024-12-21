import time

def generate_large_tree(n):
    """
    Generate a large binary tree with 'n' nodes for performance testing.
    """
    nodes = []
    for i in range(n):
        nodes.append({"name": f"Node{i}", "delay_from_parent": i, "children": []})
    
    # Simple binary tree structure (not balanced)
    for i in range(n // 2):
        if 2 * i + 1 < n:
            nodes[i]["children"].append(nodes[2 * i + 1])
        if 2 * i + 2 < n:
            nodes[i]["children"].append(nodes[2 * i + 2])
    
    return nodes[0]  # Return the root node

def measure_time_for_tree_size(n):
    """
    Measure the time taken to compute the minimum extra delay for a tree of size n.
    """
    tree_root = generate_large_tree(n)
    start_time = time.time()
    analyze_tree(tree_root)
    end_time = time.time()
    return end_time - start_time

# Test different sizes
sizes = [10, 50, 100, 200, 500, 1000]
times = [measure_time_for_tree_size(size) for size in sizes]

print("Input Size vs Running Time")
for size, time_taken in zip(sizes, times):
    print(f"Size: {size}, Time: {time_taken:.6f} seconds")


def compute_minimum_extra_delay(current_node):

    if not current_node["children"]:  # Base case: Leaf node
        return 0, 0  # No extra delay needed, max path delay to leaf is 0

    # Step 1: Recursively process each child and calculate delays
    child_delays = []
    total_extra_delay = 0

    for child in current_node["children"]:
        child_extra_delay, child_path_delay = compute_minimum_extra_delay(child)
        total_extra_delay += child_extra_delay
        child_delays.append(child_path_delay + child["delay_from_parent"])

    # Step 2: Determine the maximum path delay
    max_child_delay = max(child_delays)

    # Step 3: Balance the delays among all child paths
    for child_delay in child_delays:
        extra_delay_needed = max_child_delay - child_delay
        total_extra_delay += extra_delay_needed  # Add the required delay to balance this path

    # Return the total extra delay and the maximum delay from this node to any leaf
    return total_extra_delay, max_child_delay


def build_custom_tree():

    # Create nodes as dictionaries
    root = {"name": "Root", "delay_from_parent": 0, "children": []}
    left_child = {"name": "LeftChild", "delay_from_parent": 3, "children": []}
    right_child = {"name": "RightChild", "delay_from_parent": 2, "children": []}
    left_left = {"name": "LeftLeft", "delay_from_parent": 2, "children": []}
    left_right = {"name": "LeftRight", "delay_from_parent": 1, "children": []}
    right_left = {"name": "RightLeft", "delay_from_parent": 1, "children": []}
    right_right = {"name": "RightRight", "delay_from_parent": 3, "children": []}

    # Build tree structure
    root["children"].extend([left_child, right_child])
    left_child["children"].extend([left_left, left_right])
    right_child["children"].extend([right_left, right_right])

    return root

def analyze_tree(root):
    # Analyzes the given binary tree for clock skew and computes the total extra delay added.
 
    print("Analyzing tree to minimize clock skew...\n")
    total_extra_delay, _ = compute_minimum_extra_delay(root)
    print(f"Total extra delay added to balance the clock: {total_extra_delay}")


import matplotlib.pyplot as plt

# Plotting the running time vs input size
plt.plot(sizes, times, marker='o', linestyle='-', color='b')
plt.title("Running Time vs Input Size")
plt.xlabel("Input Size (Number of Nodes)")
plt.ylabel("Running Time (Seconds)")
plt.grid(True)
plt.show()


# Main program execution
if __name__ == "__main__":
    # Build a custom binary tree
    tree_root = build_custom_tree()

    # Analyze the tree and compute the total extra delay
    analyze_tree(tree_root)



