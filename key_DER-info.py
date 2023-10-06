import tkinter as tk
from tkinter import filedialog
from Crypto.PublicKey import RSA

def load_and_display_key_info():
    file_path = filedialog.askopenfilename(title="Select a DER key file")
    if file_path:
        try:
            with open(file_path, 'rb') as f:
                der_key_data = f.read()
                rsa_key = RSA.importKey(der_key_data)

                key_info = f"Modulus (N): {rsa_key.n}\n"
                key_info += f"Public Exponent (e): {rsa_key.e}\n"
                key_info += f"Private Exponent (D): {rsa_key.d}\n"
                key_info += f"Prime Factor 1 (P): {rsa_key.p}\n"
                key_info += f"Prime Factor 2 (Q): {rsa_key.q}\n"
                key_info += f"Exponent 1 (D mod P-1): {rsa_key.d % (rsa_key.p - 1)}\n"
                key_info += f"Exponent 2 (D mod Q-1): {rsa_key.d % (rsa_key.q - 1)}\n"
                key_info += f"Coefficient (Q^-1 mod P): {rsa_key.u}\n"

                key_info_text.delete(1.0, tk.END)  
                key_info_text.insert(tk.END, key_info)
        except Exception as e:
            key_info_text.delete(1.0, tk.END)  
            key_info_text.insert(tk.END, f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("DER Key Info by Dragon-Noir")

frame = tk.Frame(root)
frame.pack(pady=20)

file_button = tk.Button(frame, text="Open DER Key File", command=load_and_display_key_info)
file_button.pack()

key_info_text = tk.Text(frame, height=10, width=50)
key_info_text.pack()

root.mainloop()
