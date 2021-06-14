/*第一个Jpanel*/

import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

@SuppressWarnings("serial")
public class jpanel1 extends JPanel {
	/*将jpanel1单例化*/
	private static jpanel1 instance = new jpanel1(); //创建对象
	public static jpanel1 getInstance(){ 		   //获得对象
		return instance;
	}
	
	JPanel jp1;
	JPanel jp2;
	slider pen;
	slider R;
	slider B;
	slider G;
	
	private jpanel1(){
		// TODO Auto-generated constructor stub
		setLayout(null); //设置布局为空
		setBorder(BorderFactory.createTitledBorder("画笔属性"));		//设置边框
		
		/*实例化组件*/
		jp1 = new JPanel();
		jp2 = new JPanel();
		
		R = new slider("R  :");
		G = new slider("G  :");
		B = new slider("B  :");
		
		pen = new slider("Size:");
		
		/*设置组件位置*/
		jp1.setBounds(30, 30, 100, 50);
		jp2.setBounds(150, 30, 100, 50);
		R.setBounds(10, 90, 250, 30);
		G.setBounds(10, 120, 250, 30);
		B.setBounds(10, 150, 250, 30);
		pen.setBounds(10, 185, 250, 50);
		
		/*设置组件属性*/
		pen.setBorder(BorderFactory.createLoweredBevelBorder()); //设置边框
		jp1.setBorder(BorderFactory.createLoweredBevelBorder()); //设置边框
		jp2.setBorder(BorderFactory.createLoweredBevelBorder()); //设置边框
		jp1.setBackground(new Color(0,0,0));
		jp2.setBackground(new Color(0,0,0));
		
		/*添加组件*/
		add(jp1);
		add(jp2);
		add(R);
		add(G);
		add(B);
		add(pen);
		
		/*设置监听*/
		
		//滑轮改变时改变jp2的颜色
		ChangeListener listener = new ChangeListener() {
			@Override
			public void stateChanged(ChangeEvent arg0) {
				// TODO Auto-generated method stub
//				System.out.println("1");
				int r = R.getV();
				int g = G.getV();
				int b = B.getV();
				jp2.setBackground(new Color(r,g,b));
			}
		};

		/*添加对应的监听*/
		R.slider.addChangeListener(listener);
		G.slider.addChangeListener(listener);
		B.slider.addChangeListener(listener);
		
		someColors();
	}
	
	MouseAdapter mouse = new MouseAdapter() { //添加鼠标监听
		public void mouseClicked(MouseEvent e) {
			JButton btn = (JButton)e.getSource();
			if(e.getButton()==1) { //鼠标左键点击
				//更换待选区的颜色及text和slider的值
				Color newcolor = btn.getBackground();
				int r = newcolor.getRed();
				int g = newcolor.getGreen();
				int b = newcolor.getBlue();
				R.field.setText(r + "");
				G.field.setText(g + "");
				B.field.setText(b + "");
				R.slider.setValue(r);
				G.slider.setValue(g);
				B.slider.setValue(b);

				jp2.setBackground(newcolor);
			}
		}
	};
	
	
	//添加固定颜色按钮
	private void someColors() {
		// TODO Auto-generated method stub
		
		Color[] colorArray= {
				Color.white,Color.black,
				Color.DARK_GRAY,Color.cyan,
				Color.pink,Color.red,
				Color.green,Color.blue,
				Color.yellow,Color.orange
		};
		//pen.setBounds(10, 185, 250, 50);
		for(int i=0;i<colorArray.length;i++) {
			final JButton button = new JButton();
			button.setBackground(colorArray[i]);
			button.setPreferredSize(new Dimension(35,25));
			button.addMouseListener(mouse);
			button.setBounds(30+45*(i%5), 245+30*((int)i/5), 35, 25);
			this.add(button);
			}
	}
}
