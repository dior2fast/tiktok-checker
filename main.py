from urllib3 import disable_warnings
import os
from os import system
import threading
import time
import logging
try:
    import requests
except:
    print("Requests not found installing module now...")
    system('pip install requests')
    import requests
try:
    from colorama import Fore, Back, Style
except:
    print("Colorama not found installing module now...")
    system('pip install colorama')
    from colorama import Fore, Back, Style
logging.getLogger('suds').setLevel(logging.WARNING)
disable_warnings()

class Main:
    def __init__(self):
        disable_warnings()
        print(Fore.RED)
        print("  _          _        ")
        print(" | |        | |       ")
        print(" | |__   ___| |_ __ _ ")
        print(" | '_ \ / _ \ __/ _` |")
        print(" | |_) |  __/ || (_| |")
        print(" |_.__/ \___|\__\__,_|")
        print(Fore.GREEN + f"coded by dior / beta\ndsc.gg/betalol")
        self.variables = {
            'available': 0,
            'unavailable': 0,
            'retries': 0
        }
        try:
            self.threads = int(input(Fore.WHITE + "Threads: "))
        except ValueError:
            print("Please enter a valid number of threads!")
            os.system(
                'title [TikTok Username Checker] - Restart required && '
                'pause >NUL && '
                'title [TikTok Username Checker] - Exiting...'
            )
            time.sleep(3)
            quit()
        
    def _checker(self, arg):
        try:
            arg = arg.replace("\n", '')
            url=(f"https://api19-normal-c-useast1a.tiktokv.com/aweme/v1/unique/id/check/?unique_id={arg}&iid=7026260912928425734&device_id=7026260845073188357&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=210602&version_name=21.6.2&device_platform=android&ab_version=21.6.2&ssmix=a&device_type=SM-N975F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=f0bfccc997a123b5&manifest_version_code=2022106020&resolution=720*1280&dpi=240&update_version_code=2022106020&_rticket=1636035582804&current_region=NZ&app_type=normal&sys_region=US&mcc_mnc=53001&timezone_name=Asia%2FShanghai&residence=NZ&ts=1636035582&timezone_offset=28800&build_number=21.6.2&region=US&uoo=0&app_language=en&carrier_region=NZ&locale=en&op_region=NZ&ac2=wifi&cdid=8a438d2e-2dea-4dc4-b7a9-ffa83828570e")
            
            headers={
                    'Host': 'api19-normal-c-useast1a.tiktokv.com',
                    'Connection': 'keep-alive',
                    'x-Tt-Token': '012a6b6d6f0ca859868c920bed0fbc89de00dc324a56c811a80996dd798c7aa36503752930344e7b10db7fed42a72a4149da3907477f89775bfae0244a20fe48ef254133b42c049f24deb2121b9197cd17e8c-1.0.0',
                    'sdk-version': '2',
                    'User-Agent': 'com.zhiliaoapp.musically/2022106020 (Linux; U; Android 7.1.2; en_US; Build/N2G48H;tt-ok/3.10.0.2)',
                    'x-tt-store-idc': 'alisg',
                    'x-tt-store-region': 'de',
                    'Accept-Encoding': 'gzip, deflate'
                }
            
            available = requests.get(url, headers=headers, verify=False).json()['is_valid']

        except Exception as e:
            self.variables['retries'] += 1
            self._checker(arg)
        else:
            if available == True:
                self.variables['available'] += 1
                print(Fore.GREEN + f'[AVAILABLE] {arg}')
                with open('Available.txt', 'a') as f:
                    f.write(f'{arg}\n')
            else:
                self.variables['unavailable'] += 1
                print(Fore.RED + f'[UNAVAILABLE] {arg}')
    def _multi_threading(self):
        threading.Thread(target=self._update_title).start()

        for username in self.usernames:
            attempting = True

            while attempting:
                if threading.active_count() <= self.threads:
                    threading.Thread(target=self._checker, args=(username,)).start()
                    attempting = False

    def _update_title(self):
        while (checked := (self.variables['available'] + self.variables['unavailable'])) < len(
            self.usernames
        ):
            os.system(
                f'title [TikTok Username Checker by betalol] - Checked: {checked}/{self.total_usernames} ^| Av'
                f'ailable: {self.variables["available"]} ^| Unavailable: '
                f'{self.variables["unavailable"]} ^| Retries: {self.variables["retries"]}'
            )
            time.sleep(0.2)
        os.system(
            f'title [TikTok Username Checker by betalol] - Checked: {checked}/{self.total_usernames} ^| Availa'
            f'ble: {self.variables["available"]} ^| Unavailable: {self.variables["unavailable"]} ^|'
            f' Retries: {self.variables["retries"]} && pause >NUL'
        )

    def setup(self):
        error = False
        if os.path.exists((usernames_txt := 'Usernames.txt')):
            with open(usernames_txt, 'r', encoding='UTF-8', errors='replace') as f:
                self.usernames = f.read().splitlines()
            self.total_usernames = len(self.usernames)
            if self.total_usernames == 0:
                error = True
        else:
            open(usernames_txt, 'a').close()
            error = True

        if error:
            print('[!] Paste the usernames in Usernames.txt.')
            os.system(
                'title [TikTok Username Checker] - Restart required && '
                'pause >NUL && '
                'title [TikTok Username Checker] - Exiting...'
            )
            time.sleep(3)
        else:
            self._multi_threading()


if __name__ == '__main__':
    os.system('cls && title [TikTok Username Checker]')
    disable_warnings()
    main = Main()
    main.setup()
