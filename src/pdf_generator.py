from fpdf import FPDF
from datetime import datetime
import locale

class IOUGenerator:
    def __init__(self):
        self.pdf = FPDF()
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

    def _format_date(self, date_str):
        """Convert date string to formatted Spanish date."""
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        return date_obj.strftime("%d de %B de %Y")

    def generate_iou(self, data):
        """Generate the IOU PDF with the provided data."""
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Helvetica", "", 12)
        
        # Title
        self.pdf.set_font("Helvetica", "B", 16)
        self.pdf.cell(0, 10, "PAGARÉ", 0, 1, "C")
        self.pdf.ln(10)
        
        # Header with date and location
        self.pdf.set_font("Helvetica", "", 12)
        location = data.get('city', 'NO ESPECIFICADO')
        today = datetime.now().strftime("%d/%m/%Y")
        self.pdf.cell(0, 10, f"En **{location}**, a {self._format_date(today)}.", 0, 1)
        self.pdf.ln(10)

        # Main text
        amount = str(data.get('amount', 0))
        
        main_text = (
            f"Yo, **{data.get('debtor', 'NO ESPECIFICADO')}**, con domicilio en "
            f"**{data.get('debtor_address', 'NO ESPECIFICADO')}** y documento de identidad "
            f"número **{data.get('debtor_dni', 'NO ESPECIFICADO')}**, reconozco que debo y "
            f"me comprometo a pagar incondicionalmente a la orden de **{data.get('lender', 'NO ESPECIFICADO')}**, "
            f"con domicilio en **{data.get('lender_address', 'NO ESPECIFICADO')}** y documento "
            f"de identidad número **{data.get('lender_dni', 'NO ESPECIFICADO')}**, la suma de **{amount} euros**."
        )
        
        self.pdf.multi_cell(0, 10, main_text)
        self.pdf.ln(10)

        # Payment details
        payment_text = (
            f"El pago se efectuará en **{data.get('payment_place', 'NO ESPECIFICADO')}** "
            f"el día **{self._format_date(data.get('due_date', 'NO ESPECIFICADO'))}**, "
            "sin protesto ni requerimiento previo."
        )
        self.pdf.multi_cell(0, 10, payment_text)
        self.pdf.ln(10)

        # Interest clause
        interest = data.get('interest', 'NO ESPECIFICADO').replace('%', '')
        interest_text = (
            f"Este pagaré devengará un interés por cada mes de retraso del **{interest}%** "
            "sobre el saldo pendiente, desde la fecha de vencimiento hasta su completo pago."
        )
        self.pdf.multi_cell(0, 10, interest_text)
        self.pdf.ln(10)

        # Jurisdiction
        jurisdiction_text = (
            "En caso de incumplimiento, el beneficiario renuncia expresamente a los "
            "beneficios de excusión, división y orden, y se somete a la jurisdicción "
            f"de los tribunales de **{location}**, para resolver cualquier disputa "
            "derivada de este documento."
        )
        self.pdf.multi_cell(0, 10, jurisdiction_text)
        self.pdf.ln(10)

        # Confirmation
        self.pdf.multi_cell(0, 10, "Ambas partes declaran haber leído y comprendido todas las condiciones establecidas en este pagaré, firmándolo en señal de conformidad.")
        self.pdf.ln(20)

        # Signatures
        self.pdf.cell(0, 10, "FIRMAS:", 0, 1)
        self.pdf.ln(10)
        
        # Add signatures if provided
        self.pdf.cell(0, 10, "Prestamista:", 0, 1)
        if data.get('lender_signature'):
            self.pdf.image(data['lender_signature'], x=20, y=self.pdf.get_y(), w=50)
        self.pdf.ln(30)
        
        self.pdf.cell(0, 10, "Beneficiario:", 0, 1)
        if data.get('debtor_signature'):
            self.pdf.image(data['debtor_signature'], x=20, y=self.pdf.get_y(), w=50)

        return self.pdf
