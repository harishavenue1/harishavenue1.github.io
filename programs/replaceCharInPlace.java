import java.util.Arrays;
import java.util.List;
import java.util.ListIterator;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ReplaceCharInplace {
	
	public static void main(String[] args) {
		String str = "tomorrow";
		System.out.println("Replaced String "+ replacedString_1(str));
		System.out.println("Replaced String "+ replacedString_2(str));
		System.out.println("Replaced String "+ replacedString_3(str));
	}
	
	public static String replacedString_1(String str) {
		List<Character> list = str.chars().mapToObj(e->(char)e).collect(Collectors.toList());
		ListIterator<Character> lit = list.listIterator();
		while (lit.hasNext()) {
			if (lit.next() == 'o')
				lit.set('&');
		}
		return String.join("", list.stream().map(String::valueOf).collect(Collectors.toList()));
	}
	
	public static String replacedString_2(String str) {
		int count = 1;
		StringBuilder sb = new StringBuilder();
		for (char c: str.toCharArray()) {
			if (c == 'o') {
				sb.append(IntStream.range(1, ++count).boxed().map(String::valueOf).collect(Collectors.joining("")));
			} else
				sb.append(c);
		}
		return sb.toString();
	}
	
	public static String replacedString_3(String str) {
		int count = 1;
		List<String> li = Arrays.asList(str.split(""));
		ListIterator<String> lit = li.listIterator();
		while (lit.hasNext()) {
			if (lit.next().equalsIgnoreCase("o"))
				lit.set("&".repeat(count++));
		}
		return String.join("", li);
	}

}
