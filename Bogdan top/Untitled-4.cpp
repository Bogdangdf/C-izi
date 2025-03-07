#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Ведіть ім'я: ";
    cin >> a;

    for (int d = 2; a > 1; d++) {
        while (a % d == 0) {
            cout << d << " ";
            a /= d;
        }
    }

    cout << endl;
    return 0;
}
