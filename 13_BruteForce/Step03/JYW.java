import java.util.Scanner;

class Bulk{
	int weight;
	int height;
	int count = 0;
	public Bulk() {}
	public Bulk(int weight, int height) {
		this.weight = weight;
		this.height = height;
	}
	public int getWeight() {
		return weight;
	}
	public void setWeight(int weight) {
		this.weight = weight;
	}
	public int getHeight() {
		return height;
	}
	public void setHeight(int height) {
		this.height = height;
	}
	public int getCount() {
		return count;
	}
	public void setCount(int count) {
		this.count = count;
	}
	
	
}

public class Main {
	
	
		
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Bulk[] bulk = new Bulk[N];
		
		for(int i=0;i<N;i++) {
			bulk[i] = new Bulk();
			bulk[i].setWeight(sc.nextInt());
			bulk[i].setHeight(sc.nextInt());
		}
		for(int i=0;i<N-1;i++) {
			for(int j=i+1;j<N;j++) {
				if(bulk[i].getWeight()>bulk[j].getWeight()&&
												bulk[i].getHeight()>bulk[j].getHeight())
					bulk[j].count++;
				else if(bulk[i].getWeight()<bulk[j].getWeight()&&
													bulk[i].getHeight()<bulk[j].getHeight())
					bulk[i].count++;
				else
					continue;
			}
		}
		for(int i=0;i<N;i++) 
			System.out.print(bulk[i].count+1+" ");
		
		
		sc.close();
	}
}