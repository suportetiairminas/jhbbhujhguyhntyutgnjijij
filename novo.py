import yt_dlp
import getpass
import os
from InquirerPy import inquirer
from colorama import init, Style, Fore
from time import sleep

init()#para o colorama
user = getpass.getuser()#quem es tu?
caio = f"""{user} aqui tem seu contexto:
    1: para adicionar links de videos so escolher a opçao e colocar os links
    mas agora temos uma nova adiçao, o poder de colocar varios links em sequencia, so adionar um espaço entre eles, a quantidade de espaços entre links nao alteram, e pode ser a quantidade que voce quiser
    ex:(link1 link2     link3   link4  link5) ai enter na quantidade que voce estiver ok
    2: musica=caso quiser so audios
    3: videos=so videos
    4:sair=sair, qeria que fosse o que, hakear o serasa? vdd gostei da ideia caio."""
def downloa():#voce esta rodando isso aonde?
    sys = os.name
    if sys == 'posix':
        soiu = os.path.expanduser('~/Downloads')
    if sys == 'nt':
        soiu = os.path.expanduser('~\Downloads')
    return soiu

download_dir = str(downloa())

def musicas():
    link = input("manda os links")
    link = link.split()
    for i in link:
        sleep(1)
        tube = i
        ydl_opts = {
                'format': r'mp4',
                "outtmpl": os.path.join(download_dir, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    }]
                }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(tube)

def videos():
    link = input("manda os links")
    link = link.split()
    for i in link:
        sleep(1)
        tube = i
        ydl_opts = {
                'format': r'mp4',
                "outtmpl": os.path.join(download_dir, '%(title)s.%(ext)s'),
                }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(tube)


while True:
    quer = inquirer.select(
        message='qual opçao voce quer?',
        choices=['audio', 'video', 'sair', 'info', 'limpo'],
        default="Python",).execute()#a porra da GUI
    if "audio" in str(quer):
        musicas()
        continue
    elif "video" in str(quer):
        videos()
        continue
    elif "sair" in str(quer):
        break
    elif "info" in str(quer):
        print(Fore.GREEN + caio)
        continue
    elif "limpo" in str(quer):
        print("\n" *  200)
        continue

