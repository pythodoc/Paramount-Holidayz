from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus import Image, Flowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
import os

class GradientRect(Flowable):
    def __init__(self, width, height, color1, color2):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2

    def draw(self):
        self.canv.setFillColor(self.color1)
        self.canv.rect(0, 0, self.width, self.height, fill=1)

def create_advanced_brochure():
    filename = "C:\\Users\\GAURAV NAZARE\\Desktop\\paramount_holidayz\\Advanced_Thailand_Brochure.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=2*cm, bottomMargin=2*cm,
                          leftMargin=2*cm, rightMargin=2*cm)

    styles = getSampleStyleSheet()

    # Custom styles with professional typography
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Bold',
        leading=40
    )

    brand_style = ParagraphStyle(
        'BrandStyle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=10,
        fontName='Helvetica-Bold',
        leading=30
    )

    tagline_style = ParagraphStyle(
        'TaglineStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=15,
        leading=16
    )

    package_title_style = ParagraphStyle(
        'PackageTitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )

    price_style = ParagraphStyle(
        'PriceStyle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )

    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#2c3e50'),
        alignment=TA_CENTER,
        spaceAfter=15,
        fontName='Helvetica-Bold'
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.black,
        spaceAfter=8,
        leading=12
    )

    highlight_style = ParagraphStyle(
        'HighlightStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#856404'),
        alignment=TA_CENTER,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=8
    )

    # Build the PDF content
    content = []

    # Page 1: Hero Section
    # Hero Header with gradient background
    hero_data = [
        [Paragraph("PARAMOUNT HOLIDAYZ", brand_style)],
        [Paragraph("Your Trusted Travel Partner", tagline_style)],
        [Paragraph("Thailand Paradise", title_style)],
        [Paragraph("Experience the Land of Smiles with Unforgettable Adventures", tagline_style)]
    ]

    hero_table = Table(hero_data, colWidths=[16*cm])
    hero_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#1e3c72')),
        ('BOX', (0, 0), (-1, -1), 0, colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 20),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    content.append(hero_table)
    content.append(Spacer(1, 1*cm))

    # Packages Section Title
    content.append(Paragraph("Exclusive Packages", section_title_style))
    content.append(Spacer(1, 0.5*cm))

    # Package 1
    package1_data = [
        [Paragraph("Premium 3-Star Package", package_title_style)],
        [Paragraph("₹14,999", price_style)],
        [Paragraph("4 Nights • 5 Days", styles['Normal'])],
        [Paragraph("★★★", styles['Normal'])],
    ]

    package1_table = Table(package1_data, colWidths=[16*cm])
    package1_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#667eea')),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    content.append(package1_table)
    content.append(Spacer(1, 0.5*cm))

    # Package 1 Inclusions
    inclusions1_data = [
        ["✓ 4 Nights in 3-Star Hotel"],
        ["✓ Daily Breakfast"],
        ["✓ Coral Island with Lunch"],
        ["✓ Alcazar Show with Transfer"],
        ["✓ Tiger Park Entrance"],
        ["✓ Pattaya City Tour"],
        ["✓ Gems Gallery Visit"],
        ["✓ Private Airport Transfers"]
    ]

    inclusions1_table = Table(inclusions1_data, colWidths=[16*cm])
    inclusions1_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))

    content.append(inclusions1_table)
    content.append(Spacer(1, 1*cm))

    # Package 2
    package2_data = [
        [Paragraph("Luxury 4-Star Package", package_title_style)],
        [Paragraph("₹17,999", price_style)],
        [Paragraph("4 Nights • 5 Days", styles['Normal'])],
        [Paragraph("★★★★", styles['Normal'])],
    ]

    package2_table = Table(package2_data, colWidths=[16*cm])
    package2_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#764ba2')),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    content.append(package2_table)
    content.append(Spacer(1, 0.5*cm))

    # Package 2 Inclusions
    inclusions2_data = [
        ["✓ 4 Nights in 4-Star Hotel"],
        ["✓ Daily Breakfast"],
        ["✓ Coral Island with Lunch"],
        ["✓ Alcazar Show with Transfer"],
        ["✓ Tiger Park Entrance"],
        ["✓ Pattaya City Tour"],
        ["✓ Gems Gallery Visit"],
        ["✓ Private Airport Transfers"]
    ]

    inclusions2_table = Table(inclusions2_data, colWidths=[16*cm])
    inclusions2_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))

    content.append(inclusions2_table)
    content.append(PageBreak())

    # Page 2: Itinerary
    content.append(Paragraph("Your Thailand Adventure", section_title_style))
    content.append(Spacer(1, 0.5*cm))

    itinerary_data = [
        ["Day 1: Arrival in Bangkok", "Welcome to Thailand! Transfer to your Pattaya hotel for check-in and relaxation. Enjoy the scenic drive and settle into your accommodation."],
        ["Day 2: Coral Island Adventure", "Enjoy a full day at Coral Island with snorkeling, swimming, and a delicious lunch. Experience the crystal-clear waters and marine life."],
        ["Day 3: Tiger Kingdom & City Tour", "Visit Tiger Kingdom for an unforgettable wildlife experience, followed by Pattaya city sightseeing. Explore the vibrant city and its attractions."],
        ["Day 4: Alcazar Show & Gems Gallery", "Experience the spectacular Alcazar Cabaret Show and explore the fascinating Gems Gallery. Enjoy world-class entertainment and shopping."],
        ["Day 5: Departure", "Transfer to the airport for your journey home with wonderful memories. Safe travels and see you again soon!"]
    ]

    itinerary_table = Table(itinerary_data, colWidths=[6*cm, 10*cm])
    itinerary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ]))

    content.append(itinerary_table)
    content.append(PageBreak())

    # Page 3: Contact Information
    contact_data = [
        [Paragraph("Ready for Your Thailand Adventure?", section_title_style)],
        [""],
        [Paragraph("📞 Call Us: +91 9226155000", contact_style)],
        [Paragraph("📧 Email Us: sales.paramountholidayz@gmail.com", contact_style)],
        [Paragraph("📍 Visit Us: Mumbai, Maharashtra, India", contact_style)],
        [""],
        [Paragraph("© 2024 Paramount Holidayz. All rights reserved.", styles['Normal'])],
        [Paragraph("Licensed Travel Agent | Registration No: MH/2024/001", styles['Normal'])]
    ]

    contact_table = Table(contact_data, colWidths=[16*cm])
    contact_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#2d3748')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('BOX', (0, 0), (-1, -1), 0, colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    content.append(contact_table)

    # Generate PDF
    doc.build(content)
    print(f"Advanced PDF brochure created successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_advanced_brochure()