import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.ERROR_CORRECT_H,
                    box_size=8,
                    border=4
                    )

qr.add_data("https://www.instagram.com/abhay_write/")
qr.make(fit=True)
img = qr.make_image(fill_color = "red",back_color = "black")
img.save("abhay_write.png") 