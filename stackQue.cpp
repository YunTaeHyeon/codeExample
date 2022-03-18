#include <iostream>

using namespace std;

class stack{
    public:
    int *p=new int[100];
    int count=0;
    int push(void){
        cout << "number" << endl;
        cin >> p[count];
        cout << p[count] <<". add" <<endl;
        count++;
        return count;
    }
    int pop(void){
        if(count!=0){
            cout<<p[count-1]<<". remove"<<endl;
            count--;
    }
        else
            cout<< "no element" << endl;
        return count;
    }
    void list(void){
        cout<<endl<<"list"<<endl;
        for(int i=0;i<count;i++){
            cout << p[i] << endl;
        }
    }
    ~stack(){
        delete[] p;
    }
};

class que{
    public:
    int *p=new int[100];
    int count=0;
    int push(void){
        cout << "number" << endl;
        cin >> p[count];
        cout << p[count] <<". add" <<endl;
        count++;
        return count;
    }
    int pop(void){
        if(count!=0){
            cout<<p[0]<<". remove"<<endl;
            for(int i=0; i<count-1; i++){
                p[i]=p[i+1];
            }
            count--;
        }
        else
            cout<<"no element" <<endl;
        return count;
        }
    void list(void){
        cout<<endl<<"list"<<endl;
        for(int i=0;i<count;i++){
            cout << p[i] << endl;
        }
    }
     ~que(){
        delete[] p;
    }
};

int main(void){
    
    que s; // <-example
    s.push();
    s.push();
    s.push();
    s.pop();
    s.list();

    stack a;
    a.push();
    a.pop();
    a.push();
    a.push();
    a.list();
    
    return 0;
}
