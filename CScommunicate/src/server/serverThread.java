/*线程*/
package server;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.PrintStream;
import java.net.Socket;
import java.util.Random;

public class serverThread extends Thread {
	String code="";
	PrintStream output;
	BufferedReader input;
	Socket client;
	public serverThread(Socket client){
		this.client = client;
	}
	
	public void run() {
		// TODO Auto-generated constructor stub
				try {
					output= new PrintStream(client.getOutputStream());
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} //获取输出流
				
				/*生成验证码*/
				String all="0123456789";
				int codeLength = 6;
				Random random = new Random();
				
				for(int i=0;i<codeLength;i++) {		//随机生成一段验证码
					int num = random.nextInt(all.length());
					code = code + all.substring(num,num+1);
				}
				output.println(code);
				System.out.println("验证码已发送\n");
				
				output.close();
				try {
					client.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				return;
	}
	

}
