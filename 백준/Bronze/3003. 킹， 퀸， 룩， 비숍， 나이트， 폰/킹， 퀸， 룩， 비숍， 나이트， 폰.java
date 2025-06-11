import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		ArrayList<Integer> calc = new ArrayList<>(Arrays.asList(1,1,2,2,2,8));
		int i = 0;
		while(st.hasMoreTokens()) {
			int n =  calc.get(i++)- Integer.parseInt(st.nextToken());
			System.out.print(n + " ");
		}
	}

}
