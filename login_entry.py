from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login Entry v.1.0. by @hiiwilliamss')
root.geometry("925x500+300+200")
root.configure(bg="#000435")
root.resizable(False, False)


def signin():
    username = user.get()
    password = code.get()

    if username == "admin" and password == "1234":
        screen = Toplevel(root)
        screen.title("Login Entry v.1.0. by @hiiwilliamss")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        Label(screen, text="Hello!", bg="#fff", font=("Calibri(body)", 50, "bold")).pack(expand=True)

        screen.mainloop()

    elif username != "admin" and password != "1234":
        messagebox.showerror("INVALID", "Incorrect Username or Password.")

    elif password != "1234":
        messagebox.showerror("INVALID", "Incorrect Password.")

    elif username != "admin":
        messagebox.showerror("INVALID", "Incorrect Username.")


img = PhotoImage(file="login.png")
label = Label(root, image=img, bg="#000435").place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign In", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
heading.place(x=100, y=5)


def on_enter():
    user.delete(0, "end")


def on_leave():
    name = user.get()
    if name == "":
        user.insert(0, "Username")


user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", lambda args: on_enter())
user.bind("<FocusOut>", lambda args: on_leave())

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


def on_enter2():
    code.delete(0, "end")


def on_leave2():
    name = code.get()
    if name == "":
        code.insert(0, "Username")


code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft Yahei UI Light", 11), show="*")
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", lambda args: on_enter2())
code.bind("<FocusOut>", lambda args: on_leave2())

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft Yahei UI Light", 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text="Sign up!", border=0, bg="white", cursor="hand2", fg="#57a1f8")
sign_up.place(x=215, y=270)

root.mainloop()