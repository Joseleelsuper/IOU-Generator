"""
This module contains the main UI class for the application.
"""

import datetime
from tkinter import (
    OptionMenu,
    StringVar,
    Tk,
    Label,
    Entry,
    Frame,
    Toplevel,
    Button,
    filedialog,
    Canvas,
)
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
    def __init__(self, tamx: int = 1280, tamy: int = 680):
        """Initialize the UI class.

        Args:
            tamx (int, optional): Screen horizontally tam. Defaults to 860.
            tamy (int, optional): Screen vertically tam. Defaults to 680.
        """
        # Ventana principal.
        self.root = Tk()
        self.root.title("IOU Generator")
        self.root.geometry(f"{tamx}x{tamy}")

        # Creamos un frame contenedor principal usando grid
        self.main_frame = Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Ajustamos el grid para expandirse cuando se agrande la ventana
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        # Título y autor.
        self.label = Label( 
            self.main_frame, text="Pagaré Generator", font=(FONT, TAM_FONT_TITLE)
        )
        self.label.grid(
            row=0, column=1, columnspan=3, pady=PADDING_TITLES_Y, padx=PADDING_TITLES_X, sticky="n"
        )
        self.sub_label = Label(
            self.main_frame, text="by José Gallardo", font=(FONT, TAM_FONT)
        )
        self.sub_label.grid(
            row=1, column=1, columnspan=3, pady=PADDING_TITLES_Y, padx=PADDING_TITLES_X, sticky="n"
        )

        # Nombre del Prestamista
        self.lender_label = Label(
            self.main_frame, text="Prestamista:", font=(FONT, TAM_FONT)
        )
        self.lender_label.grid(
            row=2, column=0, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.lender_entry = Entry(self.main_frame, font=(FONT, TAM_FONT))
        self.lender_entry.grid(
            row=3, column=0, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )

        # Firma del Prestamista
        self.lender_sign_label = Label(
            self.main_frame, text="Firma del Prestamista:", font=(FONT, TAM_FONT)
        )
        self.lender_sign_label.grid(
            row=2, column=2, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.lender_sign_frame = Frame(self.main_frame)
        self.lender_sign_frame.grid(
            row=3, column=2, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )
        self.lender_sign_entry = Entry(self.lender_sign_frame, font=(FONT, TAM_FONT))
        self.lender_sign_entry.pack(side="left")
        self.browse_sign_button = Button(
            self.lender_sign_frame, text="...", command=self._select_signature_file
        )
        self.browse_sign_button.pack(side="left")
        self.draw_sign_button = Button(
            self.lender_sign_frame, text="✏️", command=self._open_paint
        )
        self.draw_sign_button.pack(side="left")

        # DNI del Prestamista
        self.lender_dni_label = Label(
            self.main_frame, text="DNI del Prestamista:", font=(FONT, TAM_FONT)
        )
        self.lender_dni_label.grid(
            row=2, column=4, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.lender_dni_entry = Entry(self.main_frame, font=(FONT, TAM_FONT))
        self.lender_dni_entry.grid(
            row=3, column=4, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )

        # Domicilio del Prestamista
        self.lender_address_entry = Label(
            self.main_frame, text="Domicilio del Prestamista:", font=(FONT, TAM_FONT)
        )
        self.lender_address_entry.grid(
            row=6, column=4, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.lender_address_entry = Entry(self.main_frame, font=(FONT, TAM_FONT))
        self.lender_address_entry.grid(
            row=7, column=4, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )

        # Nombre del Beneficiario
        self.debtor_label = Label(
            self.main_frame, text="Beneficiario:", font=(FONT, TAM_FONT)
        )
        self.debtor_label.grid(
            row=4, column=0, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.debtor_entry = Entry(self.main_frame, font=(FONT, TAM_FONT))
        self.debtor_entry.grid(
            row=5, column=0, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )

        # Firma del Beneficiario
        self.debtor_sign_label = Label(
            self.main_frame, text="Firma del Beneficiario:", font=(FONT, TAM_FONT)
        )
        self.debtor_sign_label.grid(
            row=4, column=2, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.debtor_sign_frame = Frame(self.main_frame)
        self.debtor_sign_frame.grid(
            row=5, column=2, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )
        self.debtor_sign_entry = Entry(self.debtor_sign_frame, font=(FONT, TAM_FONT))
        self.debtor_sign_entry.pack(side="left")
        self.browse_sign_button = Button(
            self.debtor_sign_frame, text="...", command=self._select_signature_file
        )
        self.browse_sign_button.pack(side="left")
        self.draw_sign_button = Button(
            self.debtor_sign_frame, text="✏️", command=self._open_paint
        )
        self.draw_sign_button.pack(side="left")


        # DNI del Beneficiario
        self.debtor_dni_label = Label(
            self.main_frame, text="DNI del Beneficiario:", font=(FONT, TAM_FONT)
        )
        self.debtor_dni_label.grid(
            row=4, column=4, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.debtor_dni_entry = Entry(self.main_frame, font=(FONT, TAM_FONT))
        self.debtor_dni_entry.grid(
            row=5, column=4, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )

        # Domicilio del Beneficiario
        self.debtor_address_label = Label(
            self.main_frame, text="Domicilio del Beneficiario:", font=(FONT, TAM_FONT)
        )
        self.debtor_address_label.grid(
            row=8, column=4, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.debtor_address_entry = Entry(self.main_frame, font=(FONT, TAM_FONT))
        self.debtor_address_entry.grid(
            row=9, column=4, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )

        # Cantidad de dinero prestada
        self.money_label = Label(
            self.main_frame,
            text="Cantidad prestada (Ej: 50.49):",
            font=(FONT, TAM_FONT),
        )
        self.money_label.grid(
            row=6, column=0, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.money_frame = Frame(self.main_frame)
        self.money_frame.grid(
            row=7, column=0, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )
        self.money_entry = Entry(self.money_frame, font=(FONT, TAM_FONT))
        self.money_entry.pack(side="left")
        self.euro_symbol_label = Label(
            self.money_frame, text="€", font=(FONT, TAM_FONT)
        )
        self.euro_symbol_label.pack(side="left")

        # Fecha de devolución máxima
        self.date_label = Label(
            self.main_frame,
            text="Fecha de devolución (Ej: 31/12/2024):",
            font=(FONT, TAM_FONT),
        )
        self.date_label.grid(
            row=8, column=0, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.date_frame = Frame(self.main_frame)
        self.date_frame.grid(
            row=9, column=0, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )
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
            self.main_frame,
            text="Interés por cada mes de retraso (Ej: 10%):",
            font=(FONT, TAM_FONT),
        )
        self.interest_label.grid(
            row=10, column=0, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.interest_frame = Frame(self.main_frame)
        self.interest_frame.grid(
            row=11, column=0, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )
        self.interest_entry = Entry(self.interest_frame, font=(FONT, TAM_FONT))
        self.interest_entry.pack(side="left")
        self.interest_entry.insert(0, "10%")
        self.euro_symbol_label = Label(
            self.interest_frame, text="/mes", font=(FONT, TAM_FONT)
        )
        self.euro_symbol_label.pack(side="left")

        # Ciudad
        self.city_label = Label(
            self.main_frame, text="Ciudad:", font=(FONT, TAM_FONT)
        )
        self.city_label.grid(
            row=8, column=2, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.city_entry = Entry(self.main_frame, font=(FONT, TAM_FONT))
        self.city_entry.grid(
            row=9, column=2, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )

        # Lugar de devolución
        self.place_label = Label(
            self.main_frame, text="Lugar de devolución:", font=(FONT, TAM_FONT)
        )
        self.place_label.grid(
            row=6, column=2, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="w"
        )
        self.place_frame = Frame(self.main_frame)
        self.place_frame.grid(
            row=7, column=2, padx=PADDING_X, pady=PADDING_ENTRYS_Y, sticky="w"
        )
        self.place_entry = Entry(self.place_frame, font=(FONT, TAM_FONT))
        self.place_entry.pack(side="left")
        self.place_options = ["Bizum"]
        self.place_entry.insert(0, self.place_options[0])
        self.place_var = StringVar(self.place_frame)
        self.place_var.set(self.place_options[0])
        self.place_dropdown = OptionMenu(
            self.place_frame, self.place_var, *self.place_options
        )
        self.place_dropdown.pack(side="left")

        # Botón para generar el pagaré en un PDF
        self.generate_button = Button(
            self.main_frame,
            text="Generar Pagaré",
            font=(FONT, TAM_FONT),
            command=self._generate_iou,
        )
        self.generate_button.grid(
            row=10, column=2, padx=PADDING_X, pady=PADDING_LABELS_Y, sticky="n"
        )

    def _generate_iou(self):
        """Generate the IOU PDF with the current form data."""
        from src.pdf_generator import IOUGenerator
        
        data = {
            'lender': self.lender_entry.get(),
            'lender_signature': self.lender_sign_entry.get(),
            'lender_dni': self.lender_dni_entry.get(),
            'lender_address': self.lender_address_entry.get(),
            'debtor': self.debtor_entry.get(),
            'debtor_signature': self.debtor_sign_entry.get(),
            'debtor_dni': self.debtor_dni_entry.get(),
            'debtor_address': self.debtor_address_entry.get(),
            'amount': self.money_entry.get(),
            'due_date': self.date_entry.get(),
            'interest': self.interest_entry.get(),
            'city': self.city_entry.get(),
            'payment_place': self.place_entry.get()
        }
        
        generator = IOUGenerator()
        pdf = generator.generate_iou(data)
        
        # Save the PDF
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Guardar Pagaré"
        )
        
        if file_path:
            pdf.output(file_path)

    def _open_calendar(self):
        """Open a calendar to select a date."""
        top = Toplevel(self.root)
        cal = Calendar(
            top,
            selectmode="day",
            date_pattern="dd/MM/yyyy",
            mindate=datetime.date.today() + datetime.timedelta(days=7),
        )
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
