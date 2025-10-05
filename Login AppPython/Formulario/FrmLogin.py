import tkinter as tk
from tkinter import messagebox
from Clases.Usuarios import Usuario
from Clases.Conector import Conector
from Formulario.FrmDashboard import FrmDashboard
from PIL import ImageTk, Image  
import os 

class FrmLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login de Usuario")
        self.root.geometry("900x500") 
        self.root.resizable(False, False)
        self.root.configure(bg="white")  

       
        main_frame = tk.Frame(root, bg="white")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

       
        left_frame = tk.Frame(main_frame, width=300, height=450, bg="#f0f0f0", relief="solid", bd=1)
        left_frame.pack(side="left", fill="both", expand=False, padx=(0, 20))
        left_frame.pack_propagate(False) 
        
        main_img_path = "LoginImage (1).png"
        try:
            if os.path.exists(main_img_path):
                print(f"Cargando imagen principal: {main_img_path}")
                main_img = Image.open(main_img_path)
                main_img = main_img.resize((250, 250), Image.Resampling.LANCZOS)  
                self.main_photo = ImageTk.PhotoImage(main_img)
                img_label = tk.Label(left_frame, image=self.main_photo, bg="#f0f0f0")
                img_label.pack(expand=True)  
                print("Imagen principal cargada exitosamente.")
            else:
                print(f"Advertencia: Imagen principal '{main_img_path}' no encontrada. Usando fondo gris.")
               
                fallback_label = tk.Label(left_frame, text="Login Image\n(No disponible)", font=("Arial", 12), bg="#f0f0f0")
                fallback_label.pack(expand=True)
        except Exception as e:
            print(f"Error al cargar la imagen principal '{main_img_path}': {e}. Usando fallback.")
            fallback_label = tk.Label(left_frame, text="Login Image\n(Error de carga)", font=("Arial", 12), bg="#f0f0f0")
            fallback_label.pack(expand=True)

       
        right_frame = tk.Frame(main_frame, width=300, height=450, bg="white", relief="solid", bd=1)
        right_frame.pack(side="right", fill="both", expand=True)
        right_frame.pack_propagate(False) 

       
        titulo = tk.Label(right_frame, text="Inicio de Sesión", font=("Arial", 20, "bold"), bg="white")
        titulo.pack(pady=20)

       
        user_logo_path = "user_logo.png"  
        try:
            if os.path.exists(user_logo_path):
                print(f"Cargando logo de usuario: {user_logo_path}")
                user_logo = Image.open(user_logo_path)
                user_logo = user_logo.resize((60, 60), Image.Resampling.LANCZOS) 
                self.user_photo = ImageTk.PhotoImage(user_logo)
                user_logo_label = tk.Label(right_frame, image=self.user_photo, bg="white")
                user_logo_label.pack(pady=5)
                print("Logo de usuario cargado exitosamente.")
            else:
                print(f"Advertencia: Logo de usuario '{user_logo_path}' no encontrado. Omitiendo logo.")
                
        except Exception as e:
            print(f"Error al cargar el logo de usuario '{user_logo_path}': {e}. Omitiendo logo.")

       
        form_frame = tk.Frame(right_frame, bg="white")
        form_frame.pack(pady=30)

       
        lbl_user = tk.Label(form_frame, text="Usuario:", font=("Arial", 14), bg="white")
        lbl_user.grid(row=0, column=0, padx=10, pady=15, sticky="e")

        self.txt_user = tk.Entry(form_frame, font=("Arial", 14), width=20, relief="solid", bd=1)
        self.txt_user.grid(row=0, column=1, padx=10, pady=15)

       
        lbl_pass = tk.Label(form_frame, text="Contraseña:", font=("Arial", 14), bg="white")
        lbl_pass.grid(row=1, column=0, padx=10, pady=15, sticky="e")

        self.txt_pass = tk.Entry(form_frame, font=("Arial", 14), width=20, show="*", relief="solid", bd=1)
        self.txt_pass.grid(row=1, column=1, padx=10, pady=15)

        
        buttons_frame = tk.Frame(right_frame, bg="white")
        buttons_frame.pack(pady=30)

        btn_login = tk.Button(buttons_frame, text="Ingresar", font=("Arial", 14), width=15, height=2, 
                              bg="#4CAF50", fg="white", relief="raised", bd=2, command=self.login)
        btn_login.pack(pady=10)

        btn_cancel = tk.Button(buttons_frame, text="Cancelar", font=("Arial", 14), width=15, height=2, 
                               bg="#f44336", fg="white", relief="raised", bd=2, command=root.quit)
        btn_cancel.pack(pady=5)

    def login(self):
        usuario_input = self.txt_user.get()
        clave_input = self.txt_pass.get()

        if not usuario_input or not clave_input:
            messagebox.showerror("Error", "Ingrese usuario y contraseña")
            return

        con = Conector()
        
        sql = "SELECT id, Nombre, Apellido, Email, Username, Clave, Rol FROM usuarios WHERE Username=%s AND Clave=%s"
        values = (usuario_input, clave_input)
        resultado = con.select(sql, values)

        if resultado and len(resultado) > 0:
            row = resultado[0]
            user_from_db = Usuario(row[1], row[2], row[3], row[4], row[5], row[6]) 
            
            if user_from_db.ValidarUsuario(usuario_input, clave_input):
                nombre_completo = f"{row[1]} {row[2]}"
                email = row[3]
                rol = row[6]
                
                
                self.root.destroy()
                dashboard_root = tk.Tk()
                FrmDashboard(dashboard_root, nombre_completo, email, rol)
                dashboard_root.mainloop()
            else:
                messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos ❌")
        else:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos ❌")
