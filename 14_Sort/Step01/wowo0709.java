import java.util.Arrays;
import java.io.*;

import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) throws IOException
	{
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = sc.nextInt();
		int[] numbers = new int[N];
		
		for(int i=0;i<N;i++) {
			numbers[i] = sc.nextInt();
			//numbers[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(numbers);
		for(int i=0;i<N;i++) {
			System.out.println(numbers[i]);
			//bw.write(String.valueOf(numbers[i])+"\n");
		}
		bw.flush();
		br.close();
		bw.close();
		sc.close();
	}
}