#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
  //user input
  int input;
  cout << "Enter an integer from 0 to 99: ";
  cin >> input;
  cout << "You have entered: " << input;

  //while loop
  int answer = 2;
  srand(time(NULL));
  int guess = rand() % 100;
  while (answer != 0) {
    cout << "\nGuess: " << guess;
    if (answer == -1)
      guess = (rand() % guess);

    if (answer == 1)
      guess = guess + (rand() % guess);

    if (answer != -1 && answer != 1)
      guess = guess;

    int new_answer;
    cout << "\nAnswer: ";
    cin >> new_answer;
    answer = new_answer;

  }
}
