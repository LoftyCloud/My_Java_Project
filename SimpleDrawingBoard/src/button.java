/*按钮类*/
import java.awt.AWTException;
import java.awt.Color;
import java.awt.Cursor;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JButton;
import javax.swing.JOptionPane;

@SuppressWarnings("serial")
public class button extends JButton implements MouseListener{
	canvas can = canvas.getInstance();
	String jb  = "铅笔";
	Graphics pen;
	
	public button(String s) {
		// TODO Auto-generated constructor stub
		setText(s);
		setSize(100,60);
		setBackground(Color.lightGray);
        setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR)); //添加鼠标样式
		
		addMouseListener(this);//注册监听
		
	}
	
	/*监听方法*/
	@Override
	public void mouseClicked(MouseEvent arg0) {
		// TODO Auto-generated method stub
		jb = this.getText();
		can.jt.setText(jb);
		pen = (Graphics2D)can.getGraphics();
		switch(jb) {
		case "图形撤回":
			canvas.index2 = canvas.index2 - 1;
			can.paint(pen);
			can.jt.setText("铅笔");
			break;
		case "清空画布":
			can.setBackground(can.getBackground());
			canvas.index = 0;
			canvas.index2 = 0;
			can.paint(pen);
			can.jt.setText("铅笔");
			break;
		case "保存图像":
			can.jt.setText("铅笔");
			try {
				BufferedImage myImage = null;
				mainJF jf = mainJF.getInstance();
				//保存区域的位置和大小
				//窗体的x，y偏移一点 + 画布的长和宽
				int x = jf.getX()+5;	
				int y = jf.getY()+27+55;	
				int w = can.getWidth();
				int h = can.getHeight();
				myImage = new Robot().createScreenCapture(new Rectangle(x,y,w,h));//抓屏保存MyCanvas上的内容
				String path = (String) JOptionPane.showInputDialog(null, "保存到：\n", "输入图片地址",
					       JOptionPane.PLAIN_MESSAGE, null, null,"D:\\img1.png");
					       //例如D:\\img1.jpg
				
					if(path==null||path.isEmpty()) {
						JOptionPane.showMessageDialog(null, "用户取消或输入路径为空！", "提示", JOptionPane.INFORMATION_MESSAGE);
						return;
					}
					
					else{
						
						File file=new File(path);
						if( !file.exists()){
							   try {
									file.createNewFile();
								} catch (IOException e) {
									// TODO Auto-generated catch block
									JOptionPane.showMessageDialog(null, "系统找不到指定的路径", "提示", JOptionPane.INFORMATION_MESSAGE);
									break;
								}
						 }
						 try {
							 ImageIO.write(myImage, "png",file);//将图片image写入file中
						 } catch (IOException e) {
							 // TODO Auto-generated catch block
							 JOptionPane.showMessageDialog(null, "保存失败！");
						 }
						 JOptionPane.showMessageDialog(null, "保存成功！");
					}
				}
			catch (AWTException e1) {
				System.err.println("Internal Error: " + e1); 
				e1.printStackTrace();
				}
			break;
			
		case "退出":
			can.jt.setText("铅笔");
			int n = JOptionPane.showConfirmDialog(null, "确认退出？", "退出",JOptionPane.YES_NO_OPTION);
			if(n==0)	//n==0为是，n==1为否
			System.exit(0);
			break;
		default:	
			break;
		}
	}

	@Override//鼠标进入
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

}
