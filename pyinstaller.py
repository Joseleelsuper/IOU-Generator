import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed',
    '--name=IOU_Generator',
    '--distpath=build/dist',
    '--workpath=build',
    '--specpath=.',
    '--add-data=src/ui;src/ui',
    '--add-data=src/pdf_generator.py;src',
    '--hidden-import=tkinter',
    '--hidden-import=tkcalendar',
    '--hidden-import=PIL',
    '--hidden-import=fpdf',
])