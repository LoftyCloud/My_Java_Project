package client;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.IOException;
import java.net.UnknownHostException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class C_ui extends JFrame implements MouseListener{
	JButton confirm;
	JButton input;
	JButton cancel;
	String code;
	public static String s_code;
	client c;
	
	public C_ui() {
		// TODO Auto-generated constructor stub
		this.setBounds(700,100,450,600);
		this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		this.setTitle("�ͻ���");
		
		JPanel jp = new JPanel();
		jp.setLayout(null);
		
		/*��ť*/
		confirm = new JButton("���ӷ�����");
		input = new JButton("������֤��");
		cancel = new JButton("�˳�");
		confirm.setBounds(100,275,100,50);		
		input.setBounds(250,275,100,50);
		cancel.setBounds(100,350,100,50);
		confirm.addMouseListener(this);
		input.addMouseListener(this);
		cancel.addMouseListener(this);
		
	
		c  = new client();
		jp.add(c.jt);
		jp.add(confirm);
		jp.add(input);
		jp.add(cancel);
		this.setContentPane(jp);
	}

	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		JButton button = (JButton) e.getSource();
		if(button.equals(confirm)) {
			try {
				c.jt.append("��������...\n");
				c.creatClient();
			} catch (UnknownHostException e1) {
				// TODO Auto-generated catch block
				JOptionPane.showMessageDialog(null,  "UnknownHost!", "����", JOptionPane.ERROR_MESSAGE);
				c.jt.append("����ʧ�ܣ�����ԭ��UnknownHost\n");
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				JOptionPane.showMessageDialog(null,  "IOException!", "����", JOptionPane.ERROR_MESSAGE);
				c.jt.append("����ʧ�ܣ�����ԭ��IOException\n");
			}
		}
		else if(button.equals(input)) {
			try {
				c.getflag();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				c.jt.append("��֤ʧ�ܣ�");
			}
		}
		else
			System.exit(0);
	}

	@Override
	public void mouseEntered(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mousePressed(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseReleased(MouseEvent arg0) {
		// TODO Auto-generated method stub
		
	}
	
	public static void main(String[] args) {
		C_ui  cui =new C_ui();
		cui.setVisible(true);
	}
}