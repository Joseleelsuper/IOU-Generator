"""
This module contains the main UI class for the application.
"""

from tkinter import Tk, Label, Entry, Frame, Toplevel, Button, filedialog, Canvas
from tkcalendar import Calendar
from datetime import date, timedelta

PADDING_TITLES_Y = 1
PADDING_TITLES_Y = 1
PADDING_TITLES_X = 10
PADDING_LABELS_Y = (20, 5)
PADDING_ENTRYS_Y = (0, 20)
PADDING_X = 40

FONT = "Helvetica"
TAM_FONT_TITLE = 32
TAM_FONT = 16


class UI:
    def __init__(self, tamx: int = 1280, tamy: int = 720):
        """Initialize the UI class.

        Args:
            tamx (int, optional): Screen horizontally tam. Defaults to 1280.
            tamy (int, optional): Screen vertically tam. Defaults to 720.
        """
        # Ventana principal.
        self.root = Tk()
        self.root.title("IOU Generator")
        self.root.geometry(f"{tamx}x{tamy}")

        # Título y autor.
        self.label = Label(
            self.root, text="Pagaré Generator", font=(FONT, TAM_FONT_TITLE)
        )
        self.label.pack(pady=PADDING_TITLES_Y, padx=PADDING_TITLES_X)
        self.sub_label = Label(
            self.root, text="by José Gallardo", font=(FONT, TAM_FONT)
        )
        self.sub_label.pack(pady=PADDING_TITLES_Y, padx=PADDING_TITLES_X)

        # Nombre del Prestamista
        self.lender_label = Label(self.root, text="Prestamista:", font=(FONT, TAM_FONT))
        self.lender_label.pack(anchor="w", pady=PADDING_LABELS_Y, padx=PADDING_X)
        self.lender_entry = Entry(self.root, font=(FONT, TAM_FONT))
        self.lender_entry.pack(anchor="w", pady=PADDING_ENTRYS_Y, padx=PADDING_X)

        # Nombre del Beneficiario
        self.debtor_label = Label(
            self.root, text="Beneficiario:", font=(FONT, TAM_FONT)
        )
        self.debtor_label.pack(anchor="w", pady=PADDING_LABELS_Y, padx=PADDING_X)
        self.debtor_entry = Entry(self.root, font=(FONT, TAM_FONT))
        self.debtor_entry.pack(anchor="w", pady=PADDING_ENTRYS_Y, padx=PADDING_X)

        # Cantidad de dinero prestada
        self.money_label = Label(
            self.root, text="Cantidad prestada (Ej: 50.49):", font=(FONT, TAM_FONT)
        )
        self.money_label.pack(anchor="w", pady=PADDING_LABELS_Y, padx=PADDING_X)
        self.money_frame = Frame(self.root)
        self.money_frame.pack(anchor="w", pady=PADDING_ENTRYS_Y, padx=PADDING_X)
        self.money_entry = Entry(self.money_frame, font=(FONT, TAM_FONT))
        self.money_entry.pack(side="left")
        self.euro_symbol_label = Label(
            self.money_frame, text="€", font=(FONT, TAM_FONT)
        )
        self.euro_symbol_label.pack(side="left")

        # Fecha de devolución máxima
        self.date_label = Label(
            self.root,
            text="Fecha de devolución (Ej: 31/12/2024):",
            font=(FONT, TAM_FONT),
        )
        self.date_label.pack(anchor="w", pady=PADDING_LABELS_Y, padx=PADDING_X)
        self.date_frame = Frame(self.root)
        self.date_frame.pack(anchor="w", pady=PADDING_ENTRYS_Y, padx=PADDING_X)
        self.date_entry = Entry(self.date_frame, font=(FONT, TAM_FONT))
        self.date_entry.insert(
            0, (date.today() + timedelta(days=30)).strftime("%d/%m/%Y")
        )
        self.date_entry.pack(side="left")
        self.date_button = Button(
            self.date_frame, text="📅", command=self._open_calendar
        )
        self.date_button.pack(side="left")

        # Aumento de cantidad a devolver si no paga a tiempo
        self.interest_label = Label(
            self.root,
            text="Interés por cada mes de retraso (Ej: 10%):",
            font=(FONT, TAM_FONT),
        )
        self.interest_label.pack(anchor="w", pady=PADDING_LABELS_Y, padx=PADDING_X)
        self.interest_frame = Frame(self.root)
        self.interest_frame.pack(anchor="w", pady=PADDING_ENTRYS_Y, padx=PADDING_X)
        self.interest_entry = Entry(self.interest_frame, font=(FONT, TAM_FONT))
        self.interest_entry.pack(side="left")
        self.interest_entry.insert(0, "10%")
        self.euro_symbol_label = Label(
            self.interest_frame, text="/mes", font=(FONT, TAM_FONT)
        )
        self.euro_symbol_label.pack(side="left")

        # Firma del Prestamista.
        self.lender_sign_label = Label(self.root, text="Firma del Prestamista:", font=(FONT, TAM_FONT))
        self.lender_sign_label.place(x=tamx//2 + PADDING_X, y=150)  # Adjust y value as needed
        self.lender_sign_frame = Frame(self.root)
        self.lender_sign_frame.place(x=tamx//2 + PADDING_X, y=180)  # Adjust y value as needed
        self.lender_sign_entry = Entry(self.lender_sign_frame, font=(FONT, TAM_FONT))
        self.lender_sign_entry.pack(side="left")
        self.browse_sign_button = Button(self.lender_sign_frame, text="...", command=self._select_signature_file)
        self.browse_sign_button.pack(side="left")
        self.draw_sign_button = Button(self.lender_sign_frame, text="✏️", command=self._open_paint)
        self.draw_sign_button.pack(side="left")

        # Firma del Beneficiario.
        self.debtor_sign_label = Label(self.root, text="Firma del Beneficiario:", font=(FONT, TAM_FONT))
        self.debtor_sign_label.place(x=tamx//2 + PADDING_X, y=300)  # Adjust y value as needed
        self.debtor_sign_frame = Frame(self.root)
        self.debtor_sign_frame.place(x=tamx//2 + PADDING_X, y=330)  # Adjust y value as needed
        self.debtor_sign_entry = Entry(self.debtor_sign_frame, font=(FONT, TAM_FONT))
        self.debtor_sign_entry.pack(side="left")
        self.browse_sign_button = Button(self.debtor_sign_frame, text="...", command=self._select_signature_file)
        self.browse_sign_button.pack(side="left")
        self.draw_sign_button = Button(self.debtor_sign_frame, text="✏️", command=self._open_paint)
        self.draw_sign_button.pack(side="left")

        # Lugar de devolución
        self.place_label = Label(
            self.root, text="Lugar de devolución:", font=(FONT, TAM_FONT)
        )
        self.place_label.pack(anchor="w", pady=PADDING_LABELS_Y, padx=PADDING_X)
        self.place_entry = Entry(self.root, font=(FONT, TAM_FONT))
        self.place_entry.pack(anchor="w", pady=PADDING_ENTRYS_Y, padx=PADDING_X)

    def _open_calendar(self):
        """Open a calendar to select a date."""
        top = Toplevel(self.root)
        cal = Calendar(top, selectmode="day", date_pattern="dd/MM/yyyy")
        cal.pack(padx=10, pady=10)

        def confirm_date():
            self.date_entry.delete(0, "end")
            self.date_entry.insert(0, cal.get_date())
            top.destroy()

        Button(top, text="Ok", command=confirm_date).pack(pady=5)

    def _select_signature_file(self):
        """Open a file dialog to select a signature file."""
        file_path = filedialog.askopenfilename()
        self.lender_sign_entry.delete(0, "end")
        self.lender_sign_entry.insert(0, file_path)

    def _open_paint(self):
        """Open a mini-paint to draw a signature."""
        top = Toplevel(self.root)
        top.title("Mini-Paint")
        canvas = Canvas(top, bg="white", width=300, height=100)
        canvas.pack()

        def paint(event):
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)

        canvas.bind("<B1-Motion>", paint)

        def confirm_sign():
            canvas.postscript(file="./signatures/signature_prest.eps")
            self.lender_sign_entry.delete(0, "end")
            self.lender_sign_entry.insert(0, "signature.eps")
            top.destroy()

        Button(top, text="Ok", command=confirm_sign).pack(pady=5)

    def run(self):
        """Start the main application loop."""
        self.root.mainloop()
