import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuilder a = new StringBuilder(br.readLine());
		
		a.append("??!");
		
		System.out.print(a);
	}
}
