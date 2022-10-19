//nudim sa celkom uz :,))
package sk.futurm.stvrtaci;
import java.util.*;

public class zadanie3 {
	
	//---GLOBAL-VARS---//
	 final double pi = 3.14;  
	 int r;
	 
	 
	 //---OBJECTS---//
	 Scanner scan = new Scanner(System.in);
	 

	
	public void obvodKruhu() {
		System.out.println("Zadajte polomer pre vypocet: ");
		r = scan.nextInt();
		System.out.println("Obvod kruhu je: " + 2*r*pi);
		
	}
	
	public void obsahKruhu() {
		System.out.println("Obsah krhu je: " + pi*(r*r));
	}
	
	public void objemGule() {
		System.out.println("Objem gule je: " + (4/3)*pi*(r*r*r));
		
	}
	
	
	
	public static void main(String[] args) {
         zadanie3 run = new zadanie3();
         run.obvodKruhu();
         run.obsahKruhu();
         run.objemGule();
	}

}
