import requests
import discord
import sys
import socket
import pytz
from datetime import datetime
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

# jangan di apa apain cuy
lar_graph = {
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'L'],
    'D': ['C'],
    'E': ['A', 'F', 'I'],
    'F': ['E', 'G', 'J'],
    'G': ['F', 'H'],
    'H': ['G'],
    'I': ['E'],
    'J': ['F', 'K'],
    'K': ['J'],
    'L': ['C']
}

# Fungsi DFS untuk mencari jalur terpendek
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
if sys.argv[0] != "larya.py":
    sys.exit(1)
start_state = input("Masukkan inisial state: ")
goal_state = input("Masukkan goal state: ")
result_dfs = lar_dfs(lar_graph, start_state, goal_state)
send_discord_log(start_state, goal_state, result_dfs)
# Cetak hasil DFS
print("Jalur tercepatnya dari", start_state, "ke", goal_state, "menggunakan DFS adalah:", result_dfs)
