import pyautogui
import time

dis_hor = 37
dis_ver = 37
res = [0, 0]
pw = [1600, 2200]
forja = [1720, 3030]
selecionar = [1100, 2687]
fechar = [1340, 2461]
fechar_2 = [1654, 2408]
maxi = [1188, 2693]
inic = [1144, 2918]
comerc = [1751, 2626]
vender = [1626, 2800]
inven_1 = [1946, 2779]
inven_2 = [inven_1[0] + 4*dis_hor, inven_1[1] + dis_ver]
inven_3 = [2266, inven_1[1]]
inven_4 = [inven_3[0], inven_3[1] + dis_ver]
inven_5 = [inven_4[0] + 4*dis_hor, inven_4[1] + dis_ver]
inven_6 = [inven_4[0], inven_4[1] + 2*dis_ver]


def get_coord(coord):
    coord[0] += res[0]
    coord[1] += res[1]
    return coord[0], coord[1]


def click(coord):
    pyautogui.click(get_coord(coord))


def shift_doubleclick(coord):
    pyautogui.click(get_coord(coord))
    pyautogui.keyDown('shift')
    time.sleep(0.1)
    pyautogui.doubleClick(get_coord(coord))
    time.sleep(0.1)
    pyautogui.keyUp('shift')


def confirm_sell():
    click(vender)
    pyautogui.press('y')
    pyautogui.press('y')


def sell_first(coord):
    item = [coord[0], coord[1]]
    for i in range(8):
        item[0] = coord[0] + dis_hor*i
        pyautogui.rightClick(item)
    item = [coord[0], coord[1] + dis_ver]
    for i in range(4):
        item[0] = coord[0] + dis_hor*i
        pyautogui.rightClick(item)
    confirm_sell()


def sell_sec(coord1, coord2):
    item = [coord1[0], coord1[1]]
    for i in range(4):
        item[0] = coord1[0] + dis_hor*i
        pyautogui.rightClick(item)
    item = [coord2[0], coord2[1]]
    for i in range(8):
        item[0] = coord2[0] + dis_hor*i
        pyautogui.rightClick(item)
    confirm_sell()


if __name__ == "__main__":
    click(pw)
    for i in range(20):
        time.sleep(2)
        shift_doubleclick(forja)
        time.sleep(3)
        click(selecionar)
        time.sleep(1)
        click(maxi)
        time.sleep(0.1)
        click(inic)
        time.sleep(52)

        click(fechar)
        time.sleep(0.1)
        shift_doubleclick(comerc)
        time.sleep(5)
        click(selecionar)
        time.sleep(1)
        sell_first(inven_1)
        time.sleep(0.1)
        sell_sec(inven_2, inven_3)
        time.sleep(0.1)
        sell_first(inven_4)
        time.sleep(0.1)
        sell_sec(inven_5, inven_6)
        time.sleep(0.1)
        click(fechar_2)
