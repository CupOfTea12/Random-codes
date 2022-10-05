package sk.futurm.stvrtaci;
import java.util.Arrays;

/**
*
* @author adriana stanikova
*
* Tato trieda jednoducho pracuje s polom intov...
*
/
public class Pole {

private int pole[] = new int[10];

public Pole() {
for (int i = 0; i < 10; ++i) {
pole[i] = (int) (Math.random() 100);
}
System.out.println(Arrays.toString(pole));

}

public Pole(int[] pole) {

this.pole = pole;
}

public Pole(String s) {
// vyparsuj jednotlive cisla do pola
}

// private int pole[] = new int[] { 1, 3, 4, 5, 7, 9, 77 };

int getMax() {

int result = 0;

for (int i = 0; i < pole.length; ++i) {
if (i == 0)
result = pole[i];
if (pole[i] > result) {
result = pole[i];
}
}
return result;
}

int getMin() {
int result = 0;

for (int i = 0; i < pole.length; ++i) {
if (i == 0)
result = pole[i];
if (pole[i] < result) {
result = pole[i];
}
}
return result;
}

void setReverse() {

for (int i = 0; i < pole.length / 2; ++i) {
int tmp = pole[i];
pole[i] = pole[pole.length - 1 - i];
pole[pole.length - 1 - i] = tmp;
}
}

void setSorted() {
boolean prechod = true;
while (prechod) {
prechod = false;
for (int i = 0; i < pole.length - 1; ++i) {
if (pole[i] > pole[i + 1]) {
prechod = true;
int tmp = pole[i];
pole[i] = pole[i + 1];
pole[i + 1] = tmp;
}
}
}
}

public int[] getPole() {
return pole;
}

public void setPole(int[] pole) {
this.pole = pole;
}

// neparne cisla
public int[] getOdd() {
int counter = 0;

for (int i = 0; i < pole.length; ++i) {
if (pole[i] % 2 != 0) {
counter++;
}

}
System.out.println("Pocet neparnych je " + counter);

int nove_pole[] = new int[counter];

for (int i = 0, a = 0; i < pole.length; ++i) {
if (pole[i] % 2 != 0)
nove_pole[a++] = pole[i];
}

// Arrays.copyOf(pole, counter)
return nove_pole;
}

}
