//Ethan Dahlby, ed6tf, 3.4.2021, ListItr.cpp
#include "ListItr.h"
using namespace std;

ListItr::ListItr(){  // Default constructor
  current = NULL;
}

ListItr::ListItr(ListNode* theNode){  // Constructor pointing at a node
  current = theNode;
}

bool ListItr::isPastEnd() const {  // If the iterator is *on* the dummy tail node
  if(current->next == NULL){
    return true;
  } else {
    return false;
  }
}

bool ListItr::isPastBeginning() const {  // If the iterator is *on* the dummy head node
  if(current->previous == NULL){
    return true;
  } else {
    return false;
  }
}

void ListItr::moveForward(){  // Moves the iterator to the next node
  if (!isPastEnd()){
    current = current->next;
  }
}

void ListItr::moveBackward(){  // Moves the iterator to the previous node
  if(!isPastBeginning()){
    current = current->previous;
  }
}

int ListItr::retrieve() const {  // Returns the value of the current node
  return current->value;
}
