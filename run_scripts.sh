# environment setup

# scripts
python leads.py
rm -rf linkedin_user_data
python leads2.py
python merge.py
# exporting new_users
node export-collection.js
python link.py


node update-firebase.js


rm -rf downloads
rm all_leads.csv
rm leads.json
rm linkedin_account_ids.csv
rm new_users.json


# 








