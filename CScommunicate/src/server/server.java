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
		/*�ı�������ʾ��Ϣ*/
		jt = new JTextArea();
		jt.setBounds(100,50,250,200);
		jt.setBackground(Color.lightGray);
		jt.setEditable(false);
		jt.setText("��ӭ��\n");
	}
	
	
	/*����һ��������*/
	public void setUpServer(int port) throws IOException {
		jt.append("������������...\n");
		server = new ServerSocket(port);//����һ��������
		
		while(true) {					//���пͻ�������ʱ������һ���߳���Ӧ������
			socket = server.accept();	//����һ���н���ն���socket
			jt.append("�ͻ���������\n");
			//��Ҫ��һ����ʱ����5����û�������Զ��رշ�����
			serverThread thread = new serverThread(socket);//������ͨ��accept�������һ��socket����
			thread.start();
		}
		
	}

}