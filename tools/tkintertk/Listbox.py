# coding=gbk
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=4, textvariable=var1)
l.pack()

def print_selection():
    value = lb.get('active')   # ��ù�괦��ֵԭget��lb.curselection()�����һ��ʼû�й�궨λʱ�ᱨ��.lb.get('avtive')Ҳ�У����һ��ʼĬ�Ϲ�궨λ�ڵ�һ��
    var1.set(value)

b = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b.pack()    # ����Button

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))  # ��������ΪԪ�顢list������
lb = tk.Listbox(window, listvariable=var2)  # tk.Listbox()������һ�У������������ֵ
list_items = [1, 2, 3, 4]   # ÿ���������Listbox�������end������һ��ֵ
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')   # ���������루�������㿪ʼ��
lb.insert(2, 'second')
lb.delete(2)
lb.pack()



window.mainloop()   # ��ѭ������ͣ��ˢ�£�