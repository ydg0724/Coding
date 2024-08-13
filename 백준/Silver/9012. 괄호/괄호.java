
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Stack<String> stack= new Stack<>();
        int flag;
        int n = Integer.parseInt(st.nextToken());

        for (int i=0;i<n;i++){
            flag=1;
            StringTokenizer inst = new StringTokenizer(br.readLine());
            String[] para = inst.nextToken().split("");
            for (String s : para) {
                if (s.equals("(")) stack.push(s);
                else if (s.equals(")")&& stack.isEmpty()) {
                    flag = 0;
                    break;
                }
                else stack.pop();
                }
            if(flag==0) System.out.println("NO");
            else if(stack.isEmpty()) System.out.println("YES");
            else System.out.println("NO");
            stack.clear();
            }
        }
    }

