import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int max = 1;
        char[][] candy = new char[n][n];
        for(int i=0; i<n;i++){
            String colors = br.readLine();
            for(int j=0;j<n;j++){
                candy[i][j] = colors.charAt(j);
            }
        }

        //행 순회
        for(int i=0;i<n;i++){
            for(int j=0;j<n-1;j++){
                swap(i,j,i,j+1,candy);
                int maxCheck = checkMax(candy);
                if(maxCheck>max) max = maxCheck;
                swap(i,j+1,i,j,candy);
            }
        }
        //열 순회
        for(int i=0;i<n;i++){
            for(int j=0;j<n-1;j++){
                swap(j,i,j+1,i,candy);
                int maxCheck = checkMax(candy);
                if(maxCheck>max) max = maxCheck;
                swap(j+1,i,j,i,candy);
            }
        }
        System.out.println(max);
    }

    public static void swap(int i, int j, int i1, int j1, char[][] arr){
        char tmp= arr[i][j];
        arr[i][j] = arr[i1][j1];
        arr[i1][j1] = tmp;
    }

    public static int checkMax(char[][] arr){
        int max = 1;
        //행 방향으로 탐색
        for(int i=0;i<arr.length;i++){
            int cnt=1;
            for(int j=0;j<arr.length-1;j++){
                if(arr[i][j] == arr[i][j+1]){
                    cnt++;
                    max = Math.max(max,cnt);
                }
                else cnt = 1;
            }
        }
        //열 방향으로 탐색
        for(int i=0;i<arr.length;i++){
            int cnt=1;
            for(int j=0;j<arr.length-1;j++){
                if(arr[j][i] == arr[j+1][i]){
                    cnt++;
                    max = Math.max(max,cnt);
                }
                else cnt = 1;
            }
        }

        return max;
    }
}
