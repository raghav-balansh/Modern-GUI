# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and set

from tkinter import *
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
import speedtest
import math
from PIL import ImageTk, Image
import psutil

def usage():
    cpu_count = psutil.cpu_count()
    cpu_count_label.config(text=cpu_count, image=tk_image, compound='center', fg='#00ffff')

    cpu_usage = psutil.cpu_percent(1)
    cpu_usage_label.config(text=cpu_usage, image=tk_image, compound='center', fg='#00ffff')
    cpu_usage_label.after(100, usage)

    ram_count = math.floor(psutil.virtual_memory()[0] / 1000000000)
    ram_count_text = str(ram_count) + 'GB'
    ram_count_label.config(text=ram_count_text, image=tk_image, compound='center', fg='#00ffff')

    ram_usage = psutil.virtual_memory()[2]
    ram_usage_text = str(ram_usage) + '%'
    ram_usage_label.config(text=ram_usage_text, image=tk_image, compound='center', fg='#00ffff')

    avail_ram = math.floor(psutil.virtual_memory()[1] / 1000000)
    avail_ram_text = str(avail_ram) + ' MB'
    avail_ram_label.config(text=avail_ram_text,image=tk_image, compound='center', fg='#00ffff')


def internet_speed():
    print('TESTING INERNET SPEED')
    st = speedtest.Speedtest()
    st.get_servers()
    upload_speed = str(math.floor(st.download()/(10**6))) + 'Mb/s'
    download_speed = str(math.floor(st.upload()/(10**6))) + 'Mb/s'
    ping = str(st.results.ping) + 'MS'
    upload_label.config(text=upload_speed)
    download_label.config(text=download_speed)
    ping_label.config(text=ping)


root = Tk()
root.config(bg='black')
im1 = Image.open(os.path.join(base_dir, 'sp.png'))
image1 = im1.resize((300, 350))
tk_image = ImageTk.PhotoImage(image1)

root.geometry('1700x1080')
root.title('CPU STATUS')

cpu_count_label = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='0', bd=-4)
cpu_count_label.grid(row=0, column=0)
l1 = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='CPUs',bg='black',fg='#fcba03')
l1.grid(row=1, column=0)

cpu_usage_label = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='0', bd=-4)
cpu_usage_label.grid(row=0, column=1)
l2 = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='CPU USAGE IN %', bg='black', fg='#fcba03')
l2.grid(row=1, column=1)

ram_count_label = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='0', bd=-4)
ram_count_label.grid(row=0, column=2)
l3 = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text="TOTOAL RAM", bg='black', fg='#fcba03')
l3.grid(row=1, column=2)

ram_usage_label = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='0', bd=-4)
ram_usage_label.grid(row=0, column=3)
l4 = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='TOTAL RAM', bg='black', fg='#fcba03')
l4.grid(row=1, column=3)

avail_ram_label = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='0', bd=-4)
avail_ram_label.grid(row=0, column=4)
l5 = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='AVAILABLE RAM', bg='black', fg='#fcba03')
l5.grid(row=1, column=4)

speed_button = Button(root, text='TEST INTERNET SPEED', command=internet_speed, width=20, height=3, font=('Kanit-ExtraBold', 20, 'bold'),relief=RAISED)
speed_button.grid(row=3, column=0)

download_label = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='0 Mb/s', image=tk_image, compound='center', fg='#00ffff', bd=-4)
download_label.grid(row=3, column=1)
l6 = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='DOWNLOAD SPEED', bg='black', fg='#fcba03')
l6.grid(row=4, column=1)

upload_label = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='0 Mb/s',image=tk_image, compound='center', fg='#00ffff', bd=-4)
upload_label.grid(row=3, column=2)
l7 = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='UPLOAD SPPED', bg='black', fg='#fcba03')
l7.grid(row=4, column=2)

ping_label = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='0', image=tk_image, compound='center', fg='#00ffff',bd=-4)
ping_label.grid(row=3, column=3)
l8 = Label(root, font=('Kanit-ExtraBold', 20, 'bold'), text='PING', bg='black', fg='#fcba03')
l8.grid(row=4, column=3)

usage()
root.mainloop()
