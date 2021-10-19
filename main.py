from PIL import Image, ImageFont, ImageDraw

#import images
img = Image.open('/Users/kyliecrockett/Downloads/USA.jpg')
img2 = Image.open('/Users/kyliecrockett/Downloads/Eagle.jpg')

#adding text
type = ImageDraw.Draw(img)
font = ImageFont.truetype('Phosphate.ttc', 35,)
type.text((200,130), "NOW!", font=font, fill='red')
type.text((200,100), "VOTE", font=font, fill='red')

#resize eagle photo
img2 = img2.resize((50,50))

#pasting images
img3 = img.copy()
img3.paste(img2,(230, 10))

img3.show()
img3.save('/Users/kyliecrockett/Downloads/AD.png')