#include<iostream>
//#include<conio.h>
using namespace std ;
class A 
{
	int a,b ; 
	public :
		A()
		{
			a = 10;
			b = 20 ;
		}
		~A()
		{
			cout <<"a="<<a<<endl;
			cout <<"b="<<b<<endl;
			//getche();
		}
};
main()
{
	A sample ;
}

    