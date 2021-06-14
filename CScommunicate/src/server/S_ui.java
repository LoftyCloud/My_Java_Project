package server;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.IOException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class S_ui extends JFrame implements MouseListener{
	JButton create;
	JButton confirm;
	JButton cancel;
	server s;
	int port = 9000;
	
	public S_ui() {
		// TODO Auto-generated constructor stub
		this.setBounds(250,100,450,600);
		this.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
		this.setTitle("服务端");
		
		JPanel jp = new JPanel();
		jp.setLayout(null);
		
		create = new JButton("创建服务器");
		cancel = new JButton("退出");
		create.setBounds(100,275,100,50);		
		cancel.setBounds(250,275,100,50);
		create.addMouseListener(this);
		cancel.addMouseListener(this);
		
		s = new server();
		jp.add(create);
		jp.add(cancel);
		jp.add(s.jt);
		this.setContentPane(jp);
	}

	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		JButton button = (JButton) e.getSource();
		if(button.equals(create)) {
				try {
					s.setUpServer(port);
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					s.jt.append("建立失败，端口号已经被占用了");
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
		S_ui  sui =new S_ui();
		sui.setVisible(true);
	}

}
