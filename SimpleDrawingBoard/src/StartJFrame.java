import java.awt.Color;
import java.awt.Container;
import java.awt.Cursor;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class StartJFrame extends JFrame{
	JButton button;
	Container con;

	public  StartJFrame() {
		//����
		setTitle("WELCOME!");
		setBounds(400, 250, 500, 300);
		setResizable(false); //���ɵ��ڴ��ڴ�С
		setBackground(Color.black);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		getContentPane().setLayout(null); //����
		setVisible(true);
		
		//��ť
		button=new JButton("LOADING...");
		button.setFont(new Font("����",Font.PLAIN,32));//����,��ʽ,�ֺ�
		button.setForeground(Color.white);
		button.setContentAreaFilled(false); //͸��
		button.setBorderPainted(false); //�߿�
		button.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR)); //��������ʽ
		button.setBounds(this.getWidth()/2-75, this.getHeight()/2-50, 200, 50);
		Listener listener = new Listener();
		button.addActionListener(listener);
		
		
		//����
		String path=Randompic();
		ImageIcon image=new ImageIcon(path);
		JLabel jlabel=new JLabel(image); //������ͼ�ű�ǩ��
		//��������ǩ��ӵ�frame��LayeredPane�����
		
		getLayeredPane().add(jlabel,new Integer(Integer.MIN_VALUE));
		jlabel.setBounds(0, 0, this.getWidth(), this.getHeight());
		con =this.getContentPane();
		((JPanel)con).setOpaque(false); //���ݴ���ת����JPanel //���ݴ���͸����
		con.add(button);
		
		time();
	}
	
	/*��ʱ��1s*/
	private void time() {
		// TODO Auto-generated method stub
		int time = 2;
		while(time>0) {
			time--;
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		mainJF jf= mainJF.getInstance();//����һ��mainJFʵ��
		jf.setVisible(true); 			//����Ϊ�ɼ�
		dispose(); 						//�رյ�ǰ����
	}

	/*�������ͼƬ*/
	public static String Randompic() {
		Random random=new Random();
		int i=random.nextInt(6);//����[0,6 )�������
		i++;
		String s="src/imgs/img"+i+".jpg";
		return s;
	}
	
	/*������*/
	private class Listener implements ActionListener{ //��ť����¼�
		public void actionPerformed (ActionEvent e) {
			if(e.getSource() == button) {
				mainJF jf= mainJF.getInstance();//����һ��mainJFʵ��
				jf.setVisible(true); 			//����Ϊ�ɼ�
				dispose(); 						//�رյ�ǰ����
			}
		}
	}
}