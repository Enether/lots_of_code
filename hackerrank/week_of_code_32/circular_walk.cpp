#include <iostream>
#include <map>

std::map<int, int> bestVisited;
void traverse(int* r, int n, int currPoint, int endPoint, int second);
int main() {
    int n, startPoint, endPoint;
    std::cin >> n >> startPoint >> endPoint;
    int firstVal, g, seed, p;
    std::cin >> firstVal >> g >> seed >> p;

    int r[n];
    r[0] = firstVal;
    for (int i = 1; i < n; i++) {
        r[i] = (r[i-1] * g + seed) % p;
    }

    traverse(r, n, startPoint, endPoint, 0);
    auto it = bestVisited.find(endPoint);
    if (it == bestVisited.end()) {
        std::cout << -1 << std::endl;
    } else {
        std::cout << bestVisited[endPoint] << std::endl;
    }
    return 0;
}

void traverse(int* r, int n, int currPoint, int endPoint, int second) {
//    std::cout << currPoint << "is equal to " << ((currPoint % n) + n) % n << std::endl;

    currPoint = ((currPoint % n) + n) % n;
//    currPoint = currPoint % n;
    auto it = bestVisited.find(currPoint);
    if (it != bestVisited.end()) {
        if (second >= it->second) {
            return;
        } else {
            bestVisited[currPoint] = second;
        }
    } else {
        bestVisited[currPoint] = second;
    }

    int possibleJumpoint = r[currPoint];
    if (possibleJumpoint == 0) {
        return;
    }
    if (currPoint == endPoint) {
        return;
    }
    for (int i = currPoint-possibleJumpoint; i <= currPoint+possibleJumpoint; ++i) {
        if (i == currPoint) {
            continue;
        }
        traverse(r, n, i, endPoint, second+1);
    }

}