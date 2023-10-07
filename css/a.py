from PIL import Image
import os

img = Image.open("C:\Users\smb12\OneDrive\바탕 화면\3학년 2학기 수업\캡스톤\플랜 2\image\구글아이콘.jpeg")
img_resize = img.resize((256, 256))

# 사진 사이즈 확인
print(img_resize.size)
# 결과: (256, 256)

# 사이즈 변경된 사진 저장
img_resize.save("C:\Users\smb12\OneDrive\바탕 화면\3학년 2학기 수업\캡스톤\플랜 2\image\구글아이콘1.jpeg")
os.path.isfile("C:\Users\smb12\OneDrive\바탕 화면\3학년 2학기 수업\캡스톤\플랜 2\image\구글아이콘1.jpeg")
# 결과: True