import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageOps

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = input("Enter the textual data here to convert it into a QR Code: \n")

qr_img = qr.make_image(fill="balck", back_color="white")

border_size1 = 10
border_color1 = "black"
qr_img = ImageOps.expand(qr_img, border=border_size1, fill=border_color1)

border_size1 = 30
border_color1 = "white"
qr_img = ImageOps.expand(qr_img, border=border_size1, fill=border_color1)


show_or_download = input("Do you want to show the QR or would you like to Download it ? S/D\n")
show_or_download = show_or_download.lower()
if show_or_download == 's':
    qr_img.show()
elif show_or_download == 'd':
    qr_img.save("QR.png")
print("Thank you for using our service.")