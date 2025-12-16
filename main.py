import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import platform
import psutil
# brightness
import screen_brightness_control as pct

# audio
from ctypes import cast, POINTER
import comtypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize COM library
try:
    comtypes.CoInitialize()
except:
    pass

# Global Audio Control Initialization
try:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.EndpointVolume
    volume_control = cast(interface, POINTER(IAudioEndpointVolume))
except Exception as e:
    print(f"Audio init failed: {e}")
    volume_control = None

# open google
import pyautogui

import subprocess
import sys
import webbrowser as wb

root = Tk()
root.title('GUI-GADGETs')
root.geometry('850x560+300+170')
root.resizable(False, False)
root.configure(bg='#292e2e')

# icon
image_icon = PhotoImage(file='image/icon.png')
root.iconphoto(False, image_icon)


Body = Frame(root, width=900, height=600, bg='#d6d6d6')
Body.pack(pady=20, padx=20)

# ---------------------------
LHS = Frame(Body, width=310, height=495, bg='#f4f5f5', highlightbackground='#adacb1', highlightthickness=1)
LHS.place(x=10, y=10)

# logo
photo = PhotoImage(file='image/laptop.png')
myimage = Label(LHS, image=photo, background='#f4f5f5')
myimage.place(x=2, y=20)

my_system = platform.uname()

l1 = Label(LHS, text=my_system.node, bg='#f4f5f5',
           font=('Acumin Variable Concept', 12, 'bold'), justify='center')
l1.place(x=20, y=200)

l2 = Label(LHS, text=f'Version:{my_system.version}', bg='#f4f5f5',
           font=('Acumin Variable Concept', 8), justify='center')
l2.place(x=20, y=225)

l3 = Label(LHS, text=f'System:{my_system.system}', bg='#f4f5f5',
           font=('Acumin Variable Concept', 10), justify='center')
l3.place(x=20, y=250)

l4 = Label(LHS, text=f'Machine:{my_system.machine}', bg='#f4f5f5',
           font=('Acumin Variable Concept', 10, 'bold'), justify='center')
l4.place(x=20, y=285)

l5 = Label(LHS, text=f'Total RAM installed:{round(psutil.virtual_memory().total/1000000000,2)} GB',
           bg='#f4f5f5', font=('Acumin Variable Concept', 10, 'bold'), justify='center')
l5.place(x=20, y=310)

l6 = Label(LHS, text=f'Processor:{my_system.processor}', bg='#f4f5f5',
           font=('Acumin Variable Concept', 10, 'bold'), justify='center')
l6.place(x=20, y=340)

# ----------------------------
RHS = Frame(Body, width=470, height=230, bg='#f4f5f5', highlightbackground='#adacb1', highlightthickness=1)
RHS.place(x=330, y=10)

system = Label(RHS, text='System', font=('Acumin Variable Concept', 15), bg='#f4f5f5')
system.place(x=10, y=7)


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return '%d:%02d:%02d' % (hours, minutes, seconds)


def none():
    global battery_png
    global battery_label
    battery = psutil.sensors_battery()
    percent = battery.percent
    time = convertTime(battery.secsleft)

    print(percent)
    print(time)

    lb1.config(text=f'{percent}%')
    lb1_plug.config(text=f'Charging:{str(battery.power_plugged)}')
    lb1_time.config(text=f'{time} remaining')

    battery_label = Label(RHS, background='#f4f5f5')
    battery_label.place(x=15, y=50)

    lb1.after(1000, none)
    if battery.power_plugged==True:
        battery_png = PhotoImage(file='image/charging.png')
        battery_label.config(image=battery_png)
    else:
        battery_png = PhotoImage(file='image/battery.png')
        battery_label.config(image=battery_png)


# battery
lb1 = Label(RHS, font=('Acumin Variable Concept', 30, 'bold'), bg='#f4f5f5')
lb1.place(x=200, y=40)

lb1_plug = Label(RHS, font=('Acumin Variable Concept', 10), bg='#f4f5f5')
lb1_plug.place(x=20, y=100)

lb1_time = Label(RHS, font=('Acumin Variable Concept', 10), bg='#f4f5f5')
lb1_time.place(x=200, y=100)

none()

# ################speker#################

lb1_speaker = Label(RHS, text='Speaker', font=('arial', 10, 'bold'), bg='#f4f5f5')
lb1_speaker.place(x=10, y=150)
volume_value = tk.DoubleVar()


def get_current_volume_value():
    return '{: .2f}'.format(volume_value.get())


def volume_changed(event):
    if volume_control:
        try:
            volume_control.SetMasterVolumeLevel(-float(get_current_volume_value()), None)
        except Exception as e:
            print(f"Volume error: {e}")


style = ttk.Style()
style.configure('TScale', background='#f4f5f5')

volume = ttk.Scale(RHS, from_=60, to=0, orient='horizontal', command=volume_changed, variable=volume_value)
volume.place(x=90, y=150)
volume.set(20)

# ############BRIGHTNESS#########
lb1_brightness = Label(RHS, text='Brightness', font=('arial', 10, 'bold'), bg='#f4f5f5')
lb1_brightness.place(x=7, y=185)

current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def brightness_changed(event):
    pct.set_brightness(get_current_value())


brightness = ttk.Scale(RHS, from_=0, to=100, orient='horizontal', command=brightness_changed, variable=current_value)
brightness.place(x=100, y=190)


# ################################
base_dir = os.path.dirname(os.path.abspath(__file__))


def weather():
    subprocess.Popen([sys.executable, os.path.join(base_dir, 'weather/weather.py')])


def clock():
    subprocess.Popen([sys.executable, os.path.join(base_dir, 'clock/clock.py')])

def calendar():
    subprocess.Popen([sys.executable, os.path.join(base_dir, 'calender/calender.py')])


# -----------------------mode-------------------
button_mode = True


def mode():
    global button_mode
    if button_mode:
        LHS.config(bg='#292e2e')
        myimage.config(bg='#292e2e')
        l1.config(bg='#292e2e', fg='#d6d6d6')
        l2.config(bg='#292e2e', fg='#d6d6d6')
        l3.config(bg='#292e2e', fg='#d6d6d6')
        l4.config(bg='#292e2e', fg='#d6d6d6')
        l5.config(bg='#292e2e', fg='#d6d6d6')
        l6.config(bg='#292e2e', fg='#d6d6d6')

        RHB.config(bg='#292e2e')
        app1.config(bg='#292e2e')
        app2.config(bg='#292e2e')
        app3.config(bg='#292e2e')
        app4.config(bg='#292e2e')
        app5.config(bg='#292e2e')
        app6.config(bg='#292e2e')
        app7.config(bg='#292e2e')
        app8.config(bg='#292e2e')
        app9.config(bg='#292e2e')
        app10.config(bg='#292e2e')
        apps.config(bg='#292e2e', fg='#d6d6d6')

        button_mode = False

    else:
        LHS.config(bg='#f4f5f5')
        myimage.config(bg='#f4f5f5')
        l1.config(bg='#f4f5f5', fg='#292e2e')
        l2.config(bg='#f4f5f5', fg='#292e2e')
        l3.config(bg='#f4f5f5', fg='#292e2e')
        l4.config(bg='#f4f5f5', fg='#292e2e')
        l5.config(bg='#f4f5f5', fg='#292e2e')
        l6.config(bg='#f4f5f5', fg='#292e2e')

        RHB.config(bg='#f4f5f5')
        app1.config(bg='#f4f5f5')
        app2.config(bg='#f4f5f5')
        app3.config(bg='#f4f5f5')
        app4.config(bg='#f4f5f5')
        app5.config(bg='#f4f5f5')
        app6.config(bg='#f4f5f5')
        app7.config(bg='#f4f5f5')
        app8.config(bg='#f4f5f5')
        app9.config(bg='#f4f5f5')
        app10.config(bg='#f4f5f5')
        apps.config(bg='#f4f5f5', fg='#292e2e')

        button_mode = True


def to_do():
    subprocess.Popen([sys.executable, os.path.join(base_dir, 'to_do/to_do.py')])


def screenshot():
    root.iconify()

    my_screenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    my_screenshot.save(file_path)


def file():
    subprocess.Popen(r'explorer /select, "C:\path\of\folder\file"')

def crome():
    wb.register('chrome', None)
    wb.open('https://www.google.com/')


def cpu():
    subprocess.Popen([sys.executable, os.path.join(base_dir, 'cpu/cpu.py')])


def close_window():
    root.destroy()


def calculator():
    subprocess.Popen([sys.executable, os.path.join(base_dir, 'calculater.py')])



# -----------------------------
RHB = Frame(Body, width=470, height=250, bg='#f4f5f5', highlightbackground='#adacb1', highlightthickness=1)
RHB.place(x=330, y=255)

apps = Label(RHB, text='Apps', font=('Acumin Variable Concept', 15), bg='#f4f5f5')
apps.place(x=10,y=10)

app1_image = PhotoImage(file='image/App1.png')
app1 = Button(RHB, image=app1_image, bd=1, command=weather)
app1.place(x=15, y=50)

app2_image = PhotoImage(file='image/App2.png')
app2 = Button(RHB, image=app2_image, bd=1, command=clock)
app2.place(x=100, y=50)

app3_image = PhotoImage(file='image/App3.png')
app3 = Button(RHB, image=app3_image, bd=1, command=calendar)
app3.place(x=185, y=50)

app4_image = PhotoImage(file='image/App4.png')
app4 = Button(RHB, image=app4_image, bd=1, command=mode)
app4.place(x=270, y=50)

app5_image = PhotoImage(file='image/download.png')
app5 = Button(RHB, image=app5_image, bd=1, command=to_do)
app5.place(x=355, y=50)

app6_image = PhotoImage(file='image/App6.png')
app6 = Button(RHB, image=app6_image, bd=1, command=screenshot)
app6.place(x=15,y=120)

app7_image = PhotoImage(file='image/App7.png')
app7 = Button(RHB, image=app7_image, bd=1, command=file)
app7.place(x=100,y=120)

app8_image = PhotoImage(file='image/App8.png')
app8 = Button(RHB, image=app8_image, bd=1, command=crome)
app8.place(x=185, y=120)

app9_image = PhotoImage(file='image/App9.png')
app9 = Button(RHB, image=app9_image, bd=1, command=cpu)
app9.place(x=270, y=120)

app10_image = PhotoImage(file='image/App10.png')
app10 = Button(RHB, image=app10_image, bd=1, command=close_window)
app10.place(x=355, y=120)

app11_image = PhotoImage(file='image/calculator.png')
app11 = Button(RHB, image=app11_image, bd=1, command=calculator)
app11.place(x=15, y=200)



root.mainloop()
