/*分割面板*/

import javax.swing.Box;
import javax.swing.JSplitPane;

@SuppressWarnings("serial")
public class jsplit extends JSplitPane{
	
	public jsplit() {
		// TODO Auto-generated constructor stub
		setDividerLocation(700); 		//分割条的位置
		setEnabled(false);				//分割条设为不可移动
		setVisible(true);				//设为可见
		
		JSplitPane js = new JSplitPane();	//左部为另一个分割面板
        js.setOrientation(JSplitPane.VERTICAL_SPLIT);//设置垂直分割
        js.setLeftComponent(jpanel3.getInstance());
        js.setDividerSize(5);				//设置分割线的宽度
        js.setRightComponent(canvas.getInstance());
        js.setDividerLocation(50);
        js.setEnabled(false);
		
		//将右边组件全部放入一个box内
		Box box = Box.createVerticalBox();
		box.add(jpanel1.getInstance());
		box.add(jpanel2.getInstance());
		
		/*添加左右控件*/
		setLeftComponent(js);	//创建类的实例并添加
		setRightComponent(box);
	}
}