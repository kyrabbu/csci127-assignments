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

  double answer;

  if (d >= 0)
  {
    //std::cout << "Positive Root: " << r_pos << std::endl;
    answer = r_pos;
  }
  else
  {
    //std::cout << "Negative Root: " << 0 << std::endl;
    answer = 0;
  }
  return answer; //instructions said return
}

int main()
{
  //already tested in other function
  //disc(7, -7, -3);
  //disc(1, 11, 28);
  //disc(4, 16, -48);
  //disc(5, -2.5, -3.53543);

  std::cout << quadsolve(7, -7, -3) << std::endl;
  //quadsolve(7, -7, -3) //if you do not use return
  std::cout << quadsolve(1, 11, 28) << std::endl;
  //quadsolve(1, 11, 28)
  std::cout << quadsolve(4, 16, -48) << std::endl;
  //quadsolve(4, 16, -48);
  std::cout << quadsolve(5, -2.5, -3.53543) << std::endl;
  //quadsolve(5, -2.5, -3.53543);
  std::cout << quadsolve(-4, 16, -48) << std::endl;
  //quadsolve(-4, 16, -48);
  std::cout << quadsolve(-4, 2, -21) << std::endl;
  std::cout << quadsolve(1, 0, 0) << std::endl;

  return 0;
}
