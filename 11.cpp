#include <iostream>
#include <vector>
#include <limits>

int main() {
    const int MAX_T = 1e4;
    const int MAX_N = 50;
    const std::string NOTES = "abcdefg";

    std::cout << MAX_T << "\n";

    for (int t = 0; t < MAX_T; ++t) {
        std::cout << MAX_N << "\n";

        for (int n = 0; n < MAX_N; ++n) {
            std::cout << NOTES[n % 7];  // Each note is a character from 'a' to 'g'
        }
        std::cout << "\n";
    }

    return 0;
}
