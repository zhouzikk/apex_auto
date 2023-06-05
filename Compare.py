import cv2
import Shot
import time
from ctypes import *
from hash import pxHash
import win32con
import win32gui
import win32print
from datetime import datetime


def cmpHash(hash1, hash2, shape=(10, 10)):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 相等则n计数+1，n最终为相似度
        if hash1[i] == hash2[i]:
            n = n + 1
    return n/(shape[0]*shape[1])


def aHash(img, shape=(10, 10)):
    img = cv2.resize(img, shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    s = 0
    hash_str = ''
    for i in range(shape[0]):
        for j in range(shape[1]):
            s = s + gray[i, j]
    avg = s / 100
    for i in range(shape[0]):
        for j in range(shape[1]):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


if __name__ == '__main__':

    end_date = datetime(2023, 5, 27)
    now_date = datetime.now()
    if now_date > end_date:
        exit()

    hdc = win32gui.GetDC(0)
    width = win32print.GetDeviceCaps(hdc, win32con.HORZRES)
    print("当前分辨率%s" % width)
    guns_hash, wlzy_hash = pxHash(width)
    while True:
        allstart = time.time()
        shot_path = Shot.shot1(Shot.get_px(width).guns_area)
        shot_mat = cv2.imread(shot_path)
        shot_hash = aHash(shot_mat)
        indexWeapon = 0
        for i in guns_hash:
            cmp = cmpHash(shot_hash, i[0])
            print('%s匹配度:%s' % (i[1], cmp))
            if (cmp > 0.9):
                indexWeapon = i[1]
                if i[1] == 10:  # 哈沃克
                    wlzy = Shot.shot1(Shot.get_px(width).wlzy_area_hwk)
                    wlzy_shot = aHash(cv2.imread(wlzy))
                    if (cmpHash(wlzy_shot, wlzy_hash) > 0.9):
                        print("带涡轮增压的哈沃克")
                        indexWeapon = 12

                if i[1] == 11:
                    wlzy = Shot.shot1(Shot.get_px(width).wlzy_area_zhuanzhu)
                    wlzy_shot = aHash(cv2.imread(wlzy))
                    if (cmpHash(wlzy_shot, wlzy_hash) > 0.9):
                        print("带涡轮增压的专注轻机枪")
                        indexWeapon = 13
                print("与 %s 匹配，相似度" % indexWeapon)
                break
        if (indexWeapon == 0):
            print("无匹配 indexWeapon=%s" % indexWeapon)
        with open("C:\\jh.lua", "wb", buffering=0) as file:
            file.write(bytes("indexWeapon=%s" % indexWeapon, 'utf-8'))
            file.close
        time.sleep(2)
