import imgbbpy

client = imgbbpy.SyncClient('f7898e1bdf874ac4e06a3111d218ddaa')
packname='limbozina'
for i in range(5,31):
    image = client.upload(file=packname+'/'+str(i)+'.webp')
    print(image.url)

image = client.upload(file=packname+'/0.png')
print(image.url)