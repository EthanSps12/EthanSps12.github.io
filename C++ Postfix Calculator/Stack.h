//Ethan Dahlby, ed6tf, 3.4.2021, Stack.h

#ifndef STACK_H
#define STACK_H

#include "List.h"
#include <iostream>
using namespace std;

class Stack {
 public:
  Stack();  // Constructor
  ~Stack();  // Destructor
  List * stack;  // Pointer to a list
  void push(int x);  // Add to top of stack
  void pop();  // Remove from top of stack
  int top();  // Get top item
  bool empty();  // Is the stack empty?

  friend class List;
  friend class ListItr;
  friend class ListNode; //Reminded myself about friend classes from here: https://www.geeksforgeeks.org/friend-class-function-cpp/
};

#endif
