import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        ArrayList<Integer> stack = new ArrayList<>();

        int n = Integer.parseInt(st.nextToken());
        int top = -1;
        for (int i = 0; i < n; i++) {
            StringTokenizer stWord = new StringTokenizer(br.readLine());
            String word = stWord.nextToken();
            if(word.equals("push")){
                int x = Integer.parseInt(stWord.nextToken());
                stack.add(x);
                top+=1;
            } else if(word.equals("pop")){
                if(top==-1) System.out.println(-1);
                else {
                    int x = stack.get(top);
                    System.out.println(x);
                    stack.remove(top);
                    top -= 1;
                }
            } else if(word.equals("top")){
                if(top!=-1) System.out.println(stack.get(top));
                else System.out.println(-1);

            } else if (word.equals("size")) {
                System.out.println(stack.size());
            } else if (word.equals("empty")) {
                if(top==-1) System.out.println(1);
                else System.out.println(0);
            }
        }
    }
}
