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
        
        label=tk.Lable(self.window,text='管理员登录',bg='green',font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_username=tk.Entry(self.window,width=30,font=tkFont.Font(size=14),bg='Ivory',show='*')
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
        db=pymysql.connect('localhost','root','root','student') #打开数据库连接
        cursor=db.cursor()  #使用cursor()方法获取操作游标
        sql="SELECT * FROM admin_login_k where admin_id ='%s" % (self.admin_username.get())
        try:
            cursor.execute(sql)
            
            result = cursor.fetchall()
            for row in result:
                admin_id=row[0]
                admin_pass=row[1]
                print('admin_id=%s,admin_pass=%s'% (admin_id,amdin_pass))
                
        except:
            print('错误：数据不正确!')
            messagebox.showinfo('警告！','用户名或密码不正确！')
        db.close()  #关闭数据库
        
        
        print('正在登录管理员挂你界面')
        print('self',self.admin_pass)
        print('local',admin_pass)
        
        if self.admin_pass.get()==admin_pass:
            AdminManage(self.window)   #进入管理员操作界面
        else:
            messagebox.showinfo('警告！','用户名或密码不正确！')
            
        def back(self):
            StartPage(self.window)  #显示主窗口，销毁本窗口
            
#学生登录页面
class StudentPage:
    def __init__(self,parent_window):
        parent_window.destroy()  #销毁主界面
        
        self.window=tk.TK()  #初始窗口声明
        self.window.title('学生')
            
            
            
            
                
        
