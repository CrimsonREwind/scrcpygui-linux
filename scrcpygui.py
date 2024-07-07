import tkinter as tk
from tkinter import messagebox
import subprocess

class ScrcpyGUI:
    def __init__(self, root: tk.Tk):
        # Initialize main window
        self.root = root
        self.root.title("ScrcpyGUI")
        self.root.geometry("300x110")
        self.root.configure(bg="black")

        # Button frame
        self.button_frame = tk.Frame(root, bg="black")
        self.button_frame.pack(pady=10, expand=True)

        # Define custom colors
        self.button_bg = "black"
        self.button_fg = "white"
        self.button_active_bg = "#333333"  # Darker shade for hover
        self.button_active_fg = "white"

        # Start button
        self.start_button = tk.Button(
            self.button_frame,
            text="START SCRCPY",
            command=self.execute_command,
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground=self.button_active_bg,
            activeforeground=self.button_active_fg
        )
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Stop button
        self.stop_button = tk.Button(
            self.button_frame,
            text="STOP SCRCPY",
            command=self.stop_command,
            state=tk.DISABLED,
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground=self.button_active_bg,
            activeforeground=self.button_active_fg
        )
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Advanced options button
        self.advanced_button = tk.Button(
            root,
            text="Advanced Options",
            command=self.open_advanced_options,
            bg=self.button_bg,
            fg=self.button_fg,
            activebackground=self.button_active_bg,
            activeforeground=self.button_active_fg
        )
        self.advanced_button.pack(side=tk.BOTTOM, pady=10)

        # Initialize process and advanced window variables
        self.process = None
        self.advanced_window = None

        # Dictionaries for checkboxes and entries
        self.checkboxes = {}
        self.entries = {}

        # Default values for advanced options
        self.DEFAULT_VALUES = {
            "video-bit-rate": "8M",
            "max-fps": "60",
            "video-source": "camera",
            "camera-size": "1920x1080",
            "record": "filename",
        }

    def validate_entries(self) -> bool:
        """Validate the entries in the advanced options window."""
        try:
            for arg_name, entry in self.entries.items():
                if self.checkboxes[arg_name].get():
                    if arg_name in ["video-bit-rate"] and not entry.get():
                        raise ValueError(f"Invalid value for {arg_name.replace('-', ' ')}")
                    if arg_name in ["max-fps"] and not entry.get().isdigit():
                        raise ValueError(f"Invalid value for {arg_name.replace('-', ' ')}")
            return True
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return False

    def execute_command(self) -> None:
        """Execute the scrcpy command with the selected options."""
        if not self.validate_entries():
            return

        command = ["scrcpy"]
        for arg_name, checkbox_var in self.checkboxes.items():
            if checkbox_var.get():
                if arg_name == "no-audio":
                    command.append(f"--{arg_name}")
                else:
                    value = self.entries[arg_name].get()
                    if arg_name == "record":
                        value += ".mp4"
                    command.append(f"--{arg_name}={value}")

        try:
            self.process = subprocess.Popen(command)
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("Execution Error", str(e))

    def stop_command(self) -> None:
        """Terminate the running scrcpy process."""
        if self.process:
            self.process.terminate()
            self.process = None
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def open_advanced_options(self):
        """Open the advanced options window."""
        if self.advanced_window:
            self.advanced_window.deiconify()
            return

        self.advanced_window = tk.Toplevel(self.root)
        self.advanced_window.title("Advanced Options")
        self.advanced_window.geometry("320x210")  # Adjusted height for new option
        self.advanced_window.configure(bg="black")
        self.advanced_window.protocol("WM_DELETE_WINDOW", self.advanced_window.withdraw)

        options = [
            {"label": "BitRate", "arg_name": "video-bit-rate"},
            {"label": "MAX FPS", "arg_name": "max-fps"},
            {"label": "CAMERA ONLY", "arg_name": "video-source"},
            {"label": "CAMERA SIZE", "arg_name": "camera-size"},
            {"label": "RECORD", "arg_name": "record"},
            {"label": "NO AUDIO", "arg_name": "no-audio"}, # New option
        ]

        for row, option in enumerate(options):
            checkbox_var = tk.IntVar(value=0)
            checkbox = tk.Checkbutton(
                self.advanced_window,
                text=option["label"],
                variable=checkbox_var,
                bg="black",
                fg="white",
                selectcolor="black",
                bd=0,
                highlightthickness=0,
                relief="flat",
                activebackground="black",
                activeforeground="white",
                command=lambda var=checkbox_var, arg_name=option["arg_name"]: self.toggle_entry(var, arg_name)
            )
            checkbox.grid(row=row, column=0, sticky="w", padx=5, pady=5)

            if option["arg_name"] == "no-audio":
                entry = None  # No entry needed for --no-audio
            else:
                entry = tk.Entry(
                    self.advanced_window,
                    bg="black",
                    fg="white",
                    insertbackground="grey",
                    state=tk.NORMAL
                )
                entry.grid(row=row, column=1, padx=5, pady=5)
                entry.insert(0, self.DEFAULT_VALUES.get(option["arg_name"], ""))

            self.checkboxes[option["arg_name"]] = checkbox_var
            if entry:
                self.entries[option["arg_name"]] = entry

    def toggle_entry(self, var, arg_name):
        """Enable or disable the entry based on the checkbox state."""
        if arg_name == "no-audio":
            return  # No need to toggle entry for --no-audio

        if var.get():
            self.entries[arg_name].config(state=tk.NORMAL)
        else:
            self.entries[arg_name].config(state=tk.DISABLED)
            self.entries[arg_name].delete(0, tk.END)
            self.entries[arg_name].insert(0, self.DEFAULT_VALUES[arg_name])

if __name__ == "__main__":
    root = tk.Tk()
    gui = ScrcpyGUI(root)
    root.mainloop()
