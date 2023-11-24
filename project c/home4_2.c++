#include <iostream>
#include <cmath>
using namespace std;
int main(){
     int x,y,z,q,d,m,n,i;
cout<<"please enter your firstnumber:";
cin>>x;
cout<<"please enter your second number:";
cin>>y;
cout<<"please enter your third number:";
cin>>z;
m=x-y;
q=x+z;
n=m*q;
d=(x*x)+(x*y)+(x*z)+(y*y)+(y*x)+(y*z)+(z*z)+(z*x)+(z*y);
i=d+1;
cout<<n/i;
}