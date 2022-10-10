package sk.futurum.druhaci;
import java.util.Arrays;

public class Spustac {
	public static void main(String[] args) {
    Pole pole = new Pole();

    int najvacsie = pole.getMax();
    int najmensie = pole.getMin();
    System.out.println("Najvacsie cislo je " + najvacsie);
    System.out.println("Najmensie cislo  je " + najmensie);
    System.out.print("Obratene pole: ");
    pole.reverse();
    pole.setSorted();
    System.out.println(Arrays.toString(pole.getPole()));
    System.out.println("Parnych cisel je " + pole.getNumOfEven());
    System.out.println("Neparnych cisel je " + pole.getNumOfOdd());
    System.out.println("Sucet neparnych cisel je " + pole.getSumOfOdd());
    System.out.println("Sucet parnych cisel je " + pole.getSumOfEven());
    
	}
}


