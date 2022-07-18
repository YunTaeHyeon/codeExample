#include <iostream>
using namespace std;

class cafe{
    protected:
    int price=0;

    public:
    void order(void){
        int a=0;

        while(1){
        cout<< "order" <<endl;
        cout<< "1. Americano:4500"<<endl;
        cout<< "2. CafeLatte:5000"<<endl;
        cout<< "3. MilkTea:6000" <<endl;
        
        cin>>a;
        if (a==1 || a==2 || a==3)
            pay(a);
            break;
        }
    }
    void pay(int a){
        if (a==1)
        price+=4500;
        else if(a==2)
        price+=5000;
        else
        price+=6000;

        cout<<"You have to pay "<<price<<endl;
    }
};

class trianon:public cafe{
    public:

    void boardgame(void){
        cout<< "boardgame" <<endl;
    }
};

int main(void){
    trianon cafe;
    int i=0;
    while(1){
        cout<<"welcome"<<endl<<endl;
        cout<<"1. order"<<endl;
        cout<<"2. boardgame"<<endl;
        cout<<"3. exit"<<endl;

        cin>>i;

        if(i==1)
        cafe.order();

        if(i==2)
        cafe.boardgame();

        if(i==3)
        break;
        
    }
}