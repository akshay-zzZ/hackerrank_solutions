//https://codeforces.com/problemset/problem/276/C
#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	long long n,q,t;
	cin>>n>>q;
	map <long long,long long> m;
	for(long long i=0;i<n;++i)
	{
		cin>>t;
		m[t]++;
	}
	long long x[n]={0};
	while(q--)
	{
		long long l,r;
		cin>>l>>r;
		x[l-1]++;
		if(r<n)
			x[r]--;
	}
	for(long long i=1;i<n;++i)
		x[i]+=x[i-1];
	map <long long,long long> m2;
	for(long long i=0;i<n;++i)
		m2[x[i]]++;
	long long sum=0;
	//map<long long, long long>::iterator itr1,itr2;
	for (auto itr1 = m.begin(),itr2=m2.begin(); itr1 != m.end() and itr2 != m2.end(); )
	{	//cout<<itr1->first<<' '<<itr2->first<<'\n';
		sum+=(itr1->first*itr2->first);
		m[itr1->first]--;
		m2[itr2->first]--;
		if (m[itr1->first]==0)
			itr1++;
		if (m2[itr2->first]==0)
			itr2++;
		
	}
	cout<<sum;
}
