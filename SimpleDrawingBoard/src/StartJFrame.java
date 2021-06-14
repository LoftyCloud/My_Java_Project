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
		//窗体
		setTitle("WELCOME!");
		setBounds(400, 250, 500, 300);
		setResizable(false); //不可调节窗口大小
		setBackground(Color.black);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		getContentPane().setLayout(null); //布局
		setVisible(true);
		
		//按钮
		button=new JButton("LOADING...");
		button.setFont(new Font("黑体",Font.PLAIN,32));//字体,样式,字号
		button.setForeground(Color.white);
		button.setContentAreaFilled(false); //透明
		button.setBorderPainted(false); //边框
		button.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR)); //添加鼠标样式
		button.setBounds(this.getWidth()/2-75, this.getHeight()/2-50, 200, 50);
		Listener listener = new Listener();
		button.addActionListener(listener);
		
		
		//背景
		String path=Randompic();
		ImageIcon image=new ImageIcon(path);
		JLabel jlabel=new JLabel(image); //将背景图放标签里
		//将背景标签添加到frame的LayeredPane面板里
		
		getLayeredPane().add(jlabel,new Integer(Integer.MIN_VALUE));
		jlabel.setBounds(0, 0, this.getWidth(), this.getHeight());
		con =this.getContentPane();
		((JPanel)con).setOpaque(false); //内容窗格转换成JPanel //内容窗格透明化
		con.add(button);
		
		time();
	}
	
	/*计时器1s*/
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
		mainJF jf= mainJF.getInstance();//创建一个mainJF实例
		jf.setVisible(true); 			//设置为可见
		dispose(); 						//关闭当前窗口
	}

	/*随机背景图片*/
	public static String Randompic() {
		Random random=new Random();
		int i=random.nextInt(6);//生成[0,6 )的随机数
		i++;
		String s="src/imgs/img"+i+".jpg";
		return s;
	}
	
	/*监听器*/
	private class Listener implements ActionListener{ //按钮添加事件
		public void actionPerformed (ActionEvent e) {
			if(e.getSource() == button) {
				mainJF jf= mainJF.getInstance();//创建一个mainJF实例
				jf.setVisible(true); 			//设置为可见
				dispose(); 						//关闭当前窗口
			}
		}
	}
}