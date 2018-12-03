#include <iostream>

#include <cstdlib> //fixes some things with rand()
#include <ctime>

int main()
{
  // establish the computers number
  srand(time(NULL)); //uses time as number inside ()
  int answer = rand()%100;

  int guess;

  // repeat until the answer is guessed
  //     get a guess from the user
  //     see if the guess is too low/high/just right
  std::cout << answer << "\n";
  std::cout << "Please enter a guess: ";
  std::cin >> guess;
  int guesses = 1;
  //add something to make sure it does not give the same output
  while (guess != answer){
    if (guess > answer) {
      std::cout << "You guessed too high\n";
    } else if (guess < answer){
      std::cout << "You guessed too low\n";
    }

    std::cout << "Please enter a guess: ";
    std::cin >> guesxs;
    guesses++; //added one more
  }

  std::cout << "Congratulations, you guessed the number!!!\n";
  std::cout << "It took you " << guesses << " guesses.\n";
  return 0;
}

/*
i++ : pre increment;
++i : post increment;

if (++i) -- adds 1 to i first before it uses it
if (i++) -- evaluates i then adds 1 which wont work

kind of like i = i + 1

i-- :
--i :

kind of like i = i - 1

i+= <---> i = i +
-=
*=
/=
*/
