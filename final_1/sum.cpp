#include <iostream>
#include <cmath>

int sumofsquares(int a, int b)
{
  int i;
  if (a<b)
  {
    for (i = a; i <= b; i++)
    {
      int squared = pow(i,2);
      std::cout << squared << std::endl;
    }
  }
  else
  {
    std::cout << "your input is invalid: a>b" << std::endl;
  }
  return 0;
}
int main()
{
  std::cout << "first test:" << std::endl;
  sumofsquares(5,10);
  std::cout << "\nsecond test:" << std::endl;
  sumofsquares(25,10);
  std::cout << "\nthird test:" << std::endl;
  sumofsquares(-5,5);
  std::cout << "\nfourth test:" << std::endl;
  sumofsquares(2,5);
  return 0;
}
