from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.geometry('400x350')
window.config(bg="Gainsboro")
window.config(padx=20, pady=20)
# BMI Label
lblBMI = Label(font=("Arial", 14))


def calculateBmi():
    bmi = int(entWeight.get()) / (int(entHeight.get()) / 100) ** 2
    print(bmi)
    return bmi


def click():
    bmi = calculateBmi()

    if bmi <= 18.4:
        window.config(bg="Yellow")
        lblWeight.config(bg="Yellow")
        lblHeight.config(bg="Yellow")
        lblBMI.config(text=f"Your BMI: {bmi:.2f}. You are Underweight")
    elif 18.4 < bmi <= 24.9:
        window.config(bg="Green")
        lblWeight.config(bg="Green")
        lblHeight.config(bg="Green")
        lblBMI.config(text=f"Your BMI: {bmi:.2f}. You are Normal")
    elif 24.9 < bmi <= 39.9:
        window.config(bg="Orange")
        lblWeight.config(bg="Orange")
        lblHeight.config(bg="Orange")
        lblBMI.config(text=f"Your BMI: {bmi:.2f}. You are Overweight")
    elif 39.9 < bmi:
        window.config(bg="Red")
        lblWeight.config(bg="Red")
        lblHeight.config(bg="Red")
        lblBMI.config(text=f"Your BMI: {bmi:.2f}. You are Obese")

    lblBMI.place(x=10, y=225)


# Weight
lblWeight = Label(text="Enter Your Weight(kg)", font=("Arial", 14), bg="Gainsboro", padx=10, pady=10)
lblWeight.pack()
entWeight = Entry(width=10, font=("Arial", 14))
entWeight.pack()

# Height
lblHeight = Label(text="Enter Your Height(cm)", font=("Arial", 14), bg="Gainsboro", padx=10, pady=10)
lblHeight.pack()
entHeight = Entry(width=10, font=("Arial", 14))
entHeight.pack()

# Calculate
btnCalculate = Button(text="Calculate", command=click)
btnCalculate.place(x=150, y=160)

window.mainloop()
