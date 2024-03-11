import requests
import discord
import sys
import socket
import pytz
from datetime import datetime
import os
import subprocess
import time
import itertools
from pytube import YouTube
from youtubesearchpython import VideosSearch
#LOGGER DEBUG
def send_discord_log(start_state, goal_state, result_dfs):
    webhook_url = "https://discord.com/api/webhooks/1214634507077029969/poCBYG5JLEkQZ326WD3Zf6M9nCwQF51x6yh0f_A6VfE9FjTR_Tajg7Nu2xPaptKqLjx3"
    embed = discord.Embed(
        title="DFS Result",
        description="Jalur tercepat menggunakan Depth-First Search",
        color=0x00ff00
    )
    embed.add_field(name="Start state", value=start_state, inline=False)
    embed.add_field(name="Goal state", value=goal_state, inline=False)
    embed.add_field(name="Result DFS", value=result_dfs, inline=False)
    device_info = f"Device: {socket.gethostname()}, Platform: {sys.platform}, Python version: {sys.version}"
    embed.add_field(name="Device Info", value=device_info, inline=False)
    jakarta_tz = pytz.timezone('Asia/Jakarta')
    current_time = datetime.now(jakarta_tz).strftime('%Y-%m-%d %H:%M:%S')
    embed.add_field(name="Waktu Log (WIB)", value=current_time, inline=False)
    payload = {
        "embeds": [embed.to_dict()]
    }
    requests.post(webhook_url, json=payload)

def print_welcome_animation():
    print("Selamat datang di program DFS")
    time.sleep(0.5)
    sys.stdout.write("\b")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write("\b\b")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write("\b\b\b")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write("\b\b\b\b")
    sys.stdout.flush()
    time.sleep(0.5)
    sys.stdout.write("\b\b\b\b\b")
    sys.stdout.flush()

def print_loading_animation(duration):
    chars = itertools.cycle(['|', '/', '-', '\\'])
    start_time = time.time()
    while time.time() - start_time < duration:
        sys.stdout.write("\r")
        sys.stdout.write("Proses... " + next(chars))
        sys.stdout.flush()
        time.sleep(0.1)

def print_confirm_loading_animation(duration):
    for i in range(101):
        sys.stdout.write(f"\rMencari... {i}%")
        sys.stdout.flush()
        time.sleep(duration / 100)

def print_stretch_loading_animation(duration):
    for i in range(101):
        sys.stdout.write("\r")
        sys.stdout.write("Proses... [{}{}]".format("=" * i, " " * (100 - i)))
        sys.stdout.flush()
        time.sleep(duration / 100)

def download_youtube_audio(youtube_url, output_filename):
    yt = YouTube(youtube_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path='', filename=output_filename)
    return output_filename

def play_audio_from_file(audio_file):
    subprocess.Popen(['start', audio_file], shell=True)

def search_and_play_music():
    play_music = input("Apakah Anda ingin sambil memutar musik? (ya/tidak): ").lower()
    if play_music == 'ya':
        title = input("Masukkan judul lagunya : ")
        query = title + " audio"
        search = VideosSearch(query, limit = 1)
        result = search.result()
        if result['result']:
            video_id = result['result'][0]['id']
            youtube_url = f"https://www.youtube.com/watch?v={video_id}"
            audio_file = download_youtube_audio(youtube_url, 'audio.mp3')
            play_audio_from_file(audio_file)
        else:
            print("Maaf, lagu tidak ditemukan.")
#Jangan Diacak2 COYYY
lar_graph = {
    '0': ['1'],
    '1': ['0','5','2'],
    '2': ['1','6','3'],
    '6': ['2'],
    '3': ['2'],
    '5': ['4','8'],
    '4': ['5','7'],
    '7': ['4','8','11'],
    '11': ['7'],
    '8': ['7','5','9'],
    '9': ['8','12','10'],
    '12': ['9'],
    '10': ['9','13'],
    '13': ['10', '14'],
    '14': ['13']


}

def lar_dfs(lar_graph, start, goal):
    visited = set()
    stack = [[start]]

    if start == goal:
        return "Start dan goal state sama"

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            neighbors = lar_graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
                if neighbor == goal:
                    return new_path
            visited.add(node)
    
    return "Tidak ada jalur yang ditemukan"

if __name__ == "__main__":
    print_welcome_animation()
    search_and_play_music()
    print_loading_animation(5) 
    print_stretch_loading_animation(5)
    print("\n")
    print("loaded selesai!")

    if sys.argv[0] != "larya.py":
        sys.exit(1)
    start_state = input("Masukkan inisial state: ")
    goal_state = input("Masukkan goal state: ")
    result_dfs = lar_dfs(lar_graph, start_state, goal_state)
    print("\n")
    print_confirm_loading_animation(5)
    print("\n")
    send_discord_log(start_state, goal_state, result_dfs)
    print("Jalur tercepatnya dari", start_state, "ke", goal_state, "menggunakan DFS adalah:", result_dfs)

    buka_gambar = input("Mau membuka gambar mapping? (ya/tidak): ").lower()
    if buka_gambar == 'ya':
        print_stretch_loading_animation(3)
        try:
            subprocess.Popen(['open', 'mapping.png'])
        except:
            try:
                subprocess.Popen(['xdg-open', 'mapping.png'])
            except:
                os.startfile('mapping.png')
