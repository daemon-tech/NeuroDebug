from reportlab.pdfgen import canvas

class DataReporter:
    def __init__(self, issues, fixes):
        self.issues = issues
        self.fixes = fixes

    def generate_pdf(self, filepath="report.pdf"):
        c = canvas.Canvas(filepath)
        c.drawString(100, 750, "NeuroDebug Report")
        c.drawString(100, 730, f"Issues Detected: {len(self.issues)}")
        c.drawString(100, 710, f"Fixes Applied: {len(self.fixes)}")
        c.save()
