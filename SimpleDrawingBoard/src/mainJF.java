/*������*/

import javax.swing.JFrame;

@SuppressWarnings("serial")
public class mainJF extends JFrame{//�½�һ����̳�JFrame
	/*��������button�еı��湦���õ�JF��λ�ã�*/
	private static mainJF instance = new mainJF(); //��������
	public static mainJF getInstance(){ 		   //��ö���
		return instance;
	}
	
	private mainJF()  {			
		// TODO Auto-generated constructor stub
		setTitle("���׻�ͼ��");							//����
		setBounds(200, 30, 1000, 650);					//λ�úʹ�С
		setResizable(false); 							//��С���ɵ���
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);	//�رմ����˳�����
		setLayout(null); 								//���ò���Ϊ��
		
		/*������*/
		jsplit js = new jsplit();
		setContentPane(js);		 //��������Ϊ�ָ����
	}
}
