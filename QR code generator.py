import qrcode
from PIL import Image

def generate_qr_code(text, filename='qr_code.png', size=10, border=4):
    qr = qrcode.QRCode(
        version=size,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=border,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

# --- Outside the function ---
text = input("Enter the text or URL to convert into a QR code: ")
filename = input("Enter the filename to save the QR code (default: qr_code.png): ") or 'qr_code.png'
size = int(input("Enter the size of the QR code (default: 10): ") or 10)
border = int(input("Enter the border size of the QR code (default: 4): ") or 4)

generate_qr_code(text, filename, size, border)



