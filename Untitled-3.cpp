#include <iostream>

int main() {

    int a, b;

    std::cout << "Впиши два числа: ";
    std::cin >> a >> b;

    std::cout << "Сума: " << (a + b) << std::endl;
    std::cout << "Різниця: " << (a - b) << std::endl;
    std::cout << "Добуток: " << (a * b) << std::endl;

    return 0;
}
