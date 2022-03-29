package codeExample.java;

import java.util.Scanner;

public class login {
    public static void main(String arg[]) {
        String id = "th";
        String pass1 = "1111";
        String pass2 = "2222";
        int tryNumber=0;
        while(true) {
            String getid=id();
            String getpass=pass();
            boolean isRightPass = (getpass.equals(pass1) || getpass.equals(pass2));
            if (getid.equals(id) && isRightPass) {
                System.out.println("Success");
                return;
            }
            else {
                System.out.println("one more");
                tryNumber++;
                if(tryNumber==5){
                    System.out.println("Attempts over");
                    return;
                }
            }
        }
    }
    public static String id(){
        Scanner sc = new Scanner(System.in);
        System.out.println("id");
        String inputid = sc.next();

        return inputid;
    }
    public static String pass(){
        Scanner sc = new Scanner(System.in);
        System.out.println("password");
        String inputpass = sc.next();

        return inputpass;
    }
}


