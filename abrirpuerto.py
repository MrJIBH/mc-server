'''
def conectar_tunel():
    A = ''
    if configuracion[_F] == _M:
        B = configuracion[_W]
        os.system(f'ngrok authtoken {B}')
        conf.get_default().region = configuracion[_X]
        C = ngrok.connect(25565, 'tcp')
        A = str(C).split('\"')[1::2][0].replace('tcp://', '')
    else:  # inserted
        if configuracion[_F] == _b:
            if check_dependency(_b) == _B or not os.path.exists(f'{workspace_route}/tailscale-cs/'):
                os.chdir(f'{workspace_route}')
                os.system('git clone https://github.com/elyxdev/tailscale-cs/')
                os.system('sudo bash ./tailscale-cs/script.sh')
            os.system(f'sudo bash {workspace_route}/tailscale-cs/iniciar.sh > tailscale_log.txt 2>&1 &')
            cls()
            jilog('Tailscale iniciado!')
            jilog('Puede que necesites autentificarte a continuación.')
            os.system('sudo tailscale up')
            jilog('Autentificado e iniciado!')
            D, H = obtener_salida_comando('sudo tailscale ip')
            A = D.split(_U)[0]
        else:  # inserted
            if configuracion[_F] == _S:
                try:
                    jilog('Conectando a Serveo...')
                    os.system('echo StrictHostKeyChecking no > ~/.ssh/config')
                    E = f'ssh -o StrictHostKeyChecking=no -R 0:localhost:25565 serveo.net > {workspace_route}/serveo_ip.txt &'
                    os.system(E)
                    time.sleep(5)
                    with open(f'{workspace_route}/serveo_ip.txt', 'r') as F:
                        A = F.readlines()[0].split('from ')[1][:(-1)]
                    cls()
                except Exception as G:
                    report_to_mother(f'Serveo Error:\n{G}', typet=_E)
                    jilog('Error al usar Serveo, deberías considerar usar otro servicio!')
                    time.sleep(5)
    cls()
    jilog(f'La IP del servidor es: {A} ')
    time.sleep(4)
    if configuracion[_Z] == _A:
        enviar_a_webhook(f'La IP del servidor es:  \n```fix\n{A}\n```')
        '''
import os
workspace_route = os.getcwd()
os.system('echo StrictHostKeyChecking no > ~/.ssh/config')
E = f'ssh -o StrictHostKeyChecking=no -R 0:localhost:19132 serveo.net > {workspace_route}/serveo_ip_bedrock.txt &'
os.system(E)

with open(f'{workspace_route}/serveo_ip_bedrock.txt', 'r') as F:
    print(F.readlines())
print()

