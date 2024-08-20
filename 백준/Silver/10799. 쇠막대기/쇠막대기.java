import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Stack<String> stack = new Stack<>();
        StringBuilder pipe = new StringBuilder(st.nextToken());
        int piece = 0;


        for(int i=0; i< pipe.length();i++){
            //삽입
            if(String.valueOf(pipe.charAt(i)).equals("(")){
                stack.push(String.valueOf(pipe.charAt(i)));
            }
            else{
                stack.pop();
                //자르는 경우
                if(String.valueOf(pipe.charAt(i-1)).equals("(")) piece += stack.size();
                else piece++;
            }
        }
        System.out.println(piece);
    }
}
