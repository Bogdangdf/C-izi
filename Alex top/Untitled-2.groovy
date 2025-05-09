#include <iostream>
using namespace std;

int main() {
    double R;
    const double pi = 3.14;

    cout << "Введіть радіус кола R: ";
    cin >> R;

    double area = pi * R * R;
    double circumference = 2 * pi * R;

    cout << "Площа круга: " << int(area * 100 + 0.5) / 100.0 << endl;
    cout << "Довжина кола: " << int(circumference * 100 + 0.5) / 100.0 << endl;

    return 0;
}
