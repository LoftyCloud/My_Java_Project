/*��ť��*/
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
	String jb  = "Ǧ��";
	Graphics pen;
	
	public button(String s) {
		// TODO Auto-generated constructor stub
		setText(s);
		setSize(100,60);
		setBackground(Color.lightGray);
        setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR)); //��������ʽ
		
		addMouseListener(this);//ע�����
		
	}
	
	/*��������*/
	@Override
	public void mouseClicked(MouseEvent arg0) {
		// TODO Auto-generated method stub
		jb = this.getText();
		can.jt.setText(jb);
		pen = (Graphics2D)can.getGraphics();
		switch(jb) {
		case "ͼ�γ���":
			canvas.index2 = canvas.index2 - 1;
			can.paint(pen);
			can.jt.setText("Ǧ��");
			break;
		case "��ջ���":
			can.setBackground(can.getBackground());
			canvas.index = 0;
			canvas.index2 = 0;
			can.paint(pen);
			can.jt.setText("Ǧ��");
			break;
		case "����ͼ��":
			can.jt.setText("Ǧ��");
			try {
				BufferedImage myImage = null;
				mainJF jf = mainJF.getInstance();
				//���������λ�úʹ�С
				//�����x��yƫ��һ�� + �����ĳ��Ϳ�
				int x = jf.getX()+5;	
				int y = jf.getY()+27+55;	
				int w = can.getWidth();
				int h = can.getHeight();
				myImage = new Robot().createScreenCapture(new Rectangle(x,y,w,h));//ץ������MyCanvas�ϵ�����
				String path = (String) JOptionPane.showInputDialog(null, "���浽��\n", "����ͼƬ��ַ",
					       JOptionPane.PLAIN_MESSAGE, null, null,"D:\\img1.png");
					       //����D:\\img1.jpg
				
					if(path==null||path.isEmpty()) {
						JOptionPane.showMessageDialog(null, "�û�ȡ��������·��Ϊ�գ�", "��ʾ", JOptionPane.INFORMATION_MESSAGE);
						return;
					}
					
					else{
						
						File file=new File(path);
						if( !file.exists()){
							   try {
									file.createNewFile();
								} catch (IOException e) {
									// TODO Auto-generated catch block
									JOptionPane.showMessageDialog(null, "ϵͳ�Ҳ���ָ����·��", "��ʾ", JOptionPane.INFORMATION_MESSAGE);
									break;
								}
						 }
						 try {
							 ImageIO.write(myImage, "png",file);//��ͼƬimageд��file��
						 } catch (IOException e) {
							 // TODO Auto-generated catch block
							 JOptionPane.showMessageDialog(null, "����ʧ�ܣ�");
						 }
						 JOptionPane.showMessageDialog(null, "����ɹ���");
					}
				}
			catch (AWTException e1) {
				System.err.println("Internal Error: " + e1); 
				e1.printStackTrace();
				}
			break;
			
		case "�˳�":
			can.jt.setText("Ǧ��");
			int n = JOptionPane.showConfirmDialog(null, "ȷ���˳���", "�˳�",JOptionPane.YES_NO_OPTION);
			if(n==0)	//n==0Ϊ�ǣ�n==1Ϊ��
			System.exit(0);
			break;
		default:	
			break;
		}
	}

	@Override//������
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
