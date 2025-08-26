import java.util.Arrays;
import java.util.List;
import java.util.ListIterator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class java_code {
	
	public static void main(String[] args) {
		String str = "tomorrow";
		System.out.println("Replaced String "+ replacedString_1(str));
		System.out.println("Replaced String "+ replacedString_2(str));
		System.out.println("Replaced String "+ replacedString_3(str));
	}
	
	public static String replacedString_1(String str) {
		
		// Java: Stream API to convert string to Character list
		List<Character> list = str.chars().mapToObj(e->(char)e).collect(Collectors.toList());
		
		// Java: ListIterator for bidirectional iteration with modification
		ListIterator<Character> lit = list.listIterator();
		
		while (lit.hasNext()) {
			if (lit.next() == 'o')
				
				// Java: .set() replaces current element
				lit.set('&');
		}
		
		// Java: String.join() + Stream API to convert back to string
		return String.join("", list.stream().map(String::valueOf).collect(Collectors.toList()));
	}
	
	public static String replacedString_2(String str) {
		int count = 1;
		
		// Java: StringBuilder for efficient string building
		StringBuilder sb = new StringBuilder();
		
		// Java: .toCharArray() converts string to char array for iteration
		for (char c: str.toCharArray()) {
			if (c == 'o') {
				
				// Java: IntStream.range() + Stream API to generate number sequence
				sb.append(IntStream.range(1, ++count).boxed().map(String::valueOf).collect(Collectors.joining("")));
			} else
				
				// Java: .append() adds to StringBuilder
				sb.append(c);
		}
		
		// Java: .toString() converts StringBuilder to String
		return sb.toString();
	}
	
	public static String replacedString_3(String str) {
		int count = 1;
		
		// Java: Arrays.asList() + .split("") creates list of single characters
		List<String> li = Arrays.asList(str.split(""));
		
		ListIterator<String> lit = li.listIterator();
		
		while (lit.hasNext()) {
			
			// Java: .equalsIgnoreCase() for case-insensitive comparison
			if (lit.next().equalsIgnoreCase("o"))
				
				// Java: .repeat() method (Java 11+) for string repetition
				lit.set("&".repeat(count++));
		}
		
		// Java: String.join() concatenates list elements
		return String.join("", li);
	}

}
