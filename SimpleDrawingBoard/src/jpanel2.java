/*第二个jpanel*/


import java.awt.Color;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.BorderFactory;
import javax.swing.JComboBox;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class jpanel2 extends JPanel{
	/*将jpanel2单例化*/
	canvas can = canvas.getInstance();
	private static jpanel2 instance = new jpanel2(); //创建对象
	public static jpanel2 getInstance(){ 		   //获得对象
		return instance;
	}

	private jpanel2() {							//构造函数私有化，防止其他类创建新的实例
		// TODO Auto-generated constructor stub
		setBorder(BorderFactory.createTitledBorder("图形工具"));		//设置边框
		setLayout(null);
	    // 需要选择的条目
	    String[] r = new String[]{"矩形", "圆角矩形", "填充矩形", "填充圆角矩形"};
	 
	    // 创建一个下拉列表框
	    final JComboBox<String> rect = new JComboBox<String>(r);    // 需要选择的条目
	   
	    String[] o = new String[]{"圆形", "椭圆", "填充圆形", "填充椭圆"};
	    final JComboBox<String> ovel = new JComboBox<String>(o);
	    rect.setToolTipText("选择矩形");//设置提示信息
	    ovel.setToolTipText("选择圆形");
	    rect.setBackground(Color.LIGHT_GRAY);
	    ovel.setBackground(Color.LIGHT_GRAY);
	    rect.setSelectedIndex(-1);//设置默认选中的值 
	    ovel.setSelectedIndex(-1);
	    rect.setBounds(50,25, 200,40);
	    ovel.setBounds(50,75,200,40);
	    add(rect);
	    add(ovel);
	    
	    ovel.addItemListener( new ItemListener() {
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
		        if (e.getStateChange() == ItemEvent.SELECTED) {
					can.jt.setText((String) ovel.getSelectedItem());
					rect.setSelectedIndex(-1);
					}
			}
	    }
	    );
	    rect.addItemListener( new ItemListener() {
			@Override
			public void itemStateChanged(ItemEvent e) {
				// TODO Auto-generated method stub
		        if (e.getStateChange() == ItemEvent.SELECTED) {
					can.jt.setText((String) rect.getSelectedItem());
					ovel.setSelectedIndex(-1);
		        }
			}
	    }
	    );
	    
		/*实例化按钮并添加*/
		String[] jbName ={"直线","文字","图形撤回"};
		for(int i=0;i<jbName.length;i++){
           button jbu = new button(jbName[i]);
           jbu.setBounds(50,100+(int) (50*(i+0.5)),200,40);
           add(jbu);
        }
		
	}
	
//	/*重写paint函数将图片设置为背景*/
//	protected void paintComponent(Graphics g) {
//	        super.paintComponent(g);
//	        
//	        int i= new Random().nextInt(4);				//返回一个[0,4)的整数
//	        String path = "src/background.png";	//随机的图片路径
//	        
//	        ImageIcon img = new ImageIcon(path);
//	        img.paintIcon(this, g, 30, 125);
//	        
//			int a=img.getIconHeight();
//			int b = img.getIconWidth();
//			System.out.println(a);
//			System.out.println(b);
//	        a=151,b=232;
//	    }

}
