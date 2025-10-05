import tkinter as tk
from Formulario.FrmLogin import FrmLogin

def main():
    root = tk.Tk()
    app = FrmLogin(root)
    root.mainloop()

if __name__ == "__main__":
    main()
