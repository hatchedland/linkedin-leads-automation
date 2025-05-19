import json, os, re
from datetime import datetime

# -------------------------------------------------
# 1. PATHS  – edit only if your folder changes
# -------------------------------------------------
COMBINED   = "combined-leads.json"
NEW_USERS  = "new_users.json"

# -------------------------------------------------
# 2. Util – strip to last 10 digits so +91… & 0… match
# -------------------------------------------------
def norm(phone: str) -> str:
    digits = re.sub(r"\D", "", phone or "")
    return digits[-10:]  # "" if fewer than 10 digits

# -------------------------------------------------
# 3. Load both files
# -------------------------------------------------
with open(COMBINED, "r", encoding="utf-8") as f:
    combined_data = json.load(f)

with open(NEW_USERS, "r", encoding="utf-8") as f:
    new_users_data = json.load(f)

# -------------------------------------------------
# 4. Index current phones in new_users
# -------------------------------------------------
existing_phones = {norm(u.get("phonenumber", "")) for u in new_users_data}

# -------------------------------------------------
# 5. Copy missing LinkedIn leads over
# -------------------------------------------------
added = 0
for lead in combined_data:
    phone_norm = norm(lead.get("phonenumber", ""))
    if not phone_norm:
        continue  # skip bad / empty phone
    if phone_norm in existing_phones:
        continue  # already present
    # otherwise, append
    new_users_data.append(lead)
    existing_phones.add(phone_norm)
    added += 1

print(f"✅  {added} LinkedIn leads appended to new_users.json")

# -------------------------------------------------
# 6. Backup & overwrite the new_users file
# -------------------------------------------------
ts   = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_path = f"{NEW_USERS}.{ts}.bak"
os.rename(NEW_USERS, backup_path)
print(f"🗃️  Backup saved → {backup_path}")

with open(NEW_USERS, "w", encoding="utf-8") as f:
    json.dump(new_users_data, f, indent=2, ensure_ascii=False)

print(f"🎉  new_users.json updated – total records: {len(new_users_data)}")
