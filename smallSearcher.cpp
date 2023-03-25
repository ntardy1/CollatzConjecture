
#include <iostream>
#include <cmath>

int powInt(int number, int exponent){
  int result;
  double base;
  double exp;
  base = (double) number;
  exp = (double) exponent;
  result = (int) pow(base, exp);
  return result;
}


int main(int argc, char *argv[]){
  int starter;
  int number;
  int iterations;
  int exponent;
  exponent = atoi(argv[1]);
  starter = powInt(2, exponent);
  number = starter;
  while (true){
    starter++;
    number = starter;
    iterations = 0;
    while (number > 1){
      if (iterations >= starter * 100){
        std::cout << "Hit: " << starter << "\n";
        goto end;
      } else if (number % 2 != 0){
        number = number * 3 + 1;
        iterations++;
      } else if (number % 2 == 0){
        number = number / 2;
        iterations++;
      }
    }
  }
  end:
    NULL;
}
