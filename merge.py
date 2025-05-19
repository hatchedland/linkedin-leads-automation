import json
import os

# ------------------------------------------------------------
# CONFIG – adjust only if your paths change
# ------------------------------------------------------------
BASE_DIR   = r"C:\Users\khush\Linkedn-account-2"
FILE_ONE   = os.path.join(BASE_DIR, "leads.json")
FILE_TWO   = os.path.join(BASE_DIR, "leads2.json")
OUTPUT     = os.path.join(BASE_DIR, "combined-leads.json")

# ------------------------------------------------------------
# Helper to load a JSON array safely
# ------------------------------------------------------------
def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError(f"{path} does not contain a JSON array.")
            print(f"✅  Loaded {path} – {len(data)} records")
            return data
    except FileNotFoundError:
        raise SystemExit(f"❌  File not found: {path}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"❌  JSON error in {path}: {e}")

# ------------------------------------------------------------
# Load, merge, and de-dupe
# ------------------------------------------------------------
leads1 = load_json(FILE_ONE)
leads2 = load_json(FILE_TWO)

# Merge and remove duplicates by `id`
combined = {item["id"]: item for item in leads1 + leads2}.values()
combined_list = list(combined)

# ------------------------------------------------------------
# Save result
# ------------------------------------------------------------
with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(combined_list, f, ensure_ascii=False, indent=2)

print(f"\n🎉  Combined file written → {OUTPUT}  ({len(combined_list)} unique records)")
