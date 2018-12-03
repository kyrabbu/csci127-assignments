#include <iostream>

//you do not have to declare it until you use it

using std::cout;
int main()
{
  float f;
  long int x;
  short int x; //8 bits
  int i;
  int some_variable = 10 , another_variable; //can declare multiple variables in one line
  double d; //16 sig digits

  char c;
  c = 'z';
  i = 20;
  //snake => case c++ some_variable
  //java => camel case someVariable
  i = 20;
  i = i + some_variable;
  d = i;

  i = i / 4.2; //returning 7 because you want it to be an int
  std::cout << "i = " << i << "\n";

  std::cout << "i = " << i << "\n";

  d = d / 4.2;
  std::cout << "d = " << d << "\n";

  cout << c << "\n";
  cout << true << "\n";
  cout << false << "\n";
  cout >> (i < 100) << "\n"; //must use () for order of operations
  cout << "Please enter a number: ";
  std::cin >> i;
  std::cout << "You entered: " << i << "\n";

  return 0;
}

//warning is a gcc
//g++ -Wall variables.cpp
//you must know the command line
