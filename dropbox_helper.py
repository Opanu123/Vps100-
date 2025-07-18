import os
import dropbox

# Get your Dropbox token from GitHub Secrets
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Upload the backup.zip to Dropbox folder /minecraft-backup/
with open("backup.zip", "rb") as f:
    dbx.files_upload(f.read(), "/minecraft-backup/backup.zip", mode=dropbox.files.WriteMode("overwrite"))

print("✅ Uploaded backup.zip to Dropbox")
