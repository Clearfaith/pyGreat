# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
e = tk.Entry(window, show='*' )   # tk.Entry���������show='*',��*��������, = None,ԭʼ��ʾ�����ᱻ����
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var)
    # t.insert(1.1, var)  # �ڣ�1��1��λ�ò��루������0��ʼ��

b1 = tk.Button(window, text='inster point', width=15, height=2, command=insert_point)
b1.pack()    # ����Button
b2 = tk.Button(window, text='inster end', width=15, height=2, command=insert_end)
b2.pack()    # ����Button

t = tk.Text(window, height=2)
t.pack()

window.mainloop()   # ��ѭ������ͣ��ˢ�£�