import qrcode

img = qrcode.make("https://www.instagram.com/abhay_write/")
 # Provide the link or text and use make method to make a qrcode of it.

img.save("QR_code.png") 
# Now we use save function to save our qrcode with the name we want.