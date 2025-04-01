class HashTable:
    def __init__(self, size):
        self.size = size  # Size of the hash table
        self.table = [None] * self.size  # Initialize the hash table with None
        self.count = 0  # Count of elements in the hash table

    def hash_function(self, key):
        """Hash function to compute the index for a given key."""
        return key % self.size

    def insert_linear(self, key, value):
        """Insert a key-value pair using linear probing."""
        index = self.hash_function(key)
        comparisons = 0  # Count comparisons for this insertion

        while self.table[index] is not None:
            comparisons += 1  # Increment comparison count
            index = (index + 1) % self.size  # Move to the next index

        self.table[index] = (key, value)  # Insert the key-value pair
        self.count += 1
        print(f"Inserted ({key}, {value}) at index {index} with {comparisons} comparisons.")

    def search_linear(self, key):
        """Search for a key using linear probing."""
        index = self.hash_function(key)
        comparisons = 0  # Count comparisons for this search

        while self.table[index] is not None:
            comparisons += 1  # Increment comparison count
            if self.table[index][0] == key:
                print(f"Found {key} at index {index} with {comparisons} comparisons.")
                return self.table[index][1]  # Return the value
            index = (index + 1) % self.size  # Move to the next index

        print(f"{key} not found after {comparisons} comparisons.")
        return None  # Key not found

    def insert_quadratic(self, key, value):
        """Insert a key-value pair using quadratic probing."""
        index = self.hash_function(key)
        comparisons = 0  # Count comparisons for this insertion
        i = 0  # Quadratic probing factor

        while self.table[index] is not None:
            comparisons += 1  # Increment comparison count
            i += 1  # Increment the probing factor
            index = (index + i * i) % self.size  # Move to the next index using quadratic probing

        self.table[index] = (key, value)  # Insert the key-value pair
        self.count += 1
        print(f"Inserted ({key}, {value}) at index {index} with {comparisons} comparisons.")

    def search_quadratic(self, key):
        """Search for a key using quadratic probing."""
        index = self.hash_function(key)
        comparisons = 0  # Count comparisons for this search
        i = 0  # Quadratic probing factor

        while self.table[index] is not None:
            comparisons += 1  # Increment comparison count
            if self.table[index][0] == key:
                print(f"Found {key} at index {index} with {comparisons} comparisons.")
                return self.table[index][1]  # Return the value
            i += 1  # Increment the probing factor
            index = (index + i * i) % self.size  # Move to the next index using quadratic probing

        print(f"{key} not found after {comparisons} comparisons.")
        return None  # Key not found


# Example usage
if __name__ == "__main__":
    size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(size)

    while True:
        print("\n--- Telephone Book ---")
        print("1. Insert Telephone Number (Linear Probing)")
        print("2. Search Telephone Number (Linear Probing)")
        print("3. Insert Telephone Number (Quadratic Probing)")
        print("4. Search Telephone Number (Quadratic Probing)")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter phone number: "))
            name = input("Enter name: ")
            hash_table.insert_linear(key, name)
        elif choice == 2:
            key = int(input("Enter phone number to search: "))
            hash_table.search_linear(key)
        elif choice == 3:
            key = int(input("Enter phone number: "))
            name = input("Enter name: ")
            hash_table.insert_quadratic(key, name)
        elif choice == 4:
            key = int(input("Enter phone number to search: "))
            hash_table.search_quadratic(key)
        elif choice == 5:
            print("Exiting the program.")
            break