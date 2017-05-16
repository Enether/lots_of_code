#include <iostream>
#include <vector>
std::vector<int> buildPrecomputedArr();
int main() {
    int queryCount;
    auto answers = buildPrecomputedArr();
    std::cin >> queryCount;
    for (int i = 0; i < queryCount; ++i) {
        int wantedNum;
        std::cin >> wantedNum;
        std::cout << answers[wantedNum] << std::endl;
    }
    return 0;
}

std::vector<int> buildPrecomputedArr() {
    // TODO: Paste the results from land_codegen.py
}