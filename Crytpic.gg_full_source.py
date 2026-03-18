import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os

ANTI_CHEAT_KEYWORDS = [
    b"FieldCheatDetector", b"ADetector'1", b"PersistentSingleton1", b"Entitlementcheck",
    b"AstreiodsGameManager", b"BanOnStart", b"CheckIfInUnity", b"DeleteData", b"ZzYyXx",
    b"QuestLink", b"HorrorAi", b"KSHRAnti", b"SaveManager", b"TeleportToBan", b"VersionChecker",
    b"KeyPadEnter", b"AppEntitlementCheck", b"SignatureCheck", b"ProtectedUIInt32",
    b"AsteroidSpawner", b"ProtectedInt16", b"Bullet", b"ProtectedVector4", b"ProtectedFloat",
    b"ProtectedQuaternionPref", b"ProtectedVector3Int", b"ProtectedVector2Pref",
    b"ProtectedString", b"Asteroid", b"CheatingDetectionStatus", b"AntiCheatMonitor",
    b"ProtectedUInt64", b"QuestSentailProtect", b"DllChecker", b"assembliesToCheck",
    b"AstreiodsGame", b"AntiCheatManager", b"DllSigmaThing", b"WallHackDetector",
    b"SpeedHackDetector", b"ModTool", b"GOOBEREER", b"GlitchMonke",
    b"IgottaremanethisitwasmadebyK_S_H_R", b"Kidsthesedays", b"veryfyyey", b"ApkChecker",
    b"Antimodders", b"Code.Stages.Anticheats", b"AppDeeplinkUI", b"ChangeCosmetic",
    b"coinsScripts", b"PublicZone", b"SampleUI", b"LoginHandle.IsClientLoggedIn",
    b"ConntrastStretch", b"CollisionSounds", b"Donut", b"WifiCheck", b"PlayerMovement01",
    b"HydrasPrivAntiCheat", b"imposter", b"AntiCheat", b"Funnymods", b"BloxianAnti",
    b"KokoAntiSkid", b"checkere", b"particallagreducer", b"timmyfixer", b"antidll",
    b"anti-dll", b"anti-hack", b"anti-cheat", b"anticheat", b"ModsFolderChecker",
    b"FolderVerifer", b"LemonFolderChecker", b"Melonloaderchecker", b"AntiCheats",
    b"Sgima", b"bustanut", b"coke", b"yummy", b"yummymelons", b"yummylemons",
    b"AntiModFolders", b"BadBilly", b"DisableOnEnable", b"QuitGame", b"DisableOnStart",
    b"AntiCheat2byXler", b"AntiCheatByXler", b"AntiModders", b"QuitOnCollision",
    b"DisableOnJoin", b"getBanReason", b"BanManager", b"SnowAntiRuntime",
    b"noscrippyforyou", b"UnitysAntiCheat", b"DestroyBOTrigger", b"PastebinLoader",
    b"byeeeeeeeeee", b"handscantbeextremelyfarapart", b"EnableObjectAfterDelay",
    b"PhotonTrigger", b"NetworkRig", b"NoLemonScript", b"BasilsAuth", b"sigma",
    b"GorillaQuitBox", b"spoopy", b"kick", b"DiscordWebhookTrigger", b"VoidGuard",
    b"SuspiciousBehaviourChecker", b"owner", b"DeviceCheck", b"LevelManager",
    b"GorillaManagerV2", b"AntiUABEA", b"FroggysAntiSkid", b"MeshEnable", b"tpiffail",
    b"chilloutitsjustagamelol", b"VentOpenPro", b"CumDoorButtonD", b"SigmaFPS",
    b"SharksAndMinnowsManager", b"BoxMove2", b"lnit", b"ResetToStart", b"FPSDisplayFR",
    b"FunMonkeyGONE", b"JumpScareN", b"SHRplayfabauth1", b"CheckSkuOwnership",
    b"SHRplayfabauth", b"objectsarecool", b"ownsmodcosmetics", b"AntiModder",
    b"KickIfBanned", b"QuestScript", b"kickp", b"rizz", b"DLLChecker",
    b"MeNoLoaderchecker", b"AntiKickTest", b"KickProtection", b"NoNameDetector",
    b"AIBooster", b"StoreMesh", b"hidemyshitsonofabitch", b"gameobj", b"gaymonster",
    b"moveon", b"NewBehaviourScript", b"CokesAnticheat", b"youcantgetwomenever",
    b"youbroketherules", b"IsCorrect", b"yabadabadooo", b"workrrr", b"WHYYYYY",
    b"WAAAAAA", b"Treeheehehe", b"byebye", b"byebyeee", b"rotatething", b"settingsyoo",
    b"thinghehe", b"treeman", b"heydonthaveeverything", b"whyareyoufrozen", b"nametag",
    b"Checkn", b"blablabla", b"EditorOnlyStuff", b"somethingtolurethem", b"NameDetector",
    b"ModFolderChecker", b"NoPublic", b"NoPublic125", b"sigcheck", b"Questlink",
    b"Modders", b"Modder", b"sigchecker", b"Signature Check", b"MelonLoader", b"uwumod",
    b"amongus", b"OculusByteCheck", b"HydrasBasicAntiCheat", b"ByteCheck",
    b"FieldCheatDetector", b"ADetector'1", b"PersistentSingleton1",
    b"Entitlementcheck", b"AstreiodsGameManager", b"BanOnStart",
    b"CheckIfInUnity", b"DeleteData", b"ZzYyXx", b"QuestLink",
    b"HorrorAi", b"KSHRAnti", b"SaveManager", b"TeleportToBan",
    b"VersionChecker", b"KeyPadEnter", b"AppEntitlementCheck",
    b"SignatureCheck", b"ProtectedUIInt32", b"AsteroidSpawner",
    b"ProtectedInt16", b"Bullet", b"ProtectedVector4", b"ProtectedFloat",
    b"ProtectedQuaternionPref", b"ProtectedVector3Int",
    b"ProtectedVector2Pref", b"ProtectedString", b"Asteroid",
    b"CheatingDetectionStatus", b"AntiCheatMonitor", b"ProtectedUInt64",
    b"QuestSentailProtect", b"DllChecker", b"assembliesToCheck",
    b"AstreiodsGame", b"AntiCheatManager", b"DllSigmaThing",
    b"WallHackDetector", b"SpeedHackDetector", b"ModTool", b"GOOBEREER",
    b"GlitchMonke", b"IgottaremanethisitwasmadebyK_S_H_R",
    b"Kidsthesedays", b"veryfyyey", b"ApkChecker", b"Antimodders",
    b"Code.Stages.Anticheats", b"AppDeeplinkUI", b"ChangeCosmetic",
    b"coinsScripts", b"PublicZone", b"SampleUI",
    b"LoginHandle.IsClientLoggedIn", b"ConntrastStretch",
    b"CollisionSounds", b"Donut", b"WifiCheck", b"PlayerMovement01",
    b"HydrasPrivAntiCheat", b"imposter", b"AntiCheat", b"Funnymods",
    b"BloxianAnti", b"KokoAntiSkid", b"checkere", b"particallagreducer",
    b"timmyfixer", b"antidll", b"anti-dll", b"anti-hack", b"anti-cheat",
    b"anticheat", b"ModsFolderChecker", b"FolderVerifer",
    b"LemonFolderChecker", b"Melonloaderchecker", b"AntiCheats",
    b"Sgima", b"bustanut", b"coke", b"yummy", b"yummymelons",
    b"yummylemons", b"AntiModFolders", b"BadBilly", b"DisableOnEnable",
    b"QuitGame", b"DisableOnStart", b"AntiCheat2byXler",
    b"AntiCheatByXler", b"AntiModders", b"QuitOnCollision",
    b"DisableOnJoin", b"getBanReason", b"BanManager",
    b"SnowAntiRuntime", b"noscrippyforyou", b"UnitysAntiCheat",
    b"DestroyBOTrigger", b"PastebinLoader", b"byeeeeeeeeee",
    b"handscantbeextremelyfarapart", b"EnableObjectAfterDelay",
    b"PhotonTrigger", b"NetworkRig", b"NoLemonScript", b"BasilsAuth",
    b"sigma", b"GorillaQuitBox", b"spoopy", b"kick",
    b"DiscordWebhookTrigger", b"VoidGuard", b"SuspiciousBehaviourChecker",
    b"owner", b"DeviceCheck", b"LevelManager", b"GorillaManagerV2",
    b"AntiUABEA", b"FroggysAntiSkid", b"MeshEnable", b"tpiffail",
    b"chilloutitsjustagamelol", b"VentOpenPro", b"CumDoorButtonD",
    b"SigmaFPS", b"SharksAndMinnowsManager", b"BoxMove2", b"lnit",
    b"ResetToStart", b"FPSDisplayFR", b"FunMonkeyGONE", b"JumpScareN",
    b"SHRplayfabauth1", b"CheckSkuOwnership", b"SHRplayfabauth",
    b"objectsarecool", b"ownsmodcosmetics", b"AntiModder",
    b"KickIfBanned", b"QuestScript", b"kickp", b"rizz", b"DLLChecker",
    b"MeNoLoaderchecker", b"AntiKickTest", b"KickProtection",
    b"NoNameDetector", b"AIBooster", b"StoreMesh",
    b"hidemyshitsonofabitch", b"gameobj", b"gaymonster", b"moveon",
    b"NewBehaviourScript", b"CokesAnticheat", b"youcantgetwomenever",
    b"youbroketherules", b"IsCorrect", b"yabadabadooo", b"workrrr",
    b"WHYYYYY", b"WAAAAAA", b"Treeheehehe", b"byebye", b"byebyeee",
    b"rotatething", b"settingsyoo", b"thinghehe", b"treeman",
    b"heydonthaveeverything", b"whyareyoufrozen", b"nametag",
    b"Checkn", b"blablabla", b"EditorOnlyStuff",
    b"somethingtolurethem", b"NameDetector", b"ModFolderChecker",
    b"NoPublic", b"NoPublic125", b"sigcheck", b"Questlink",
    b"Modders", b"Modder", b"sigchecker", b"Signature Check",
    b"MelonLoader", b"uwumod", b"amongus", b"OculusByteCheck",
    b"HydrasBasicAntiCheat", b"ByteCheck", b"BanOnStart", 
    b"AntiCheatMonitor", b"CheatingDetectionStatus", b"GOOBEREER"
]

# Color scheme
BG_PRIMARY = "#0f0618"
BG_SECONDARY = "#1a0f2e"
BG_TERTIARY = "#2d1b4e"
ACCENT_PRIMARY = "#d946ef"
ACCENT_SECONDARY = "#a855a8"
ACCENT_LIGHT = "#f0abfc"
TEXT_PRIMARY = "#d946ef"
TEXT_SECONDARY = "#a855a8"

filepath = None
modified_data = None
removal_log = []

# ===== DRAGGABLE WINDOW CLASS =====
class DraggableWindow(tk.Tk):
    """Tk window with borderless, transparent, and draggable features."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Borderless and transparent
        self.overrideredirect(True)
        self.attributes('-alpha', 0.95)
        
        # Dragging variables
        self.drag_data = {"x": 0, "y": 0}
        self.title_bar = None
        self.title_label = None
        
    def create_title_bar(self, title_text="Menu"):
        """Create a draggable title bar with close button."""
        self.title_bar = tk.Frame(self, bg=BG_SECONDARY, height=30)
        self.title_bar.pack(fill=tk.X, side=tk.TOP)
        self.title_bar.pack_propagate(False)
        
        # Title label
        self.title_label = tk.Label(
            self.title_bar, 
            text=title_text, 
            bg=BG_SECONDARY, 
            fg=ACCENT_PRIMARY, 
            font=("Courier New", 10, "bold")
        )
        self.title_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Close button
        close_btn = tk.Button(
            self.title_bar,
            text="✕",
            bg=BG_SECONDARY,
            fg=ACCENT_SECONDARY,
            font=("Arial", 12, "bold"),
            command=self.destroy,
            bd=0,
            padx=8,
            pady=2,
            activebackground=BG_SECONDARY,
            activeforeground=ACCENT_PRIMARY,
            highlightthickness=0,
            cursor="hand2"
        )
        close_btn.pack(side=tk.RIGHT, padx=5, pady=2)
        
        # Bind dragging to title bar and label
        self.title_bar.bind("<Button-1>", self._on_press)
        self.title_bar.bind("<B1-Motion>", self._on_drag)
        self.title_label.bind("<Button-1>", self._on_press)
        self.title_label.bind("<B1-Motion>", self._on_drag)
    
    def _on_press(self, event):
        """Record initial mouse position for dragging."""
        self.drag_data["x"] = event.x_root - self.winfo_x()
        self.drag_data["y"] = event.y_root - self.winfo_y()
    
    def _on_drag(self, event):
        """Move window as mouse moves."""
        x = event.x_root - self.drag_data["x"]
        y = event.y_root - self.drag_data["y"]
        self.geometry(f"+{x}+{y}")

# ===== FUNCTIONS =====
def load_file():
    global filepath, modified_data, removal_log
    path = filedialog.askopenfilename(filetypes=[("Unity3D Files", "*.unity3d")])
    if path:
        filepath = path
        modified_data = None
        removal_log = []
        status_label.config(text=f"✓ Loaded: {os.path.basename(path)}", fg=ACCENT_LIGHT)
        log_output.delete("1.0", tk.END)
        log_output.insert(tk.END, f"> File loaded: {os.path.basename(path)}\n")

def remove_antis():
    global modified_data, removal_log
    if not filepath or not os.path.exists(filepath):
        messagebox.showerror("Error", "No valid file loaded.")
        return

    def process():
        global modified_data, removal_log
        status_label.config(text="Processing...", fg=ACCENT_PRIMARY)
        log_output.delete("1.0", tk.END)
        log_output.insert(tk.END, "> Scanning file...\n")
        removal_log = []

        with open(filepath, "rb") as f:
            data = bytearray(f.read())

        total_removed = 0
        for keyword in ANTI_CHEAT_KEYWORDS:
            count = data.count(keyword)
            if count > 0:
                total_removed += count
                removal_log.append(f"{keyword.decode(errors='ignore')} (x{count})")
                while keyword in data:
                    idx = data.find(keyword)
                    data[idx:idx+len(keyword)] = b"\x00" * len(keyword)

        modified_data = bytes(data)
        status_label.config(text=f"✓ Complete! Removed {total_removed} instances", fg=ACCENT_LIGHT)
        
        log_output.delete("1.0", tk.END)
        log_output.insert(tk.END, f"> SCAN COMPLETE\n")
        log_output.insert(tk.END, f"> Total instances removed: {total_removed}\n")
        log_output.insert(tk.END, f"> Unique antis detected: {len(removal_log)}\n\n")
        log_output.insert(tk.END, "─" * 60 + "\n\n")
        
        if removal_log:
            for item in removal_log:
                log_output.insert(tk.END, f"  ◆ {item}\n")
        else:
            log_output.insert(tk.END, "  [No anticheat detected]\n")

    threading.Thread(target=process, daemon=True).start()

def save_file():
    if modified_data is None:
        messagebox.showerror("Error", "No antis removed yet. Run scan first.")
        return
    save_path = filedialog.asksaveasfilename(
        defaultextension=".unity3d",
        initialfile="data_clean.unity3d",
        filetypes=[("Unity3D Files", "*.unity3d")]
    )
    if save_path:
        with open(save_path, "wb") as f:
            f.write(modified_data)
        status_label.config(text=f"✓ Saved: {os.path.basename(save_path)}", fg=ACCENT_LIGHT)
        log_output.insert(tk.END, f"\n> Successfully saved to: {os.path.basename(save_path)}\n")

def view_logs():
    log_output.delete("1.0", tk.END)
    if not removal_log:
        log_output.insert(tk.END, "> No logs available\n> Load and scan a file first\n")
    else:
        log_output.insert(tk.END, f"> REMOVAL LOG ({len(removal_log)} items)\n")
        log_output.insert(tk.END, "─" * 60 + "\n\n")
        for item in removal_log:
            log_output.insert(tk.END, f"  ◆ {item}\n")

class HoverButton(tk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.default_bg = kwargs.get('bg', BG_TERTIARY)
        self.default_fg = kwargs.get('fg', ACCENT_PRIMARY)
        self.hover_bg = kwargs.get('activebackground', ACCENT_PRIMARY)
        self.hover_fg = kwargs.get('activeforeground', BG_PRIMARY)
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    
    def on_enter(self, event):
        self.config(bg=self.hover_bg, fg=self.hover_fg)
    
    def on_leave(self, event):
        self.config(bg=self.default_bg, fg=self.default_fg)

# ===== UI INITIALIZATION =====
root = DraggableWindow()
root.geometry("720x800+100+100")
root.configure(bg=BG_PRIMARY)
root.resizable(False, False)

# Create draggable title bar
root.create_title_bar("cryptic.gg - anti remover")

# Header
header_frame = tk.Frame(root, bg=BG_SECONDARY, height=70)
header_frame.pack(fill="x", padx=0, pady=0)
header_frame.pack_propagate(False)

# Decorative top bar
tk.Frame(root, bg=ACCENT_PRIMARY, height=3).pack(fill="x", side="top", before=header_frame)

# Title section
title = tk.Label(header_frame, text="RAYVO DECODED TS", fg=ACCENT_PRIMARY, bg=BG_SECONDARY,
                 font=("Courier New", 32, "bold"))
title.pack(pady=(15, 5))

subtitle = tk.Label(header_frame, text="anti remover", fg=ACCENT_SECONDARY, bg=BG_SECONDARY,
                    font=("Courier New", 10, "italic"))
subtitle.pack(pady=(0, 5))

version = tk.Label(header_frame, text="v1.0", fg=TEXT_SECONDARY, bg=BG_SECONDARY,
                   font=("Courier New", 8))
version.pack()

# Control Panel
control_frame = tk.Frame(root, bg=BG_PRIMARY)
control_frame.pack(fill="x", padx=25, pady=20)

btn_style = {
    "bg": BG_TERTIARY,
    "fg": ACCENT_PRIMARY,
    "font": ("Courier New", 10, "bold"),
    "relief": "flat",
    "bd": 0,
    "pady": 14,
    "cursor": "hand2",
    "activebackground": ACCENT_PRIMARY,
    "activeforeground": BG_PRIMARY,
    "highlightthickness": 0,
}

load_btn = HoverButton(control_frame, text="LOAD UNITY3D", command=load_file, **btn_style)
load_btn.pack(pady=8, fill="x")

scan_btn = HoverButton(control_frame, text="REMOVE ANTI", command=remove_antis, **btn_style)
scan_btn.pack(pady=8, fill="x")

save_btn = HoverButton(control_frame, text="SAVE FILE", command=save_file, **btn_style)
save_btn.pack(pady=8, fill="x")

log_btn = HoverButton(control_frame, text="VIEW LOGS", command=view_logs, **btn_style)
log_btn.pack(pady=8, fill="x")

# Status indicator
status_frame = tk.Frame(root, bg=BG_PRIMARY)
status_frame.pack(fill="x", padx=25, pady=(10, 15))

status_dot = tk.Label(status_frame, text="●", fg=TEXT_SECONDARY, bg=BG_PRIMARY, font=("Arial", 8))
status_dot.pack(side="left", padx=(0, 8))

status_label = tk.Label(status_frame, text="waiting for file...", fg=TEXT_SECONDARY, bg=BG_PRIMARY,
                        font=("Courier New", 9), justify="left")
status_label.pack(side="left", fill="x")

# Divider
tk.Frame(root, bg=BG_TERTIARY, height=1).pack(fill="x", padx=20)

# Output Log
log_frame = tk.Frame(root, bg=BG_PRIMARY)
log_frame.pack(padx=20, pady=15, fill="both", expand=True)

log_title = tk.Label(log_frame, text="[ output ]", fg=ACCENT_SECONDARY, bg=BG_PRIMARY,
                     font=("Courier New", 9, "bold"))
log_title.pack(anchor="w", pady=(0, 8))

# Log text with scrollbar
log_container = tk.Frame(log_frame, bg=BG_TERTIARY, highlightthickness=0)
log_container.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(log_container, bg=BG_TERTIARY, troughcolor=BG_PRIMARY, 
                         activebackground=ACCENT_PRIMARY, width=8)
scrollbar.pack(side="right", fill="y")

log_output = tk.Text(log_container, height=18, width=90, bg=BG_SECONDARY, fg=ACCENT_PRIMARY,
                     font=("Courier New", 8), relief="flat", bd=0, 
                     insertbackground=ACCENT_PRIMARY, insertwidth=1,
                     yscrollcommand=scrollbar.set, padx=12, pady=10)
log_output.pack(side="left", fill="both", expand=True)
scrollbar.config(command=log_output.yview)

# Footer
footer_frame = tk.Frame(root, bg=BG_SECONDARY, height=1)
footer_frame.pack(fill="x", side="bottom")

root.mainloop()