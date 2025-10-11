import urllib.request
import zipfile
import os
import subprocess
import sys

def download_and_install_wkhtmltopdf():
    """Download and install wkhtmltopdf for Windows"""

    # wkhtmltopdf download URL for Windows 64-bit
    url = "https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.msvc2015-win64.exe"
    installer_path = "C:\\Users\\GAURAV NAZARE\\Desktop\\paramount_holidayz\\wkhtmltopdf_installer.exe"

    print("Downloading wkhtmltopdf installer...")

    try:
        # Download the installer
        urllib.request.urlretrieve(url, installer_path)
        print(f"Downloaded installer to: {installer_path}")

        # Run the installer (silent installation)
        print("Installing wkhtmltopdf...")
        result = subprocess.run([installer_path, '/S'], capture_output=True, text=True)

        if result.returncode == 0:
            print("wkhtmltopdf installed successfully!")

            # Try to find the installation path
            possible_paths = [
                "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe",
                "C:\\Program Files (x86)\\wkhtmltopdf\\bin\\wkhtmltopdf.exe",
                "C:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
            ]

            wkhtmltopdf_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    wkhtmltopdf_path = path
                    break

            if wkhtmltopdf_path:
                print(f"wkhtmltopdf found at: {wkhtmltopdf_path}")
                return wkhtmltopdf_path
            else:
                print("wkhtmltopdf installed but executable not found in expected locations")
                return None
        else:
            print(f"Installation failed: {result.stderr}")
            return None

    except Exception as e:
        print(f"Error during installation: {e}")
        return None

    finally:
        # Clean up installer file
        if os.path.exists(installer_path):
            os.remove(installer_path)
            print("Cleaned up installer file")

if __name__ == "__main__":
    path = download_and_install_wkhtmltopdf()
    if path:
        print(f"\nwkhtmltopdf is ready to use at: {path}")
        print("You can now run the PDF converter script.")
    else:
        print("\nFailed to install wkhtmltopdf automatically.")
        print("Please download and install it manually from:")
        print("https://wkhtmltopdf.org/downloads.html")