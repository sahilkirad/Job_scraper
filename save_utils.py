import csv
import json
import os

def save_to_csv(data, filename="weworkremotely_jobs.csv"):
    if not data:
        print("[!] No data to save to CSV.")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"[✓] Saved {len(data)} job(s) to CSV: {filename}")

def save_to_json(data, filename="weworkremotely_jobs.json"):
    if not data:
        print("[!] No data to save to JSON.")
        return

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[✓] Saved {len(data)} job(s) to JSON: {filename}")