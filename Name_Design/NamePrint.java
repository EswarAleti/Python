import java.io.*;
import java.util.concurrent.TimeUnit;
public class NamePrint
{
	public static void main(String[] args)throws IOException,InterruptedException
	{
		FileReader fr=new FileReader("name.txt");
		BufferedReader br=new BufferedReader(fr);

		String s="";
		while((s=br.readLine())!=null)
		{
			System.out.print("\t\t");
			for(int i=0;i<s.length();i++)
			{
				System.out.print(s.charAt(i));
				TimeUnit.MILLISECONDS.sleep(80);
			}
			System.out.println();
		}
	}
}