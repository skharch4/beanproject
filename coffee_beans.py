import tkinter as tk
from tkinter import messagebox
import sqlite3
import database

MENU_PROMPT = """-- Coffee Bean App --

Please choose one of those options:

1) Add a new bean
2) See all beans
3) Find a bean by name
4) See the best preparation method for a bean
5) Delete Bean
6)Update Bean
7) Exit

Your selection: """

def menu():
    connection = database.connect()
    database.create_tables(connection)

    window = tk.Tk()
    window.title("Coffee Bean App")
    window.geometry("400x300")

    bg_color = "#F5F5F5"
    label_color = "#333333"
    btn_color = "#4CAF50"

    window.configure(bg=bg_color)

    label_menu = tk.Label(window, text="Coffee Bean App", bg=bg_color, fg=label_color, font=("Arial", 16, "bold"))
    label_menu.pack(pady=10)

    def handle_selection(selection):
        if selection == "Add a new bean":
            prompt_add_new_bean(connection)
        elif selection == "See all beans":
            prompt_see_all_beans(connection)
        elif selection == "Find a bean by name":
            prompt_find_bean_by_name(connection)
        elif selection == "See the best preparation method":
            prompt_best_method(connection)
        elif selection == "Delete bean":
            prompt_delete_bean(connection)
        elif selection == "Edit bean":
            prompt_update_bean(connection)
        elif selection == "Exit":
            window.destroy()
        else:
            messagebox.showerror("Error", "Invalid selection")

    def on_selection(selection):
        handle_selection(selection)

    btn_add_new = tk.Button(window, text="Add a new bean", command=lambda: on_selection("Add a new bean"), bg=btn_color, fg="white")
    btn_add_new.pack(pady=5)

    btn_see_all = tk.Button(window, text="See all beans", command=lambda: on_selection("See all beans"), bg=btn_color, fg="white")
    btn_see_all.pack(pady=5)

    btn_find_bean = tk.Button(window, text="Find a bean by name", command=lambda: on_selection("Find a bean by name"), bg=btn_color, fg="white")
    btn_find_bean.pack(pady=5)

    btn_best_method = tk.Button(window, text="See the best preparation method", command=lambda: on_selection("See the best preparation method"), bg=btn_color, fg="white")
    btn_best_method.pack(pady=5)

    btn_delete_bean = tk.Button(window, text="Delete bean", command=lambda: on_selection("Delete bean"), bg=btn_color, fg="white")
    btn_delete_bean.pack(pady=5)

    btn_edit_bean = tk.Button(window, text="Edit bean", command=lambda: on_selection("Edit bean"), bg=btn_color, fg="white")
    btn_edit_bean.pack(pady=5)

    btn_exit = tk.Button(window, text="Exit", command=lambda: on_selection("Exit"), bg=btn_color, fg="white")
    btn_exit.pack(pady=5)

    window.mainloop()




def prompt_add_new_bean(connection):
    window = tk.Tk()
    window.title("Add New Bean")
    window.geometry("400x300")

    bg_color = "#F5F5F5"
    label_color = "#333333"
    btn_color = "#4CAF50"

    window.configure(bg=bg_color)

    label_title = tk.Label(window, text="Add New Bean", bg=bg_color, fg=label_color, font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    def on_submit():
        name = entry_name.get()
        method = entry_method.get()
        rating = int(entry_rating.get())

        database.add_bean(connection, name, method, rating)
        messagebox.showinfo("Success", "Bean added successfully")

        window.destroy()

    label_name = tk.Label(window, text="Name:", bg=bg_color, fg=label_color)
    label_name.pack()

    entry_name = tk.Entry(window)
    entry_name.pack()

    label_method = tk.Label(window, text="Method:", bg=bg_color, fg=label_color)
    label_method.pack()

    entry_method = tk.Entry(window)
    entry_method.pack()

    label_rating = tk.Label(window, text="Rating (1-100):", bg=bg_color, fg=label_color)
    label_rating.pack()

    entry_rating = tk.Entry(window)
    entry_rating.pack()

    btn_submit = tk.Button(window, text="Submit", command=on_submit, bg=btn_color, fg="white")
    btn_submit.pack(pady=10)
    btn_return = tk.Button(window, text="Return to Menu", command=window.destroy, bg=btn_color, fg="white")
    btn_return.pack(pady=10)

    window.mainloop()



def prompt_see_all_beans(connection): #Пишемо функцію щоб побачити всі зерна
    beans = database.get_all_beans(connection)

    window = tk.Tk()
    window.title("All Beans")
    window.geometry("400x300")

    bg_color = "#F5F5F5"
    label_color = "#333333"

    window.configure(bg=bg_color)

    label_title = tk.Label(window, text="All Beans", bg=bg_color, fg=label_color, font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    label_beans = tk.Label(window, text="Bean List:", bg=bg_color, fg=label_color)
    label_beans.pack()

    for bean in beans:
        label_bean = tk.Label(window, text=f" ID: {bean[0]}, Name: {bean[1]}, Method: {bean[2]}, Rating: {bean[3]}/100",
                              bg=bg_color, fg=label_color)
        label_bean.pack()
    btn_return = tk.Button(window, text="Return to Menu", command=window.destroy, bg=btn_color, fg="white")
    btn_return.pack(pady=10)

    window.mainloop()


def prompt_find_bean_by_name(connection): #Пишемо функцію для пошуку зерна по назві. Також робимо інтерфейс.
    window = tk.Tk()
    window.title("Find Bean by Name")
    window.geometry("400x300")

    bg_color = "#F5F5F5"
    label_color = "#333333"
    btn_color = "#4CAF50"

    window.configure(bg=bg_color)

    label_title = tk.Label(window, text="Find Bean by Name", bg=bg_color, fg=label_color,
                           font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    def on_submit(): #Тут отримаємо назву зерна
        name = entry_name.get()
        beans = database.get_beans_name(connection, name)

        results_window = tk.Toplevel(window)
        results_window.title("Search Results")
        results_window.geometry("400x300")

        results_window.configure(bg=bg_color)

        label_results = tk.Label(results_window, text="Search Results:", bg=bg_color, fg=label_color)
        label_results.pack()

        for bean in beans:
            label_bean = tk.Label(results_window, text=f"Name: {bean[1]}, Method: {bean[2]}, Rating: {bean[3]}/100",
                                  bg=bg_color, fg=label_color)
            label_bean.pack()

    label_name = tk.Label(window, text="Name:", bg=bg_color, fg=label_color)
    label_name.pack()

    entry_name = tk.Entry(window)
    entry_name.pack()

    btn_submit = tk.Button(window, text="Submit", command=on_submit, bg=btn_color, fg="white")
    btn_submit.pack(pady=10)
    btn_return = tk.Button(window, text="Return to Menu", command=window.destroy, bg=btn_color, fg="white")
    btn_return.pack(pady=10)

    window.mainloop()


def prompt_best_method(connection):
    window = tk.Tk()
    window.title("Best Preparation Method")
    window.geometry("400x300")

    bg_color = "#F5F5F5"
    label_color = "#333333"
    btn_color = "#4CAF50"

    window.configure(bg=bg_color)

    label_title = tk.Label(window, text="Best Preparation Method", bg=bg_color, fg=label_color,
                           font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    def on_submit():
        name = entry_name.get()
        best_method = database.get_best_preparation(connection, name)

        messagebox.showinfo("Best Preparation Method", f"The best preparation method for {name} is: {best_method[2]}")

        window.destroy()

    label_name = tk.Label(window, text="Name:", bg=bg_color, fg=label_color)
    label_name.pack()

    entry_name = tk.Entry(window)
    entry_name.pack()

    btn_submit = tk.Button(window, text="Submit", command=on_submit, bg=btn_color, fg="white")
    btn_submit.pack(pady=10)
    btn_return = tk.Button(window, text="Return to Menu", command=window.destroy, bg=btn_color, fg="white")
    btn_return.pack(pady=10)

    window.mainloop()
def prompt_update_bean(connection):
    window = tk.Tk()
    window.title("Update Bean")
    window.geometry("400x300")

    bg_color = "#F5F5F5"
    label_color = "#333333"
    btn_color = "#4CAF50"

    window.configure(bg=bg_color)

    label_title = tk.Label(window, text="Update Bean", bg=bg_color, fg=label_color, font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    def on_submit():
        bean_id = int(entry_id.get())
        name = entry_name.get()
        method = entry_method.get()
        rating = int(entry_rating.get())

        if database.update_bean(connection, bean_id, name, method, rating):
            messagebox.showinfo("Success", f"Bean with ID {bean_id} updated successfully")
        else:
            messagebox.showerror("Error", f"Failed to update bean with ID {bean_id}")

        window.destroy()

    label_id = tk.Label(window, text="Bean ID:", bg=bg_color, fg=label_color)
    label_id.pack()

    entry_id = tk.Entry(window)
    entry_id.pack()

    label_name = tk.Label(window, text="Name:", bg=bg_color, fg=label_color)
    label_name.pack()

    entry_name = tk.Entry(window)
    entry_name.pack()

    label_method = tk.Label(window, text="Method:", bg=bg_color, fg=label_color)
    label_method.pack()

    entry_method = tk.Entry(window)
    entry_method.pack()

    label_rating = tk.Label(window, text="Rating (1-100):", bg=bg_color, fg=label_color)
    label_rating.pack()

    entry_rating = tk.Entry(window)
    entry_rating.pack()

    btn_submit = tk.Button(window, text="Submit", command=on_submit, bg=btn_color, fg="white")
    btn_submit.pack(pady=10)
    btn_return = tk.Button(window, text="Return to Menu", command=window.destroy, bg=btn_color, fg="white")
    btn_return.pack(pady=10)

    window.mainloop()


def prompt_delete_bean(connection):
    window = tk.Tk()
    window.title("Delete Bean")
    window.geometry("400x300")

    bg_color = "#F5F5F5"
    label_color = "#333333"
    btn_color = "#4CAF50"

    window.configure(bg=bg_color)

    label_title = tk.Label(window, text="Delete Bean", bg=bg_color, fg=label_color, font=("Arial", 16, "bold"))
    label_title.pack(pady=10)

    def delete_single_bean():
        bean_id = int(entry_id.get())

        if database.delete_bean(connection, bean_id):
            messagebox.showinfo("Success", f"Bean with ID {bean_id} deleted successfully")
        else:
            messagebox.showinfo("Error", f"Failed to delete bean with ID {bean_id}")

        window.destroy()

    def delete_all_beans():
        if messagebox.askyesno("Delete All Beans", "Are you sure you want to delete all beans?"):
            database.delete_all_beans(connection)
            messagebox.showinfo("Success", "All beans deleted successfully")
        else:
            messagebox.showinfo("Delete Cancelled", "Deletion of all beans cancelled")

        window.destroy()

    label_id = tk.Label(window, text="Bean ID (Leave empty to delete all):", bg=bg_color, fg=label_color)
    label_id.pack()

    entry_id = tk.Entry(window)
    entry_id.pack()

    btn_delete_single = tk.Button(window, text="Delete Single Bean", command=delete_single_bean, bg=btn_color,
                                  fg="white")
    btn_delete_single.pack(pady=10)

    btn_delete_all = tk.Button(window, text="Delete All Beans", command=delete_all_beans, bg=btn_color,
                               fg="white")
    btn_delete_all.pack(pady=5)
    btn_return = tk.Button(window, text="Return to Menu", command=window.destroy, bg=btn_color, fg="white")
    btn_return.pack(pady=10)
    window.mainloop()





conn = sqlite3.connect("users.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
conn.commit()

#Функція для логіну
def login():
    username = entry_username.get()
    password = entry_password.get()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
  #Прописуємо цей код, щоби вікно з зернами відкривалося ТІЛЬКИ в разі вдалої авторизації
    if result:
        messagebox.showinfo("Login Successful", "Welcome, {}!".format(username))
        conn.close()
        window.destroy()
        menu()
        return True# Open the Coffee Bean App menu
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        return False

#Функція для регістрації
def register():
    username = entry_username.get()
    password = entry_password.get()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = c.fetchone()

    if result:
        messagebox.showerror("Registration Failed", "Username already exists")
    else: #Створюємо запис в БД
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully")

    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)


window = tk.Tk()
window.title("Login System")
window.geometry("400x200")


bg_color = "#F5F5F5"
label_color = "#333333"
btn_color = "#4CAF50"

window.configure(bg=bg_color)
#Пишемо інтерфейс для вікна авторизації
label_username = tk.Label(window, text="Username", bg=bg_color, fg=label_color)
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

label_password = tk.Label(window, text="Password", bg=bg_color, fg=label_color)
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

btn_login = tk.Button(window, text="Login", command=login, bg=btn_color, fg="white")
btn_login.pack()

btn_register = tk.Button(window, text="Register", command=register, bg=btn_color, fg="white")
btn_register.pack()

window.mainloop()


"""
if __name__ == "__main__":
    if login(True):
        menu()
"""