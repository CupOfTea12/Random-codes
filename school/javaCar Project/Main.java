public class Main {
    public static void main(String[] args) {
        Car car = new Car("Toyota", "V6", 4, 6, 2022, 5000.5);
        
        System.out.println("Znacka: " + car.getZnacka());
        System.out.println("Motor: " + car.getMotor());
        System.out.println("Pocet kolies: " + car.getPocetKolies());
        System.out.println("Pocet svetiel: " + car.getPocetSvetiel());
        System.out.println("Rok vyroby: " + car.getRokVyroby());
        System.out.println("Pocet najazdenych kilometrov: " + car.getPocetNajazdenychKilometrov());
    }
}
