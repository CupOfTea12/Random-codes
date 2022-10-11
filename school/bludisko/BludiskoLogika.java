
package bludisko;


 class BludiskoLogika {
    
    int rozmer;
    Bludisko [][] bludisko;
    
    
    int bludisko2[][]=new int[5][5];
    
    
    public BludiskoLogika(int rozmer) {
        this.bludisko = new Bludisko[rozmer][rozmer];
        this.rozmer = rozmer;
    }
    
    public static void main(String[] args) {
        new BludiskoLogika(5);
    }

}
