/*主窗体*/

import javax.swing.JFrame;

@SuppressWarnings("serial")
public class mainJF extends JFrame{//新建一个类继承JFrame
	/*单例化（button中的保存功能用到JF的位置）*/
	private static mainJF instance = new mainJF(); //创建对象
	public static mainJF getInstance(){ 		   //获得对象
		return instance;
	}
	
	private mainJF()  {			
		// TODO Auto-generated constructor stub
		setTitle("简易画图板");							//标题
		setBounds(200, 30, 1000, 650);					//位置和大小
		setResizable(false); 							//大小不可调节
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);	//关闭窗体退出程序
		setLayout(null); 								//设置布局为空
		
		/*添加组件*/
		jsplit js = new jsplit();
		setContentPane(js);		 //将内容设为分割面板
	}
}
