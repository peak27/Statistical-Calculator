import numpy as np
from math import sqrt
from collections import Counter
from tkinter import *
sccal=Tk()
sccal.geometry('400x500')
sccal.configure(bg='lightblue')
sccal.title("Prashant's Calculator")
sccal.iconbitmap('C:/Users/mjpk2/OneDrive/Desktop/Statistical Calculator/icon.ico')

def mean():
    global  averag, dset
    stext = ment.get()
    numlist = [float(x) for x in stext.split(',')]
    dset = Label(sccal, text = "\nYour Dataset: \n" + str(numlist), bg='lightblue', font=("Helvetica", 13))
    dset.pack(pady=10)
    mean = 0.0
    for i in numlist:
        mean += i
    mean = mean / float(len(numlist))
    mean = round(mean, 2)
    averag = Label(sccal, text='Mean: '+ str(mean), bg='lightblue', anchor = 'center', font=("Helvetica", 13))
    averag.pack()
    myButton['state'] = DISABLED
    return

def median():
    global median
    stext = ment.get()
    numlist = [float(x) for x in stext.split(',')]
    #dset = Label(sccal, text = "\nYour Dataset: " + str(numlist)).pack()
    snums = sorted(numlist)
    pos = (len(snums) - 1) // 2

    if len(snums) % 2 == 0:
        med = ((snums[pos] + snums[pos + 1]) / 2.0)
        median = Label(sccal, text='Median: ' + str(med), bg='lightblue', anchor = 'center', font=("Helvetica", 13))
        median.pack(fill='both')
        return
    else:
        med = snums[pos]
        median = Label(sccal, text='Median: ' + str(med), bg='lightblue', anchor = 'center', font=("Helvetica", 13))
        median.pack(fill='both')
        return

def mode():
    global mode
    stext = ment.get()
    numlist = [float(x) for x in stext.split(',')]
    # dset = Label(sccal, text = "\nYour Dataset: " + str(numlist), font=("Helvetica", 13)).pack()
    data = Counter(numlist)
    md = dict(data)
    freq = max(list(data.values()))
    mde = [i for i, v in md.items() if v == freq]

    if len(mde) == len(numlist):
        md = "No Mode Found"
        mode = Label(sccal, text='Mode: ' + str(md), bg='lightblue', anchor = 'center', font=("Helvetica", 13))
        mode.pack(fill='both')
        return
    else:
        md = mde
        mode = Label(sccal, text='Mode: ' + str(md), bg='lightblue', anchor = 'center', font=("Helvetica", 13))
        mode.pack(fill='both')
        return

def stdev():
    global stdev, varian
    stext = ment.get()
    numlist = [float(x) for x in stext.split(',')]
    std_dev = sqrt(sum([(i - np.mean(numlist)) ** 2 for i in numlist]) / (len(numlist) - 1))
    std_dev = round(std_dev, 2)
    variance = std_dev ** 2
    variance = round(variance, 2)
    stdev = Label(sccal, text='Standard Deviation : '+ str(std_dev), bg='lightblue', anchor = 'center', font=("Helvetica", 13))
    stdev.pack()
    varian = Label(sccal, text='Variance : ' + str(variance), bg='lightblue', anchor = 'w', font=("Helvetica", 13))
    varian.pack()
    return

def clear():
    averag.destroy()
    dset.destroy()
    median.destroy()
    mode.destroy()
    stdev.destroy()
    varian.destroy()
    myentry.delete(0, 'end')
    clearButton['state'] = NORMAL


myLabel = Label(sccal, text = '\nStatistical Calculator',relief="flat", bg='lightblue', font=("arial", 17, "bold")).pack()
myLabel = Label(sccal, text = '\nPlease Enter The Numbers Below', bg='lightblue', font=("arial", 12, "bold")).pack()
myLabel = Label(sccal, text = '(Separated by Comma)', bg='lightblue', font=("arial", 9, "bold")).pack(pady=9)

ment = StringVar()
myentry = Entry(sccal, textvariable=ment, width=20, font=("arial", 17))
myentry.pack()



myButton = Button(sccal, text="Calculate", command=lambda :[mean(),median(),mode(),stdev()])
myButton.pack(pady=8)

clearButton = Button(sccal, text="clear", command=clear)
clearButton.pack(pady=8)


#exitButton = Button(sccal, text="Exit", command=sccal.quit())
#exitButton.pack()

sccal.mainloop()


# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)