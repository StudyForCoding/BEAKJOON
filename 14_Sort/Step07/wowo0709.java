import java.util.StringTokenizer;
import java.util.Arrays;
import java.io.*;

class Coordinate implements Comparable<Coordinate>{
	int x;
	int y;
	
	@Override
	public int compareTo(Coordinate coor) {
		if(this.y<coor.y)
			return -1;
		else if(this.y == coor.y) {
			if(this.x<coor.x)
				return -1;
			else
				return 1;
		}
		else
			return 1;
	}
}

public class Main {
	
    public static void main(String[] args) throws Exception {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        Coordinate[] coor = new Coordinate[N];
        for(int i=0;i<N;i++) {
        	st = new StringTokenizer(br.readLine());
        	coor[i] = new Coordinate();
        	coor[i].x = Integer.parseInt(st.nextToken());
        	coor[i].y = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(coor);
        for(Coordinate i:coor)
        	bw.write(i.x+" "+i.y+"\n");
        
        bw.flush();
        br.close();
        bw.close();
    }
}