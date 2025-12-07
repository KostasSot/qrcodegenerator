import qrcode

def generate_qr():
    url = input("Enter the URL: ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()

    print("Check your opened windows!")

if __name__ == "__main__":
    generate_qr()