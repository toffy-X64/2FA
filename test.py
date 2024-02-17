import customtkinter as tk

root = tk.CTk()
root.geometry("400x240")
root.overrideredirect(True)

frame = tk.CTkFrame(master=root,
                               width=200,
                               height=200,
                               corner_radius=10,
                               fg_color="red")
frame.place(x=20, y=20)
root.mainloop()