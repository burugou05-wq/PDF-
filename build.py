import subprocess, sys, pathlib

HERE = pathlib.Path(__file__).parent.resolve()
APP      = HERE / "img2pdf_app.py"
MANIFEST = HERE / "dpi_aware.manifest"
DIST     = HERE / "dist"

print("=" * 52)
print("  画像→PDF 変換ツール  v1.0  -  Build Tool")
print("=" * 52)

print("\n[1/3] Installing libraries ...")
subprocess.check_call([sys.executable, "-m", "pip", "install",
    "pillow", "pillow-avif-plugin", "pillow-heif",
    "img2pdf",
    "pyturbojpeg", "numpy",
    "tkinterdnd2",
    "pyinstaller", "--quiet"])

print("\n[2/3] Building EXE ...")
hidden = [
    "pillow_avif",
    "pillow_heif",
    "img2pdf",
    "turbojpeg",
    "numpy",
    "tkinterdnd2",
    "PIL._tkinter_finder",
    "tkinter",
    "tkinter.ttk",
    "tkinter.filedialog",
    "tkinter.messagebox",
    "tkinter.font",
    "ctypes",
    "ctypes.wintypes",
    "urllib.request",
    "threading",
    "json",
    "shutil",
    "io",
    "tempfile",
    "re",
]
hi_args = []
for h in hidden:
    hi_args += ["--hidden-import", h]

ICON = HERE / "app_icon.ico"
icon_args = ["--icon", str(ICON)] if ICON.exists() else []

# dpi_aware.manifest を EXE に埋め込む（--manifest オプション）
# これにより Windows が EXE 起動時に Per-Monitor V2 DPI 対応と認識し、
# 自動ビットマップ拡大（ぼやけの原因）を抑制する
manifest_args = ["--manifest", str(MANIFEST)] if MANIFEST.exists() else []
if not MANIFEST.exists():
    print("  [!] dpi_aware.manifest が見つかりません。DPI設定なしでビルドします。")

subprocess.check_call([
    sys.executable, "-m", "PyInstaller",
    "--onefile", "--windowed",
    "--name", "画像PDF変換ツール",
    "--distpath", str(DIST),
    "--workpath", str(HERE / "build_tmp"),
    "--specpath", str(HERE),
    *icon_args,
    *manifest_args,
    *hi_args,
    str(APP)
])

exe = DIST / "画像PDF変換ツール.exe"
if exe.exists():
    print("\n[3/3] SUCCESS!")
    print(f"\n  >>> EXE: {exe}\n")
else:
    print("\n[!] EXE not found. Check errors above.")

input("\nPress Enter to close ...")
