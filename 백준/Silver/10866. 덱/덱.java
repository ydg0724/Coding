import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Integer> Deque = new ArrayList<>();
        int top=-1;
        int bottom=0;
        int n = Integer.parseInt(st.nextToken());

        for(int i=0;i<n;i++){
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            String order = st1.nextToken();

            if(order.equals("push_front")){
                int num = Integer.parseInt(st1.nextToken());
                Deque.add(bottom,num);
                top++;
            }
            else if(order.equals("push_back")){
                int num = Integer.parseInt(st1.nextToken());
                Deque.add(++top,num);
            }
            else if(order.equals("pop_front")){
                if(bottom>top) System.out.println(-1);
                else System.out.println(Deque.get(bottom++));
            }
            else if(order.equals("pop_back")){
                if(bottom>top) System.out.println(-1);
                else System.out.println(Deque.get(top--));
            }
            else if(order.equals("size")){
                System.out.println(top-bottom+1);
            }
            else if(order.equals("empty")){
                if(bottom>top) System.out.println(1);
                else System.out.println(0);
            }
            else if(order.equals("front")){
                if(bottom>top) System.out.println(-1);
                else System.out.println(Deque.get(bottom));
            }
            else if(order.equals("back")){
                if(bottom>top) System.out.println(-1);
                else System.out.println(Deque.get(top));
            }
        }
    }
}
