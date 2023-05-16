package Main;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        List<Car> cars = createCarList();

        // Print the list of available cars
        System.out.println("Available Cars:");
        for (int i = 0; i < cars.size(); i++) {
            System.out.println((i + 1) + ". " + cars.get(i).getZnacka());
        }

        // Prompt the user to select a car
        System.out.print("Select a car (1-" + cars.size() + "): ");
        Scanner scanner = new Scanner(System.in);
        int choice = scanner.nextInt();

        // Check if the choice is valid
        if (choice >= 1 && choice <= cars.size()) {
            Car selectedCar = cars.get(choice - 1);

            // Print the parameters for the selected car
            System.out.println("\nSelected Car Parameters:");
            System.out.println("Znacka: " + selectedCar.getZnacka());
            System.out.println("Motor: " + selectedCar.getMotor());
            System.out.println("Pocet kolies: " + selectedCar.getPocetKolies());
            System.out.println("Pocet svetiel: " + selectedCar.getPocetSvetiel());
            System.out.println("Rok vyroby: " + selectedCar.getRokVyroby());
            System.out.println("Pocet najazdenych kilometrov: " + selectedCar.getPocetNajazdenychKilometrov());
        } else {
            System.out.println("Invalid choice.");
        }

        scanner.close();
    }

    // Method to create a list of cars
    public static List<Car> createCarList() {
        List<Car> cars = new ArrayList<>();

        cars.add(new Car("Toyota", "V6", 4, 6, 2022, 5000.5));
        cars.add(new Car("Honda", "V8", 4, 8, 2021, 8000.2));
        cars.add(new Car("Ford", "V4", 4, 4, 2023, 200.7));
        cars.add(new Car("Chevrolet", "V6", 4, 6, 2022, 3500.9));
        cars.add(new Car("BMW", "V6", 4, 6, 2020, 10000.0));
        
        return cars;
    }
}
