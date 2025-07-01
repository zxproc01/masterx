import json
import os

# --- CONFIG ---
GITHUB_USER = "zxproc01"
REPO_NAME = "ninitproc14"
BRANCH = "master"
PROC_DIR = "proc"
OUTPUT_JSON_FILE = "live.json"

# Path to proc folder
proc_path = os.path.join(os.getcwd(), PROC_DIR)

# List all files in proc
files = os.listdir(proc_path)

# Filter for .mp4.enc files only (optional)
files = [f for f in files if f.endswith(".mp4.enc")]

if not files:
    print("⚠️ No .mp4.enc files found in proc folder.")
    exit(1)

# Build JSON list
json_list = []

for i, filename in enumerate(files, start=1):
    url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/refs/heads/{BRANCH}/{PROC_DIR}/{filename}"
    entry = {
        "name": f"Live wallpaper{i}",
        "url": url
    }
    json_list.append(entry)

# Write to JSON file
output_path = os.path.join(os.getcwd(), OUTPUT_JSON_FILE)
with open(output_path, "w") as f:
    json.dump(json_list, f, indent=2)

print(f"✅ JSON written to {output_path}")
