from PIL import Image
images = []

w = 6000
h = 4242

for i in range(29):
    image = Image.open(f"{i+1:02d}.png")
    delta_w = abs(w-image.size[0])
    delta_h = abs(h-image.size[1])
    if delta_w < delta_h:
        images.append(image.resize((w, int((w/image.size[0])*image.size[1])))) #if delta w is greater than delta h
    else:
        images.append(image.resize((int((h/image.size[1])*image.size[0]), h)))

# w = max([image.size[0] for image in images])
# print(w)
# h = max([image.size[1] for image in images])
# print(h)

'''CROPPING CODE'''

cropped = []

for image in images:
    cropped.append(
        image.crop((
                    -1*((w-image.size[0])/2),
                    -1*((h-image.size[1])/2),
                    (image.size[0]+((w-image.size[0])/2)),
                    (image.size[1]+((h-image.size[1])/2))
                ))
    )
q = 1
for image in cropped:
    image.save(f"sign_{q:02d}.png")
    #.resize((int(w), int(h)))
    q+=1

print("done")
