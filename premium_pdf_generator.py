from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus import Image, Flowable, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.graphics.shapes import Drawing, Rect, Circle, String
from reportlab.graphics import renderPDF
import os

class ColoredBackground(Flowable):
    def __init__(self, width, height, color):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, fill=1)

class GradientBackground(Flowable):
    def __init__(self, width, height, color1, color2):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2

    def draw(self):
        # Create gradient effect
        for i in range(int(self.height)):
            ratio = i / self.height
            r = self.color1.red + (self.color2.red - self.color1.red) * ratio
            g = self.color1.green + (self.color2.green - self.color1.green) * ratio
            b = self.color1.blue + (self.color2.blue - self.color1.blue) * ratio
            color = colors.Color(r, g, b)
            self.canv.setFillColor(color)
            self.canv.rect(0, self.height - i - 1, self.width, 1, fill=1)

def create_premium_brochure():
    filename = "C:\\Users\\GAURAV NAZARE\\Desktop\\paramount_holidayz\\Premium_Thailand_Brochure.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=1*cm, bottomMargin=1*cm,
                          leftMargin=1.5*cm, rightMargin=1.5*cm)

    styles = getSampleStyleSheet()

    # Enhanced custom styles
    brand_style = ParagraphStyle(
        'BrandStyle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=8,
        fontName='Helvetica-Bold',
        leading=32
    )

    tagline_style = ParagraphStyle(
        'TaglineStyle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=20,
        leading=18
    )

    hero_title_style = ParagraphStyle(
        'HeroTitle',
        parent=styles['Heading1'],
        fontSize=36,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=15,
        fontName='Helvetica-Bold',
        leading=42
    )

    hero_subtitle_style = ParagraphStyle(
        'HeroSubtitle',
        parent=styles['Normal'],
        fontSize=16,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=25,
        leading=20
    )

    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading1'],
        fontSize=26,
        textColor=HexColor('#2c3e50'),
        alignment=TA_CENTER,
        spaceAfter=12,
        fontName='Helvetica-Bold',
        leading=30
    )

    package_title_style = ParagraphStyle(
        'PackageTitle',
        parent=styles['Heading2'],
        fontSize=20,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=8,
        fontName='Helvetica-Bold',
        leading=24
    )

    price_style = ParagraphStyle(
        'PriceStyle',
        parent=styles['Heading1'],
        fontSize=32,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=8,
        fontName='Helvetica-Bold',
        leading=36
    )

    duration_style = ParagraphStyle(
        'DurationStyle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=10,
        leading=16
    )

    stars_style = ParagraphStyle(
        'StarsStyle',
        parent=styles['Normal'],
        fontSize=16,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=15,
        leading=18
    )

    inclusion_style = ParagraphStyle(
        'InclusionStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black,
        spaceAfter=6,
        leading=14
    )

    highlight_title_style = ParagraphStyle(
        'HighlightTitle',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=HexColor('#856404'),
        alignment=TA_CENTER,
        spaceAfter=5,
        fontName='Helvetica-Bold'
    )

    highlight_text_style = ParagraphStyle(
        'HighlightText',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#856404'),
        alignment=TA_CENTER,
        spaceAfter=8
    )

    itinerary_day_style = ParagraphStyle(
        'ItineraryDay',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=HexColor('#667eea'),
        spaceAfter=6,
        fontName='Helvetica-Bold',
        leading=16
    )

    itinerary_desc_style = ParagraphStyle(
        'ItineraryDesc',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.black,
        spaceAfter=8,
        leading=12
    )

    contact_title_style = ParagraphStyle(
        'ContactTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=15,
        fontName='Helvetica-Bold'
    )

    contact_label_style = ParagraphStyle(
        'ContactLabel',
        parent=styles['Heading3'],
        fontSize=14,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=5,
        fontName='Helvetica-Bold'
    )

    contact_value_style = ParagraphStyle(
        'ContactValue',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.white,
        alignment=TA_CENTER,
        spaceAfter=10
    )

    footer_style = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.gray,
        alignment=TA_CENTER,
        spaceAfter=5
    )

    # Build the PDF content
    content = []

    # Page 1: Hero Section
    # Hero background with gradient
    hero_bg = GradientBackground(19*cm, 8*cm, HexColor('#1e3c72'), HexColor('#2a5298'))
    content.append(hero_bg)
    content.append(Spacer(1, -8*cm))  # Move content up to overlay on background

    # Hero content
    hero_data = [
        [Paragraph("PARAMOUNT HOLIDAYZ", brand_style)],
        [Paragraph("Your Trusted Travel Partner", tagline_style)],
        [Paragraph("Thailand Paradise", hero_title_style)],
        [Paragraph("Experience the Land of Smiles with Unforgettable Adventures", hero_subtitle_style)]
    ]

    hero_table = Table(hero_data, colWidths=[17*cm])
    hero_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.transparent),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    content.append(hero_table)
    content.append(Spacer(1, 2*cm))

    # Packages Section
    content.append(Paragraph("Exclusive Packages", section_title_style))
    content.append(Spacer(1, 0.5*cm))

    # Package 1
    package1_header = [
        [Paragraph("Premium 3-Star Package", package_title_style)],
        [Paragraph("₹14,999", price_style)],
        [Paragraph("4 Nights • 5 Days", duration_style)],
        [Paragraph("★★★", stars_style)]
    ]

    package1_header_table = Table(package1_header, colWidths=[17*cm])
    package1_header_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#667eea')),
        ('BOX', (0, 0), (-1, -1), 3, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ]))

    content.append(package1_header_table)
    content.append(Spacer(1, 0.3*cm))

    # Package 1 inclusions
    inclusions1 = [
        "✓ 4 Nights in 3-Star Hotel",
        "✓ Daily Breakfast",
        "✓ Coral Island with Lunch",
        "✓ Alcazar Show with Transfer",
        "✓ Tiger Park Entrance",
        "✓ Pattaya City Tour",
        "✓ Gems Gallery Visit",
        "✓ Private Airport Transfers"
    ]

    inclusions1_data = [[Paragraph(item, inclusion_style)] for item in inclusions1]
    inclusions1_table = Table(inclusions1_data, colWidths=[17*cm])
    inclusions1_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ROUNDEDCORNERS', [5, 5, 5, 5]),
    ]))

    content.append(inclusions1_table)
    content.append(Spacer(1, 0.5*cm))

    # Package 1 highlight
    highlight1_data = [
        [Paragraph("✨ Premium Experience", highlight_title_style)],
        [Paragraph("Enjoy luxury transfers and exclusive sightseeing", highlight_text_style)]
    ]

    highlight1_table = Table(highlight1_data, colWidths=[17*cm])
    highlight1_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#fff3cd')),
        ('BOX', (0, 0), (-1, -1), 2, HexColor('#ffc107')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ]))

    content.append(highlight1_table)
    content.append(Spacer(1, 1*cm))

    # Package 2
    package2_header = [
        [Paragraph("Luxury 4-Star Package", package_title_style)],
        [Paragraph("₹17,999", price_style)],
        [Paragraph("4 Nights • 5 Days", duration_style)],
        [Paragraph("★★★★", stars_style)]
    ]

    package2_header_table = Table(package2_header, colWidths=[17*cm])
    package2_header_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#764ba2')),
        ('BOX', (0, 0), (-1, -1), 3, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ROUNDEDCORNERS', [10, 10, 10, 10]),
    ]))

    content.append(package2_header_table)
    content.append(Spacer(1, 0.3*cm))

    # Package 2 inclusions
    inclusions2 = [
        "✓ 4 Nights in 4-Star Hotel",
        "✓ Daily Breakfast",
        "✓ Coral Island with Lunch",
        "✓ Alcazar Show with Transfer",
        "✓ Tiger Park Entrance",
        "✓ Pattaya City Tour",
        "✓ Gems Gallery Visit",
        "✓ Private Airport Transfers"
    ]

    inclusions2_data = [[Paragraph(item, inclusion_style)] for item in inclusions2]
    inclusions2_table = Table(inclusions2_data, colWidths=[17*cm])
    inclusions2_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ROUNDEDCORNERS', [5, 5, 5, 5]),
    ]))

    content.append(inclusions2_table)
    content.append(Spacer(1, 0.5*cm))

    # Package 2 highlight
    highlight2_data = [
        [Paragraph("💎 Luxury Experience", highlight_title_style)],
        [Paragraph("Superior comfort with premium 4-star accommodation", highlight_text_style)]
    ]

    highlight2_table = Table(highlight2_data, colWidths=[17*cm])
    highlight2_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor('#fff3cd')),
        ('BOX', (0, 0), (-1, -1), 2, HexColor('#ffc107')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ]))

    content.append(highlight2_table)
    content.append(PageBreak())

    # Page 2: Itinerary
    content.append(Paragraph("Your Thailand Adventure", section_title_style))
    content.append(Spacer(1, 0.5*cm))

    itinerary_data = [
        [Paragraph("Day 1: Arrival in Bangkok", itinerary_day_style),
         Paragraph("Welcome to Thailand! Transfer to your Pattaya hotel for check-in and relaxation. Enjoy the scenic drive and settle into your accommodation.", itinerary_desc_style)],
        [Paragraph("Day 2: Coral Island Adventure", itinerary_day_style),
         Paragraph("Enjoy a full day at Coral Island with snorkeling, swimming, and a delicious lunch. Experience the crystal-clear waters and marine life.", itinerary_desc_style)],
        [Paragraph("Day 3: Tiger Kingdom & City Tour", itinerary_day_style),
         Paragraph("Visit Tiger Kingdom for an unforgettable wildlife experience, followed by Pattaya city sightseeing. Explore the vibrant city and its attractions.", itinerary_desc_style)],
        [Paragraph("Day 4: Alcazar Show & Gems Gallery", itinerary_day_style),
         Paragraph("Experience the spectacular Alcazar Cabaret Show and explore the fascinating Gems Gallery. Enjoy world-class entertainment and shopping.", itinerary_desc_style)],
        [Paragraph("Day 5: Departure", itinerary_day_style),
         Paragraph("Transfer to the airport for your journey home with wonderful memories. Safe travels and see you again soon!", itinerary_desc_style)]
    ]

    itinerary_table = Table(itinerary_data, colWidths=[6*cm, 11*cm])
    itinerary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ROUNDEDCORNERS', [8, 8, 8, 8]),
    ]))

    content.append(itinerary_table)
    content.append(PageBreak())

    # Page 3: Contact Information
    contact_bg = ColoredBackground(19*cm, 10*cm, HexColor('#2d3748'))
    content.append(contact_bg)
    content.append(Spacer(1, -10*cm))

    contact_data = [
        [Paragraph("Ready for Your Thailand Adventure?", contact_title_style)],
        [""],
        [Paragraph("📞 Call Us", contact_label_style)],
        [Paragraph("+91 9226155000", contact_value_style)],
        [Paragraph("📧 Email Us", contact_label_style)],
        [Paragraph("sales.paramountholidayz@gmail.com", contact_value_style)],
        [Paragraph("📍 Visit Us", contact_label_style)],
        [Paragraph("Mumbai, Maharashtra, India", contact_value_style)],
        [""],
        [Paragraph("© 2024 Paramount Holidayz. All rights reserved.", footer_style)],
        [Paragraph("Licensed Travel Agent | Registration No: MH/2024/001", footer_style)]
    ]

    contact_table = Table(contact_data, colWidths=[17*cm])
    contact_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.transparent),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))

    content.append(contact_table)

    # Generate PDF
    doc.build(content)
    print(f"Premium PDF brochure created successfully: {filename}")

    # Check file size
    file_size = os.path.getsize(filename)
    print(f"File size: {file_size} bytes ({file_size/1024:.1f} KB)")

    return filename

if __name__ == "__main__":
    create_premium_brochure()