# Port By LiuAlvinas/Alvin For Lord Userbot From Ulttoid
# Based Plugins
# Fixed By ManusiaRakitann/Koala
# Dont Remove


# Alvin Ganteng

import os

import cv2
from PIL import Image

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.tiny(?: |$)(.*)")
async def _(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await event.edit("`Balas Ke Sticker`")
        return
    xx = await event.edit("`Memproses...`")
    ik = await bot.download_media(reply_message.media)
    im1 = Image.open("ezbwbot/ezbwbot.png")
    if ik.endswith(".tgs"):
        await event.client.download_media(reply_message, "ult.tgs")
        os.system("lottie_convert.py ult.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        json.close()
        jsn = jsn.replace("512", "2000")
        open("json.json", "w").write(jsn)
        os.system("lottie_convert.py json.json ult.tgs")
        file = "ult.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        dani, busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await event.client.send_file(event.chat_id, file, reply_to=event.reply_to_msg_id)
    await xx.delete()
    os.remove(file)
    os.remove(ik)


# Port By Alvin Ganteng/liualvinas
# Lord - Userbot

CMD_HELP.update(
    {
        "tiny": "`.tiny`\
    \nPenjelasan: Untuk Memperkecil Sticker."
    }
)
