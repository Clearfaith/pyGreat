# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x200')

def insert_point():
    var = e.get()
    t.insert('insert', var)
    # t.insert(1.1, var)  # �ڣ�1��1��λ�ò��루������0��ʼ��

def insert_end():
    var = e.get()
    t.insert('end', var)


e = tk.Entry(window, show='*' )   # �����
# tk.Entry���������show='*',��*��������, = None,ԭʼ��ʾ�����ᱻ����
e.pack()    # ���������

b1 = tk.Button(window, text='inster point', width=15, height=2, command=insert_point)
b1.pack()    # ����Button
b2 = tk.Button(window, text='inster end', width=15, height=2, command=insert_end)
b2.pack()    # ����Button

t = tk.Text(window, height=2)
t.pack()

window.mainloop()   # ��ѭ������ͣ��ˢ�£�