#include <iostream>
#include <cmath>

double disc(double a, double b, double c) //in case parameters are not integers
{
  double squared = pow(b,2);
  double ac = a*c;
  double four = 4*ac;
  double result = squared - four;
  std::cout << "\nDiscriminant: " << result << std::endl;
  return result;
}

double quadsolve(double a, double b, double c)
{
  double d = disc(a,b,c);
  double square = sqrt(d);
  double first_pos = (-b + square);
  double r_pos = first_pos/(2*a); //final answer
  //double first_neg = (-b - square); //unused
  //double r_neg = first_neg/(2*a); //final answer-unused

  if (d >= 0)
  {
    std::cout << "Positive Root: " << r_pos << std::endl;
  }
  else
  {
    std::cout << "Negative Root: " << 0 << std::endl;
  }
  return 0;
}

int main()
{
  //already tested in other function
  //disc(7, -7, -3);
  //disc(1, 11, 28);
  //disc(4, 16, -48);
  //disc(5, -2.5, -3.53543);

  quadsolve(7, -7, -3);
  quadsolve(1, 11, 28);
  quadsolve(4, 16, -48);
  quadsolve(5, -2.5, -3.53543);
  quadsolve(-5, -2.5, -3.53543);
  quadsolve(-4, 16, -48);
  return 0;
}
