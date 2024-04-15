import tkinter as tk
from tkinter import messagebox
import os
class SheduleForm:


    def __init__(self, master):
        self.master = master
        self.master.title("Task Scheduler Form")

        self.schedule_type_var = tk.StringVar(self.master)
        self.task_name = tk.Entry(self.master)
        self.day_var = tk.StringVar(self.master)
        self.month_var = tk.StringVar(self.master)
        self.start_time = tk.Entry(self.master)
        self.interval_var = tk.StringVar(self.master)
        self.end_time = tk.Entry(self.master)
        self.duration_var = tk.StringVar(self.master)
        self.start_date = tk.Entry(self.master)
        self.end_date = tk.Entry(self.master)
        self.xml_file = tk.Entry(self.master)
        self.level_var = tk.StringVar(self.master)
        self.delay_time = tk.Entry(self.master)
        self.hresult_var = tk.StringVar(self.master)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Schedule Type:").grid(row=0, column=0)
        tk.Radiobutton(self.master, text="Minute", variable=self.schedule_type_var, value="MINUTE").grid(row=0,
                                                                                                         column=1)
        tk.Radiobutton(self.master, text="Hourly", variable=self.schedule_type_var, value="HOURLY").grid(row=0,
                                                                                                         column=2)
        tk.Radiobutton(self.master, text="Daily", variable=self.schedule_type_var, value="DAILY").grid(row=0,
                                                                                                       column=3)
        tk.Radiobutton(self.master, text="Weekly", variable=self.schedule_type_var, value="WEEKLY").grid(row=0,
                                                                                                         column=4)
        tk.Radiobutton(self.master, text="Monthly", variable=self.schedule_type_var, value="MONTHLY").grid(row=0,
                                                                                                           column=5)

        tk.Label(self.master, text="Task Name:").grid(row=1, column=0)
        self.task_name.grid(row=1, column=1, columnspan=5)

        tk.Label(self.master, text="Day:").grid(row=2, column=0)
        tk.Entry(self.master, textvariable=self.day_var).grid(row=2, column=1)

        tk.Label(self.master, text="Month:").grid(row=3, column=0)
        tk.Entry(self.master, textvariable=self.month_var).grid(row=3, column=1)

        tk.Label(self.master, text="Start Time:").grid(row=4, column=0)
        tk.Entry(self.master, textvariable=self.start_time).grid(row=4, column=1)

        tk.Label(self.master, text="Interval:").grid(row=5, column=0)
        tk.Entry(self.master, textvariable=self.interval_var).grid(row=5, column=1)

        tk.Label(self.master, text="End Time:").grid(row=6, column=0)
        tk.Entry(self.master, textvariable=self.end_time).grid(row=6, column=1)

        tk.Label(self.master, text="Duration:").grid(row=7, column=0)
        tk.Entry(self.master, textvariable=self.duration_var).grid(row=7, column=1)

        tk.Label(self.master, text="Start Date:").grid(row=8, column=0)
        tk.Entry(self.master, textvariable=self.start_date).grid(row=8, column=1)

        tk.Label(self.master, text="End Date:").grid(row=9, column=0)
        tk.Entry(self.master, textvariable=self.end_date).grid(row=9, column=1)

        tk.Label(self.master, text="XML File:").grid(row=10, column=0)
        tk.Entry(self.master, textvariable=self.xml_file).grid(row=10, column=1)

        tk.Label(self.master, text="Level:").grid(row=11, column=0)
        tk.Radiobutton(self.master, text="Highest", variable=self.level_var, value="HIGHEST").grid(row=11, column=1)
        tk.Radiobutton(self.master, text="Normal", variable=self.level_var, value="NORMAL").grid(row=11, column=2)

        tk.Label(self.master, text="Delay Time:").grid(row=12, column=0)
        tk.Entry(self.master, textvariable=self.delay_time).grid(row=12, column=1)

        tk.Label(self.master, text="HResult:").grid(row=13, column=0)
        tk.Entry(self.master, textvariable=self.hresult_var).grid(row=13, column=1)

        tk.Button(self.master, text="Submit", command=self.submit_form).grid(row=14, column=0, columnspan=5)

def submit_form():
    scheduletype = schedule_type_var.get()
    taskname = task_name.get()
    day = day_var.get()
    month = month_var.get()
    starttime = start_time.get()
    interval = interval_var.get()
    endtime = end_time.get()
    duration = duration_var.get()
    startdate = start_date.get()
    enddate = end_date.get()
    xmlfile = xml_file.get()
    level = level_var.get()
    delaytime = delay_time.get()
    hresult = hresult_var.get()

    command = (f'cmd /c "schtasks /create /sc {scheduletype} /tn {taskname} '
               f'/tr "{os.getcwd()}" '
               f'/d {day} '
               f'/m {month} '
               f'/st {starttime} '
               f'/ri {interval} '
               f'/et {endtime} '
               f'/du {duration} '
               f'/sd {startdate} '
               f'/ed {enddate} '
               f'/xml {xmlfile} '
               f'/rl {level} '
               f'/delay {delaytime} '
               f'/hresult {hresult}"')

    messagebox.showinfo("Command", command)

root = tk.Tk()
root.title("Task Scheduler Form")

schedule_type_var = tk.StringVar(root)
task_name = tk.Entry(root)
day_var = tk.StringVar(root)
month_var = tk.StringVar(root)
start_time = tk.Entry(root)
interval_var = tk.StringVar(root)
end_time = tk.Entry(root)
duration_var = tk.StringVar(root)
start_date = tk.Entry(root)
end_date = tk.Entry(root)
xml_file = tk.Entry(root)
level_var = tk.StringVar(root)
delay_time = tk.Entry(root)
hresult_var = tk.StringVar(root)

tk.Label(root, text="Schedule Type:").pack()
tk.Radiobutton(root, text="Minute", variable=schedule_type_var, value="MINUTE").pack()
tk.Radiobutton(root, text="Hourly", variable=schedule_type_var, value="HOURLY").pack()
tk.Radiobutton(root, text="Daily", variable=schedule_type_var, value="DAILY").pack()
tk.Radiobutton(root, text="Weekly", variable=schedule_type_var, value="WEEKLY").pack()
tk.Radiobutton(root, text="Monthly", variable=schedule_type_var, value="MONTHLY").pack()

tk.Label(root, text="Task Name:").pack()
task_name.pack()

tk.Label(root, text="Day:").pack()
tk.Entry(root, textvariable=day_var).pack()

tk.Label(root, text="Month:").pack()
tk.Entry(root, textvariable=month_var).pack()

tk.Label(root, text="Start Time:").pack()
tk.Entry(root, textvariable=start_time).pack()

tk.Label(root, text="Interval:").pack()
tk.Entry(root, textvariable=interval_var).pack()

tk.Label(root, text="End Time:").pack()
tk.Entry(root, textvariable=end_time).pack()

tk.Label(root, text="Duration:").pack()
tk.Entry(root, textvariable=duration_var).pack()

tk.Label(root, text="Start Date:").pack()
tk.Entry(root, textvariable=start_date).pack()

tk.Label(root, text="End Date:").pack()
tk.Entry(root, textvariable=end_date).pack()

tk.Label(root, text="XML File:").pack()
tk.Entry(root, textvariable=xml_file).pack()

tk.Label(root, text="Level:").pack()
tk.Radiobutton(root, text="Highest", variable=level_var, value="HIGHEST").pack()
tk.Radiobutton(root, text="Normal", variable=level_var, value="NORMAL").pack()

tk.Label(root, text="Delay Time:").pack()
tk.Entry(root, textvariable=delay_time).pack()

tk.Label(root, text="HResult:").pack()
tk.Entry(root, textvariable=hresult_var).pack()

tk.Button(root, text="Submit", command=submit_form).pack()

root.mainloop()