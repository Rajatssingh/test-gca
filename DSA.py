class Solution:
    """
    A class containing implementations of Depth-First Search (DFS),
    Breadth-First Search (BFS), and Binary Search algorithms.
    """

    def __init__(self):
        """
        Constructor for the Solution class.  While not strictly necessary
        for this example, it's good practice to include one, especially if
        you anticipate adding more functionality or state to the class later.
        """
        pass  # No initialization is needed for this example, so we use 'pass'.

    def dfs(self, graph: dict, start_node: int) -> list:
        """
        Depth-First Search (DFS) algorithm implementation.

        Args:
            graph (dict): A dictionary representing the graph where keys are nodes
                          and values are lists of their neighbors.
            start_node (int): The node to start the DFS traversal from.

        Returns:
            list: A list containing the nodes visited in DFS order.  Returns an
                  empty list if the graph is empty or the start node is not in the graph.
        """
        visited = []  # List to keep track of visited nodes
        stack = [start_node]  # Stack for DFS traversal

        if not graph or start_node not in graph:
            return []  # Handle empty graph or invalid start node

        while stack:
            node = stack.pop()  # Get the top node from the stack
            if node not in visited:
                visited.append(node)  # Mark the node as visited
                # Add neighbors to the stack in reverse order to maintain
                # a consistent traversal order (if needed).
                neighbors = graph.get(node, [])
                stack.extend(neighbors) # push all the neighbors of the node into the stack

        return visited

    def bfs(self, graph: dict, start_node: int) -> list:
        """
        Breadth-First Search (BFS) algorithm implementation.

        Args:
            graph (dict): A dictionary representing the graph where keys are nodes
                          and values are lists of their neighbors.
            start_node (int): The node to start the BFS traversal from.

        Returns:
            list: A list containing the nodes visited in BFS order. Returns an
                  empty list if the graph is empty or the start node is not in the graph.
        """
        visited = []  # List to keep track of visited nodes
        queue = [start_node]  # Queue for BFS traversal
        if not graph or start_node not in graph:
            return []  # Handle empty graph or invalid start node

        while queue:
            node = queue.pop(0)  # Get the front node from the queue
            if node not in visited:
                visited.append(node)  # Mark the node as visited
                neighbors = graph.get(node, [])
                queue.extend(neighbors)  # Add neighbors to the queue
        return visited

    def binary_search(self, arr: list, target: int) -> int:
        """
        Binary Search algorithm implementation.  Iterative version.

        Args:
            arr (list): A sorted list of integers.
            target (int): The integer to search for in the list.

        Returns:
            int: The index of the target element if found, otherwise -1.
                 Returns -1 if the input array is empty.
        """
        if not arr:
            return -1  # Handle empty array

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2  # Calculate the middle index
            if arr[mid] == target:
                return mid  # Target found, return the index
            elif arr[mid] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        return -1  # Target not found

    def binary_search_recursive(self, arr: list, target: int, left: int, right: int) -> int:
        """
        Recursive implementation of Binary Search.

        Args:
            arr (list): A sorted list of integers.
            target (int): The integer to search for in the list.
            left (int): The starting index of the search space.
            right (int): The ending index of the search space.

        Returns:
            int: The index of the target element if found, otherwise -1.
        """
        if not arr:
            return -1

        if left > right:
            return -1  # Base case: target not found

        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return self.binary_search_recursive(arr, target, mid + 1, right)
        else:
            return self.binary_search_recursive(arr, target, left, mid - 1)
        
    def binary_search_starter(self, arr: list, target: int) -> int:
        """
        A wrapper function to start the recursive binary search.
        This function handles the initial call with the full array range.

        Args:
            arr (list): A sorted list of integers.
            target (int): The integer to search for in the list.

        Returns:
            int: The index of the target element if found, otherwise -1.
        """
        if not arr:
            return -1
        return self.binary_search_recursive(arr, target, 0, len(arr) - 1)


def main():
    """
    Main function to demonstrate the usage of the Solution class and its methods.
    """
    # Create an instance of the Solution class
    solution = Solution()

    # Example graph for DFS and BFS
    graph = {
        0: [1, 2],
        1: [2, 0, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3],
    }

    # Example usage of DFS
    print("DFS Traversal:")
    dfs_result = solution.dfs(graph, 0)
    print(dfs_result)  # Output: [0, 2, 4, 3, 1] (or a similar valid DFS traversal)

    # Example usage of BFS
    print("\nBFS Traversal:")
    bfs_result = solution.bfs(graph, 0)
    print(bfs_result)  # Output: [0, 1, 2, 3, 4] (or a similar valid BFS traversal)

    # Example usage of Binary Search
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_element = 23
    binary_search_result = solution.binary_search(sorted_array, target_element)
    print(f"\nBinary Search: Target {target_element} found at index {binary_search_result}")  # Output: 5

    target_element = 50
    binary_search_result = solution.binary_search(sorted_array, target_element)
    print(f"Binary Search: Target {target_element} found at index {binary_search_result}")  # Output: -1

    # Example of the recursive binary search
    target_element_recursive = 16
    recursive_result = solution.binary_search_starter(sorted_array, target_element_recursive)
    print(f"\nRecursive Binary Search: Target {target_element_recursive} found at index {recursive_result}") # Output: 4

    target_element_recursive = 100
    recursive_result = solution.binary_search_starter(sorted_array, target_element_recursive)
    print(f"Recursive Binary Search: Target {target_element_recursive} found at index {recursive_result}") # Output: -1

if __name__ == "__main__":
    """
    This ensures that the main function is called only when the script is
    executed directly (not when imported as a module).
    """
    main()
