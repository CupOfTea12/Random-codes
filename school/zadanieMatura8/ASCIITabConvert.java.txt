
package asciitabconvert;
//---LIBRARIES---//
import java.util.*;



public class ASCIITabConvert {
    //---GLOBAL-VARIABILES---//
    String input;
    
    
    //---OBJECTS---//
    Scanner scan = new Scanner(System.in);
    //---MAIN---//
    public void porovnajASCII(){
        //input
        System.out.println("Zadajte charakter: ");
        input = scan.nextLine();
        
        //porovnavanie
        char asciiThingie=input.charAt(0);
        int castAscii = (int) asciiThingie;
         System.out.println("Hodnota zadaneho charakteru  ' " + asciiThingie + " ' v ASCII tabulke je : " + castAscii);
         
    }

    public static void main(String[] args) {
        ASCIITabConvert run = new ASCIITabConvert();
        run.porovnajASCII();
        
    }
    
}
