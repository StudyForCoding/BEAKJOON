import java.util.Scanner;

public class Main {
		
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String stringI;
		
		int N = sc.nextInt();
		int n = 0, answer = 0;
		
		for(int i=1;i<N;i++) {
			n = i;
			stringI = Integer.toString(i);
			for(int j=0;j<stringI.length();j++) {
				n += stringI.charAt(j) - '0';
			}
			if(n == N) {
				answer = i;
				System.out.print(answer);
				break;
			}
		}
		if(answer == 0)
			System.out.print(answer);
		
		sc.close();
	}
}