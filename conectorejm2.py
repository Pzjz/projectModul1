from tkinter import*
from conectorejmVenta import Ventana

def main():
    root = Tk()
    root.wm_title("Gestor hospitalario CEFIT")
    root.iconbitmap("iconOne.ico")
    app = Ventana(root)
    app.mainloop()

if __name__ == "__main__":
    main()