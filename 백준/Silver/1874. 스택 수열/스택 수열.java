
import java.util.* ;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Stack<Integer> stack = new Stack<>();
        int n = Integer.parseInt(st.nextToken());
        int count =1;
        ArrayList<String> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            int target = Integer.parseInt(st1.nextToken());
            while(count<=target){
                stack.push(count++);
                result.add("+");
            }
            //마지막 스택과 타겟이 같은 경우
            while(!stack.isEmpty() && stack.get(stack.size()-1) == target)  {
                stack.pop();
                result.add("-");
            }
        }
        if(!stack.isEmpty()) System.out.println("NO");
        else for (String s : result) System.out.println(s);

    }
}
