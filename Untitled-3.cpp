#include <iostream>

using namespace std;

int main() {
    const int D = 1000;
    bool sieve[D + 1];

    for (int i = 2; i <= D; i++) {
        sieve[i] = true;
    }

    for (int i = 2; i <= D; i++) {
        if (sieve[i]) {
            for (int j = i * 2; j <= D; j += i) {
                sieve[j] = false;
            }
        }
    }

    for (int i = 2; i <= D; i++) {
        if (sieve[i]) {
            cout << i << " ";
        }
    }
    cout << endl;
    return 0;
}
