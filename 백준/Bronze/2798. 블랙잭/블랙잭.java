import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int[] card = new int[n];
        for(int i=0;i<n;i++) card[i] = Integer.parseInt(st1.nextToken());

        int max = 0;
        for(int i=0;i<n-2;i++){
            for(int j=i+1;j<n-1;j++){
                for(int k=j+1;k<n;k++){
                    int sum = card[i]+card[j]+card[k];
                    if(max<sum && sum<=m) max = sum;
                }
            }
        }
        System.out.println(max);
    }
}
