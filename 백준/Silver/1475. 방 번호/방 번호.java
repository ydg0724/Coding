import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] cnt = new int[10];
        String room = br.readLine();
        int result=1;

        for(int i=0;i<room.length();i++){
            int num = Character.getNumericValue(room.charAt(i));
            cnt[num]++;
        }
        int sixNine = cnt[6] + cnt[9];
        cnt[6] = sixNine/2;
        if(sixNine%2==1) cnt[6]++;
        for(int i=0;i<9;i++) {
            result = Math.max(result, cnt[i]);
        }

        System.out.println(result);
    }
}
