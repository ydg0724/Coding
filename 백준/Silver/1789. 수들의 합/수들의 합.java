import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long n =Long.parseLong(br.readLine());
        int cnt = 0;
        int i =1;
        while(n>=i){
            n -= i++;
            cnt++;
        }
        System.out.println(cnt);
    }
}
