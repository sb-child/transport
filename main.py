from PIL import Image, ImageDraw, ImageFont
import random
import qrcode
import datetime


def main():
    name = input("您的英文名是啥? ")
    eth_input = input("您的变态坊是? ")
    if (eth_input.startswith("0x") or eth_input.startswith("0X")) and len(eth_input) == 42:
        eth_addr = "0x" + eth_input[2:].upper()
    elif len(eth_input) == 40:
        eth_addr = "0x" + eth_input.upper()
    else:
        eth_addr = "0x" + \
            "".join(random.choices("ABCDEF" + "1234567890", k=40))
        print("计算机无法理解您的变态坊, 于是随机生成了:", eth_addr)
    pron = input("您的代词是? ")
    if pron.find("she") != -1:
        pron = "ILLA/she"
    elif pron.find("he") != -1:
        pron = "ILLE/He"
    else:
        pron = "ILLVD/They"
    try:
        date_born_input = input("您的出生日期是?(格式: 2022.1.1) ")
        date_born_parse = datetime.datetime.strptime(
            date_born_input, "%Y.%m.%d")
        date_born = date_born_parse.strftime("%Y / %m %b / %d").upper()
    except KeyboardInterrupt as e:
        raise e
    except Exception as e:
        print("您输入的日期格式不正确:", e)
        return
    place = input("您在何处出生? ")

    id_1 = "P<TGD" + name.replace(" ", "<")
    id_1 += "<" * (44 - len(id_1))
    id_2 = eth_addr + "<" * 2
    qr = qrcode.QRCode(version=1,
                       box_size=4,
                       border=0)
    qr.add_data(eth_addr)
    qr_img = qr.make_image(fill_color="black",
                           back_color="transparent")
    qr.make(fit=True)
    date_now = datetime.datetime.now().strftime("%Y / %m %b / %d").upper()

    f_number = ImageFont.truetype("data-latin.ttf", size=60)
    f_text = ImageFont.truetype("SourceSansPro-Semibold.otf", size=35)
    f_id = ImageFont.truetype("JetBrainsMono-Regular.ttf", size=50)
    im = Image.open("background.png")
    mask = Image.open("mask.png")
    head = Image.open("head.png")  # 照片

    imd = ImageDraw.ImageDraw(im)
    imd.text((1147, 175), eth_addr[2:6] + eth_addr[38:42], font=f_number,
             fill="#ff9ea8")  # BTH地址首末
    imd.text((500, 292), name, font=f_text, fill="black")  # 名字
    imd.text((1004, 292), pron, font=f_text, fill="black")  # 代词
    imd.text((500, 510), date_born,
             font=f_text, fill="black")  # 出生日期
    imd.text((1004, 510), place, font=f_text, fill="black")  # 出生地点
    imd.text((500, 615), date_now,
             font=f_text, fill="black")  # 签发日期
    imd.text((88, 794), id_1,
             font=f_id, fill="black")  # 签发日期
    imd.text((88, 874), id_2,
             font=f_id, fill="black")  # 签发日期
    head = head.resize((356, 486))

    im.paste(qr_img, (1270, 20), mask=qr_img)
    im.alpha_composite(head, (105, 221))
    im.alpha_composite(mask)

    im.save("out.png")


if __name__ == "__main__":
    main()
