package motus2it;

import java.util.*;


public class mainer {
	
	//---OBJECTS---//
	Scanner scan = new Scanner(System.in);

	
	public void fibonnaci() {
		int i = 1, n = 0, firstTerm = 1, secondTerm = 1;
		System.out.println("Zadajte mnozstvo cisiel vo vypise: ");
		n= scan.nextInt();
	    System.out.println("Fibonnaciho postupnost " + n + " terms:");

	    while (i <= n) {
	      System.out.print(firstTerm + ", ");

	      int nextTerm = firstTerm + secondTerm;
	      firstTerm = secondTerm;
	      secondTerm = nextTerm;

	      i++;
	    }
	}
	

	public static void main(String[] args) {
		mainer run = new mainer();
		run.fibonnaci();
		

}
}
