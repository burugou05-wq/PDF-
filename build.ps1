Write-Host "=== Image to PDF Converter - Build ===" -ForegroundColor Cyan

# Check Python
try { python --version | Out-Null } catch {
    Write-Host "ERROR: Python not found. Install from https://www.python.org/downloads/" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[1/3] Installing libraries..." -ForegroundColor Yellow
pip install pillow pyinstaller

Write-Host "[2/3] Building EXE..." -ForegroundColor Yellow
pyinstaller --onefile --windowed --name "ImageToPDF" img2pdf_app.py

Write-Host "[3/3] Done! Check dist\ImageToPDF.exe" -ForegroundColor Green
Read-Host "Press Enter to exit"
