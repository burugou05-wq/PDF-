@echo off
python --version
if errorlevel 1 goto nopy
pip install pillow pyinstaller
pyinstaller --onefile --windowed --name ImageToPDF img2pdf_app.py
echo Done! EXE is in the dist folder.
goto end
:nopy
echo Python not found. Install from https://www.python.org/downloads/
:end
pause
