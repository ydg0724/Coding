import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int E = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int cnt = 1;
        int i = 1, j = 1, k = 1;
        while(!(E==i && S==j && M==k)) {
            i++;
            j++;
            k++;
            cnt++;
            if(i>15) i=1;
            if(j>28) j=1;
            if(k>19) k=1;
        }
        System.out.println(cnt);
    }
}
