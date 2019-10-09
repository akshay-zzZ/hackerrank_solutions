/***
  *
 ***/
#include<iostream>
#include<set>
#include<string.h>

using namespace std;
int main()
{
    long int i, j, n, l, sum;
    set <long int> s;
    string str;
    cin>>str>>n;
    l=str.length();
    long int val[n];
    for(i=0;i<n;++i)
        cin>>val[i];
    for(i=0;i<(l);++i)
    {
        sum=0;
        j=i;
        while(str[i]==str[j] && j<l)
        {
            sum+=(str[i]-96);
            ++j;
            s.insert(sum);
        }
        i=(j-1);
    }
    for(i=0;i<n;++i)
        if(s.find(val[i])!=s.end())
            cout<<"Yes\n";
        else
            cout<<"No\n";
    return 0;
}        
