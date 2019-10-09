/***
  *
 ***/
#include<iostream>

using namespace std;
int main()
{
	int i, n, anz, freq[101]={0};
	cin>>n;
	for(i=0;i<n;++i)
	{
		cin>>anz;
		freq[anz]++;
	}
	anz=0;
	for(i=0;i<101;++i)
		anz+=(freq[i]/2);
	cout<<anz;
	return 0;
}
