import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        ArrayList<Integer> Circle = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int kill = -1;

        for(int i=1;i<=n;i++){
            Circle.add(i);
        }

        while(!Circle.isEmpty()){
            kill+=k;
            if(kill>=Circle.size()){
                kill %= Circle.size();
            }
            result.add(Circle.get(kill));
            Circle.remove(kill--);
        }

        System.out.print("<");
        for(int i=0;i< result.size()-1;i++) System.out.print(result.get(i)+", ");
        System.out.print(result.get(result.size()-1));
        System.out.print(">");
    }
}
