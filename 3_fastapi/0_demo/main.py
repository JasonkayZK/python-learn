# 1 导入turtle
import turtle as tt

# 2 创建画布（设置画布宽高与窗口标题）
tt.setup(800, 600)
tt.title("ITB业生")

# 3 设置画笔（颜色、线宽、速度）
tt.pencolor("red")
tt.width(4)
tt.speed(1)

# 4 设置抬笔与落笔
tt.up()  # 抬笔

# 5 移动画笔（前进/后退、位置）
tt.goto(0, 100)  # 移动（0, 100）
tt.down()  # 落笔

# 6 绘制圆（圆环、圆弧、实心圆）
#  --------------- 绘制圆环  -------------------
tt.circle(50)  # 绘制半径为50的圆形


#  --------------- 绘制圆弧  -------------------
tt.up()
tt.pencolor("blue")
tt.goto(-50, -100)  # 移动（-50, -100）
tt.down()
tt.circle(60, -180)  # 绘制半径为60的圆形，弧度为-180

#  --------------- 绘制实心圆  -------------------
tt.up()
tt.pencolor("green")
tt.goto(100, 200)  # 移动（100, 200）
tt.down()
tt.dot(80, "orange")  # 绘制半径为90的圆形，填充为橙色

# 7 循环画布
tt.mainloop()
