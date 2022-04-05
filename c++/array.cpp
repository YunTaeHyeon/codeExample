#include<iostream>
#include<string>
using namespace std;

int main(){
    string s;
    cout<<"문자열 입력"<<endl;

    cout<<s<<endl;

    string *str=new string();
    str->append("hi");

    cout<<*str<<endl;

/*    string arr[5];
    for(int i=0; i<5; i++){
        getline(cin,arr[i]);
    }
    for(int j=0; j<5; j++){
        cout<<arr[j]<<endl;
    }
    */
   string *arr=new string[5];
    for(int i=0; i<5; i++){
        getline(cin,arr[i]);
    }
    for(int j=0; j<5; j++){
        cout<<arr[j]<<endl;
    }
}