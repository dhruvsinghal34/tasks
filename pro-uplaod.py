from PIL import Image
print("these are the three daily tasks")
print("and there steps")
print("1) food preperation")
img = Image.open('preperation of food.png')
print(img.format)
print(img.mode)
print(img.size)
img.show()

print("2) bathing")
img = Image.open('eating.png')
print(img.format)
print(img.mode)
print(img.size)
img.show()

print("3) bathing")
img = Image.open('bathing.png')
print(img.format)
print(img.mode)
print(img.size)
img.show()
