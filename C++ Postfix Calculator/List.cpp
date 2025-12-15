//Ethan Dahlby, ed6tf, 3.4.2021, List.cpp
#include "List.h"
using namespace std;

List::List(){
  head=new ListNode();  // Dummy head node to represent the beginning of the list
  tail=new ListNode();  // Dummy tail node to represent the beginning of the list
  head->next=tail;  // When list is empty, the head and tail are connected to each other and nothing else
  head->previous=NULL;
  tail->previous=head;
  tail->next=NULL;
  count = 0;  // Length of list
}

// Copy constructor
// Called when the code looks something like List list2 = list1;
// (In other words, it is called when you are trying to construct a **new** list from an existing one)
List::List(const List& source) {
    head=new ListNode();
    tail=new ListNode();
    head->next=tail;
    tail->previous=head;
    count=0;

    // Make a deep copy of the list
    // Start at the head of the old list and go through each list node, adding to the end of the new list
    ListItr iter(source.head->next);
    while (!iter.isPastEnd()) {
        insertAtTail(iter.retrieve());
        iter.moveForward();
    }
}

List::~List(){
  makeEmpty();  // Removes all nodes except the head and tail
  delete head;
  delete tail;
}

// Copy assignment operator
// Called when the code looks something like list2 = list1;
// (In other words, it is called when you are trying to set an **existing** list equal to another one)
List& List::operator=(const List& source) {
    if (this == &source) {
        // The two are the same list; no need to do anything
        return *this;
    } else {
        // Clear out anything this list contained
        // before copying over the items from the other list
        makeEmpty();

        // Make a deep copy of the list
        ListItr iter(source.head->next);
        while (!iter.isPastEnd()) {
            insertAtTail(iter.retrieve());
            iter.moveForward();
        }
    }
    return *this;
}

bool List::isEmpty() const {
  // The list is empty if the tail comes right after the head and there is nothing after, and vice versa
  return (head->next->next == NULL && tail->previous->previous == NULL); //Made sure && was and from here: https://en.cppreference.com/w/cpp/language/operator_logical
}

void List::makeEmpty(){
  ListItr emptyItr = ListItr(head);
  emptyItr.moveForward();  // Do not delete the head
  while(emptyItr.current->next != NULL){  // Stop while on the tail node
    emptyItr.moveForward();
    remove(emptyItr.current->previous->value);  // Move forward and delete the last node, so as to not delete the node you are on
  }
}

ListItr List::first(){
  return ListItr(head->next);  // The head is not a real element, it just helps signify the real first element
}

ListItr List::last(){
  return ListItr(tail->previous);  // Ditto
}

void List::insertAfter(int x, ListItr position){  // Creates a new node and adjusts pointers so previous node points to it and it points to next node
  ListNode* newNextNode = new ListNode();
  newNextNode->value = x;
  newNextNode->next = position.current->next;
  newNextNode->previous = position.current;
  position.current->next->previous = newNextNode;
  position.current->next = newNextNode;
}

void List::insertBefore(int x, ListItr position){  // Same as insertAfter, but adjusting the pointers of different nodes
  ListNode* newPrevNode = new ListNode();
  newPrevNode->value = x;
  newPrevNode->next = position.current;
  newPrevNode->previous = position.current->previous;
  position.current->previous->next = newPrevNode;
  position.current->previous = newPrevNode;
}

void List::insertAtTail(int x){  // Same, but using the tail as the next node
  ListNode* newNode = new ListNode();
  newNode->value = x;
  newNode->next = tail;
  newNode->previous = tail->previous;
  tail->previous->next = newNode;
  tail->previous = newNode;
}

ListItr List::find(int x){  // Goes through each node until it finds x. If it reaches the tail, it means the list does not contain x.
  ListItr findItr = ListItr(head);
  while (findItr.current->value != x){
    findItr.moveForward();
    if(findItr.current->next == NULL){
      return findItr;
    }
  }
  return findItr;
}

void List::remove(int x){
  ListItr removeItr = find(x);
  removeItr.current->previous->next = removeItr.current->next;  // Adjust pointers so nothing points to x
  removeItr.current->next->previous = removeItr.current->previous;
  delete removeItr.current;
}

int List::size() const {  // Iterates through the list and counts each node
  ListItr newItr = ListItr(head);
  int count = -1;  // Because the head does not count towards the length
  while(!(newItr.current->next == NULL)){
    count++;
    newItr.moveForward();
  }
  return count;
}

void printList(List& source, bool forward){
  string toPrint = "";
  if(forward){  // If the order is forward
    ListItr printFItr = source.first();  // Iterate through each node, adding the contents to the string to print
    while(!(printFItr.isPastEnd())){
      string stringIntF = to_string(printFItr.retrieve()); //Looked up how to cast int to string from https://stackoverflow.com/questions/5590381/easiest-way-to-convert-int-to-string-in-c
      toPrint = toPrint + stringIntF + " ";
      printFItr.moveForward();
    }
    cout << toPrint + "\n";
  } else {  // If the order is backward
    ListItr printBItr = source.last();
    while(!(printBItr.isPastBeginning())){
      string stringIntB = to_string(printBItr.retrieve());
      toPrint = toPrint + stringIntB + " ";
      printBItr.moveBackward();
    }
    cout << toPrint + "\n";
  }
}
