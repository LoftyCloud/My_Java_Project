/*�ָ����*/

import javax.swing.Box;
import javax.swing.JSplitPane;

@SuppressWarnings("serial")
public class jsplit extends JSplitPane{
	
	public jsplit() {
		// TODO Auto-generated constructor stub
		setDividerLocation(700); 		//�ָ�����λ��
		setEnabled(false);				//�ָ�����Ϊ�����ƶ�
		setVisible(true);				//��Ϊ�ɼ�
		
		JSplitPane js = new JSplitPane();	//��Ϊ��һ���ָ����
        js.setOrientation(JSplitPane.VERTICAL_SPLIT);//���ô�ֱ�ָ�
        js.setLeftComponent(jpanel3.getInstance());
        js.setDividerSize(5);				//���÷ָ��ߵĿ��
        js.setRightComponent(canvas.getInstance());
        js.setDividerLocation(50);
        js.setEnabled(false);
		
		//���ұ����ȫ������һ��box��
		Box box = Box.createVerticalBox();
		box.add(jpanel1.getInstance());
		box.add(jpanel2.getInstance());
		
		/*������ҿؼ�*/
		setLeftComponent(js);	//�������ʵ�������
		setRightComponent(box);
	}
}