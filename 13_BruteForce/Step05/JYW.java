import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int countSix = 0,count = 0;
		String number;
		int answer = 0;
		
		for(int i=666;;i++) {
			number = Integer.toString(i);
			for(int j=2;j<number.length();j++) {
					if(number.charAt(j-2)=='6'&&number.charAt(j-1)=='6'&&number.charAt(j)=='6') {
						count++;
						break;
					}		
			}
			if(count == N) {
				answer = i;
				break;
			}
				
		}
		System.out.println(answer);
		
		sc.close();
	}
}