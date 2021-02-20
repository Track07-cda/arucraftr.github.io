names = ['Krakened76', 'Asaka_aqua', 'Cyan_Bunny', 'tiange98', 'Garry_Lokei', 'circuit_Z', 'Edgardo_qwq', 'saber977', 'Dazzlingme', '9yiyiyi', 'FeiNiaoCou', 'chen1979', 'Aiba_Yukina', 'bigyummyy', 'chen1256', '19hugo', 'Bugalin2007', '114514yeshou', '1600425548', 'SmileyJay', 'FatCat', 'Selimers', 'sophie_desu', 'zhangyi123', 'mieamie', 'Kakng', 'tapia54', 'Track07_cda', 'Chirski_Eidu', 'HGwolf', 'YGOOB', 'Tao_xing']
names.sort()

def outhtml():
    for name in names:
        print('            <li><div class="card"><img src="'+'/faces/'+name+'.jpg'+'" class="positive"><div class="negative"><br>个人留言</div></div><p>'+name+'</p></li>')
outhtml()