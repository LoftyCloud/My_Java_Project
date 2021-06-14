/*定义画布*/

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
	/*将canvas单例化*/
	private static canvas instance = new canvas(); //创建对象
	public static canvas getInstance(){ 		   //获得对象
		return instance;
	}

	jpanel1 jp1 = jpanel1.getInstance();//获取jpanel1实例
	JTextArea jt = new JTextArea("铅笔");
	
	int x1,x2,y1,y2;
	int x3,x4,y3,y4;//设置参数
	shape[] sharr = new shape[6750000];	//设置用来保存曲线的数组
	shape[] sharr2 = new shape[10000];	//保存图案
	public static int index = 0;		//记录数组长度
	public static int index2 = 0;
	String button ;
	Graphics2D g ;						//定义画笔，但是无法获取
	/*在JFrame没有show之前,所有JFrame上的组件都无法得到Graphics,此时Graphics还不存在,得到的是空指针*/
	
	private canvas() {
		// TODO Auto-generated constructor stub
		setBackground(Color.white);		//设置画布背景颜色
		this.setVisible(true);
		
		
		/*注册鼠标监听*/
		addMouseMotionListener(this);	
		addMouseListener(this);	
	}
	
	
	@Override//鼠标拖拽
	public void mouseDragged(MouseEvent e) {
		// TODO Auto-generated method stub
		/*获取画笔*/
		g = (Graphics2D)this.getGraphics();
		
		//设置画笔颜色、属性
		BasicStroke bs=new BasicStroke(jp1.pen.getV(),BasicStroke.CAP_ROUND,BasicStroke.JOIN_BEVEL);
		g.setColor(jp1.jp2.getBackground());
		g.setStroke(bs);
		
		button = jt.getText();
		switch(button) {	//根据button的值选择不同的功能
		case "橡皮":
			g.setColor(getBackground());
			break;
		case "铅笔":
			break;
		default:
			return;
		}
		
		//画线
		x2 = e.getX()-20;//考虑到新光标视觉上的偏移，对获取到的x、y进行变换
		y2 = e.getY()-10;
		g.drawLine(x1,y1,x2,y2);
		sharr[index++] = new shape(x1,y1,x2,y2,button,g.getColor(),jp1.pen.getV(),null);
		x1 = x2;
		y1 = y2;
	}

	@Override//鼠标移动
	public void mouseMoved(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override//鼠标点击
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override//鼠标进入，更改新光标，并设置颜色
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		jp1.jp1.setBackground(jp1.jp2.getBackground());
		
		String url = "src/imgs/pen.png";					//新光标的位置
		Toolkit tk = Toolkit.getDefaultToolkit();  
		Image image = new ImageIcon(url).getImage();  
		Cursor cursor = tk.createCustomCursor(image, new Point(30, 30), "norm"); 
		setCursor(cursor); 
	}

	@Override//鼠标退出
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@SuppressWarnings("null")
	@Override//鼠标按压
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		x1 = e.getX()-20;
		y1 = e.getY()-10;
		x3 = e.getX()-20;
		y3 = e.getY()-10;
		
		g = (Graphics2D)this.getGraphics();		//重新获取画笔
		BasicStroke bs=new BasicStroke(jp1.pen.getV(),BasicStroke.CAP_ROUND,BasicStroke.JOIN_BEVEL);
		g.setColor(jp1.jp2.getBackground());
		g.setStroke(bs);
		
		button = jt.getText();	//获取按钮的信息
		if (button.equals("文字")) {
			jt.setText("铅笔");
			String str = (String) JOptionPane.showInputDialog(null, "请输入：\n", "输入文字", JOptionPane.PLAIN_MESSAGE, null, null,
	                null);
			if(str!=null||!str.isEmpty()) {
				g.drawString(str, x1, y1);
				sharr2[index2++] = new shape(x1,y1,x2,y2,button,g.getColor(),jp1.pen.getV(),str);
			}
		}
	}

	@Override//鼠标松开
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		button = jt.getText();
		x4 = e.getX()-20;
		y4 = e.getY()-10;
		
		//图形的x,y,width,height
		int x = Math.min(x3, x4);
		int y = Math.min(y3, y4);
		int w = Math.abs(x3-x4);
		int h = Math.abs(y3-y4);//Math.abs():取绝对值
		
		switch(button) {
		case "直线":
			/*画线+记录*/
			g.drawLine(x3,y3,x4,y4);
			sharr2[index2++] = new shape(x3,y3,x4,y4,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "矩形":
			g.drawRect(x,y,w,h);
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "椭圆":
			g.drawOval(x,y,w,h);
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "圆形":
			g.drawOval(x,y,w,w);
			sharr2[index2++] = new shape(x,y,w,w,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "圆角矩形":
			g.drawRoundRect(x, y, w, h,40,25);//画一个圆角矩形 
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "填充矩形":
			g.fillRect(x,y,w,h);
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "填充圆形":
			g.fillOval(x, y, w, w);
			sharr2[index2++] = new shape(x,y,w,w,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "填充椭圆":
			g.fillOval(x, y, w, h);
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		case "填充圆角矩形":
			g.fillRoundRect(x, y, w, h,40,25);//涂一个圆角矩形块 
			sharr2[index2++] = new shape(x,y,w,h,button,g.getColor(),jp1.pen.getV(),null);
			break;
		default:
			break;
		}
		
		x3 = e.getX()-20;
		y3 = e.getY()-10;
	}
	
	/*重写paint方法*/
	public void paint(Graphics g){  //paint方法只需重写，不需调用
		super.paint(g);  //调用父类的paint方法画出窗体
		
		//画笔属性
		BasicStroke bs = new BasicStroke(jp1.pen.getV(),BasicStroke.CAP_ROUND,BasicStroke.JOIN_BEVEL);
		Graphics2D gp2d = (Graphics2D) g;
        gp2d.setStroke(bs);
        gp2d.setColor(jp1.jp2.getBackground());
        
        for(int i=0;i<index;i++) {
        	if(sharr[i]!=null) { //重写绘画图像
        		sharr[i].repaint(g);
        	}
        	else {
        		break;
        	}
        }
        for(int j=0;j<index2;j++) {
        	if(sharr2[j]!=null) { //重写绘画图像
        		sharr2[j].repaint(g);
        	}
        	else {
        		break;
        	}
        }
	}
}