import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os

class FrmDashboard:
    def __init__(self, root, nombre, email, rol):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("900x500")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        
        top_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        top_frame.pack(fill="x")

        lbl_welcome = tk.Label(
            top_frame,
            text=f"Bienvenido, {nombre} ({rol})",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="white"
        )
        lbl_welcome.pack(side="left", padx=20)

      
        base_path = os.getcwd()

       
        logout_path = os.path.join(base_path, "logout.png")
        self.logout_img = ImageTk.PhotoImage(Image.open(logout_path).resize((32, 32), Image.Resampling.LANCZOS))
        btn_logout = tk.Button(
            top_frame,
            image=self.logout_img,
            bg="#2c3e50",
            relief="flat",
            command=self.logout
        )
        btn_logout.pack(side="right", padx=10)

      
        self.icons = {}
        for icon_name in ["website_icon.png", "linkedin_icon.png", "facebook_icon.png"]:
            path = os.path.join(base_path, icon_name)
            if os.path.exists(path):
                img = Image.open(path).resize((28, 28), Image.Resampling.LANCZOS)
                self.icons[icon_name] = ImageTk.PhotoImage(img)
            else:
                self.icons[icon_name] = None

        if self.icons["website_icon.png"]:
            btn_web = tk.Button(top_frame, image=self.icons["website_icon.png"], bg="#2c3e50", relief="flat")
            btn_web.pack(side="right", padx=5)
        if self.icons["linkedin_icon.png"]:
            btn_linkedin = tk.Button(top_frame, image=self.icons["linkedin_icon.png"], bg="#2c3e50", relief="flat")
            btn_linkedin.pack(side="right", padx=5)
        if self.icons["facebook_icon.png"]:
            btn_facebook = tk.Button(top_frame, image=self.icons["facebook_icon.png"], bg="#2c3e50", relief="flat")
            btn_facebook.pack(side="right", padx=5)

       
        content_frame = tk.Frame(self.root, bg="white")
        content_frame.pack(expand=True, fill="both")

        lbl_info = tk.Label(
            content_frame,
            text=f"Email: {email}",
            font=("Arial", 14),
            bg="white",
            fg="black"
        )
        lbl_info.pack(pady=20)

        lbl_msg = tk.Label(
            content_frame,
            text="Este es tu Dashboard ✅",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        lbl_msg.pack(pady=10)

      
        profile_path = os.path.join(base_path, "FrmDashboard (1).png")
        if os.path.exists(profile_path):
            profile_img = Image.open(profile_path).resize((120, 120), Image.Resampling.LANCZOS)
            self.profile_photo = ImageTk.PhotoImage(profile_img)
            lbl_profile = tk.Label(content_frame, image=self.profile_photo, bg="white")
            lbl_profile.pack(pady=15)
        else:
            lbl_profile = tk.Label(content_frame, text="(Imagen de perfil no encontrada)", font=("Arial", 12), bg="white", fg="gray")
            lbl_profile.pack(pady=15)
            
        lbl_panel = tk.Label(
            content_frame,
            text="Panel Administrativo",
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#34495e"
        )
        lbl_panel.pack(pady=10)

    def logout(self):
        """Cerrar sesión y volver al login"""
        self.root.destroy()
        from Formulario.FrmLogin import FrmLogin  
        login_root = tk.Tk()
        FrmLogin(login_root)
        login_root.mainloop()
