import java.util.Arrays;
import java.util.Collections;
import java.io.*;

public class Main {
 
    public static void main(String[] args) throws Exception {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String N = br.readLine();
        Integer[] sortedN = new Integer[N.length()];
        for(int i=0;i<N.length();i++)
        	sortedN[i] = (int) N.charAt(i);
        Arrays.sort(sortedN,Collections.reverseOrder());
        for(int i:sortedN)
        	bw.write(i);
        bw.flush();
        br.close();
        bw.close();
    }
}