#include <iostream>

int main() {
    int n;
    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        int name = 1;
        for (int j = 0; j <= i; ++j) {
            std::cout << name << " ";
            name = name * (i - j) / (j + 1);
        }
        std::cout << std::endl;
    }

    return 0;
}