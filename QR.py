import qrcode
data = input("Enter text or url: ")
qr = qrcode.make(data)
qr.save("qrcode.png")
print("Qr code generated successfully")