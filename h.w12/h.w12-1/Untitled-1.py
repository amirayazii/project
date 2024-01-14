#include <iostream>
#include <cmath>
using namespace std;
const double pi = 3.14159265;
double deg_to_rad =( double deg){
    
    return * pi / 180.0;
}
double tan_x(double x){
    
    double rad=deg_to_rad(x);
    return tan(rad);
}
int main(){
    
    double x;
    std::cout <<"Enter x in degrees:";
    std::cin >> x;
    double result=tan_x(x);
    std::cout <<"tan("<<x<<")="<<result<<"\n";
    
    
    
    return 0;
    
}