import tkinter as tk
from tkinter import ttk

def find_even_odd():
    number = int(entry_number.get())
    if number % 2 == 0:
        result.set(f"{number} is Even")
    else:
        result.set(f"{number} is Odd")

def convert_temperature():
    temp = float(entry_temperature.get())
    if var.get() == 1:
        result_temp.set(f"{temp} Celsius is {(temp * 9/5) + 32} Fahrenheit")
    else:
        result_temp.set(f"{temp} Fahrenheit is {(temp - 32) * 5/9} Celsius")

def register_survey():
    survey_info = f"Name: {entry_name.get()}\nDOB: {entry_dob.get()}\nMobile: {entry_mobile.get()}\nQualification: {entry_qualification.get()}\nCity: {entry_city.get()}"
    result_survey.set(survey_info)

def register_student():
    student_info = f"Name: {entry_student_name.get()}\nClass: {entry_class.get()}\nRollno: {entry_rollno.get()}\nMaths: {slider_maths.get()}\nEnglish: {slider_english.get()}\nScience: {slider_science.get()}"
    result_student.set(student_info)

root = tk.Tk()
root.title("Python Project Coming.....")

# Even and Odd Section
frame_even_odd = tk.Frame(root)
frame_even_odd.pack(pady=10)

tk.Label(frame_even_odd, text="Find Even and Odd Number").grid(row=0, columnspan=2)
tk.Label(frame_even_odd, text="Enter a Number:").grid(row=1, column=0)
entry_number = tk.Entry(frame_even_odd)
entry_number.grid(row=1, column=1)
tk.Button(frame_even_odd, text="Find", command=find_even_odd).grid(row=2, columnspan=2)
result = tk.StringVar()
tk.Label(frame_even_odd, textvariable=result).grid(row=3, columnspan=2)

# Temperature Conversion Section
frame_temperature = tk.Frame(root)
frame_temperature.pack(pady=10)

tk.Label(frame_temperature, text="To Calculate Temperature").grid(row=0, columnspan=2)
entry_temperature = tk.Entry(frame_temperature)
entry_temperature.grid(row=1, columnspan=2)
var = tk.IntVar()
tk.Radiobutton(frame_temperature, text="Celsius to Fahrenheit", variable=var, value=1).grid(row=2, column=0)
tk.Radiobutton(frame_temperature, text="Fahrenheit to Celsius", variable=var, value=2).grid(row=2, column=1)
tk.Button(frame_temperature, text="Calculate", command=convert_temperature).grid(row=3, columnspan=2)
result_temp = tk.StringVar()
tk.Label(frame_temperature, textvariable=result_temp).grid(row=4, columnspan=2)

# Survey Details Section
frame_survey = tk.Frame(root)
frame_survey.pack(pady=10)

tk.Label(frame_survey, text="Survey Details").grid(row=0, columnspan=2)
tk.Label(frame_survey, text="Your Name:").grid(row=1, column=0)
entry_name = tk.Entry(frame_survey)
entry_name.grid(row=1, column=1)
tk.Label(frame_survey, text="D.O.B:").grid(row=2, column=0)
entry_dob = tk.Entry(frame_survey)
entry_dob.grid(row=2, column=1)
tk.Label(frame_survey, text="Mobile No.:").grid(row=3, column=0)
entry_mobile = tk.Entry(frame_survey)
entry_mobile.grid(row=3, column=1)
tk.Label(frame_survey, text="Qualification:").grid(row=4, column=0)
entry_qualification = tk.Entry(frame_survey)
entry_qualification.grid(row=4, column=1)
tk.Label(frame_survey, text="City:").grid(row=5, column=0)
entry_city = tk.Entry(frame_survey)
entry_city.grid(row=5, column=1)
tk.Button(frame_survey, text="Register", command=register_survey).grid(row=6, columnspan=2)
result_survey = tk.StringVar()
tk.Label(frame_survey, textvariable=result_survey).grid(row=7, columnspan=2)

# Student Report Section
frame_student = tk.Frame(root)
frame_student.pack(pady=10)

tk.Label(frame_student, text="Student Report").grid(row=0, columnspan=2)
tk.Label(frame_student, text="Student Name:").grid(row=1, column=0)
entry_student_name = tk.Entry(frame_student)
entry_student_name.grid(row=1, column=1)
tk.Label(frame_student, text="Class:").grid(row=2, column=0)
entry_class = tk.Entry(frame_student)
entry_class.grid(row=2, column=1)
tk.Label(frame_student, text="Rollno:").grid(row=3, column=0)
entry_rollno = tk.Entry(frame_student)
entry_rollno.grid(row=3, column=1)
tk.Label(frame_student, text="Maths:").grid(row=4, column=0)
slider_maths = tk.Scale(frame_student, from_=0, to=100, orient=tk.HORIZONTAL)
slider_maths.grid(row=4, column=1)
tk.Label(frame_student, text="English:").grid(row=5, column=0)
slider_english = tk.Scale(frame_student, from_=0, to=100, orient=tk.HORIZONTAL)
slider_english.grid(row=5, column=1)
tk.Label(frame_student, text="Science:").grid(row=6, column=0)
slider_science = tk.Scale(frame_student, from_=0, to=100, orient=tk.HORIZONTAL)
slider_science.grid(row=6, column=1)
tk.Button(frame_student, text="Register", command=register_student).grid(row=7, columnspan=2)
result_student = tk.StringVar()
tk.Label(frame_student, textvariable=result_student).grid(row=8, columnspan=2)

root.mainloop()
