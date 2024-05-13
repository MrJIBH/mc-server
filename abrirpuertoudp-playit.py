import os
from datetime import datetime
from discord_webhook import DiscordWebhook

os.system(f'curl -SsL https://playit-cloud.github.io/ppa/key.gpg | sudo apt-key add -') 
os.system(f'sudo curl -SsL -o /etc/apt/sources.list.d/playit-cloud.list https://playit-cloud.github.io/ppa/playit-cloud.list')
print('Actualizando')
os.system(f'sudo apt update &>/dev/null && sudo apt install playit &>/dev/null && echo "Playit.gg instalado" || echo "Error al instalar playit"')
os.system(f'playit')

'''
A = datetime.now()
B = str(datetime.timestamp(A)).split('.')[0]
C = f'> <t:{B}>: {msg}'
D = DiscordWebhook(url='https://discord.com/api/webhooks/1239444589606342766/OneW8KEZO8oeniynbysIIz-B7no9Qah366TxeaTIbhReaQMVppHdMovz9KnUiz-iGpqV', content=C)
D.execute()
'''