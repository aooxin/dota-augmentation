import aug

A=aug.aug("images","lables","aug-images","aug-lables")# 原始图片路径 原始lables路径 扩充到的图片路径 扩充到的lables路径
# A.Rotate(angle=90)

# A.RandomResize()
A.AddWeather()
