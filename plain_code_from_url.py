import qrcode
from PIL import Image
import argparse
from urllib.parse import urlparse

def url_to_filename(url):
    """
    Convert URL to a valid filename by removing protocol and replacing '/' with '_'.

    Args:
        url (str): The URL to convert

    Returns:
        str: A filename derived from the URL
    """
    # Parse the URL
    parsed = urlparse(url)
    # Combine netloc and path, replace '/' with '_'
    filename_base = (parsed.netloc + parsed.path).replace('/', '_').replace('\\', '_')
    # Remove any trailing underscores and add extension
    filename_base = filename_base.rstrip('_')
    return f"{filename_base}.png"

def generate_qr_code(url, filename=None, output_path="qrcodes"):
    """
    Generate a QR code from a URL and save it as an image file.

    Args:
        url (str): The URL to encode in the QR code
        filename (str): The filename to save the QR code image (optional)
        output_path (str): The directory path to save the QR code image

    Returns:
        str: Path to the saved QR code image
    """
    # Generate filename from URL if not provided
    if filename is None:
        filename = url_to_filename(url)

    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=20,  # Size of each box in pixels
        border=1,  # Border size in boxes
    )

    # Add URL data to QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(f"{output_path}/{filename}")
    print(f"QR code saved as: {output_path}/{filename}")

    # Display the image
    img.show()

    return filename

def main():
    """Main function to run the QR code generator with argument parsing."""
    parser = argparse.ArgumentParser(description='Generate QR code from URL')
    parser.add_argument('url', help='The URL to generate QR code for')
    parser.add_argument('--filename', help='Custom filename (optional)')
    parser.add_argument('--output-path', default='qrcodes', help='Output directory path (default: qrcodes)')

    args = parser.parse_args()
    url = args.url.strip()

    if not url:
        print("Error: URL cannot be empty!")
        return

    # Add protocol if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
        print(f"Added protocol: {url}")

    # Generate QR code
    try:
        generate_qr_code(url, args.filename, args.output_path)
    except Exception as e:
        print(f"Error generating QR code: {e}")

main()
