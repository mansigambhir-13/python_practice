import qrcode
from PIL import Image
import requests
from io import BytesIO
import os

def download_github_logo(save_path='github_logo.png'):
    url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.save(save_path)
        print(f"✅ GitHub logo downloaded and saved as '{save_path}'")
    except Exception as e:
        print(f"❌ Failed to download logo: {e}")

def generate_github_qr_with_logo(github_url, filename='github_qr_with_logo.png', logo_path='github_logo.png'):
    # Step 1: Create a QR Code object
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(github_url)
    qr.make(fit=True)

    # Step 2: Create QR image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Step 3: Check and load logo
    if not os.path.exists(logo_path):
        download_github_logo(logo_path)

    logo = Image.open(logo_path)
    logo_size = 80
    logo = logo.resize((logo_size, logo_size))

    # Step 4: Paste logo in the center
    qr_width, qr_height = qr_img.size
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

    # Step 5: Save and show
    qr_img.save(filename)
    print(f"✅ QR code with logo saved as '{filename}'")
    qr_img.show()

# ------------------- Run it -------------------

github_profile_url = input("Enter your GitHub profile URL:https://github.com/mansigambhir-1 ").strip()
generate_github_qr_with_logo(github_profile_url)
