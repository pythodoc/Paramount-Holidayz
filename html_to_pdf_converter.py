import pdfkit
import os
from pathlib import Path

def convert_html_to_pdf():
    # Path to the HTML file
    html_file = "C:\\Users\\GAURAV NAZARE\\Desktop\\paramount_holidayz\\advanced_brochure.html"
    output_pdf = "C:\\Users\\GAURAV NAZARE\\Desktop\\paramount_holidayz\\Premium_Thailand_Brochure.pdf"

    # Check if HTML file exists
    if not os.path.exists(html_file):
        print(f"HTML file not found: {html_file}")
        return None

    # PDF options for professional output
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
        'no-outline': None,
        'enable-local-file-access': None,
        'disable-smart-shrinking': None,
        'print-media-type': None,
        'dpi': 300,
        'zoom': 1.0,
        'page-break-before': 'body',
        'footer-center': 'Page [page] of [topage]',
        'footer-font-size': 8,
        'footer-spacing': 5,
    }

    try:
        # Convert HTML to PDF
        pdfkit.from_file(html_file, output_pdf, options=options)
        print(f"Premium PDF brochure created successfully: {output_pdf}")

        # Check file size
        file_size = os.path.getsize(output_pdf)
        print(f"File size: {file_size} bytes ({file_size/1024:.1f} KB)")

        return output_pdf

    except Exception as e:
        print(f"Error creating PDF: {e}")
        print("Trying alternative method...")

        # Fallback method
        try:
            # Try with basic options
            basic_options = {
                'page-size': 'A4',
                'margin-top': '0.5in',
                'margin-right': '0.5in',
                'margin-bottom': '0.5in',
                'margin-left': '0.5in',
            }
            pdfkit.from_file(html_file, output_pdf, options=basic_options)
            print(f"PDF created with basic options: {output_pdf}")
            return output_pdf

        except Exception as e2:
            print(f"Alternative method also failed: {e2}")
            return None

if __name__ == "__main__":
    convert_html_to_pdf()