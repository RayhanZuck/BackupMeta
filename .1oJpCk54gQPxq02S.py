#Tools Backup By Rayhan
#Sc Buat Jalanin Sc Aja Di Recode LoL

import os, time

M = '\x1b[1;91m' # MERAH
K = '\x1b[1;93m' # KUNING
H = '\x1b[1;92m' # HIJAU
P = '\x1b[1;97m' # PUTIH
B = '\x1b[1;96m' # BIRU

os.system('clear')
print(f'{P}-----------------------------------------------------')
print(f"""| {M},---.          |              ,---,          |    {P}|{M}   
{P}| {M}|---',---.,   .|---.,---.,---. .-' .   .,---.|__/ {P}|{M} 
{P}| {M}|  \ ,---||   ||   |,---||   ||    |   ||    |  \ {P}|
{P}| `   ``---^`---|`   '`---^`   '`---'`---'`---'`   `|
{P}|           `---'                                   |""")
print(f'-----------------------------------------------------')
print(f'| {K}Tools Ini Dibuat Oleh Rayhan, Good Job ! {P}|')
print(f'--------------------------------------------')
print(f'| {H}Github Saya{P}  : github.com/RayhanZuck |')
print(f'| {H}Facebook Saya{P}: fb.com/Rayhan.27.Xyz  |')
print(f'| {H}Facebook Saya{P}: fb.com/RayhanBusiness |')
print(f'-----------------------------------------')
print(f'{P}| Ketik {H}Run {P}Untuk Masuk Ke Dalam Script |')
print(f'| Ketik {K}FB {P}Untuk Mengunjungi FB Author  |')
print(f'| Ketik {M}Out {P}Untuk Keluar Dari Script    |')
print(f'{P}-----------------------------------------')

pilih = input(f'{K}\nKetik{P}: {H}')
if pilih == 'run' or pilih == 'Run':
      __import__("meta").cek_pw()
if pilih == 'fb' or pilih == 'Fb':
      print(f'\n---------------------------------------------------\n| {K}>_< Terimakasih Telah Mengunjungi FB Author >_<{H} |\n---------------------------------------------------\n')
      os.system('xdg-open https://www.facebook.com/rayhanbusiness')
      time.sleep(3)
      os.system('python .1oJpCk54gQPxq02S.py')
if pilih == 'out' or pilih == 'out':
      print('Terimakasih Telah Menggunakan Script Ini Enjoy>_<\n')
      exit()
