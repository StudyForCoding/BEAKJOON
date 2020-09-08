import java.util.Scanner;

public class Main {
		
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N,M;
		N = sc.nextInt();
		M = sc.nextInt();
		int[] card = new int[N];
		int temp = 0,answer = 0;
		
		for(int i=0;i<N;i++)
			card[i] = sc.nextInt();
		
		for(int i = 0;i < N-2;i++) {
			for(int j=i+1;j<N-1;j++) {
				for(int k=j+1;k<N;k++) {
					temp = card[i]+card[j]+card[k];
					if(temp>M)
						continue;
					else
						answer=(answer>=temp)?answer:temp;
				}
			}
		}
		
		System.out.print(answer);
		
		sc.close();
	}
}