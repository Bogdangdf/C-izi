#include <iostream>

bool isPalindrome(int num) {
    int reversed = 0, original = num;
    while (num > 0) {
        reversed = reversed * 10 + num % 10;
        num /= 10;
    }
    return original == reversed;
}

int main() {
    for (int i = 1; i < 100; i++) {
        if (isPalindrome(i) && isPalindrome(i * i)) {
            std::cout << i << " -> " << i * i << std::endl;
        }
    }
    return 0;
}
