# LinkedIn Leads Automation

A tool for automating the process of collecting and managing LinkedIn leads, using Firebase for data storage.

## Files

- `export-collection.js`: Main script for exporting LinkedIn leads.
- `leads.py`: Python script for lead management.
- `link.py`: Python script for handling LinkedIn links.
- `merge.py`: Python script for merging lead data.
- `update-firebase.js`: Script for updating Firebase with lead data.
- `run_scripts.sh`: Shell script to run after installing dependencies.

## Dependencies

- `firebase-admin`
- `playwright`
- `python-dotenv`

## Installation

### Python Virtual Environment

1.  Create a virtual environment using `python3 -m venv venv`.
2.  Activate the virtual environment using `source venv/bin/activate`.
3.  Install the Python dependencies using `pip install -r requirements.txt`.


### Running the Scripts

1.  Run the `run_scripts.sh` script using `./run_scripts.sh`. The script will install the Python dependencies from the `requirements.txt` file.
