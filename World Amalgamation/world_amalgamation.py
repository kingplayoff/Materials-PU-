import sys

class DisjointSetUnion:
    def __init__(self, size: int):
        # Initialize parent array where each element points to itself
        # Allocated with size + 1 to handle 1-based indexing seamlessly
        self.parent = list(range(size + 1)) #

    def find(self, x: int) -> int:
        """
        Finds the root representative of element X with recursive Path Compression.
        Amortized Time Complexity: O(alpha(N))
        """
        if self.parent[x] == x:
            return x #
        
        # Path Compression Step: point node directly to the absolute root leader
        self.parent[x] = self.find(self.parent[x]) #
        return self.parent[x]

    def union_sets(self, x: int, y: int) -> bool:
        """
        Amalgamates the sets containing elements X and Y.
        Returns True if a new merge occurred, False if they were already unified.
        """
        root_x = self.find(x) #
        root_y = self.find(y) #

        if root_x != root_y:
            # Link one root to another to complete the merge
            self.parent[root_x] = root_y #
            return True
        return False

def main():
    # Diagnostic test simulation with a world size of 5 countries
    print("--- Diagnostic Run ---")
    dsu = DisjointSetUnion(5)
    
    # Merge worlds 1 and 2, then 2 and 3
    dsu.union_sets(1, 2)
    dsu.union_sets(2, 3)
    
    # Query union states
    print(f"Are 1 and 3 unified? -> {'YES' if dsu.find(1) == dsu.find(3) else 'NO'}") # Expected: YES
    print(f"Are 1 and 4 unified? -> {'YES' if dsu.find(1) == dsu.find(4) else 'NO'}") # Expected: NO

    # Standard template configured to parse text inputs from Online Judge streaming batches
    # Expects token inputs: N (size), followed by operation query tokens
    # e.g., "U x y" for Union, "Q x y" for Query (Adjust characters to match your assignment specs)
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    dsu_system = DisjointSetUnion(n)
    
    idx = 1
    while idx < len(input_data):
        op_type = input_data[idx]
        
        # Guard clause for terminal cases if specified by platform
        if op_type == "END":
            break
            
        x = int(input_data[idx+1])
        y = int(input_data[idx+2])
        idx += 3
        
        if op_type == "U": # Union command
            dsu_system.union_sets(x, y)
        elif op_type == "Q": # Query connection command
            if dsu_system.find(x) == dsu_system.find(y):
                print("YES") #
            else:
                print("NO") #
    """

if __name__ == "__main__":
    main()