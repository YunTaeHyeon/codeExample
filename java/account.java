package codeExample.java;

interface Bank{
    void deposit(int a);
    void withdraw(int b);
    void Nowmoney();
}
class accountManage implements Bank{
    int money;
    accountManage(int money){
        this.money=money;
    }
    public void deposit(int a){
        System.out.println(Integer.toString(a)+"원 입금");
        money=money+a;
    }
    public void withdraw(int b){
        if(money>=b) {
            System.out.println(Integer.toString(b) + "원 출금");
            money = money - b;
        }
        else
            System.out.println("잔액 부족");
    }
    public void Nowmoney(){
        System.out.println(Integer.toString(money)+"원");
    }
}

public class account{
    public static void main(String[] args) {
        accountManage a= new accountManage(0);
        a.Nowmoney();
        a.deposit(10000);
        a.Nowmoney();
        a.withdraw(11000);
        a.withdraw(5000);
        a.Nowmoney();
    }
}
