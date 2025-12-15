//Ethan Dahlby, ed6tf, 3.4.2021, postfixCalculator.cpp

#include "postfixCalculator.h"
#include <iostream>
#include <string>
#include <cstdlib>
#include "Stack.h"
using namespace std;

PostfixCalculator::PostfixCalculator(){  // Default constructor

}

int PostfixCalculator::run(){
  string token;
  int intToken;
  theStack = new Stack();
  while (cin >> token) {  // Receive input
    if(token == "+"){
      theStack = add(theStack);  // Do the addition operation
    } else if (token == "-"){
      theStack = subtract(theStack);  // Do the substraction operation
    } else if (token == "*"){
      theStack = multiply(theStack);  // Do the multiplication operation
    } else if (token == "/"){
      theStack = divide(theStack);  // Do the division operation
    } else if (token == "~"){
      theStack = makeNegative(theStack);  // Do the negative operation
    } else {
      intToken = stoi(token);  // Changes the string to an int
      theStack->push(intToken);  // Add to the stack
    }
  }
  checkIfEmpty(theStack);
  int answer = theStack->top();
  theStack->pop();
  delete theStack;
  return answer;  // When done, return the remaining value (the answer), and delete the stack
}

Stack * PostfixCalculator::add(Stack * paramStack){  // Adding removes the top two numbers, adds them, then pushes them back on the stack
  checkIfEmpty(paramStack);
  int first = paramStack->top();
  paramStack->pop();
  checkIfEmpty(paramStack);
  int second = paramStack->top();
  paramStack->pop();
  int added = first + second;
  paramStack->push(added);
  return paramStack;
};

Stack * PostfixCalculator::subtract(Stack * paramStack){  // Removes first two numbers, subtracts the first one *from* the second one, then pushes the result onto the stack
  checkIfEmpty(paramStack);
  int first = paramStack->top();
  paramStack->pop();
  checkIfEmpty(paramStack);
  int second = paramStack->top();
  paramStack->pop();
  int subtracted = second - first;
  paramStack->push(subtracted);
  return paramStack;
};

Stack * PostfixCalculator::multiply (Stack * paramStack){  // Removes top two, multiplies them, pushes result on to the stack
  checkIfEmpty(paramStack);
  int first = paramStack->top();
  paramStack->pop();
  checkIfEmpty(paramStack);
  int second = paramStack->top();
  paramStack->pop();
  int multiplied = first * second;
  paramStack->push(multiplied);
  return paramStack;
};

Stack * PostfixCalculator::divide(Stack * paramStack){  // Removes the top two, divides the second by the first
  checkIfEmpty(paramStack);
  int first = paramStack->top();
  paramStack->pop();
  checkIfEmpty(paramStack);
  int second = paramStack->top();
  paramStack->pop();
  int divided = second / first;
  paramStack->push(divided);
  return paramStack;
};

Stack * PostfixCalculator::makeNegative(Stack * paramStack){  // Removes the top number, multiplies it by -1, and pushes it back onto the stack
  checkIfEmpty(paramStack);
  int num = paramStack->top();
  paramStack->pop();
  num = num * (-1);
  paramStack->push(num);
  return paramStack;
};

void PostfixCalculator::checkIfEmpty(Stack * toCheck){  // Verifies stack is not empty, throwing an error and exiting if it is
  if(toCheck->empty()){
    cout << "Error: Stack is empty \n";
    exit(-1);
  }
}
