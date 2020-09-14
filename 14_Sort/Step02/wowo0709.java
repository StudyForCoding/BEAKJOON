import java.util.ArrayList;
import java.util.Collections;
import java.io.*;

import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) throws IOException
	{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		ArrayList<Integer> numbers = new ArrayList<Integer>();
		
		for(int i=0;i<N;i++) {
			numbers.add(Integer.parseInt(br.readLine()));
		}
		Collections.sort(numbers);
		for(int i:numbers) {
			bw.write(i+"\n");
		}
        bw.flush();
	}
}