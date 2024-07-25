# Label Studio Automatically Backup by using Python and Cron

1. Edit your Label Studio ip address, port, your api key, and backup dir in "ls_runAllBackup.py"
2. Go to your terminal, and type "crontab -e", scroll down to the last row by using arrow button, and enter the configuration at the last row as in "edit_your_crontab.txt"

Notes:
- My cron config is to backup at 12.oopm, Monday-Friday
- Please add backup folder /label_studio/backup/port1 and /label_studio/backup/port2

# Duplicate Checker for Comparing the Dataset with the Backup

1. Open "ls_duplicateChecker.py", edit your directories, run the code
2. Go to Label Studio, import the "cleaned_data.csv"(no annotation/label)
3. Import again but this time is the backup json file (pre-annotations, with skipped/cancelled tasks)

Notes:
- Please change read csv/json file based on your dataset
