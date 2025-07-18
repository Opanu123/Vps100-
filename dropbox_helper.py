import dropbox
import os
import sys

# Using DROPBOX_TOKEN from GitHub secrets
ACCESS_TOKEN = os.environ['DROPBOX_TOKEN']

def upload(local_path, dropbox_path):
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    with open(local_path, "rb") as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    print(f"✅ Uploaded to Dropbox at {dropbox_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] != "upload":
        print("Usage: python3 dropbox_helper.py upload <local_path> <dropbox_path>")
        sys.exit(1)
    upload(sys.argv[2], sys.argv[3])
