#imports library for generating qrcode
import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=20,
                   border=2)

#adds URL or text to qrcode
qr.add_data("google.com")
qr.make(fit=True)

#creates image of the qrcode
img = qr.make_image(fill_color="black", back_color="white")
#saves the image
img.save("GoogleQRCode.png")