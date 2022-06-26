#include <iostream>
#include <string>
using namespace std;


class Human{
    protected:
    string name;
    int age;
    public:
    void walking(){
        cout<<"walk"<<endl;
    }
    void sleeping(){
        cout<<"sleep"<<endl;
    }
};

class Student: public Human{
    protected:
    string school;
    public:
    Student(string name,int age,string school){
        this->name=name;
        this->age=age;
        this->school=school;
    }
    void goSchool(){
        cout<<"go to school"<<endl;
    }
};

int main(void){
    Student Yun("Yun",23,"Dankook");
    Yun.walking();
    Yun.goSchool(); 
    Yun.sleeping();  
}