#include<iostream>
using namespace std;
int gcd(int a < int b ){
    
    if (b==0)
    {
        return a;
    }
    else{
        
        
        return gcd(b,a%b);
        
        
        
        
    }
    
}
int main(){
    
    cout <<"the greatest comin divisor of two two natural numbers \n\n";
    
    
    int x,y;
    
    while (true)
    {
        cout <<" x = ";
        cin>>x;
        cout <<" y = ";
        cin >>y;
        
        
        if (x<1||y<1){
            
            cout <<"the program is terminated.";
            
            
            
            
        }
    }
    cout <<"gcd ="<<gcd(x,y)<<endl<<endl;
    
    
}