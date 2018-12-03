#include <iostream> //kind of like import

//def main()
//print('Hello World')
//return 0

/*everything you write must be within a function or a class
int(eger) => return type
'x' is not the same as "x"

using namespace std; => NEVER DO THIS
*/

using std::cout;
int main() //must have a main()
{
  cout << "Hello World! " << 123 << " " << 55.22 << std::endl;
  cout << "\nMore stuff";
  return 0; //similar to python but if you do not put this
  //you will not know what it results to, usually returns last value which is weird
}
// ; separates statements
//std::cout => in the standard library, there is something called console out
//and we can send stuff to it
//endl => end line
