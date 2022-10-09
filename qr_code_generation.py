import qrcode
id =input("Enter your id")
name= input("ENter your name")
features = qrcode.QRCode(version=1,box_size=20,border=3)
features.add_data({"Id":id,"Name":name})
features.make(fit=True)
generate_image = features.make_image(fill_color='black',back_color="white")
generate_image.save("image.png")
