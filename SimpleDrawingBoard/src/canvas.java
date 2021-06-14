/*���廭��*/

import java.awt.BasicStroke;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Cursor;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Point;
import java.awt.Toolkit;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;

import javax.swing.ImageIcon;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;



@SuppressWarnings("serial")
public class canvas extends Canvas implements MouseMotionListener,MouseListener{
	/*��canvas������*/
	private static canvas instance = new canvas(); //��������
	public static canvas getInstance(){ 		   //��ö���
		return instance;
	}

	jpanel1 jp1 = jpanel1.getInstance();//��ȡjpanel1ʵ��
	JTextArea jt = new JTextArea("Ǧ��");
	
	int x1,x2,y1,y2;
	int x3,x4,y3,y4;//���ò���
	shape[] sharr = new shape[6750000];	//���������������ߵ�����
	shape[] sharr2 = new shape[10000];	//����ͼ��
	public static int index = 0;		//��¼���鳤��
	public static int index2 = 0;
	String button ;
	Graphics2D g ;						//���廭�ʣ������޷���ȡ
	/*��JFrameû��show֮ǰ,����JFrame�ϵ�������޷��õ�Graphics,��ʱGraphics��������,�õ����ǿ�ָ��*/
	
	private canvas() {
		// TODO Auto-generated constructor stub
		setBackground(Color.white);		//���û���������ɫ
		this.setVisible(true);
		
		
		/*ע��������*/
		addMouseMotionListener(this);	
		addMouseListener(this);	
	}
	
	
	@Override//�����ק
	public void mouseDragged(MouseEvent e) {
		// TODO Auto-generated method stub
		/*��ȡ����*/
		g = (Graphics2D)this.getGraphics();
		
		//���û�����ɫ������
		BasicStroke bs=new BasicStroke(jp1.pen.getV(),BasicStroke.CAP_ROUND,BasicStroke.JOIN_BEVEL);
		g.setColor(jp1.jp2.getBackground());
		g.setStroke(bs);
		
		button = jt.getText();
		switch(button) {	//����button��ֵѡ��ͬ�Ĺ���
		case "��Ƥ":
			g.setColor(getBackground());
			break;
		case "Ǧ��":
			break;
		default:
			return;
		}
		
		//����
		x2 = e.getX()-20;//���ǵ��¹���Ӿ��ϵ�ƫ�ƣ��Ի�ȡ����x��y���б任
		y2 = e.getY()-10;
		g.drawLine(x1,y1,x2,y2);
		sharr[index++] = new shape(x1,y1,x2,y2,button,g.getColor(),jp1.pen.getV(),null);
		x1 = x2;
		y1 = y2;
	}

	@Override//����ƶ�
	public void mouseMoved(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override//�����
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override//�����룬�����¹�꣬��������ɫ
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		jp1.jp1.setBackground(jp1.jp2.getBackground());
		
		String url = "src/imgs/pen.png";					//�¹���λ��
		Toolkit tk = Toolkit.getDefaultToolkit();  
		Image image = new ImageIcon(url).getImage();  
		Cursor cursor = tk.createCustomCursor(image, new Point(30, 30), "norm"); 
		setCursor(cursor); 
	}

	@Override//����˳�
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@SuppressWarnings("null")
	@Override//��갴ѹ
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		x1 = e.getX()-20;
		y1 = e.getY()-10;
		x3 = e.getX()-20;
		y3 = e.getY()-10;
		
		g = (Graphics2D)this.getGraphics();		//���»�ȡ����
		BasicStroke bs=new BasicStroke(jp1.pen.getV(),BasicStroke.CAP_ROUND,BasicStroke.JOIN_BEVEL);
		g.setColor(jp1.jp2.getBackground());
		g.setStroke(bs);
		
		button = jt.getText();	//��ȡ��ť����Ϣ
		if (button.equals("����")) {
			jt.setText("Ǧ��");
			String str = (String) JOptionPane.showInputDialog(null, "�����룺\n", "��������", JOptionPane.PLAIN_MESSAGE, null, null,
	                null);
			if(str!=null||!str.isEmpty()) {
				g.drawString(str, x1, y1);
				sharr2[index2++] = new shape(x1,y1,x2,y2,button,g.getColor(),jp1.pen.getV(),str);
			}
		}
	}

	@Override//����ɿ�
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		button = jt.getText();
		x4 = e.getX()-20;
		y4 = e.getY()-10;
		
		//ͼ�ε�x,y,width,height
		int x = Math.min(x3, x4);
		int y = Math.min(y3, y4);
		int w = Math.abs(x3-x4);
		int h = Math.abs(y3-y4);//Math.abs():ȡ����ֵ
		
		switch(button) {
		case "ֱ��":
			/*����+��¼*/
			g.drawLine(x3,y3,x4,y4);
			sharr2[index2++] = new shape(x3,y3,x4,y4,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "����":
			g.drawRect(x,y,w,h);
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "��Բ":
			g.drawOval(x,y,w,h);
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "Բ��":
			g.drawOval(x,y,w,w);
			sharr2[index2++] = new shape(x,y,w,w,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "Բ�Ǿ���":
			g.drawRoundRect(x, y, w, h,40,25);//��һ��Բ�Ǿ��� 
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "������":
			g.fillRect(x,y,w,h);
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "���Բ��":
			g.fillOval(x, y, w, w);
			sharr2[index2++] = new shape(x,y,w,w,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "�����Բ":
			g.fillOval(x, y, w, h);
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "���Բ�Ǿ���":
			g.fillRoundRect(x, y, w, h,40,25);//Ϳһ��Բ�Ǿ��ο� 
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		default:
			break;
		}
		
		x3 = e.getX()-20;
		y3 = e.getY()-10;
	}
	
	/*��дpaint����*/
	public void paint(Graphics g){  //paint����ֻ����д���������
		super.paint(g);  //���ø����paint������������
		
		//��������
		BasicStroke bs = new BasicStroke(jp1.pen.getV(),BasicStroke.CAP_ROUND,BasicStroke.JOIN_BEVEL);
		Graphics2D gp2d = (Graphics2D) g;
        gp2d.setStroke(bs);
        gp2d.setColor(jp1.jp2.getBackground());
        
        for(int i=0;i<index;i++) {
        	if(sharr[i]!=null) { //��д�滭ͼ��
        		sharr[i].repaint(g);
        	}
        	else {
        		break;
        	}
        }
        for(int j=0;j<index2;j++) {
        	if(sharr2[j]!=null) { //��д�滭ͼ��
        		sharr2[j].repaint(g);
        	}
        	else {
        		break;
        	}
        }
	}
}