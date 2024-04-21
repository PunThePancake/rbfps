import tkinter
import tkinter.messagebox
import customtkinter
import os
import json

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("rbfps v1.0")
        self.geometry(f"{650}x{580}")
        self.resizable(width=False, height=False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 0, 0), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="rbfps", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="check for unlock")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.unlocked_label = customtkinter.CTkLabel(self.sidebar_frame, text="", anchor="s")
        self.unlocked_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="appearance", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(5, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="ui scale", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="input target fps")
        self.entry.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nesw")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text="set fps", command=self.main_button_1_event, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=1, column=3, padx=(20, 20), pady=(20, 20), sticky="ns")

        # set default values
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        directory = os.path.expanduser(r'~\AppData\Local\Roblox\Versions')
        target_json = "ClientAppSettings.json"
        print("checking if .json file exists")

        self.unlocked_label.configure(text="checking...")

        try:
            for root, dirs, files in os.walk(directory):
                if target_json in files:
                    json_file_path = os.path.join(root, target_json)
                    with open(json_file_path, 'r') as f:
                        json_data = json.load(f)
                        fps_value = json_data.get('DFIntTaskSchedulerTargetFps')
                        if fps_value:
                            print(f"unlock found: {fps_value}")
                            self.unlocked_label.configure(text="✅ unlock found: " + fps_value + "fps")
                            self.title("rbfps v1.0 - enabled")
                            return fps_value
        except OSError as e:
            print(f"Error: {e}")

        print("unlock not found")
        self.unlocked_label.configure(text="❌ unlock not found")
        self.title("rbfps v1.0 - disabled")
        return None
    
    def main_button_1_event(self):
        fps_limit = self.entry.get()

        def find_folder_with_exe(directory, target_exe):
            try:
                for root, dirs, files in os.walk(directory):
                    if target_exe in files:
                        return root
            except OSError as e:
                print(f"Error: {e}")

        def create_client_settings(folder):
            client_settings_folder = os.path.join(folder, "ClientSettings")
            os.makedirs(client_settings_folder, exist_ok=True)
            json_data = {
                "DFIntTaskSchedulerTargetFps": fps_limit
            }
            json_file_path = os.path.join(client_settings_folder, "ClientAppSettings.json")
            try:
                with open(json_file_path, "w") as json_file:
                    json.dump(json_data, json_file, indent=4)
                print("ClientSettings folder and config file created successfully.")
            except Exception as e:
                print(f"Error creating JSON file: {e}")

        directory = os.path.expanduser(r'~\AppData\Local\Roblox\Versions')
        target_exe = "RobloxPlayerBeta.exe"

        folder = find_folder_with_exe(directory, target_exe)
        if folder:
            print(f"Folder containing 'RobloxPlayerBeta.exe' found: {folder}")
            create_client_settings(folder)
        else:
            print("No folder containing 'RobloxPlayerBeta.exe' found in the specified directory.")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
