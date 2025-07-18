import dropbox
import os

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
BACKUP_FILE = "backup.zip"

dbx = dropbox.Dropbox(ACCESS_TOKEN)

with open(BACKUP_FILE, "rb") as f:
    dbx.files_upload(f.read(), f"/vps_backups/{BACKUP_FILE}", mode=dropbox.files.WriteMode.overwrite)

print("✅ Backup uploaded to Dropbox.")
