from tkinter.constants import GROOVE, RAISED, RIDGE
import cv2
import time
from datetime import date, datetime
import tkinter as tk 
from tkinter import Frame, ttk, messagebox
from tkinter import *
import os

window = tk.Tk()
window.title('BIT QR-Attendance System')
window.geometry('500x500')                           
year= tk.StringVar()      
branch= tk.StringVar()
period= tk.StringVar()

title = tk.Label(window,text="Attendance System V-089",bd=10,relief=tk.GROOVE,font=("times new roman",20),bg="lavender",fg="black")
title.pack(side=tk.TOP,fill=tk.X)

Manage_Frame=Frame(window,bg="lavender")
Manage_Frame.place(x=0,y=80,width=480,height=530)

ttk.Label(window, text = "Year",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=150)
combo_search=ttk.Combobox(window,textvariable=year,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('1','2','3','4','5') 
combo_search.place(x=250,y=150)

ttk.Label(window, text = "Branch",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=200)
combo_search=ttk.Combobox(window,textvariable=branch,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=("BCA","BBA","BCOM","BA","BSC","MCA","MBA","BAM")
combo_search.place(x=250,y=200)

ttk.Label(window, text = "Period",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=250)
combo_search=ttk.Combobox(window,textvariable=period,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('1','2','3','4','5','6','7','8','9','10')
combo_search.place(x=250,y=250)

def checkk():
    if(year.get() and branch.get() and period.get()):
        window.destroy()
    else:
        messagebox.showwarning("Warning", "All fields required!!")

exit_button = tk.Button(window,width=13, text="Submit",font=("Times New Roman", 15),command=checkk,bd=2,relief=RIDGE)
exit_button.place(x=300,y=330)



Manag_Frame=Frame(window,bg="lavender")
Manag_Frame.place(x=480,y=80,width=450,height=530)

canvas = Canvas(Manag_Frame, width = 300, height = 300,background="lavender")      
canvas.pack()      
# script_dir = os.path.dirname(os.path.abspath(__file__))
# img_path = os.path.join(script_dir, "bg.png")
# img = PhotoImage(file=img_path)      
# canvas.create_image(50,50, anchor=NW, image=img) 

def on_closing():
    window.destroy()
    exit()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()

cap = cv2.VideoCapture(0)
names=[]
today=date.today()
d= today.strftime("%b-%d-%Y")

filename = f"{branch.get()}-{year.get()}_{d}_Period{period.get()}.csv"
print(f"Attendance file: {os.path.abspath(filename)}")
fob=open(filename,'w+')
fob.write("Reg No.,Branch,Year,Period,In Time\n")

def enterData(z):   
    if z in names:
        pass
    else:
        it=datetime.now()
        names.append(z)
        z=''.join(str(z))
        intime = it.strftime("%H:%M:%S")

        fob.write(f"{z},{branch.get()},{year.get()},{period.get()},{intime}\n")
        fob.flush()  # Ensure data is written immediately
    return names
    
print('Reading...')

def checkData(data):
    # data=str(data)    
    if data in names:
        print('Already Present')
    else:
        print(f'QR Data detected: {data}')
        print('\n'+str(len(names)+1)+'\n'+'present...')
        enterData(data)

def decode_qr(frame):
    detector = cv2.QRCodeDetector()
    val, points, straight_qr = detector.detectAndDecode(frame)
    return val

while True:
    _, frame = cap.read()         
    qr_data = decode_qr(frame)
    if qr_data:  # Only check if QR code was actually detected
        checkData(qr_data)
        time.sleep(1)
        
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)&0xFF
    # Close if 'g' is pressed or window is closed
    if key == ord('g') or cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1:
        break
    
cap.release()
cv2.destroyAllWindows()
fob.close()
print(f"\nAttendance saved to: {os.path.abspath(filename)}")
print(f"Total students: {len(names)}")
