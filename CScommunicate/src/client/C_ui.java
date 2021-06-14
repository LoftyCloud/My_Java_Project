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
		this.setTitle("客户端");
		
		JPanel jp = new JPanel();
		jp.setLayout(null);
		
		/*按钮*/
		confirm = new JButton("连接服务器");
		input = new JButton("输入验证码");
		cancel = new JButton("退出");
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
				c.jt.append("正在连接...\n");
				c.creatClient();
			} catch (UnknownHostException e1) {
				// TODO Auto-generated catch block
				JOptionPane.showMessageDialog(null,  "UnknownHost!", "错误", JOptionPane.ERROR_MESSAGE);
				c.jt.append("连接失败，错误原因：UnknownHost\n");
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				JOptionPane.showMessageDialog(null,  "IOException!", "错误", JOptionPane.ERROR_MESSAGE);
				c.jt.append("连接失败，错误原因：IOException\n");
			}
		}
		else if(button.equals(input)) {
			try {
				c.getflag();
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				c.jt.append("验证失败！");
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