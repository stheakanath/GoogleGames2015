import java.util.HashSet;

public class Sieve {

	public static void main(String[] args) {

		long sum = 0;

		for (int i = 11; i < 1000000; i += 2) {
			if (i % 2 != 0 && i % 3 != 0 && i%5 != 0 && i%7 != 0) {
				sum += i;
			}
		}
		System.out.println(sum);
	}
}