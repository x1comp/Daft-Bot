import tkinter as tk 
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import subprocess


# GUI window
root = tk.Tk()
root.title("Tweaking Utility")
root.geometry('750x450')
Tab_Control = ttk.Notebook(root)

#----TABS-----#

#Start Tab
Start = ttk.Frame(Tab_Control)
Tab_Control.add(Start, text='Start')

#Tweaks Tab
Tweaks = ttk.Frame(Tab_Control)
Tab_Control.add(Tweaks, text='Tweaks')
Tab_Control.pack(expand=1, fill="both")

#Apperance Tab
Apperance = ttk.Frame(Tab_Control)
Tab_Control.add(Apperance, text='Apperance')
Tab_Control.pack(expand=2, fill="both")

#Cleanup Tab
Cleanup = ttk.Frame(Tab_Control)
Tab_Control.add(Cleanup, text='Cleanup')
Tab_Control.pack(expand=3, fill="both")

#Debloat Tab
Debloat = ttk.Frame(Tab_Control)
Tab_Control.add(Debloat, text='Debloat')
Tab_Control.pack(expand=3, fill="both")

#Tab Name Labels
ttk.Label(Tweaks, text="").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(Apperance, text="").grid(column=0, row=0, padx=10, pady=10)

icon=PhotoImage(file="assets\\ds.png")
root.iconphoto(False, icon)

my_label = Label(Start, text="", font=("Consolas", 15), bg="#263D42", fg="white")
my_label.place(relwidth=0.8, relheight=0.15, relx=0.1, rely=0.15)

#----BUTTON FUNCTIONS-----#

#Start Button Function
def restorePoint():
    os.startfile('lib\\Create A Restore Point.lnk')
    input('Press ENTER to exit')

def startup():
    os.startfile('lib\\Startup Apps.lnk')
    input('Press ENTER to exit')


# Tweak Button Functions
def regTweaks():
    os.startfile('lib\\Registry Tweaks.reg')
    input('Press ENTER to exit')

def NvidiaGPUTweaks():
    os.startfile('lib\\properties_for_rent.py')
    input('Press ENTER to exit')

def AudioTweaks():
    os.startfile('lib\\Change Sound Settings.lnk')
    input('Press ENTER to exit')

def winTweaks():
    os.startfile('lib\\Optimize ALL Windows Settings.reg')
    input('Press ENTER to exit')
    
def latencyTweaks():
    os.startfile('lib\\Latency BCD Tweaks.cmd')
    input('Press ENTER to exit')

def DisableWinDefender():
    os.startfile('lib\\Disable Windows Defender.reg')
    input('Press ENTER to exit')
    
def networkTweaks():
    os.startfile('lib\\Network Latency Optimizations.cmd')
    input('Press ENTER to exit')
    
def UndoTweaks():
    os.startfile('lib\\student_accomodation.py')
    input('Press ENTER to exit')
    

def DisableDriverSearching():
    os.startfile('lib\\Disable Automatic Driver Updates.reg')
    input('Press ENTER to exit')

def DisableWinUpdate():
    subprocess.call(['runas','/FullTrust' '/Diyon Shibu:Administrator', 'lib\\Turn Off Auto Windows Updates.cmd'])

def BCDTweaks():
    os.startfile('lib\\student_accomodation.py')
    input('Press ENTER to exit')

# Apperance Button Functions

def ApplyNDrestartA():
     os.system("shutdown /r /t 1")

def TaskBar():
    os.startfile('lib\\properties_for_rent.py')
    input('Press ENTER to exit')

def Themes():
    os.startfile('lib\\properties_for_sale.py')
    input('Press ENTER to exit')
    
def darkMode():
    os.startfile('lib\\properties_to_share.py')
    input('Press ENTER to exit')
    
def lightMode():
    os.startfile('lib\\student_accomodation.py')
    input('Press ENTER to exit')

#Cleanup
def TempFilesCleanup():
    os.startfile('lib\\Delete Temporary Files.cmd')
    input('Press ENTER to exit')

def OldRestorePointCleanup():
    os.startfile('lib\\Create A Restore Point.lnk')
    input('Press ENTER to exit')
    
def WindowsUpdateCleanup():
    os.startfile('lib\\Delete Windows Update Cache.cmd')
    input('Press ENTER to exit')
    
def LogFilesCleanup():
    os.startfile('lib\\Delete Log Files.cmd')
    input('Press ENTER to exit')

#Debloat
def BasicDebloat():
    os.startfile('lib\\Debloat Script.cmd')
    input('Press ENTER to exit')

def AdvancedDebloat():
    os.startfile('lib\\Debloat Script.cmd')
    input('Press ENTER to exit')
    
def DeleteUnusedApps():
    os.startfile('lib\\Uninstall Apps You Don_t Need.lnk')
    input('Press ENTER to exit')
    
def DisableOneDrive():
    os.startfile('lib\\student_accomodation.py')
    input('Press ENTER to exit')

def ApplyNDrestart():
     os.system("shutdown /r /t 1")

#right click button functions
def help():
	my_label.config(text="For Detailed info read the readme.md")

def credits():
	my_label.config(text="This Tweaking Utility was developed by Diyon Shibu")

def my_popup(e):
	my_menu.tk_popup(e.x_root, e.y_root)

def browseFiles():
      filename = filedialog.askopenfilename(initialdir = "lib", title = "Select a File", filetypes = (("all files","*.*"), ("Text files", "*.txt*"),))
 #----TAB BUTTONS----#   

 #Start
restorePoint = tk.Button(Start, text="Create Restore Point", padx=23, pady=15, fg="white", bg="#263D42", command=restorePoint)
restorePoint.place(relx=0.21, rely=0.487, anchor=CENTER)

startup = tk.Button(Start, text="Disable Startup Apps", padx=23, pady=15, fg="white", bg="#263D42", command=startup)
startup.place(relx=0.81, rely=0.487, anchor=CENTER)

# Tweaks
regTweaks = tk.Button(Tweaks, text="Registry Tweaks", padx=23, pady=15, fg="white", bg="#263D42", command=regTweaks)
regTweaks.place(relx=0.81, rely=0.387, anchor=CENTER)

NvidiaGPUTweaks = tk.Button(Tweaks, text="Nvidia GPU Tweaks", padx=20, pady=15, fg="white", bg="#263D42", command=NvidiaGPUTweaks)
NvidiaGPUTweaks.place(relx=0.81, rely=0.225, anchor=CENTER)

DisableWinDefender = tk.Button(Tweaks, text="Disable Windows Defender", padx=1, pady=15, fg="white", bg="#263D42", command=DisableWinDefender)
DisableWinDefender.place(relx=0.21, rely=0.225, anchor=CENTER)

winTweaks = tk.Button(Tweaks, text="Windows Tweaks", padx=22, pady=15, fg="white", bg="#263D42", command=winTweaks)
winTweaks.place(relx=0.21, rely=0.55, anchor=CENTER)

networkTweaks = tk.Button(Tweaks, text="Network Tweaks", padx=22.15, pady=16, fg="white", bg="#263D42", command=networkTweaks)
networkTweaks.place(relx=0.21, rely=0.71, anchor=CENTER)

latencyTweaks = tk.Button(Tweaks, text="Latency Tweaks", padx=23, pady=15, fg="white", bg="#263D42", command=latencyTweaks)
latencyTweaks.place(relx=0.810, rely=0.55, anchor=CENTER)

UndoTweaks = tk.Button(Tweaks, text="Undo Tweaks", padx=16, pady=11, fg="white", bg="#263D42", command=UndoTweaks)
UndoTweaks.place(relx=0.520, rely=0.725, anchor=CENTER)

ApplyNDrestart = tk.Button(Tweaks, text="Apply And Restart", padx=16, pady=11, fg="white", bg="#263D42", command=ApplyNDrestart)
ApplyNDrestart.place(relx=0.520, rely=0.925, anchor=CENTER)

AudioTweaks = tk.Button(Tweaks, text="Audio Tweaks", padx=28.225, pady=15, fg="white", bg="#263D42", command=AudioTweaks)
AudioTweaks.place(relx=0.21, rely=0.870, anchor=CENTER)

DisableDriverSearching = tk.Button(Tweaks, text="Disable Driver Searching", padx=2, pady=15, fg="white", bg="#263D42", command=DisableDriverSearching)
DisableDriverSearching.place(relx=0.81, rely=0.71, anchor=CENTER)

DisableWinUpdate = tk.Button(Tweaks, text="Disable Windows Updates", padx=1, pady=15, fg="white", bg="#263D42", command=DisableWinUpdate)
DisableWinUpdate.place(relx=0.21, rely=0.387, anchor=CENTER)

BCDTweaks = tk.Button(Tweaks, text="BCD Tweaks", padx=28.225, pady=15, fg="white", bg="#263D42", command=BCDTweaks)
BCDTweaks.place(relx=0.81, rely=0.870, anchor=CENTER)

#Apperance
TaskBar = tk.Button(Apperance, text="Taskbar customization", padx=20, pady=15, fg="white", bg="#263D42", command=TaskBar)
TaskBar.place(relx=0.81, rely=0.387, anchor=CENTER)

Themes = tk.Button(Apperance, text="Themes customization", padx=20, pady=15, fg="white", bg="#263D42", command=Themes)
Themes.place(relx=0.21, rely=0.225, anchor=CENTER)

darkMode = tk.Button(Apperance, text="Enable Dark Mode", padx=30, pady=15, fg="white", bg="#263D42", command=darkMode)
darkMode.place(relx=0.21, rely=0.387, anchor=CENTER)

lightMode = tk.Button(Apperance, text="Enable Light Mode", padx=29, pady=15, fg="white", bg="#263D42", command=lightMode)
lightMode.place(relx=0.81, rely=0.225, anchor=CENTER)

ApplyNDrestartA = tk.Button(Apperance, text="Apply And Restart", padx=16, pady=11, fg="white", bg="#263D42", command=ApplyNDrestartA)
ApplyNDrestartA.place(relx=0.520, rely=0.925, anchor=CENTER)

UndoTweaks = tk.Button(Apperance, text="Undo Tweaks", padx=16, pady=11, fg="white", bg="#263D42", command=UndoTweaks)
UndoTweaks.place(relx=0.520, rely=0.725, anchor=CENTER)

#cleanup
TempFilesCleanup = tk.Button(Cleanup, text="Temporary File Cleanup", padx=20, pady=15, fg="white", bg="#263D42", command=TempFilesCleanup)
TempFilesCleanup.place(relx=0.81, rely=0.387, anchor=CENTER)

UndoTweaks = tk.Button(Cleanup, text="Undo Tweaks", padx=16, pady=11, fg="white", bg="#263D42", command=UndoTweaks)
UndoTweaks.place(relx=0.520, rely=0.725, anchor=CENTER)

OldRestorePointCleanup = tk.Button(Cleanup, text="Delete Old Restore Points", padx=20, pady=15, fg="white", bg="#263D42", command=OldRestorePointCleanup )
OldRestorePointCleanup.place(relx=0.21, rely=0.225, anchor=CENTER)

WindowsUpdateCleanup = tk.Button(Cleanup, text="Windows Update Cleanup", padx=18, pady=15, fg="white", bg="#263D42", command=WindowsUpdateCleanup)
WindowsUpdateCleanup.place(relx=0.21, rely=0.387, anchor=CENTER)

LogFilesCleanup = tk.Button(Cleanup, text="Log File Cleanup", padx=38, pady=15, fg="white", bg="#263D42", command=LogFilesCleanup)
LogFilesCleanup.place(relx=0.81, rely=0.225, anchor=CENTER)

ApplyNDrestart = tk.Button(Cleanup, text="Apply And Restart", padx=16, pady=11, fg="white", bg="#263D42", command=ApplyNDrestart)
ApplyNDrestart.place(relx=0.520, rely=0.925, anchor=CENTER)

#Debloat
UndoTweaks = tk.Button(Debloat, text="Undo Tweaks", padx=16, pady=11, fg="white", bg="#263D42", command=UndoTweaks)
UndoTweaks.place(relx=0.520, rely=0.725, anchor=CENTER)

BasicDebloat = tk.Button(Debloat, text="Basic Debloat", padx=30, pady=15, fg="white", bg="#263D42", command=BasicDebloat)
BasicDebloat.place(relx=0.81, rely=0.387, anchor=CENTER)

AdvancedDebloat = tk.Button(Debloat, text="Advanced Debloat", padx=20, pady=15, fg="white", bg="#263D42", command=AdvancedDebloat )
AdvancedDebloat.place(relx=0.21, rely=0.225, anchor=CENTER)

DeleteUnusedApps = tk.Button(Debloat, text="Delete Unused Apps", padx=18, pady=15, fg="white", bg="#263D42", command=DeleteUnusedApps)
DeleteUnusedApps.place(relx=0.21, rely=0.387, anchor=CENTER)

DisableOneDrive = tk.Button(Debloat, text="Disable OneDrive", padx=20, pady=15, fg="white", bg="#263D42", command=DisableOneDrive)
DisableOneDrive.place(relx=0.81, rely=0.225, anchor=CENTER)

ApplyNDrestart = tk.Button(Debloat, text="Apply And Restart", padx=16, pady=11, fg="white", bg="#263D42", command=ApplyNDrestart)
ApplyNDrestart.place(relx=0.520, rely=0.925, anchor=CENTER)

# right click
my_menu = Menu(root, tearoff=False)
my_menu.add_command(label="Show Credits", command=credits)
my_menu.add_command(label="Get Help", command=help)
my_menu.add_command(label="Edit Filter Options", command=browseFiles)
my_menu.add_separator()
my_menu.add_command(label="Exit", command=root.quit)

root.bind("<Button-3>", my_popup)
root.mainloop()
