import java.util.Arrays;
import java.io.*;

public class Main {
 
    public static void main(String[] args) throws Exception {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine()), sum = 0;
        int[] number = new int[N];
        int[] unsignedNum = new int[4001]; int[] signedNum = new int[4001];
        int max = 0;
        
        Arrays.fill(unsignedNum, 0); Arrays.fill(signedNum, 0);
        
        for(int i=0;i<N;i++) {
        	number[i] = Integer.parseInt(br.readLine());
        	sum += number[i];
        	if(number[i]>=0) {
        		unsignedNum[number[i]]++;
        		max = (max>unsignedNum[number[i]])?max:unsignedNum[number[i]];
        	}
        	else {
        		signedNum[-number[i]]++;
        		max = (max>signedNum[-number[i]])?max:signedNum[-number[i]];
        	}
        }
        Arrays.sort(number);
        
        int count = 0, mode = 0;
        for(int i=0;i<8001;i++) {
        	if(i<4000) {
        		if(signedNum[4000-i] == max) {
        			mode = i - 4000;
        			count++;
        		}
        	}
        	else {
        		if(unsignedNum[i-4000] == max) {
        			mode = i - 4000;
        			count++;
        		}
        	}
        	if(count == 2)
        		break;
        }
        int mean = 0;
        if((float)sum/N>=0)
        	mean = (int)Math.round((float)sum/N);
        else
        	mean = -(int)Math.round(Math.abs((float)sum/N));

        bw.write(mean+"\n");
        bw.write(number[(N-1)/2]+"\n");
        bw.write(mode+"\n");
        bw.write(number[N-1]-number[0]+"");
     
        br.close();
        bw.close();
    }
}