import requests
import os

names = ['Krakened76', 'Asaka_aqua', 'Cyan_Bunny', 'tiange98', 'Garry_Lokei', 'circuit_Z', 'Edgardo_qwq', 'saber977', 'Dazzlingme', '9yiyiyi', 'FeiNiaoCou', 'chen1979', 'Aiba_Yukina', 'bigyummyy', 'chen1256', '19hugo', 'Bugalin2007', '114514yeshou', '1600425548', 'SmileyJay', 'FatCat', 'Selimers', 'sophie_desu', 'zhangyi123', 'mieamie', 'Kakng', 'tapia54', 'Track07_cda', 'Chirski_Eidu', 'HGwolf', 'YGOOB', 'Tao_xing']

for name in names:
    if not os.path.exists(name + '.jpg'):
        url = 'https://minecraftskinstealer.com/api/v1/skin/download/face/' + name
        face = requests.get(url)
        playFile = open(name + '.jpg' ,'wb')
        playFile.write(face.content)

print('完成')
