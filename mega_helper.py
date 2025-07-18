# mega_helper.py
import sys
import os
from mega import Mega

def mega_login():
    email = os.getenv("MEGA_EMAIL")
    password = os.getenv("MEGA_PASSWORD")
    mega = Mega()
    return mega.login(email, password)

def download_plugins(mega, remote_folder, local_folder):
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)
    files = mega.get_files()
    for file_id, file_info in files.items():
        if 'a' in file_info:
            name = file_info['a']['n']
            if name.startswith(remote_folder):
                print(f"Downloading {name} ...")
                mega.download(file_info, dest_path=local_folder)

def upload_backup(mega, local_file, remote_path):
    print(f"Uploading {local_file} to {remote_path} ...")
    mega.upload(local_file, remote_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:\n  python3 mega_helper.py upload <local_path> <remote_path>\n  python3 mega_helper.py download_plugins <remote_folder> <local_folder>")
        sys.exit(1)
    mega = mega_login()
    cmd = sys.argv[1]
    if cmd == "upload":
        local_file = sys.argv[2]
        remote_path = sys.argv[3]
        upload_backup(mega, local_file, remote_path)
    elif cmd == "download_plugins":
        remote_folder = sys.argv[2]
        local_folder = sys.argv[3]
        download_plugins(mega, remote_folder, local_folder)
    else:
        print("Unknown command")
