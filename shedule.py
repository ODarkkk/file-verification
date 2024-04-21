import tkinter as tk
from tkinter import messagebox
import os

class SheduleForm:
    def create_widgets(self):
        self.schedule_type_var = tk.StringVar()
        self.task_name = tk.Entry()
        self.day_var = tk.StringVar()
        self.month_var = tk.StringVar()
        self.start_time = tk.Entry()
        self.interval_var = tk.StringVar()
        self.end_time = tk.Entry()
        self.duration_var = tk.StringVar()
        self.start_date = tk.Entry()
        self.end_date = tk.Entry()
        self.xml_file = tk.Entry()
        self.level_var = tk.StringVar()
        self.delay_time = tk.Entry()
        self.hresult_var = tk.StringVar()

        tk.Label(text="Schedule Type:").grid(row=0, column=0)
        tk.Radiobutton(text="Minute", variable=self.schedule_type_var, value="MINUTE").grid(row=0, column=1)
        tk.Radiobutton(text="Hourly", variable=self.schedule_type_var, value="HOURLY").grid(row=0, column=2)
        tk.Radiobutton(text="Daily", variable=self.schedule_type_var, value="DAILY").grid(row=0, column=3)
        tk.Radiobutton(text="Weekly", variable=self.schedule_type_var, value="WEEKLY").grid(row=0, column=4)
        tk.Radiobutton(text="Monthly", variable=self.schedule_type_var, value="MONTHLY").grid(row=0, column=5)

        tk.Label(text="Task Name:").grid(row=1, column=0)
        self.task_name.grid(row=1, column=1, columnspan=5)

        tk.Label(text="Day:").grid(row=2, column=0)
        tk.Entry(textvariable=self.day_var).grid(row=2, column=1)

        tk.Label(text="Month:").grid(row=3, column=0)
        tk.Entry(textvariable=self.month_var).grid(row=3, column=1)

        tk.Label(text="Start Time:").grid(row=4, column=0)
        tk.Entry(textvariable=self.start_time).grid(row=4, column=1)

        tk.Label(text="Interval:").grid(row=5, column=0)
        tk.Entry(textvariable=self.interval_var).grid(row=5, column=1)

        tk.Label(text="End Time:").grid(row=6, column=0)
        tk.Entry(textvariable=self.end_time).grid(row=6, column=1)

        tk.Label(text="Duration:").grid(row=7, column=0)
        tk.Entry(textvariable=self.duration_var).grid(row=7, column=1)

        tk.Label(text="Start Date:").grid(row=8, column=0)
        tk.Entry(textvariable=self.start_date).grid(row=8, column=1)

        tk.Label(text="End Date:").grid(row=9, column=0)
        tk.Entry(textvariable=self.end_date).grid(row=9, column=1)

        tk.Label(text="XML File:").grid(row=10, column=0)
        tk.Entry(textvariable=self.xml_file).grid(row=10, column=1)

        tk.Label(text="Level:").grid(row=11, column=0)
        tk.Radiobutton(text="Highest", variable=self.level_var, value="HIGHEST").grid(row=11, column=1)
        tk.Radiobutton(text="Normal", variable=self.level_var, value="NORMAL").grid(row=11, column=2)

        tk.Label(text="Delay Time:").grid(row=12, column=0)
        tk.Entry(textvariable=self.delay_time).grid(row=12, column=1)

        tk.Label(text="HResult:").grid(row=13, column=0)
        tk.Entry(textvariable=self.hresult_var).grid(row=13, column=1)

        tk.Button(text="Submit", command=self.submit_form).grid(row=14, column=0, columnspan=5)

    def submit_form(self):
        scheduletype = self.schedule_type_var.get()
        taskname = self.task_name.get()
        day = self.day_var.get()
        month = self.month_var.get()
        starttime = self.start_time.get()
        interval = self.interval_var.get()
        endtime = self.end_time.get()
        duration = self.duration_var.get()
        startdate = self.start_date.get()
        enddate = self.end_date.get()
        xmlfile = self.xml_file.get()
        level = self.level_var.get()
        delaytime = self.delay_time.get()
        hresult = self.hresult_var.get()

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

        os.system(f'cmd /c "{command}"')

        #messagebox.showinfo("Command", command)

