package strvtaci.fizzbus;

public class Maturita1 {
	
	public static void main(String[] args) {
		//fizzbus code
		
		
      for (int i =0; i <=1000; i++) {
    	  if(i % 3 == 0 && i % 5 == 0) {
    		  System.out.println(i + " FizzBuzz");
    	  }
    	  else if (i % 5 == 0) {
				System.out.println(i + " Buzz");
			}
			else if (i % 3 == 0) {
				System.out.println(i + " Fizz");
			}
			else if (i % 4 == 0) {
				System.out.println(i + " Geno");
			}
			else {
				System.out.println(i);
			}
			
    	  
      }

	}

}
