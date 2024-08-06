import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int result=0, cnt,cur,tmp,pre;
        int mem=0;

        for(int i=1;i<=n;i++) {
            cnt=0;
            cur=n;
            pre = i;
            while(cur>=0){
                cur = cur-pre;
                cnt++;
                tmp= cur;
                cur = pre;
                pre = tmp;
            }
            if(result<cnt) {
                result = cnt;
                mem=i;
            }
        }
        System.out.println(result);
        while (n>=0){
            System.out.print(n+" ");
            n = n-mem;
            tmp = n;
            n = mem;
            mem = tmp;
        }
    }
}
