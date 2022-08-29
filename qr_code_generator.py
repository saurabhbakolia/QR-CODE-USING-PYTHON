import qrcode
import image

qr = qrcode.QRCode(
    version = 10,
    box_size = 15,
    border = 5
)

data = "hello this is a text"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(back_color=("white"), fill_color=("black"))
img.save("text.png")