import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;

public class shape {  //����һ��ͼ������
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
		//���ݲ�ͬ��ͼ������ѡ��ͬ���ػ淽��
			public void repaint(Graphics g) {
				BasicStroke bs=new BasicStroke(size,BasicStroke.CAP_ROUND,BasicStroke.JOIN_BEVEL);
				Graphics2D gp2d = (Graphics2D) g;
			    gp2d.setStroke(bs);
				gp2d.setColor(color);
				
				switch(name) {
				case "ֱ��":
					gp2d.drawLine(x1, y1, x2, y2);
					break;
				case "����":
					gp2d.drawRect(x1,y1,x2,y2); //�����x1,y1,x2,y2�ֱ��Ӧx,y,width,height
					break;
				case "��Բ":
					gp2d.drawOval(x1,y1,x2,y2);
					break;
				case "Ǧ��":
					gp2d.drawLine(x1, y1, x2, y2);
					break;
				case "����":
					gp2d.drawString(s, x1, y1);
					break;
				case "Բ��":
					gp2d.drawOval(x1,y1,x2,y2);
					break;
				case "Բ�Ǿ���":
					gp2d.drawRoundRect(x1, y1, x2, y2,40,25);//��һ��Բ�Ǿ��� 
					break;
				case "������":
					gp2d.fillRect(x1, y1, x2, y2);
					break;
				case "���Բ�Ǿ���":
					gp2d.fillRoundRect(x1, y1, x2, y2,40,25);//��һ��Բ�Ǿ��� 
					break;
				case "���Բ��":
					g.fillOval(x1, y1, x2, y2);
					break;
				case "�����Բ":
					g.fillOval(x1, y1, x2, y2);
					break;
				default:
					break;
				}
			}
	}

