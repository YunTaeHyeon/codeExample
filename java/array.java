public class array {
    public static void main(String[] args) {
        int[] array=new int[5];
        int i=0;
        while(i<array.length){
            array[i]=1;
            i++;
        }
        i=0;
        while(i<array.length){
            System.out.println(array[i]);
            i++;
        }
    }
}
