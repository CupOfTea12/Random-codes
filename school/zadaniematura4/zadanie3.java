package sk.futurm.stvrtaci;

//---LIBARRIES---//
import java.util.*;


public class Zadanie4 {
    
    //---GLOBAL-VARS---//
    int cislo;
    int counter=0;
    
    //---OBJECTS---//
    Scanner  scan = new Scanner(System.in);
    
    
    public void kolkoCifier(){
        System.out.println("Zadajte cislo:  " );
        try{
    cislo = scan.nextInt();
}
catch(InputMismatchException e){
    System.out.println("Presiahol si moznu velkost datoveho typu INT");  
}
        
         if(cislo ==0){
            System.out.println("Cislo sa rovna nule, program bol ukonceny");
        }else{
  
        while (cislo != 0) {
      cislo /= 10;
      ++counter;
    }
        System.out.println("Pocet cifier v zadanom cisle je :  " + counter +".");
        
        
         }
    }

    
    public static void main(String[] args) {
        Zadanie4 run = new Zadanie4();
        run.kolkoCifier();
    }
    
}
