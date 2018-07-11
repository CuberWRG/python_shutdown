import os
import tkinter as tk
from  tkinter import messagebox

# 定时关机
def on_click():
	time = xls_text.get().lstrip()
	if time == "0" or time == "":
		os.system("shutdown -s")
		exit()
	else:
		index = 1
		try:
			a = int(time)
			if len(time) > 6:
				tk.messagebox.showinfo("提示", "请输入一个稍小的数字")
				return 1
		except:
			tk.messagebox.showinfo("错误", "请输入一个正确的数字")
			index = 0
			return 0
		if index == 1:
			os.system("shutdown -s -t " + time)
			tk.messagebox.showinfo("完成", "计算机将在 "+time+" 秒后关机！")
# 定时重启
def on_click3():
	time = xls_text.get().lstrip()
	if time == "0" or time == "":
		os.system("shutdown -r")
		exit()
	else:
		index = 1
		try:
			a = int(time)
			if len(time) > 6:
				tk.messagebox.showinfo("提示", "请输入一个稍小的数字")
				return 1
		except:
			tk.messagebox.showinfo("错误", "请输入一个正确的数字")
			index = 0
			return 0
		if index == 1:
			os.system("shutdown -r -t " + time)
			tk.messagebox.showinfo("完成", "计算机将在 "+time+" 秒后重启！")
# 取消关机
def on_click2():
	os.system("shutdown -a")

root = tk.Tk()
root.geometry('400x200+200+200')
root.title("自动关机 power by : 王荣光")
xls_text = tk.StringVar()

l1 = tk.Label(root, text="请输入关机定时(0或空为立即执行)")
l1.pack()
xls = tk.Entry(root, textvariable=xls_text)
xls_text.set(" ")
xls.pack()

tk.Button(root, text="设置关机", command=on_click).pack()
tk.Button(root, text="设置重启", command=on_click3).pack()
tk.Button(root, text="立即取消", command=on_click2).pack()
root.mainloop()