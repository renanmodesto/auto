#https://www.delftstack.com/pt/tutorial/tkinter-tutorial/tkinter-combobox/

import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('500x100')

# -------------------------------------------------------------------------------------------------------

# Combobox Project
labelProject = tk.Label(app, text="Choose your project")
labelProject.grid(column=0, row=0)

comboProject = ttk.Combobox(app,
                            values=[
                                "January",
                                "February",
                                "March",
                                "April"])

print(dict(comboProject))
comboProject.grid(column=0, row=1)
comboProject.current(1)

# Combobox Test Plan
labelTestPlan = tk.Label(app, text="Choose your Test Plan")
labelTestPlan.grid(column=1, row=0)

comboTestPlan = ttk.Combobox(app,
                             values=[
                                 "January",
                                 "February",
                                 "March",
                                 "April"])


print(dict(comboTestPlan))
comboTestPlan.grid(column=1, row=1)
comboTestPlan.current(2)

# Combobox Test Suit
labelTestSuit = tk.Label(app, text="Choose your Test Suit")
labelTestSuit.grid(column=2, row=0)

comboTestSuit = ttk.Combobox(app,
                             values=[
                                 "January",
                                 "February",
                                 "March",
                                 "April"])


print(dict(comboTestSuit))
comboTestSuit.grid(column=2, row=1)
comboTestSuit.current(3)

print(comboProject.current(), comboProject.get(), comboTestPlan.current(), comboTestPlan.get(),
      comboTestSuit.current(), comboTestSuit.get())

# -------------------------------------------------------------------------------------------------------

# Save evidence
chkSaveEvidence = tk.BooleanVar()
chkSaveEvidence.set(False)

chkExample = tk.Checkbutton(app, text='Save evidence', var=chkSaveEvidence)
chkExample.grid(column=0, row=3)

# -------------------------------------------------------------------------------------------------------
app.iconbitmap('C:\IBOPE\envAutomation\AutomacaoQA\images\Robot.ico')
app.title("Automation QA")
app.mainloop()
