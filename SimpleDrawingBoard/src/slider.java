import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.JTextField;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

/*����*/

@SuppressWarnings("serial")
public class slider extends JPanel{
	int v=0;
	JLabel label;
	JTextField field;
	JSlider slider;
	
	/*JLabel+ JTextArea+ JSlider ����Ͻṹ*/
	public slider(String s) {
		setLayout(null);
		// TODO Auto-generated constructor stub
		 label = new JLabel(s);
		 field = new JTextField("0");
		 field.setEditable(false);
		 field.setBorder(null);

		 if (s.equals("Size:")) {
			 slider = new JSlider(0,20,0);
			 label.setBounds(10,5,40,40);
			 field.setBounds(40,5,30,40);
			 slider.setBounds(70,5,170,40);
		 }
		 else {
			 slider = new JSlider(0,255,0);
			 label.setBounds(10,5,40,20);
			 field.setBounds(40,5,30,20);
			 slider.setBounds(70,5,170,20);
		 }
		 
		 add(label);
		 add(field);
		 add(slider);
		 
		 /*���ָı�ʱ�ı�field��ֵ*/
		 slider.addChangeListener(new ChangeListener() {//��Ӽ���
			@Override//�����ı�
			public void stateChanged(ChangeEvent e) { 
				// TODO Auto-generated method stub
				v = slider.getValue();
				field.setText(v + "");
			}
		 });
	}
	public int getV() { //��ȡ���ֵ�ֵ
		return v;
	}
}