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
		/*实例化按钮并添加*/
		setBorder(BorderFactory.createTitledBorder("常规工具"));		//设置边框
		setLayout(null); 

		String[] jbName ={"铅笔","橡皮","清空画布","保存图像","退出"};
		for(int i=0;i<jbName.length;i++){
           button jbu = new button(jbName[i]);
           jbu.setBounds(50+120*i,13,100,30);
           add(jbu);
        }
	}
	

}
