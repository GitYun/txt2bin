# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from distutils import command
import struct
from sys import byteorder
from tkinter import *
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import filedialog
import tkinter
from tkinter.filedialog import *
from tkinter import messagebox
import os
from tokenize import String

def openfile():
    global file_content
    filename = filedialog.askopenfilename(parent=window)
    if (filename != ''):
        input_text.set(filename)

    # read file as string:
    val = format.get()
    if (val == 'Raw'):
        f = open(filename, 'rb')
    else:
        f = open(filename, 'r')

    file_content = f.read()
    f.close()

def selectOutFilename():
    global out_filename
    out_filename = filedialog.asksaveasfilename(initialfile="txt2bin.bin", 
        filetypes=[("Bin文件", ".bin")])
    if (out_filename != ''):
        output_text.set(out_filename)

def convert():
    if (format.get() == 'Raw'):
        with open(out_filename, 'wb') as fbinary:
            fbinary.write(file_content)
            fbinary.close()
    else:
        values = file_content.split(" ")
        in_txt = []

        for i in range(len(values)):
            in_txt.append(int((values[i]), base=10))

        byte_len = int(byte_num.get()[0], base=10)

        with open(out_filename, 'wb') as fbinary:
            for i in range(len(values)):
                if (byte_len == 1):
                    if in_txt[i] < 256:
                        blen = 1
                    elif in_txt[i] < 65536:
                        blen = 2
                    elif in_txt[i] <= 0xFFFFFF:
                        blen = 3
                    else:
                        blen = 4
                elif (byte_len == 2):
                    if (in_txt[i] in range(65536, 0xFFFFFFFF)):
                        blen = 4
                    else:
                        blen = 2
                else:
                    blen = 4
                fbinary.write(int.to_bytes(in_txt[i], blen, byteorder=endian.get()))
            
            fbinary.close()

    convert_state.set("完成")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    window = Tk()
    window.geometry('400x150')
    window.title("txt_2_bin_converter")
    
    input_text = StringVar()
    output_text = StringVar()
    convert_state = StringVar()

    Label(window, text="输入路径:").grid(column=0, row=0, sticky=(W))
    Entry(window, width=40, textvariable=input_text).grid(column=1, row=0, sticky=(W), columnspan=4)
    btn0 = Button(window, text="选择", width=5, command=openfile).grid(column=5, row=0, padx=10)

    Label(window, text="输出路径:").grid(column=0, row=1, sticky=(W))
    Entry(window, width=40, textvariable=output_text).grid(column=1, row=1, sticky=(W), columnspan=4)
    btn1 = Button(window, text="选择", width=5, command=selectOutFilename).grid(column=5, row=1, padx=10)

    Label(window, text="转换状态:").grid(column=0, row=2, sticky=(W))
    Entry(window, width=40, textvariable=convert_state, state='readonly').grid(column=1, row=2, sticky=(W), columnspan=4)
    btn2 = Button(window, text="转换", width=5, command=convert).grid(column=5, row=2, padx=10)    

    Label(window, text="其他配置:").grid(column=0, row=4, sticky=(W))

    endian = StringVar()
    endian.set('little')
    Label(window, text="大小端").grid(column=1, row=3, sticky=(W))
    OptionMenu(window, endian, 'little', 'big').grid(column=1, row=4, sticky=(W))

    byte_num = StringVar()
    byte_num.set('2B')
    Label(window, text="字节数").grid(column=2, row=3, sticky=(W))
    OptionMenu(window, byte_num, '1B', '2B', '4B').grid(column=2, row=4, sticky=(W))

    format = StringVar()
    format.set("Hex")
    Label(window, text="转换格式").grid(column=3, row=3, sticky=(W))
    OptionMenu(window, format, 'Hex', 'Raw').grid(column=3, row=4, sticky=(W))

    window.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/