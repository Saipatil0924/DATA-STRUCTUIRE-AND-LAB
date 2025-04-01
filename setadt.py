def create_set():
    """Create an empty set."""
    return set()

def add(new_element, s):
    """Add a new element to the set."""
    s.add(new_element)

def remove(element, s):
    """Remove an element from the set. Print a message if not found."""
    if element in s:
        s.remove(element)
    else:
        print(f"Element {element} not found in the set.")

def contains(element, s):
    """Check if the element is in the set."""
    return element in s

def size(s):
    """Return the number of elements in the set."""
    return len(s)

def iterator(s):
    """Return an iterator for the set."""
    return iter(s)

def intersection(s1, s2):
    """Return a new set that is the intersection of two sets."""
    return s1.intersection(s2)

def union(s1, s2):
    """Return a new set that is the union of two sets."""
    return s1.union(s2)

def difference(s1, s2):
    """Return a new set that is the difference of two sets."""
    return s1.difference(s2)

def subset(s1, s2):
    """Check if the first set is a subset of the second set."""
    return s1.issubset(s2)

# Menu-driven program
if __name__ == "__main__":
    set1 = create_set()
    set2 = create_set()

    while True:
        print("\n--- Set Operations Menu ---")
        print("1. Add element to Set 1")
        print("2. Remove element from Set 1")
        print("3. Check if element is in Set 1")
        print("4. Size of Set 1")
        print("5. Add element to Set 2")
        print("6. Remove element from Set 2")
        print("7. Check if element is in Set 2")
        print("8. Size of Set 2")
        print("9. Intersection of Set 1 and Set 2")
        print("10. Union of Set 1 and Set 2")
        print("11. Difference of Set 1 and Set 2")
        print("12. Check if Set 1 is a subset of Set 2")
        print("13. Exit")

        choice = int(input("Enter your choice (1-13): "))

        if choice == 1:
            element = int(input("Enter element to add to Set 1: "))
            add(element, set1)
            print(f"Added {element} to Set 1.")
        elif choice == 2:
            element = int(input("Enter element to remove from Set 1: "))
            remove(element, set1)
        elif choice == 3:
            element = int(input("Enter element to check in Set 1: "))
            print(f"Set 1 contains {element}: {contains(element, set1)}")
        elif choice == 4:
            print("Size of Set 1:", size(set1))
        elif choice == 5:
            element = int(input("Enter element to add to Set 2: "))
            add(element, set2)
            print(f"Added {element} to Set 2.")
        elif choice == 6:
            element = int(input("Enter element to remove from Set 2: "))
            remove(element, set2)
        elif choice == 7:
            element = int(input("Enter element to check in Set 2: "))
            print(f"Set 2 contains {element}: {contains(element, set2)}")
        elif choice == 8:
            print("Size of Set 2:", size(set2))
        elif choice == 9:
            print("Intersection of Set 1 and Set 2:", intersection(set1, set2))
        elif choice == 10:
            print("Union of Set 1 and Set 2:", union(set1, set2))
        elif choice == 11:
            print("Difference of Set 1 and Set 2:", difference(set1, set2))
        elif choice == 12:
            print("Set 1 is a subset of Set 2:", subset(set1, set2))
        elif choice == 13:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")