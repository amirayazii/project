#include <iostream>
using namespace std;

// function to check if a number is Prime
bool isprime(int num) {
    if (num <= 1) {
        return false;
    }
for (int i = 2; i * i <= num; ++i) {
    if (num % i == o) {
        return false
    }
}
return true;;
}

// Function to find the sum of prime numbers up to N 
int sum Ofprimes(int N) {
    int sum = 0;
    for (int i = 2; i <= N; ++i) {
        if(isprime(i)) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int N;
    cout << "enter a positive integer N: ";
    cin >> N;
    
    int result = sumOfprimes(N);
    cout << "sum of prime numbers up to " << N << ": " << result << endl;

return 0;
}