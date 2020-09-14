import java.util.Arrays;
import java.util.Comparator;
import java.io.*;

public class Main {
	
    public static void main(String[] args) throws Exception {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        String[] word = new String[N];
        for(int i=0;i<N;i++)
        	word[i] = br.readLine();
        Arrays.sort(word);
        
        Comparator<String> sortWord = new Comparator<String>() {
        	@Override
        	public int compare(String w1,String w2){
        		return w1.length() - w2.length();
        	}
        };
        Arrays.sort(word,sortWord);
        for(int i=0;i<N;i++) {
        	if(i>0&&word[i].equals(word[i-1]))
        		continue;
        	bw.write(word[i]+"\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}