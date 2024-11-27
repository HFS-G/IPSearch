import requests
from colorama import init, Fore, Back, Style

# Инициализация colorama
init(autoreset=True)

logo = """
  _____ _____   _____                     _     
 |_   _|  __ \ / ____|                   | |    
   | | | |__) | (___   ___  __ _ _ __ ___| |__  
   | | |  ___/ \___ \ / _ \/ _` | '__/ __| '_ \ 
  _| |_| |     ____) |  __/ (_| | | | (__| | | |
 |_____|_|    |_____/ \___|\__,_|_|  \___|_| |_|"""

def get_ip_info(ip):
    data = {}

    try:
        # Попытка получить данные с ipinfo.io
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        if response.status_code == 200:
            data = response.json()
        else:
            print(Fore.YELLOW + "ipinfo.io не предоставил данные, переход к резервному API.")

        # Если данные отсутствуют, использовать резервный API ip-api.com
        if not data or 'error' in data:
            response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting,query')
            if response.status_code == 200:
                data = response.json()
                if data.get('status') != 'success':
                    print(Fore.RED + "ip-api.com также не смог предоставить данные.")
                    return
            else:
                print(Fore.RED + "ip-api.com также не смог предоставить данные.")
                return

        # Форматированный вывод информации
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "\n" + "-"*50)
        print(Fore.GREEN + f"{'IP:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('ip', data.get('query', 'N/A'))}")
        print(Fore.YELLOW + f"{'Хостнейм:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('hostname', 'N/A')}")
        print(Fore.CYAN + f"{'Anycast:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('anycast', 'N/A')}")
        print(Fore.MAGENTA + f"{'Город:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('city', 'N/A')}")
        print(Fore.BLUE + f"{'Регион:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('region', data.get('regionName', 'N/A'))}")
        print(Fore.RED + f"{'Страна:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('country', 'N/A')}")
           # Исправление: использование двойных кавычек внутри f-строки
        location = data.get('loc', f"{data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
        print(Fore.LIGHTMAGENTA_EX + f"{'Местоположение:':<25}" + Fore.WHITE + Style.BRIGHT + f" {location}")
        print(Fore.LIGHTYELLOW_EX + f"{'Провайдер:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('org', data.get('isp', 'N/A'))}")
        print(Fore.LIGHTBLUE_EX + f"{'ASN:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('asn', {}).get('asn', data.get('as', 'N/A'))}")
        print(Fore.LIGHTWHITE_EX + f"{'Компания:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('company', {}).get('name', data.get('asname', 'N/A'))}")
        print(Fore.LIGHTCYAN_EX + f"{'Оператор:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('carrier', {}).get('name', 'N/A')}")
        print(Fore.LIGHTMAGENTA_EX + f"{'Почтовый индекс:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('postal', data.get('zip', 'N/A'))}")
        print(Fore.LIGHTYELLOW_EX + f"{'Часовой пояс:':<25}" + Fore.WHITE + Style.BRIGHT + f" {data.get('timezone', 'N/A')}")
        print(Back.BLACK + Fore.WHITE + Style.BRIGHT + "-"*50 + "\n")

    except requests.RequestException as e:
        print(Fore.RED + f"Ошибка при получении данных: {e}")

if __name__ == "__main__":
    print(Fore.RED + logo)
    print()
    print("Crate By" + Fore.BLUE + " @hfsadm " + Fore.WHITE + "| Chanale: " + Fore.BLUE + "@hfsads" + Fore.WHITE + "        1.0")
    print()
    print()
    ip_address = input(Fore.WHITE + "Введите IP-адрес: ")
    get_ip_info(ip_address)
