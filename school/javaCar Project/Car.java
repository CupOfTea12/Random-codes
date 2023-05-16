public class Car {
    private String znacka;
    private String motor;
    private int pocetKolies;
    private int pocetSvetiel;
    private int rokVyroby;
    private double pocetNajazdenychKilometrov;

    // Constructor
    public Car(String znacka, String motor, int pocetKolies, int pocetSvetiel, int rokVyroby, double pocetNajazdenychKilometrov) {
        this.znacka = znacka;
        this.motor = motor;
        this.pocetKolies = pocetKolies;
        this.pocetSvetiel = pocetSvetiel;
        this.rokVyroby = rokVyroby;
        this.pocetNajazdenychKilometrov = pocetNajazdenychKilometrov;
    }

    // Getters
    public String getZnacka() {
        return znacka;
    }

    public String getMotor() {
        return motor;
    }

    public int getPocetKolies() {
        return pocetKolies;
    }

    public int getPocetSvetiel() {
        return pocetSvetiel;
    }

    public int getRokVyroby() {
        return rokVyroby;
    }

    public double getPocetNajazdenychKilometrov() {
        return pocetNajazdenychKilometrov;
    }
}
