#include <iostream>
#include <cmath>

using namespace std;
int main() {
    
    int m,n,r,q;
    
    cout<<"please enter your number\n";
    
    cin>>m;
    cout<<"devided to\n";
    cin>>n;
    if (m==n) {
        
        cout<<"your q is 1 and your r is 0";
    }
q=0;
r=0;
while (m>=n) {
    
    m=m-n;
    q++;
}
cout<<r<<" ";
cout<<q;

}







