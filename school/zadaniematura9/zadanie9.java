
package sk.futurm.stvrtaci;

//---LIBRARIES---//
import java.util.*;
public class zadanie9 {

	//---GLOBAL-VARIABILES---//
	Scanner scan = new Scanner(System.in);
	int factorial;
	int i,fact=1;
	
	public void calculate() {
		System.out.println("Enter the factorial number: ");
	    factorial = scan.nextInt();
	    System.out.println("You've entered ! " + factorial );
	    for(i=1;i<=factorial;i++){    
	        fact=fact*i;    
	    } 
	    System.out.println("Factorial of "+factorial+" is: "+fact);    
	 }  
	      	
	
	
	
	public static void main(String[] args) {
		zadanie9 run = new zadanie9();
		run.calculate();

	}

}
