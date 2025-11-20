import qrcode


# -------------------------------
# First QR Code (Black & White)
# -------------------------------
data1 = "https://www.google.com"

qr1 = qrcode.QRCode(version=1, box_size=10, border=5)
qr1.add_data(data1)
qr1.make(fit=True)

img1 = qr1.make_image(fill_color="black", back_color="white")
img1.save("myqrcode.png")

print("Black & white QR Code generated: myqrcode.png")

# -------------------------------
# Second QR Code (Colored)
# -------------------------------
data2 = "https://github.com/"

qr2 = qrcode.QRCode(version=1, box_size=10, border=4)
qr2.add_data(data2)
qr2.make(fit=True)

img2 = qr2.make_image(fill_color="blue", back_color="white")
img2.save("colored_qr.png")

print("Colored QR Code generated: colored_qr.png")
