import java.util.*;
import java.io.*;

public class Stocks {
	
	public static void main(String[] args) {

		HashMap<Character, Character> letters = new HashMap<Character, Character>();

		letters.put('A', '2');
		letters.put('B', '2');
		letters.put('C', '2');
		letters.put('D', '3');
		letters.put('E', '3');
		letters.put('F', '3');
		letters.put('G', '4');
		letters.put('H', '4');
		letters.put('I', '4');
		letters.put('J', '5');
		letters.put('K', '5');
		letters.put('L', '5');
		letters.put('M', '6');
		letters.put('N', '6');
		letters.put('O', '6');
		letters.put('P', '7');
		letters.put('Q', '7');
		letters.put('R', '7');
		letters.put('S', '7');
		letters.put('T', '8');
		letters.put('U', '8');
		letters.put('V', '8');
		letters.put('W', '9');
		letters.put('X', '9');
		letters.put('Y', '9');
		letters.put('Z', '9');

		HashMap<String, Integer> map = new HashMap<String, Integer>();

		try {
			Scanner file = new Scanner(new FileReader("stocks"));
			while (file.hasNext()) {
				String x = "";
				String next = file.nextLine();
				for (int i = 0; i < next.length(); i++){
    				char c = next.charAt(i);        
   					x += letters.get(c);
				}
				if (map.containsKey(x)) {
					map.put(x, map.get(x) + 1);
				} else {
					map.put(x, 1);
				}
			}
			//System.out.println(map);
			int count = 0;
			Collection c = map.values();
		    Iterator itr = c.iterator();
		    while (itr.hasNext()) {
		      int d = (int) itr.next();
		      if (d == 1) {
		      	count += 1;
		      }
		    }
		    System.out.println(count);
		} catch (Exception e){System.out.println("error");}


	}
}