package bludisko;

class Bludisko {
//---VARIABILES---//
int cislo;
char cross= '+';
String rozdelenie="----";
String oddelenie ="|";



public Bludisko(int cislo) {
        this.cislo = cislo;
    }

 public void zobraz() {
        System.out.printf("%02d ", this.cislo);
    }
    
    public static void main(String[] args) {
     
    }
    
}
