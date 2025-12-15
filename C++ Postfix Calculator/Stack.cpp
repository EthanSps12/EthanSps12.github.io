//Ethan Dahlby, ed6tf, 3.4.2021, Stack.cpp

#include "Stack.h"
#include "List.h"
#include <iostream>
using namespace std;

// Restricting some features of the list to make it work as a stack, where you can only add and delete from the end.

Stack::Stack(){  // Default constructor, creates a new empty stack
  stack = new List();
}

Stack::~Stack(){  // Default destructor
}

void Stack::push(int x){  // Adds an item to the top of the stack
  stack->insertAtTail(x);
}

void Stack::pop(){  // Removes an item from the top of the stack
  ListItr popItr = stack->last();
  popItr.current->previous->next = popItr.current->next;  // Adjusting pointers
  popItr.current->next->previous = popItr.current->previous;
  delete popItr.current;
}

int Stack::top(){  // Gets the top item on the stack
  return stack->last().retrieve();
}

bool Stack::empty(){  // Checks if the stack is empty
  return stack->isEmpty();
}
