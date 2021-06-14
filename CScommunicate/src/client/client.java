package client;

import java.awt.Color;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

import javax.swing.JOptionPane;
import javax.swing.JTextArea;

public class client {
	/*定义输入输出流*/
	BufferedReader input;
	Socket socket;
	String code;
	public static String s_code;
	int flag;
	File verify ;
	JTextArea jt;//通过JTextArea显示对话
	
	public client() {
		// TODO Auto-generated constructor stub
		/*文本区域，显示信息*/
		jt = new JTextArea();
		jt.setBounds(100,50,250,200);
		jt.setBackground(Color.lightGray);
		jt.setEditable(false);
	}

	public void creatClient() throws UnknownHostException, IOException {
		// TODO Auto-generated method stub
		//客户端创建一个socket连接服务器
	    InetAddress addr = InetAddress.getLocalHost();
		socket = new Socket(addr,9000);//客户端通过实例化获得socket对象，尝试连接指定服务器和端口
		jt.append("连接...！\n");

		input = new BufferedReader(new InputStreamReader(socket.getInputStream())); //获取输入流
		String s_code = input.readLine();
		String text = "验证码为："+ s_code +"\n";
		jt.append(text);
		
		verify = new File("src\\client\\output.txt"); 
		if(!verify.exists()) {
			verify.createNewFile();
		}
		BufferedWriter fileout = new BufferedWriter(new FileWriter(verify));
		fileout.write(s_code);//将s_code存入文件
		fileout.close();
	}
	
//	public void returncode() throws IOException {
//		output= new PrintStream(socket.getOutputStream()); //获取输出流
//		output.println(code);
//		output.close();
//	}
	
	@SuppressWarnings("resource")
	public void getflag() throws IOException{
		code = JOptionPane.showInputDialog("请输入你的验证码:");
		jt.append("您输入的验证码为："+code+"\n");
		
		try {//添加一个空指针异常检测
			if(!verify.exists()||verify.length()==0){//检测文件是否不存在或者为空
				System.out.println("1");
				jt.append("验证失败！\n");
				return;
			}
		}catch(NullPointerException e){
			jt.append("验证失败，请检查服务器连接\n");
			return;
		}
		
		InputStreamReader reader = new InputStreamReader(new FileInputStream(verify)); // 建立一个输入流对象reader  
        BufferedReader br = new BufferedReader(reader); // 建立一个对象，它把文件内容转成计算机能读懂的语言  
        s_code = br.readLine();	//读取验证码
		if(code.equals(s_code)) {
			jt.append("验证成功！\n");
		}
		else {
			jt.append("验证失败！\n");
		}
	}
}
