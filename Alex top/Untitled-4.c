#include <iostream>
using namespace std;

const int MAX_N = 10; 
int N;
int a[MAX_N];

void find(int pos, int start, int sum, int product) {
    if (pos == N) {
        if (sum == product) {
        
            for (int i = 0; i < N; i++) {
                cout << a[i] << " ";
            }
            cout << endl;
        }
        return;
    }

    for (int i = start; i <= 10; i++) { 
        a[pos] = i;
        find(pos + 1, i, sum + i, product * i);
    }
}

int main() {
    cout << "Напиши N: ";
    cin >> N;

    if (N <= 0 || N > MAX_N) {
        cout << "Впиши 1 " << MAX_N << endl;
        return 1;
    }

    find(0, 1, 0, 1);

    return 0;
}