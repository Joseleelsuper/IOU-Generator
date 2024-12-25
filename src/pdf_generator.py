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
        self.pdf.write(10, "En ")
        self.pdf.set_font("Helvetica", "B", 12)
        self.pdf.write(10, f"{location}")
        self.pdf.set_font("Helvetica", "", 12)
        self.pdf.write(10, ", a ")
        self.pdf.set_font("Helvetica", "B", 12)
        self.pdf.write(10, self._format_date(today))
        self.pdf.set_font("Helvetica", "", 12)
        self.pdf.write(10, ".")
        self.pdf.ln(10)

        # Main text
        amount = str(data.get('amount', 0))
        
        def write_normal_with_bold(normal_text, bold_text):
            self.pdf.set_font("Helvetica", "", 12)
            self.pdf.write(10, normal_text)
            self.pdf.set_font("Helvetica", "B", 12)
            self.pdf.write(10, bold_text)
            self.pdf.set_font("Helvetica", "", 12)

        self.pdf.write(10, "Yo, ")
        write_normal_with_bold("", data.get('debtor', 'NO ESPECIFICADO'))
        self.pdf.write(10, ", con domicilio en ")
        write_normal_with_bold("", data.get('debtor_address', 'NO ESPECIFICADO'))
        self.pdf.write(10, " y documento de identidad número ")
        write_normal_with_bold("", data.get('debtor_dni', 'NO ESPECIFICADO'))
        self.pdf.write(10, ", reconozco que debo y me comprometo a pagar incondicionalmente a la orden de ")
        write_normal_with_bold("", data.get('lender', 'NO ESPECIFICADO'))
        self.pdf.write(10, ", con domicilio en ")
        write_normal_with_bold("", data.get('lender_address', 'NO ESPECIFICADO'))
        self.pdf.write(10, " y documento de identidad número ")
        write_normal_with_bold("", data.get('lender_dni', 'NO ESPECIFICADO'))
        self.pdf.write(10, ", la suma de ")
        write_normal_with_bold("", f"{amount} euros")
        self.pdf.write(10, ".")
        self.pdf.ln(10)

        # Payment details
        self.pdf.write(10, "El pago se efectuará en ")
        write_normal_with_bold("", data.get('payment_place', 'NO ESPECIFICADO'))
        self.pdf.write(10, " el día ")
        write_normal_with_bold("", self._format_date(data.get('due_date', 'NO ESPECIFICADO')))
        self.pdf.write(10, ", sin protesto ni requerimiento previo.")
        self.pdf.ln(10)

        # Interest clause
        interest = data.get('interest', 'NO ESPECIFICADO').replace('%', '')
        self.pdf.write(10, "Este pagaré devengará un interés por cada mes de retraso del ")
        write_normal_with_bold("", f"{interest}%")
        self.pdf.write(10, " sobre el saldo pendiente, desde la fecha de vencimiento hasta su completo pago.")
        self.pdf.ln(10)

        # Jurisdiction
        self.pdf.write(10, "En caso de incumplimiento, el beneficiario renuncia expresamente a los beneficios de excusión, división y orden, y se somete a la jurisdicción de los tribunales de ")
        write_normal_with_bold("", location)
        self.pdf.write(10, ", para resolver cualquier disputa derivada de este documento.")
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
