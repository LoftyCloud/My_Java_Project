package server;
import java.awt.Color;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

import javax.swing.JTextArea;

public class server {
	ServerSocket server;
	Socket socket;
	String code ="";
	String c_code;
	JTextArea jt;
	int flag;
	
	public server() {
		// TODO Auto-generated constructor stub
		/*文本区域，显示信息*/
		jt = new JTextArea();
		jt.setBounds(100,50,250,200);
		jt.setBackground(Color.lightGray);
		jt.setEditable(false);
		jt.setText("欢迎！\n");
	}
	
	
	/*建立一个服务器*/
	public void setUpServer(int port) throws IOException {
		jt.append("服务器建立中...\n");
		server = new ServerSocket(port);//建立一个服务器
		
		while(true) {					//当有客户机连接时，创建一个线程响应该连接
			socket = server.accept();	//定义一个中介接收对象socket
			jt.append("客户机已连接\n");
			//需要加一个定时器，5秒钟没人连接自动关闭服务器
			serverThread thread = new serverThread(socket);//服务器通过accept方法获得一个socket对象
			thread.start();
		}
		
	}

}