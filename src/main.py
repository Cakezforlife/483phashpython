import tlsh


normal_photo = open("../imgs/normal/my_photo-1.jpg", "rb")
normal_photo_2 = open("../imgs/normal/my_photo-2.jpg", "rb")
changed_photo = open("../imgs/change/my_photo-2.jpg", "rb")

nh1 = tlsh.hash(normal_photo.read())
nh2 = tlsh.hash(normal_photo_2.read())
ch1 = tlsh.hash(changed_photo.read())

nscore = tlsh.diff(nh1, nh2)
cscore = tlsh.diff(nh1, ch1)

assert tlsh.diff(nh1, nh1) == 0

print(nscore)
print(cscore)