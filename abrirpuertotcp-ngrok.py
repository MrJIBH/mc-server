#ingeniería inversa al script inicial
try:
    from pyngrok import conf, ngrok
except:
    os.system('pip -q install pyngrok')
    from pyngrok import conf, ngrok

A = ''
import os
token = '2g6i5svXLSkYL9tUyQIYgZL8OHy_7AfL62zejSSr7HazYnTr8'
os.system(f'ngrok authtoken {token}')
conf.get_default().region = 'us'
C = ngrok.connect(19132, 'udp')
A = str(C).split('\"')[1::2][0].replace('udp://', '')