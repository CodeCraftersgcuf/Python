import tkinter as tk
from tkinter import filedialog, messagebox

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")
        self.root.geometry("800x600")

        self.text = tk.Text(self.root, font=("Helvetica", 12))
        self.text.pack(expand=True, fill="both")

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Bold", command=self.make_text_bold)
        self.format_menu.add_command(label="Italic", command=self.make_text_italic)
        self.format_menu.add_command(label="Underline", command=self.make_text_underline)

    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.root.title("Untitled - Notepad")

    def open_file(self):
        file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "r") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", f.read())
            self.root.title(file)

    def save_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            with open(file, "w") as f:
                f.write(self.text.get("1.0", tk.END))
            self.root.title(file)
            messagebox.showinfo("Info", "File saved successfully!")

    def make_text_bold(self):
        current_tags = self.text.tag_names("sel.first")
        if "bold" in current_tags:
            self.text.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.text.tag_add("bold", "sel.first", "sel.last")
            self.text.tag_configure("bold", font=("Helvetica", 12, "bold"))

    def make_text_italic(self):
        current_tags = self.text.tag_names("sel.first")
        if "italic" in current_tags:
            self.text.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.text.tag_add("italic", "sel.first", "sel.last")
            self.text.tag_configure("italic", font=("Helvetica", 12, "italic"))

    def make_text_underline(self):
        current_tags = self.text.tag_names("sel.first")
        if "underline" in current_tags:
            self.text.tag_remove("underline", "sel.first", "sel.last")
        else:
            self.text.tag_add("underline", "sel.first", "sel.last")
            self.text.tag_configure("underline", font=("Helvetica", 12, "underline"))

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
