interface TV{
    void turnOn();
    void turnOff();
    void upVolume(int a);
    void downVolume(int b);
    void nowVolume();
}

class smartTV implements TV{
    int volume;
    int TVON=0;

    smartTV(int volume){this.volume=volume;}

    public void turnOn(){
        System.out.println("Turn on TV");
        TVON=1;
    }
    public void turnOff(){
        if(TVON==1)
            System.out.println("Turn off TV");
        else
            System.out.println("no answer");
    }

    public void upVolume(int a){
        System.out.println(Integer.toString(a)+". UP");
        volume=volume+a;
    }
    public void downVolume(int b){
        System.out.println(Integer.toString(b)+". Down");
        volume=volume-b;
        if(volume<0)
            volume=0;
    }
    public void nowVolume(){
        System.out.println("Volume is "+Integer.toString(volume));
    }

}

public class WatchingTV{
    public static void main(String[] args) {
        smartTV s = new smartTV(10);
        s.turnOn();
        s.nowVolume();
        s.upVolume(1);
        s.nowVolume();
        s.downVolume(2);
        s.nowVolume();
        s.turnOff();
    }
}