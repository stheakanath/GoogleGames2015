import java.util.*;
import java.io.*;

public class Chutes {

	static Random diceRoller = new Random();


	public static void main (String[] args) {
		int times = 100000000;
		double total  = 0;
		//Random diceRoller = new Random();
		for (int i = 0; i < times; i ++) {
			total += roll();
		}
		System.out.println(total / times);
	}

	public static double roll() {
		// Random diceRoller = new Random();
		int turns = 0;
		int place = 0;
		while (place < 30) {
			int next = diceRoller.nextInt(6) + 1;
			if (next == 6) {
				place = 0;
			} else {
				place += next;
			}
			turns += 1;
		}
		return turns;
	}
}