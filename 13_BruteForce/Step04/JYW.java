import java.util.Arrays;
import java.util.Scanner;


public class Main {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		
		char[][] blackChessBoard = new char[8][8];
		char[][] whiteChessBoard = new char[8][8];
		char[][] board = new char[N][M];
		String blackRow = "BWBWBWBW", whiteRow = "WBWBWBWB";
		String temp;
		
		for(int i=0;i<8;i++) {
			for(int j=0;j<8;j++) {
				if(i%2==0) {
					blackChessBoard[i][j] = blackRow.charAt(j);
					whiteChessBoard[i][j] = whiteRow.charAt(j);
				}
				else {
					blackChessBoard[i][j] = whiteRow.charAt(j);
					whiteChessBoard[i][j] = blackRow.charAt(j);
				}
			}
		}
		
		for(int i=0;i<N;i++) {
			temp = sc.next();
			for(int j=0;j<M;j++) {
				board[i][j] = temp.charAt(j);
			}
		}
		
		int[][] blackDifferenceCount = new int[N-7][M-7];
		int[][] whiteDifferenceCount = new int[N-7][M-7];
		int[][] differenceCount = new int[N-7][M-7];
		
		for(int i=0;i<N-7;i++) {
			Arrays.fill(blackDifferenceCount[i],0);
			Arrays.fill(whiteDifferenceCount[i],0);
		}
		
		for(int i=0;i<N-8+1;i++) {
			for(int j=0;j<M-8+1;j++) {
				for(int k=0;k<8;k++) {
					for(int l=0;l<8;l++) {
						if(board[i+k][j+l]!=blackChessBoard[k][l])
							blackDifferenceCount[i][j]++;
						if(board[i+k][j+l]!=whiteChessBoard[k][l])
							whiteDifferenceCount[i][j]++;
						
					}
				}
				differenceCount[i][j] = (blackDifferenceCount[i][j]>whiteDifferenceCount[i][j])?
						whiteDifferenceCount[i][j]:blackDifferenceCount[i][j];
			}
		}
		
		int answer = differenceCount[0][0];
		for(int i=0;i<N-7;i++) {
			for(int j=0;j<M-7;j++) 
				answer=(answer>differenceCount[i][j])?
							differenceCount[i][j]:answer;
		}
		
		System.out.println(answer);
		
		sc.close();
	}
}