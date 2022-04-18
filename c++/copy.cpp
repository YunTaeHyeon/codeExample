#include <iostream>
using namespace std;

/* int main(){
    int* a=new int(3);
    int* b=new int(5);

    cout <<"a의 주소(복사전)"<< a<<endl;
    cout <<"b의 주소(복사전)"<< b<<endl;

    a=b

    cout <<"a의 주소"<<a<<endl;
    cout <<"b의 주소"<<b<<endl;

    delete a;
    delete b;
}
*/
//에러 발생함

class num{
private:
    int *a;
public:
    num(int m){
        cout<<"생성자 호출"<<endl;
        a=new int;
        *a=m;
    }
    num(const num& obj){
        cout<<"복사 생성자 호출"<<endl;
        a=new int;
        *a=obj.getA();
    }
    int getA() const{
        return *a;
    }
    void setA(int m){
        *a=m;
    }
    void printA(){
        cout<<*a<<endl;
    }
    ~num(){
        cout<<"소멸자 호출"<<endl;
        delete a;
    }
};

int main(void){
    num i(5);
    i.printA();
    num y=i;
    y.setA(3);
    y.printA();


    return 0;
}