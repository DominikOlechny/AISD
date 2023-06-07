#include <iostream>
using namespace std;

void Merge(int l, int m, int r, int A[], int B[]);

int main(int argc, char** argv) {
    //dwie połowy tablicy - [0..4]; [5..9] - powinny być posortowane rosnąca 
    int A[]{ 1,35,42,65,68,25,55,59,70,79 };
    int B[sizeof(A)/sizeof(A[0])];

    Merge(0, 5, 9, A, B);
    for (int b : B)
        cout << b << ' ';
    return 0;
}

void Merge(int l, int m, int r, int A[], int B[]) {
    int i, j, k;
    i = k = l;
    j = m;

    while (i < m && j <= r) {
        if (A[i] <= A[j]) {
            B[k] = A[i];
            i++;
        } else {
            B[k] = A[j];
            j++;
        }
        k++;
    }

    while (i < m) {
        B[k] = A[i];
        i++;
        k++;
    }

    while (j <= r) {
        B[k] = A[j];
        j++;
        k++;
    }
}