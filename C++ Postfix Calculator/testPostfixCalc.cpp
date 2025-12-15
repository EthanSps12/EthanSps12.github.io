//Ethan Dahlby, ed6tf, 3.4.2021, testPostfixCalculator.cpp

#include "postfixCalculator.h"
#include <iostream>
using namespace std;

int main(){  // Creates and runs a new postfix calculator and prints the answer
  PostfixCalculator * postfxCalc = new PostfixCalculator();
  int answer = postfxCalc->run();
  cout << to_string(answer);
  return 0;
}
