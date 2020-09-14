import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Comparator;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws Exception {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        String[][] member = new String[N][2];
        for(int i=0;i<N;i++) {
        	st = new StringTokenizer(br.readLine());
        	member[i][0] = st.nextToken();
        	member[i][1] = st.nextToken();
        }
        
        Comparator<String[]> SortMember = new Comparator<String[]>() {
        	@Override
        	public int compare(String[] mem1,String[] mem2) {
        		return Integer.parseInt(mem1[0]) - Integer.parseInt(mem2[0]);
        	}
        };
        Arrays.sort(member,SortMember);
        for(String[] i:member)
        	bw.write(i[0]+" "+i[1]+"\n");
        
        bw.flush();
        br.close();
        bw.close();
    }
}