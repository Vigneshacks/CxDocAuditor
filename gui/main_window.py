import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import traceback
import threading

from services.inventory_report import generate_inventory_report


class CxDocAuditorApp:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("CxDoc Auditor")

        self.root.geometry("750x280")

        self.root.resizable(False, False)

        self.root.configure(padx=20, pady=20)

        self.system_folder = tk.StringVar()

        self.output_folder = tk.StringVar(value="outputs")

        self.status = tk.StringVar(value="Ready")

        self.build_ui()

    # --------------------------------------------------

    def build_ui(self):

        # Root Folder

        tk.Label(self.root, text="System Folder").grid(row=0, column=0, sticky="w")

        tk.Entry(self.root, textvariable=self.system_folder, width=60).grid(
            row=1, column=0, padx=(0, 10)
        )

        tk.Button(self.root, text="Browse", command=self.select_system_folder).grid(
            row=1, column=1
        )

        # ------------------------------

        tk.Label(self.root, text="Output Folder").grid(
            row=2, column=0, pady=(20, 0), sticky="w"
        )

        tk.Entry(self.root, textvariable=self.output_folder, width=60).grid(
            row=3, column=0, padx=(0, 10)
        )

        tk.Button(self.root, text="Browse", command=self.select_output_folder).grid(
            row=3, column=1
        )

        # ------------------------------

        self.generate_button = tk.Button(
             
            self.root,
            text="Generate Report",
            width=25,
            command=self.start_report_generation
        )

        self.generate_button.grid(
             row=4,
            column=0,
            columnspan=2,
            pady=25
)

        # ------------------------------

        tk.Label(self.root, text="Status:").grid(row=5, column=0, sticky="w")

        tk.Label(self.root, textvariable=self.status).grid(row=6, column=0, sticky="w")

    # --------------------------------------------------

    def select_system_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.system_folder.set(folder)

    # --------------------------------------------------

    def select_output_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.output_folder.set(folder)

    # --------------------------------------------------
    # --------------------------------------------------
    def start_report_generation(self):

        if not self.system_folder.get():
            messagebox.showerror(
                "Missing Folder",
                "Please select a system folder."
            )
            return

        self.generate_button.config(state="disabled")
        self.status.set("Scanning folders...")

        worker = threading.Thread(
            target=self.generate_report,
            daemon=True
        )

        worker.start()

    # --------------------------------------------------
    def generate_report(self):

        self.root.after(
            0,
            lambda: self.status.set("Generating report...")
        )

        try:

            report = generate_inventory_report(
                Path(self.system_folder.get()),
                Path(self.output_folder.get()),
            )

            self.root.after(
                0,
                lambda: self.status.set("Report Generated Successfully")
            )

            self.root.after(
                0,
                lambda: messagebox.showinfo(
                    "Success",
                    f"Report created:\n\n{report}"
                )
            )

        except Exception as e:


            traceback.print_exc()
            error_message = f"{type(e).__name__}\n\n{e}"
            self.root.after(
        0,
        lambda: messagebox.showerror(
            "Error",
            error_message
        )
    )



    

    

        finally:

            self.root.after(
                0,
                lambda: self.generate_button.config(state="normal")
            )

def run():

    app = CxDocAuditorApp()

    app.root.mainloop()
