# QR Code Generator

Here we are generating qr codes by two approches.

1. Noraml approch
2. Modified approch

Let's see what in __Normal approch :__

<br />

## 1. Normal Approch
<br />

### 3 steps :
1. import qrcode module
2. Use make function to create qrcode of given link.
3. Use save method to save the qr code and in brackets give the name to the file.

<br />

### Conclusion (Problem)

It is simple 3 step process to generate qrcode. But in case we want to avoid errors we need to approch a modified or you can say suitable approch for QR code generation.


<br />

## 2. Modified Approch

<br />

### Requirements :
1. qrcode module
2. PIL module
3. Image module

<br />

### Working

First we import qrcode then we import PIL and from PIL module we import Image.
<br />

After that we create a variable __qr__ then we call our method qrocode then in qrcode we call method QRCode(QRCode will modify our code.) Now in QRCode we give the specifications what we want to modify then we modify the version,error_correction,box_size,border etc. 
<br />

After this we add data to qr variable(qr.add_data("give the link here."))

Then we use make method to create our modified qrcode(qr.make(fit=True))

Now we want to save qrcode in the form of image(.png format) for make that kind of image we use __img__ variable and use make_image method(img = qr.make_image) In make image we give 2 parameters what will be the color of __fill color__(fill color means a color which is visible in back color) and what will be the __back color__.

Now for saving this image we use save method.(img.save("give the name to file"))

### Conclusion

So that's how we will be able to modify our qrcode.