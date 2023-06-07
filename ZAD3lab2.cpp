#include <iostream>
#include <vector>
using namespace std;

int FindMax(const vector<int>& arr, int start, int end) {
    if (start == end) {
        // Przypadek bazowy - wektor zawiera tylko jeden element
        return arr[start];
    }

    int mid = (start + end) / 2;
    int maxLeft = FindMax(arr, start, mid);      // Największy element z lewej części wektora
    int maxRight = FindMax(arr, mid + 1, end);   // Największy element z prawej części wektora

    // Zwracamy większy z dwóch największych elementów
    return max(maxLeft, maxRight);
}

int main() {
    vector<int> arr = { 7, 2, 10, 15, 4, 9, 12 };
    int maxElement = FindMax(arr, 0, arr.size() - 1);
    cout << "Najwiekszy element: " << maxElement << endl;
    return 0;
}