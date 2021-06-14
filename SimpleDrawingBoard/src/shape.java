import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;

public class shape {  //定义一个图案的类
		private int x1,x2,y1,y2;
		private String name;
		private Color color;
		private int size;
		private String s;
		public shape(int x1,int y1,int x2,int y2,String name, Color color,int size,String s){
			this.x1 = x1;
			this.x2 = x2;
			this.y1 = y1;
			this.y2 = y2;
			this.name = name;
			this.color = color;
			this.size = size;
			this.s = s;
		}		
		//根据不同的图案名字选择不同的重绘方法
			public void repaint(Graphics g) {
				BasicStroke bs=new BasicStroke(size,BasicStroke.CAP_ROUND,BasicStroke.JOIN_BEVEL);
				Graphics2D gp2d = (Graphics2D) g;
			    gp2d.setStroke(bs);
				gp2d.setColor(color);
				
				switch(name) {
				case "直线":
					gp2d.drawLine(x1, y1, x2, y2);
					break;
				case "矩形":
					gp2d.drawRect(x1,y1,x2,y2); //这里的x1,y1,x2,y2分别对应x,y,width,height
					break;
				case "椭圆":
					gp2d.drawOval(x1,y1,x2,y2);
					break;
				case "铅笔":
					gp2d.drawLine(x1, y1, x2, y2);
					break;
				case "文字":
					gp2d.drawString(s, x1, y1);
					break;
				case "圆形":
					gp2d.drawOval(x1,y1,x2,y2);
					break;
				case "圆角矩形":
					gp2d.drawRoundRect(x1, y1, x2, y2,40,25);//画一个圆角矩形 
					break;
				case "填充矩形":
					gp2d.fillRect(x1, y1, x2, y2);
					break;
				case "填充圆角矩形":
					gp2d.fillRoundRect(x1, y1, x2, y2,40,25);//画一个圆角矩形 
					break;
				case "填充圆形":
					g.fillOval(x1, y1, x2, y2);
					break;
				case "填充椭圆":
					g.fillOval(x1, y1, x2, y2);
					break;
				default:
					break;
				}
			}
	}

