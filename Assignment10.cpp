//Write c++ program for storing binary number using doubly linked lists.write functions:
// a) To Compute 1'a and 2's complement 
// b) add two binary number 

#include <iostream>
#include <string>
#include <sstream>

using namespace std;

// Node structure for the doubly linked list
struct Node {
    int bit;         // Stores a single bit (0 or 1)
    Node* prev;     // Pointer to the previous node
    Node* next;     // Pointer to the next node

    Node(int b) : bit(b), prev(nullptr), next(nullptr) {}
};

// Class for the doubly linked list
class BinaryNumber {
private:
    Node* head;     // Head of the list
    Node* tail;     // Tail of the list

public:
    // Constructor
    BinaryNumber() : head(nullptr), tail(nullptr) {}

    // Function to insert a bit at the end of the list
    void insertBit(int bit) {
        if (bit != 0 && bit != 1) {
            cout << "Invalid bit. Only 0 and 1 are allowed." << endl;
            return;
        }

        Node* newNode = new Node(bit);
        if (!head) {
            head = tail = newNode; // List is empty
        } else {
            tail->next = newNode;   // Link new node at the end
            newNode->prev = tail;   // Link back to the tail
            tail = newNode;         // Update tail
        }
    }

    // Function to display the binary number
    void display() const {
        Node* current = head;
        while (current) {
            cout << current->bit;
            current = current->next;
        }
        cout << endl;
    }

    // Function to compute 1's complement
    BinaryNumber onesComplement() const {
        BinaryNumber complement;
        Node* current = head;
        while (current) {
            complement.insertBit(current->bit == 0 ? 1 : 0);
            current = current->next;
        }
        return complement;
    }

    // Function to compute 2's complement
    BinaryNumber twosComplement() const {
        BinaryNumber complement = onesComplement();
        complement.addOne(); // Add 1 to the 1's complement
        return complement;
    }

    // Function to add one to the binary number
    void addOne() {
        Node* current = tail;
        int carry = 1;
        while (current && carry) {
            int sum = current->bit + carry;
            current->bit = sum % 2; // Set the current bit
            carry = sum / 2;        // Update carry
            current = current->prev;
        }
        if (carry) { // If there's still carry, insert a new node at the front
            insertBit(1);
        }
    }

    // Function to add another binary number
    BinaryNumber add(const BinaryNumber& other) const {
        BinaryNumber result;
        Node* current1 = tail;
        Node* current2 = other.tail;

        int carry = 0;
        while (current1 || current2 || carry) {
            int bit1 = (current1) ? current1->bit : 0;
            int bit2 = (current2) ? current2->bit : 0;

            int sum = bit1 + bit2 + carry;
            result.insertBit(sum % 2); // Insert the sum bit
            carry = sum / 2;            // Update carry

            if (current1) current1 = current1->prev;
            if (current2) current2 = current2->prev;
        }

        // The bits are inserted in reverse order, reverse the result
        return result.reverse();
    }

    // Function to reverse the order of the list (to display correctly)
    BinaryNumber reverse() const {
        BinaryNumber reversed;
        Node* current = tail;
        while (current) {
            reversed.insertBit(current->bit);
            current = current->prev;
        }
        return reversed;
    }

    // Function to delete the list
    void clear() {
        Node* current = head;
        while (current) {
            Node* temp = current;
            current = current->next;
            delete temp; // Free memory
        }
        head = tail = nullptr; // Reset head and tail
    }

    // Destructor to ensure list is cleared
    ~BinaryNumber() {
        clear();
    }
};

// Main function
int main() {
    BinaryNumber binaryNum1;
    BinaryNumber binaryNum2;

    // Inserting binary numbers (example)
    cout << "Enter first binary number (e.g., 1101): ";
    string input1;
    cin >> input1;
    for (char bit : input1) {
        binaryNum1.insertBit(bit - '0');
    }

    cout << "Enter second binary number (e.g., 1011): ";
    string input2;
    cin >> input2;
    for (char bit : input2) {
        binaryNum2.insertBit(bit - '0');
    }

    cout << "First binary number: ";
    binaryNum1.display();

    cout << "Second binary number: ";
    binaryNum2.display();

    // Compute and display 1's complement
    cout << "1's complement of first binary number: ";
    binaryNum1.onesComplement().display();

    // Compute and display 2's complement
    cout << "2's complement of first binary number: ";
    binaryNum1.twosComplement().display();

    // Add the two binary numbers and display the result
    BinaryNumber sum = binaryNum1.add(binaryNum2);
    cout << "Sum of the two binary numbers: ";
    sum.display();

    return 0;
}
