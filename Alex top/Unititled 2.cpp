#include <iostream>

int main() {
    
    char name[10]; 

    std::cout << "Впиши ім'я:";
    std::cin.getline(name, 10); 
    
    std::cout << "Hello " << name << "!" << std::endl;

    return 0;
}