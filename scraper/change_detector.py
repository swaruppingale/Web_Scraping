import json
import hashlib

def hash_content(content):
    return hashlib.sha256(content.encode()).hexdigest()

def is_content_changed(url, content, snapshot_file):
    new_hash = hash_content(content)

    try:
        with open(snapshot_file, "r") as f:
            old_data = json.load(f)
    except FileNotFoundError:
        old_data = {}

    if old_data.get(url) != new_hash:
        old_data[url] = new_hash
        with open(snapshot_file, "w") as f:
            json.dump(old_data, f, indent=2)
        return True

    return False
