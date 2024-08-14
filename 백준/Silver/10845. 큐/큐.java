import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        ArrayList<Integer> queue = new ArrayList<>();
        int bottom = 0;
        int top = -1;
        int n = Integer.parseInt(st.nextToken());

        for(int i=0;i<n;i++){
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            String order = st1.nextToken();
            if(order.equals("push")){
                int num = Integer.parseInt(st1.nextToken());
                queue.add(num);
                top+=1;
            }
            if(order.equals("pop")){
                if(top<bottom) System.out.println(-1);
                else System.out.println(queue.get(bottom++));
            }
            if(order.equals("size")){
                if(top<bottom) System.out.println(0);
                else System.out.println(top-bottom+1);
            }
            if(order.equals("empty")){
                if(top<bottom) System.out.println(1);
                else System.out.println(0);
            }
            if(order.equals("front")){
                if(top<bottom) System.out.println(-1);
                else System.out.println(queue.get(bottom));
            }
            if(order.equals("back")){
                if(top<bottom) System.out.println(-1);
                else System.out.println(queue.get(top));
            }
        }
    }
}
