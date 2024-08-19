import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        StringBuffer editor = new StringBuffer(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        int cursor = editor.length();

        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            String order = st.nextToken();
            if(order.equals("L")){
                if(cursor>0) cursor--;
            } else if (order.equals("D")) {
                if(cursor<editor.length()) cursor++;
            } else if (order.equals("B")) {
                if(cursor>0) editor.deleteCharAt(--cursor);
            } else if (order.equals("P")) {
                String Char = st.nextToken();
                editor.insert(cursor++,Char);
            }
        }
        System.out.println(editor);
    }
}
