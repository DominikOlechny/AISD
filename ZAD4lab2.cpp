#include <iostream>
#include <vector>
using namespace std;

int CalculateSum(const vector<int>& arr, int start, int end) {
    if (start == end) {
        // Przypadek bazowy - tablica zawiera tylko jeden element
        return arr[start];
    }

    int mid = (start + end) / 2;
    int sumLeft = CalculateSum(arr, start, mid);       // Suma elementów z lewej części tablicy
    int sumRight = CalculateSum(arr, mid + 1, end);    // Suma elementów z prawej części tablicy

    // Zwracamy sumę dwóch sum
    return sumLeft + sumRight;
}

int main() {
    vector<int> arr = { 1, 2, 3, 4, 5 };
    int sum = CalculateSum(arr, 0, arr.size() - 1);
    cout << "Suma elementow: " << sum << endl;
    return 0;
}