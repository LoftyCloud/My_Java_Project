import javax.swing.BorderFactory;
import javax.swing.JPanel;

@SuppressWarnings("serial")
public class jpanel3  extends JPanel{
	private static jpanel3 Instance = new jpanel3();
	public static jpanel3 getInstance() {
		return Instance;
	}
	
	private jpanel3(){
		// TODO Auto-generated constructor stub
		/*ʵ������ť�����*/
		setBorder(BorderFactory.createTitledBorder("���湤��"));		//���ñ߿�
		setLayout(null); 

		String[] jbName ={"Ǧ��","��Ƥ","��ջ���","����ͼ��","�˳�"};
		for(int i=0;i<jbName.length;i++){
           button jbu = new button(jbName[i]);
           jbu.setBounds(50+120*i,13,100,30);
           add(jbu);
        }
	}
	

}
