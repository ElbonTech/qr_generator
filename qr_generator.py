#Simple QR code generator.... 
import qrcode
file_name = input("Enter QR Code file Name: ")
file_format = ".png"


file_png=file_name+file_format
data = input("Enter data to encode in QR code: ")

qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save(file_png)

print("QR code generated and saved as '",file_name,".png!")
