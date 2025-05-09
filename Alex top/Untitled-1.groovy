#include <iostream>
using namespace std;


int main() {
    double A, B, C;

    cout << "Довжина A: ";
    cin >> A;

    cout << "Ширина B: ";
    cin >> B;

    cout << "Висота C: ";
    cin >> C;

    double volume = A * B * C;

    double surfaceArea = 2 * (A * B + A * C + B * C)

    cout << "Об'єм паралелепіпеда: " << volume << endl;
    cout << "Площа паралелепіпеда: " << surfaceArea << endl;

    return 0;
}
