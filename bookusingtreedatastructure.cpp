#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Node structure for the tree
struct Node {
    string title;  // Title of the chapter, section, or subsection
    vector<Node*> children;  // Children nodes (sections or subsections)

    Node(string t) : title(t) {}  // Constructor to initialize the node
};

// Function to print the tree nodes
void printTree(Node* node, int level = 0) {
    if (node == nullptr) return;  // Base case: if the node is null, return

    // Print the title with indentation based on the level
    cout << string(level * 2, ' ') << node->title << endl;

    // Recursively print each child node
    for (Node* child : node->children) {
        printTree(child, level + 1);
    }
}

// Function to delete the tree and free memory
void deleteTree(Node* node) {
    if (node == nullptr) return;  // Base case: if the node is null, return

    // Recursively delete each child node
    for (Node* child : node->children) {
        deleteTree(child);
    }
    delete node;  // Delete the current node
}

// Function to create a chapter with sections and subsections
Node* createChapter() {
    string chapterTitle;
    cout << "Enter chapter title: ";
    cin.ignore(); // Clear the input buffer
    getline(cin, chapterTitle);
    Node* chapter = new Node(chapterTitle);

    int numSections;
    cout << "Enter number of sections in " << chapterTitle << ": ";
    cin >> numSections;

    for (int i = 0; i < numSections; ++i) {
        string sectionTitle;
        cout << "Enter title for section " << (i + 1) << ": ";
        cin.ignore(); // Clear the input buffer
        getline(cin, sectionTitle);
        Node* section = new Node(sectionTitle);

        int numSubsections;
        cout << "Enter number of subsections in " << sectionTitle << ": ";
        cin >> numSubsections;

        for (int j = 0; j < numSubsections; ++j) {
            string subsectionTitle;
            cout << "Enter title for subsection " << (j + 1) << ": ";
            cin.ignore(); // Clear the input buffer
            getline(cin, subsectionTitle);
            section->children.push_back(new Node(subsectionTitle));
        }

        chapter->children.push_back(section);
    }

    return chapter;
}

int main() {
    // Create the root node (Book)
    Node* book = new Node("Book Title");

    int numChapters;
    cout << "Enter number of chapters in the book: ";
    cin >> numChapters;

    for (int i = 0; i < numChapters; ++i) {
        cout << "Creating chapter " << (i + 1) << ":\n";
        Node* chapter = createChapter();
        book->children.push_back(chapter);
    }

    // Print the tree
    cout << "\nBook Structure:" << endl;
    printTree(book);

    // Clean up memory
    deleteTree(book);

    return 0;
}