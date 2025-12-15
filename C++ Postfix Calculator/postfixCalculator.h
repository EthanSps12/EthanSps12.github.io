//Ethan Dahlby, ed6tf, 3.4.2021, postfixCalculator.h

#ifndef POSTFIXCALCULATOR_H
#define POSTFIXCALCULATOR_H
#include <iostream>
#include <string>
#include <cstdlib>
#include "Stack.h"
using namespace std;

class PostfixCalculator{
public:
  PostfixCalculator(); //Forgot to put constructor here, looked up error here to remind me: https://stackoverflow.com/questions/49516548/calucatenumbers-is-missing-exception-specification-noexcept
  int run();  // Waits for input and performs calculatons
  Stack * add(Stack * paramStack);  // Addition operator
  Stack * subtract(Stack * paramStack);  // Subtraction operator
  Stack * multiply(Stack * paramStack);  // Multiplication operator
  Stack * divide(Stack * paramStack);  // Division operator
  Stack * makeNegative(Stack * paramStack);  // Negation operator
  void checkIfEmpty(Stack * toCheck);  // Verifies stack is not empty
private:
  Stack * theStack;  // Pointer to a stack
};

#endif
