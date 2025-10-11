from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

def create_thailand_brochure():
    # Create PDF document
    filename = "C:\\Users\\GAURAV NAZARE\\Desktop\\paramount_holidayz\\Thailand_Brochure.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=30,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    package_title_style = ParagraphStyle(
        'PackageTitle',
        parent=styles['Heading2'],
        fontSize=20,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=15
    )

    price_style = ParagraphStyle(
        'PriceStyle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )

    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black,
        spaceAfter=8
    )

    highlight_style = ParagraphStyle(
        'HighlightStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.darkgoldenrod,
        alignment=TA_CENTER,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )

    # Build the PDF content
    content = []

    # Header Section
    header_table_data = [
        [Paragraph("PARAMOUNT HOLIDAYZ", title_style)],
        [Paragraph("Your Trusted Travel Partner", subtitle_style)],
        [Paragraph("Thailand Paradise", title_style)],
        [Paragraph("Experience the Land of Smiles with Unforgettable Adventures", subtitle_style)]
    ]

    header_table = Table(header_table_data, colWidths=[15*cm])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.blue),
        ('BOX', (0, 0), (-1, -1), 0, colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 20),
    ]))

    content.append(header_table)
    content.append(Spacer(1, 20))

    # Packages Section Title
    content.append(Paragraph("Exclusive Packages", styles['Heading1']))
    content.append(Spacer(1, 20))

    # Package 1
    package1_data = [
        [Paragraph("Premium 3-Star Package", package_title_style)],
        [Paragraph("₹14,999", price_style)],
        [Paragraph("4 Nights • 5 Days", styles['Normal'])],
        [Paragraph("★★★", styles['Normal'])],
    ]

    package1_table = Table(package1_data, colWidths=[15*cm])
    package1_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.blue),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    content.append(package1_table)
    content.append(Spacer(1, 10))

    # Package 1 Inclusions
    inclusions_data = [
        ["✓ 4 Nights in 3-Star Hotel"],
        ["✓ Daily Breakfast"],
        ["✓ Coral Island with Lunch"],
        ["✓ Alcazar Show with Transfer"],
        ["✓ Tiger Park Entrance"],
        ["✓ Pattaya City Tour"],
        ["✓ Gems Gallery Visit"],
        ["✓ Private Airport Transfers"]
    ]

    inclusions_table = Table(inclusions_data, colWidths=[15*cm])
    inclusions_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
    ]))

    content.append(inclusions_table)
    content.append(Spacer(1, 20))

    # Package 2
    package2_data = [
        [Paragraph("Luxury 4-Star Package", package_title_style)],
        [Paragraph("₹17,999", price_style)],
        [Paragraph("4 Nights • 5 Days", styles['Normal'])],
        [Paragraph("★★★★", styles['Normal'])],
    ]

    package2_table = Table(package2_data, colWidths=[15*cm])
    package2_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.purple),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    content.append(package2_table)
    content.append(Spacer(1, 10))

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

    inclusions2_table = Table(inclusions2_data, colWidths=[15*cm])
    inclusions2_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
    ]))

    content.append(inclusions2_table)
    content.append(Spacer(1, 20))

    # Itinerary Section
    content.append(Paragraph("Your Thailand Adventure", styles['Heading1']))
    content.append(Spacer(1, 15))

    itinerary_data = [
        ["Day 1: Arrival in Bangkok", "Welcome to Thailand! Transfer to your Pattaya hotel for check-in and relaxation."],
        ["Day 2: Coral Island Adventure", "Enjoy a full day at Coral Island with snorkeling, swimming, and a delicious lunch."],
        ["Day 3: Tiger Kingdom & City Tour", "Visit Tiger Kingdom for an unforgettable wildlife experience, followed by Pattaya city sightseeing."],
        ["Day 4: Alcazar Show & Gems Gallery", "Experience the spectacular Alcazar Cabaret Show and explore the fascinating Gems Gallery."],
        ["Day 5: Departure", "Transfer to the airport for your journey home with wonderful memories."]
    ]

    itinerary_table = Table(itinerary_data, colWidths=[5*cm, 10*cm])
    itinerary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ]))

    content.append(itinerary_table)
    content.append(Spacer(1, 20))

    # Contact Information
    content.append(Paragraph("Ready for Your Thailand Adventure?", styles['Heading1']))
    content.append(Spacer(1, 10))

    contact_data = [
        ["📞 Call Us", "+91 9226155000"],
        ["📧 Email Us", "sales.paramountholidayz@gmail.com"],
        ["📍 Visit Us", "Mumbai, Maharashtra, India"]
    ]

    contact_table = Table(contact_data, colWidths=[5*cm, 10*cm])
    contact_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('BOX', (0, 0), (-1, -1), 1, colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.white),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
    ]))

    content.append(contact_table)
    content.append(Spacer(1, 20))

    # Footer
    footer_text = "© 2024 Paramount Holidayz. All rights reserved. | Licensed Travel Agent | Registration No: MH/2024/001"
    content.append(Paragraph(footer_text, styles['Normal']))

    # Generate PDF
    doc.build(content)
    print(f"PDF brochure created successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_thailand_brochure()