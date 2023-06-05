from PIL import ImageGrab
import time
import os
# import pyautogui

# guns_area=(1554, 962, 1709, 1000)


class Area_1080():
    guns_area = (1619, 965, 1659, 1005)
    wlzy_area_hwk = (1605, 1000, 1630, 1025)
    wlzy_area_zhuanzhu = (1632, 1000, 1657, 1025)


class Area_1440():
    guns_area = (2165, 1280, 2220, 1330)
    wlzy_area_hwk = (2138, 1332, 2173, 1367)
    wlzy_area_zhuanzhu = (2176, 1332, 2211, 1367)


# 获取分辨率
def get_px(px):
    if px == 1920:
        return Area_1080
    else:
        return Area_1440


path = os.path.join(os.getcwd(), "shot_gun.png")


def shot1(area):
    try:
        shot = ImageGrab.grab(area)
        shot.save(path)
    finally:
        return path


# def shot2():
#     img = pyautogui.screenshot(region=[1605, 1000, 25, 25])
#     path = os.path.join(os.getcwd(), "shot_gun.png")
#     img.save(path)
#     return path


if __name__ == '__main__':
    shot1(get_px().guns_area)
