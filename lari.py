#Tools Backup By Rayhan

import os,sys,time,requests,json,re,random,itertools,threading
from colorama import Fore,Back,init

M = '\x1b[1;91m' # MERAH
K = '\x1b[1;93m' # KUNING
H = '\x1b[1;92m' # HIJAU
P = '\x1b[1;97m' # PUTIH
B = '\x1b[1;96m' # BIRU

os.system('clear')
os.system('git pull')
print(f"""
{M}                                                  
,---.          |              ,---,          |    
|---',---.,   .|---.,---.,---. .-' .   .,---.|__/ 
|  \ ,---||   ||   |,---||   ||    |   ||    |  \ 
{P}`   ``---^`---|`   '`---^`   '`---'`---'`---'`   `
          `---'                                   
---------------------------------------------------
""")
print(f'{K}Tools Created By Rayhan\n')
print(f'{B}Ketika Crack Diharuskan Memasukkan Username\nDan Password, Masukkan Seperti Dibawah!\n')
print(f'{P}[{K}?{P}] Enter SC Username ({H}required{P}) : {H}meta')
print(f'{P}[{K}?{P}] Enter Sc Passwoed ({H}required{P}) : {H}metaroyid\n')
print(f'{M}Sc Ini Bukan Buatan Saya Melainkan ({P}Roy ID{M})!!\n')

print(f'{P}Ketik {H}Run {P}Untuk Masuk Ke Dalam Script\nKetik {M}Out {P}Untuk Keluar Dari Script')
pilih = input(f'{K}\nKetik{P}: ')
if pilih == 'run' or pilih == 'Run':
      __import__("meta").cek_pw()
if pilih == 'out' or pilih == 'Out':
      print(f'{B}\nTerimakasih Telah Menggunakan Tools Ini Enjoy>_<\n')
      
