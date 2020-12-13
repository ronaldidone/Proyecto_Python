import requests,json,glob,os,shutil,msvcrt

fo = open("\\\\192.168.0.4\\t$\\efact\\envio.txt", "r")
contenido = fo.read()
fo.seek(0, 0)

#if contenido == '':
 #    letra = 0
#else:
tmp = fo.readlines()[-1]
tmp = tmp.split()
letra = tmp[0]
fo.close()
print(letra)
      
URL = "http://localhost/bcontrollerb/public/api/login"
password2 = "secret"
username2 = "ronald.idone@gmail.com"
type2 = "password"
headers  ={}# {"Content-Type": "application/x-www-form-urlencoded","Authorization": "Basic Y2xpZW50OnNlY3JldA=="}
params = {
"username": username2,
    "password": password2,
    "grant_type": type2
}    

      
resp = requests.post(URL , headers = headers ,params=params, data=json.dumps(params))

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
    
else:
    print('Hay Token')

acceso=resp.json()
token=acceso["access_token"]

print(letra)
