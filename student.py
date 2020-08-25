# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 14:27:32 2020

@author: hnyangzy
"""

import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  #图形界面
import tkinter.messagebox as messagebox


class StartPage:
    def __init__(self,parent_window):
        parent_window.destroy() #销毁子界面
        
        self.window=tk.Tk()  #初始框声明
        self.window.title('学生信息管理系统')
        self.window.geometry('300x470')
        
        
        label = Label(self.window, text="学生信息管理系统", font=("Verdana", 20))
        label.pack(pady=100)  #pady=100界面长度
        
        Button(self.window,text='管理员登录',font=tkFont.Font(size=(16)),command=lambda :AdminPage(self.window),width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        Button(self.window,text='学生登录',font=tkFont.Font(size=16),command=lambda :StudentPage(self.window),width=30,height=2,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        Button(self.window,text='关于',font=tkFont.Font(size=16),command=lambda:AboutPage(self.window),width=30,height=2, fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        Button(self.window,text='退出系统',font= tkFont.Font(size=16),height=2, command=self.window.destroy,width=30,fg='white',bg='gray',activebackground='black',activeforeground='white').pack()
        
        self.window.mainloop()  #主消息循环
        
        
#管理员登录页面
class AdminPage:
    def __init__(self,parent_window):
        parent_window.destroy() #销毁主界面
        
        self.window = tk.Tk() #初始框声明
        self.window.title('管理员登录页面')
        self.window.geometry('300x450')
        
        label=tk.Label(self.window,text='管理员姓名',bg='green',font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_username=tk.Entry(self.window,width=30,font=tkFont.Font(size=14),bg='Ivory')
        self.admin_username.pack()
        
        label=tk.Label(self.window,text='管理员密码',bg='green',font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass=tk.Entry(self.window,width=30,font=tkFont.Font(size=14),bg='Ivory',show='*')
        self.admin_pass.pack()
        
        Button(self.window,text='登录',width=8,font=tkFont.Font(size=12),command=self.login).pack(pady=40)
        Button(self.window,text='返回首页',width=8,font=tkFont.Font(size=12),command=self.back).pack()
        
        self.window.protocol('WM_DELETE_WINDOW',self.back)  #捕捉右上角关闭点击
        self.window.mainloop() #进入消息循环
        
        
    def login(self):
        print(str(self.admin_username.get()))
        print(str(self.admin_pass.get()))
        
        admin_pass=None
        
        #数据库操作，查询管理员表
        db=pymysql.connect(host='localhost',user='root',password='123456',db='student',port=3306) #打开数据库连接
        cursor=db.cursor()  #使用cursor()方法获取操作游标
        sql="SELECT * FROM admin_login_k where admin_id ='%s'"% (self.admin_username.get())
        try:
            db.ping(reconnect=True)
            cursor.execute(sql)
            result = cursor.fetchall()
            
            for row in result:
                admin_id=row[0]
                admin_pass=row[1]
                #print('admin_id=%s,admin_pass=%s'% (admin_id,amdin_pass))
                
        except:
            print('错误：数据不正确!')
            messagebox.showinfo('警告！','用户名或密码不正确！')
        db.close()  #关闭数据库
        
        
        print('正在登录管理员界面')
        print('self',self.admin_pass)
        print('local',admin_pass)
        
        if (self.admin_pass.get()==admin_pass):
            AdminMange(self.window)   #进入管理员操作界面
        else:
            messagebox.showinfo('警告！','用户名或密码不正确！')
            
    def back(self):
            StartPage(self.window)  #显示主窗口，销毁本窗口
            
#学生登录页面
class StudentPage:
    def __init__(self,parent_window):
        parent_window.destroy()  #销毁主界面
        
        self.window=tk.Tk()  #初始窗口声明
        self.window.title('学生登录')
        self.window.geometry('300x450')
        
        label = tk.Label(self.window,text='学生登录',bg='green',font=tkFont.Font(size=30),width=30,height=2)
        label.pack()
        
        label=tk.Label(self.window,text='学生账号：',font=tkFont.Font(size=14)).pack(pady=25)
        self.student_id=tk.Entry(self.window,width=30,font=tkFont.Font(size=14),bg='Ivory')
        self.student_id.pack()
        
        label=tk.Label(self.window, text='学生密码：',font=tkFont.Font(size=(14))).pack(pady=25)
        self.student_pass=tk.Entry(self.window,width=30,font=tkFont.Font(size=14),bg='Ivory',show=('*'))
        self.student_pass.pack()
        
        
        Button(self.window,text='登录',width=8,font=tkFont.Font(size=12),command=self.login).pack(pady=40)
        Button(self.window,text='返回首页',width=8,font=tkFont.Font(size=12),command=self.back).pack()
        
        self.window.protocol("WM_DELETE_WINDOW", self.back)  #捕捉右上角关闭点击
        self.window.mainloop()  #进入消息循环
        
        
    def login(self):
        print(str(self.student_id.get()))
        print(str(self.student_pass.get()))
        stu_pass=None
        
        #数据库操作 查询学生表
        db=pymysql.connect(host='localhost',user='root',password='123456',db='student')  #打开数据库连接
        cursor=db.cursor()  #使用cursor()方法获得操作游标
        sql="select * from stu_login_k where stu_id='%s'"% (self.student_id.get())
        try:
            db.ping(reconnect=True)
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                stu_id=row[0]
                stu_pass=row[1]
                
                print('stu_id=%s,stu_pass=%s'% (stu_id,stu_pass))
                
        except :
                print('错误；数据不正确')
                messagebox.showinfo('警告！','用户名或密码不正确！')
                
        db.close()  #关闭数据库
            
        print('正在登录学生信息查看界面')
        print('self',self.student_pass.get())
        print('local',stu_pass)
        
        if self.student_pass.get()==stu_pass:
            StudentView(self.window,self.student_id.get())  #进入学生查看界面
        else:
            messagebox.showinfo('警告！','用户名或密码不正确！')
            
            
    def back(self):
        StartPage(self.window) #显示主窗口 销毁本窗口
      
        
#管理员操作界面
class AdminMange:
    def __init__(self,parent_window):
        parent_window.destroy() #销毁主界面
        
        self.window=Tk()  #初始窗口声明
        self.window.title('管理员操作界面')
        
        self.frame_left_top=tk.Frame(width=300,height=200)
        self.frame_right_top=tk.Frame(width=200,height=200)
        self.frame_center=tk.Frame(width=500,height=400)
        self.frame_bottom=tk.Frame(width=650,height=50)
        
        
        #定义下方中心列表区域
        self.columns=('学号','姓名','性别','年龄')
        self.tree=ttk.Treeview(self.frame_center,show='headings',height=18,columns=self.columns)
        self.vbar=ttk.Scrollbar(self.frame_center,orient=VERTICAL,command=self.tree.yview)
        
        #定义树形结构与滚动条
        self.tree.config(yscrollcommand=self.vbar.set)
        
        
        #表格的标题
        self.tree.column('学号',width=150,anchor='center')  #表示列，不显示
        self.tree.column('姓名',width=150, anchor='center')
        self.tree.column('性别',width=100, anchor='center')
        self.tree.column('年龄',width=100, anchor='center')
        
        
        #调研方法获取表格内容插入
        self.tree.grid(row=0, column=0,sticky=NSEW)
        self.vbar.grid(row=0,column=1,sticky=NS)
        
        self.id=[]
        self.name=[]
        self.gender = []
        self.age = []
        
        #打开数据库连接
        db=pymysql.connect(host='localhost',user='root',password='123456',db='student')
        cursor=db.cursor()
        sql="select * from student_k"  
        try:
            
            #执行sql语句
            cursor.execute(sql)
            
            #获取所有记录列表
            results=cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.gender.append(row[2])
                self.age.append(row[3])
                
                
        except:
            print('错误：数据不正确')
            messagebox.showinfo('警告！','数据库连接失败！')
            
            
        db.close()  #关闭数据库连接
        
        print('test**************************')
        for i in range(min(len(self.id),len(self.name),len(self.gender),len(self.age))):   #写入数据
            self.tree.insert('',i,values=(self.id[i],self.name[i],self.gender[i],self.age[i]))
            
        for col in self.columns:  #绑定函数，使表头可排序
            self.tree.heading(col,text=col,command=lambda _col=col:self.tree_sort_column(self.tree,_col,False))
         
            
        #定义顶部区域
        #定义左上方区域
        
        self.top_title=Label(self.frame_left_top,text='学生信息：',font=('Verdana',20))
        self.top_title.grid(row=0,column=0,columnspan=2, sticky=NSEW,padx=50, pady=10)
        self.left_top_frame=tk.Frame(self.frame_left_top)
        self.var_id=StringVar() #声明学号
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_age = StringVar()
        
        #学号
        
        self.right_top_id_label=Label(self.frame_left_top,text='学号:',font=('Verdana',15))
        self.right_top_id_entry=Entry(self.frame_left_top,textvariable=self.var_id,font=('Verdana',15))
        self.right_top_id_label.grid(row=1, column=0)  #位置设置
        self.right_top_id_entry.grid(row=1,column=1)
        
        #姓名
        
        self.right_top_name_label=Label(self.frame_left_top,text='姓名：',font=('Verdana',15))
        self.right_top_name_entry=Entry(self.frame_left_top,textvariable=self.var_name,font=('Verdana',15))
        self.right_top_name_label.grid(row=2,column=0)
        self.right_top_name_entry.grid(row=2,column=1)
        
        #性别
        self.right_top_gender_label=Label(self.frame_left_top,text='性别：',font=('Verdana',15))
        self.right_top_gender_entry=Entry(self.frame_left_top,textvariable=self.var_gender, font=('Verdana',15))
        self.right_top_gender_label.grid(row=3,column=0)
        self.right_top_gender_entry.grid(row=3,column=1)
        
        #年龄
        self.right_top_age_label=Label(self.frame_left_top,text='年龄：',font=('Verdana',15))
        self.right_top_age_entry=Entry(self.frame_left_top,textvariable=self.var_age, font=('Verdana',15))
        self.right_top_age_label.grid(row=4,column=0)
        self.right_top_age_entry.grid(row=4,column=1)
        
        #定义右上方区域
        
        self.right_top_title=Label(self.frame_right_top,text='操作',font=('Verdana',20))
        self.tree.bind('<Button-1>', self.click)  #左键获取位置
        self.right_top_button1=ttk.Button(self.frame_right_top,text='新建学生信息',width=20,command=self.new_row)
        self.right_top_button2=ttk.Button(self.frame_right_top,text='更新选中学生信息',width=20,command=self.updata_row)
        self.right_top_button3=ttk.Button(self.frame_right_top,text='删除选中学生信息',width=20,command=self.del_row)
        self.right_top_button4=ttk.Button(self.frame_right_top,text='返回首页',width=20,command=self.back)
        
        #位置设置
        
        self.right_top_title.grid(row=1,column=0,pady=10)
        self.right_top_button1.grid(row=2,column=0,padx=20,pady=5)
        self.right_top_button2.grid(row=3,column=0,padx=20,pady=5)
        self.right_top_button3.grid(row=4,column=0,padx=20,pady=5)
        self.right_top_button4.grid(row=5,column=0,padx=20,pady=5)
        
        #整体区域定位
        
        self.frame_left_top.grid(row=0,column=0,padx=2,pady=5)
        self.frame_right_top.grid(row=0,column=1,padx=30,pady=30)
        self.frame_center.grid(row=1,column=0,columnspan=2,padx=4,pady=5)
        self.frame_bottom.grid(row=2,column=0,columnspan=2)
        
        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)
        
        
        #开始显示主菜单
        self.frame_left_top.tkraise() #开始显示主菜单
        self.frame_right_top.tkraise()        
        self.frame_center.tkraise()        
        self.frame_bottom.tkraise()
        
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
 
    def back(self):
        StartPage(self.window) 
            
            
            
    def click(self,event):
        self.col=self.tree.identify_column(event.x)  #列
        self.row=self.tree.identify_row(event.y)   #行
        
        print(self.col)
        print(self.row)
        self.row_info=self.tree.item(self.row, 'values')
        self.var_id.set(self.row_info[0])
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.right_top_age_entry=Entry(self.frame_left_top,state='disabled',textvariable=self.var_id,font=('Verdana',15))
        
        print('')
        
    def tree_sort_column(self,tv,col,reverse):  #Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
            tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    
            
    
    def new_row(self):
        #print('123')
        #print(self.var_id.get())
        #print(self.var_name.get())
        #print(self.var_gender.get())
        #print(self.var_age.get())
        #print(self.id)
        if str(self.var_id.get()) in self.id:
        	messagebox.showinfo('警告！', '该学生已存在！')
        else:
            
            if self.var_id.get() != '' and self.var_name.get() != '' and self.var_gender.get() != '' and self.var_age.get() != '':
				# 打开数据库连接
                pymysql.connect(host='localhost',user='root',password='123456',db='student',charset='utf8')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql="insert into student_k (id,name,gender,age) values ('%s','%s','%s','%s')" %(self.var_id.get(),self.var_name.get(),self.var_gender.get(),self.var_age.get())  # SQL 插入语句
                try:
                    
                    db.ping(reconnect=True)
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '数据库连接失败！')
                db.close()  # 关闭数据库连接
 
                self.id.append(self.var_id.get())
                self.name.append(self.var_name.get())
                self.gender.append(self.var_gender.get())
                self.age.append(self.var_age.get())
                self.tree.insert('', len(self.id) - 1, values=(
                self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                self.age[len(self.id) - 1]))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')
            else:
                messagebox.showinfo('警告！', '请填写学生数据')
 
    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if (self.var_id.get() == self.row_info[0]):  # 如果所填学号 与 所选学号一致
            # 打开数据库连接
                db = pymysql.connect(host="localhost", user="root", password="123456", db="student")
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "UPDATE student_k SET name = '%s', gender = '%s', age = '%s' \
                    WHERE id = '%s'" % (self.var_name.get(), self.var_gender.get(), self.var_age.get(), self.var_id.get())  # SQL 插入语句
                try:
                    db.ping(reconnect=True)
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    #messagebox.showinfo('提示！', '更新成功！')
                    #self.tree.update()
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接
 
                id_index = self.id.index(self.row_info[0])
                self.name[id_index] = self.var_name.get()
                self.gender[id_index] = self.var_gender.get()
                self.age[id_index] = self.var_age.get()
 
                self.tree.item(self.tree.selection()[0], values=(
                self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                self.var_age.get()))  # 修改对于行信息
                self.tree.update()
                messagebox.showinfo('提示！', '更新成功！')
            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')
 
    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host="localhost", user="root", password="123456", db="student")
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM student_k WHERE id = '%s'" % (self.row_info[0]) # SQL 删除语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
                db.close()  # 关闭数据库连接
 
                id_index = self.id.index(self.row_info[0])
                print(id_index)
                del self.id[id_index]
                del self.name[id_index]
                del self.gender[id_index]
                del self.age[id_index]
                print(self.id)
                self.tree.delete(self.tree.selection()[0])  # 删除所选行
                print(self.tree.get_children())
                
    
 
 
# 学生查看信息界面
class StudentView:
    def __init__(self, parent_window, student_id):
        parent_window.destroy() # 销毁主界面
 
        self.window = tk.Tk()  # 初始框的声明
        self.window.title('关于')
        self.window.geometry('300x450')  # 这里的乘是小x
 
        label = tk.Label(self.window, text='学生信息查看', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack(pady=20)
 
        self.id = '学号:' + ''
        self.name = '姓名:' + ''
        self.gender = '性别:' + ''
        self.age = '年龄:' + ''
		# 打开数据库连接
        print(student_id)
        db = pymysql.connect(host="localhost",user="root", password="123456", db="student")
        cursor = db.cursor()# 使用cursor()方法获取操作游标
        sql = "SELECT * FROM student_k WHERE id = '%s'" % (student_id) # SQL 查询语句
        try:
			# 执行SQL语句
            db.ping(reconnect=True)
            cursor.execute(sql)
			# 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id = '学号:' + row[0]
                self.name = '姓名:' + row[1]
                self.gender = '性别:' + row[2]
                self.age = '年龄:' + row[3]
        except:
            print("Error: unable to fetch data")
            self.messagebox.showinfo('出错！')
        db.close()		# 关闭数据库连接
 
        Label(self.window, text=self.id, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.name, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.gender, font=('Verdana', 18)).pack(pady=5)
        Label(self.window, text=self.age, font=('Verdana', 18)).pack(pady=5) 

        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=16), command=self.back).pack(pady=25)
 
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环
 
    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口
 
 
# About页面
class AboutPage:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁主界面
 
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('关于')
		self.window.geometry('300x450')  # 这里的乘是小x
 
		label = tk.Label(self.window, text='学生信息管理系统', bg='green', font=('Verdana', 20), width=30, height=2)
		label.pack()
 
		Label(self.window, text='作者：十四的月亮', font=('Verdana', 18)).pack(pady=30)
		Label(self.window, text='blog.csdn.net/kdongyi', font=('Verdana', 18)).pack(pady=5)
 
		Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack(pady=100)
 
		self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
		self.window.mainloop()  # 进入消息循环
 
	def back(self):
		StartPage(self.window)  # 显示主窗口 销毁本窗口
 
 
if __name__ == '__main__':
	try:
		# 打开数据库连接 连接测试
		db = pymysql.connect(host='localhost',user= 'root',password='123456', db='student',port=3306)
		# 使用cursor()方法获取操作游标
		cursor = db.cursor()
		# 如果数据表不存在则创建表 若存在则跳过
		# 设置主键唯一
		sql = """CREATE TABLE IF NOT EXISTS student_k(
				id char(20) NOT NULL,
				name char(20) default NULL,
				gender char(5) default NULL,  
				age char(5) default NULL,
				PRIMARY KEY (id)
				
				) ENGINE = InnoDB 
				DEFAULT	CHARSET = utf8
				"""
		cursor.execute(sql)
		# 如果数据表不存在则创建表 若存在则跳过
		sql = """CREATE TABLE IF NOT EXISTS admin_login_k(
						admin_id char(20) NOT NULL,
						admin_pass char(20) default NULL,
						PRIMARY KEY (admin_id)
						) ENGINE = InnoDB 
						DEFAULT	CHARSET = utf8
						"""
		cursor.execute(sql)
		# 如果数据表不存在则创建表 若存在则跳过
		sql = """CREATE TABLE IF NOT EXISTS stu_login_k(
						stu_id char(20) NOT NULL,
						stu_pass char(20) default NULL,
						PRIMARY KEY (stu_id)
						) ENGINE = InnoDB 
						DEFAULT	CHARSET = utf8
						"""
		cursor.execute(sql)
 
		# 关闭数据库连接
		db.close()
 
		# 实例化Application
		window = tk.Tk()
		StartPage(window)
	except:
		messagebox.showinfo('错误！', '连接数据库失败！')
    
        
            
        

        
        
        
        
        
        
        
            
            
            
            
                
        
