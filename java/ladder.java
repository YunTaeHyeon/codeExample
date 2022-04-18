import java.util.Random;
import java.util.Scanner;

public class ladder{
    public static void makeladder(){
        int howmany=input();
        int[] result=new int[howmany];

        Random random=new Random();
        for(int i=0; i<howmany; i++){
            result[i]=random.nextInt(2);
        }

        System.out.println("몇 번 고를래?");
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();


        if(result[a-1]==0){
            System.out.println("꽝!");
        }
        else
            System.out.println("통과!");
    }

    public static int input(){
        Scanner sc=new Scanner(System.in);
        System.out.println("몇명?: ");
        int s=sc.nextInt();

        return s;
    }

    public static void main(String[] args) {
        makeladder();
    }
}