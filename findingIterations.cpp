#include <iostream>
#include <vector>

void printResults(std::vector<int> seeds, std::vector<int> iterations){
    for (int i = 0; i < seeds.size(); i++){
        std::cout << seeds[i] << ":" << iterations[i] << "\n";
    }
}

int findingSingleIteration(int seed){
    int iterations;
    iterations = 0;
    while (seed >= 1){
        if (seed == 1){
            break;
        } else if (seed % 2 == 0){
            seed = seed / 2;
            iterations++;
        } else if (seed % 2 != 0){
            seed = seed * 3 + 1;
            iterations++;
        }
    }
    return iterations;
}

std::vector<int> findingArrayIterations(std::vector<int> seeds){
    int number;
    int iterations;
    iterations = 0;
    std::vector<int> Iterations;
    std::vector<double> percentages;
    percentages = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9};
    for (int j = 0; j < seeds.size(); j++){
        number = seeds[j];
        /*
        if (seeds.size() > 10000){
            for (int i = 0; i < percentages.size(); i++){
                if (number == percentages[i] * seeds[seeds.size() - 1]){
                    std::cout << percentages[i] * 100 << "%" << "\n";
                }
            }
        }*/
        while (number >= 1){
            if (number == 1){
                Iterations.push_back(iterations);
                iterations = 0;
                break;
            } else if (number % 2 != 0){
                number = number * 3 + 1;
                iterations++;
            } else if (number % 2 == 0){
                number = number / 2;
                iterations++;
            }
        }
    }
    return Iterations;
}

int main(int argc, char *argv[]){
    int iterations;
    int lowerBound;
    int upperBound;
    lowerBound = atoi(argv[1]);
    upperBound = atoi(argv[2]);
    std::vector<int> seeds;
    for (int i = lowerBound; i <= upperBound; i++){
            seeds.push_back(i);
        }
    std::vector<int> Iterations;
    if (argc == 2){
        iterations = findingSingleIteration(lowerBound);
        std::cout << "Seed: " << argv[1] << "\n";
        std::cout << "Iterations: " << iterations;
    } else if (argc == 3){
        Iterations = findingArrayIterations(seeds);
        std::cout << "Iterations: " << "\n";
        printResults(seeds, Iterations);
    }
}

// Does C++ have a time library/module like Python?
// If so, can it track time elapsed or estimate the time that a task will take?