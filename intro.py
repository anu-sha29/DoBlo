import tkinter as tk
from PIL import Image, ImageTk

class AppStartWindow(tk.Tk):
    def __init__(self, icon_path):
        super().__init__()
        self.title("App Starting...")
        self.geometry("400x400")
        self.configure(bg="white")  # White background

        # Load and resize icon
        self.original_icon = Image.open("C:\Users\ANANNYA I\OneDrive\Desktop\doblo\icon.jpeg").resize((200, 200))
        self.icon_label = tk.Label(self, bg="white")
        self.icon_label.pack(expand=True)

        # Animation variables
        self.alpha = 0
        self.fade_in()

    def fade_in(self):
        if self.alpha <= 255:
            # Apply transparency
            icon_with_alpha = self.original_icon.copy()
            icon_with_alpha.putalpha(self.alpha)
            tk_icon = ImageTk.PhotoImage(icon_with_alpha)

            self.icon_label.config(image=tk_icon)
            self.icon_label.image = tk_icon

            self.alpha += 15  # Increase transparency step
            self.after(100, self.fade_in)  # Repeat every 100ms
        else:
            # After animation completes, proceed to main app
            self.after(1000, self.open_main_app)

    def open_main_app(self):
        self.destroy()
        main_app = tk.Tk()
        main_app.title("Main App Window")
        main_app.geometry("600x400")
        main_app.configure(bg="white")  # White background for main window too
        tk.Label(main_app, text="Welcome to the App!", font=("Arial", 20), bg="white").pack(expand=True)
        main_app.mainloop()

if __name__ == "__main__":
    # Replace with your uploaded icon file path
    AppStartWindow("C:\Users\ANANNYA I\OneDrive\Desktop\doblo\icon.jpeg").mainloop()