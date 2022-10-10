#codinng = utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest

# image = Image.open("F:/1.png")
# text = pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-4","492365","1857c28070854dcaaaf791500f459285" )
r.addFilePara("image", "F:/imcooc1.png")
r.addBodyPara("typeId", "35")  #35识别英文数字混合，5位
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
text = res.json()['showapi_res_body']['Result']  #json中提取Result结果
print(text) # 返回信息



