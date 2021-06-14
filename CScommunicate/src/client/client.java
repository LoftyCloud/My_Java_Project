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
	/*�������������*/
	BufferedReader input;
	Socket socket;
	String code;
	public static String s_code;
	int flag;
	File verify ;
	JTextArea jt;//ͨ��JTextArea��ʾ�Ի�
	
	public client() {
		// TODO Auto-generated constructor stub
		/*�ı�������ʾ��Ϣ*/
		jt = new JTextArea();
		jt.setBounds(100,50,250,200);
		jt.setBackground(Color.lightGray);
		jt.setEditable(false);
	}

	public void creatClient() throws UnknownHostException, IOException {
		// TODO Auto-generated method stub
		//�ͻ��˴���һ��socket���ӷ�����
	    InetAddress addr = InetAddress.getLocalHost();
		socket = new Socket(addr,9000);//�ͻ���ͨ��ʵ�������socket���󣬳�������ָ���������Ͷ˿�
		jt.append("����...��\n");

		input = new BufferedReader(new InputStreamReader(socket.getInputStream())); //��ȡ������
		String s_code = input.readLine();
		String text = "��֤��Ϊ��"+ s_code +"\n";
		jt.append(text);
		
		verify = new File("src\\client\\output.txt"); 
		if(!verify.exists()) {
			verify.createNewFile();
		}
		BufferedWriter fileout = new BufferedWriter(new FileWriter(verify));
		fileout.write(s_code);//��s_code�����ļ�
		fileout.close();
	}
	
//	public void returncode() throws IOException {
//		output= new PrintStream(socket.getOutputStream()); //��ȡ�����
//		output.println(code);
//		output.close();
//	}
	
	@SuppressWarnings("resource")
	public void getflag() throws IOException{
		code = JOptionPane.showInputDialog("�����������֤��:");
		jt.append("���������֤��Ϊ��"+code+"\n");
		
		try {//���һ����ָ���쳣���
			if(!verify.exists()||verify.length()==0){//����ļ��Ƿ񲻴��ڻ���Ϊ��
				System.out.println("1");
				jt.append("��֤ʧ�ܣ�\n");
				return;
			}
		}catch(NullPointerException e){
			jt.append("��֤ʧ�ܣ��������������\n");
			return;
		}
		
		InputStreamReader reader = new InputStreamReader(new FileInputStream(verify)); // ����һ������������reader  
        BufferedReader br = new BufferedReader(reader); // ����һ�����������ļ�����ת�ɼ�����ܶ���������  
        s_code = br.readLine();	//��ȡ��֤��
		if(code.equals(s_code)) {
			jt.append("��֤�ɹ���\n");
		}
		else {
			jt.append("��֤ʧ�ܣ�\n");
		}
	}
}
