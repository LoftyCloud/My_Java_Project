/*�ڶ���jpanel*/


import java.awt.Color;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

import javax.swing.BorderFactory;
import javax.swing.JComboBox;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class jpanel2 extends JPanel{
	/*��jpanel2������*/
	canvas can = canvas.getInstance();
	private static jpanel2 instance = new jpanel2(); //��������
	public static jpanel2 getInstance(){ 		   //��ö���
		return instance;
	}

	private jpanel2() {							//���캯��˽�л�����ֹ�����ഴ���µ�ʵ��
		// TODO Auto-generated constructor stub
		setBorder(BorderFactory.createTitledBorder("ͼ�ι���"));		//���ñ߿�
		setLayout(null);
	    // ��Ҫѡ�����Ŀ
	    String[] r = new String[]{"����", "Բ�Ǿ���", "������", "���Բ�Ǿ���"};
	 
	    // ����һ�������б��
	    final JComboBox<String> rect = new JComboBox<String>(r);    // ��Ҫѡ�����Ŀ
	   
	    String[] o = new String[]{"Բ��", "��Բ", "���Բ��", "�����Բ"};
	    final JComboBox<String> ovel = new JComboBox<String>(o);
	    rect.setToolTipText("ѡ�����");//������ʾ��Ϣ
	    ovel.setToolTipText("ѡ��Բ��");
	    rect.setBackground(Color.LIGHT_GRAY);
	    ovel.setBackground(Color.LIGHT_GRAY);
	    rect.setSelectedIndex(-1);//����Ĭ��ѡ�е�ֵ 
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
	    
		/*ʵ������ť�����*/
		String[] jbName ={"ֱ��","����","ͼ�γ���"};
		for(int i=0;i<jbName.length;i++){
           button jbu = new button(jbName[i]);
           jbu.setBounds(50,100+(int) (50*(i+0.5)),200,40);
           add(jbu);
        }
		
	}
	
//	/*��дpaint������ͼƬ����Ϊ����*/
//	protected void paintComponent(Graphics g) {
//	        super.paintComponent(g);
//	        
//	        int i= new Random().nextInt(4);				//����һ��[0,4)������
//	        String path = "src/background.png";	//�����ͼƬ·��
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
