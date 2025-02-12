#include <iostream>

int main() {
    int n;
    std::cin >> n;

    for (int i = 1; i <= n; ++i) {
        for (int j = i; j <= n; ++j) {
            for (int h = j; h <= n; ++h) {
                if (i * i + j * j == h * h) {
                    std::cout << i << " " << j << " " << h << std::endl;
                }
            }
        }
    }

    return 0;
}