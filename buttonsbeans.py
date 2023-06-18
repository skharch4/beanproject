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

    def add_new_bean():
        window.destroy()
        prompt_add_new_bean(connection)

    def see_all_beans():
        window.destroy()
        prompt_see_all_beans(connection)

    def find_bean_by_name():
        window.destroy()
        prompt_find_bean_by_name(connection)

    def see_best_method():
        window.destroy()
        prompt_best_method(connection)

    def delete_bean():
        window.destroy()
        prompt_delete_bean(connection)

    def delete_all_beans():
        if messagebox.askyesno("Delete All Beans", "Are you sure you want to delete all beans?"):
            database.delete_all_beans(connection)
            messagebox.showinfo("Success", "All beans deleted successfully")
        else:
            messagebox.showinfo("Delete Cancelled", "Deletion of all beans cancelled")

    btn_add_new = tk.Button(window, text="Add a new bean", command=add_new_bean, bg=btn_color, fg="white")
    btn_add_new.pack(pady=5)

    btn_see_all = tk.Button(window, text="See all beans", command=see_all_beans, bg=btn_color, fg="white")
    btn_see_all.pack(pady=5)

    btn_find_bean = tk.Button(window, text="Find a bean by name", command=find_bean_by_name, bg=btn_color, fg="white")
    btn_find_bean.pack(pady=5)

    btn_best_method = tk.Button(window, text="See the best preparation method", command=see_best_method,
                                bg=btn_color, fg="white")
    btn_best_method.pack(pady=5)

    btn_delete_bean = tk.Button(window, text="Delete bean", command=delete_bean, bg=btn_color, fg="white")
    btn_delete_bean.pack(pady=5)

    btn_delete_all = tk.Button(window, text="Delete all beans", command=delete_all_beans,
                               bg=btn_color, fg="white")
    btn_delete_all.pack(pady=5)

    btn_exit = tk.Button(window, text="Exit", command=window.quit, bg=btn_color, fg="white")
    btn_exit.pack(pady=5)

    window.mainloop()
