# Label Studio Automatically Backup by using Python and Cron

1. Edit your Label Studio ip address, port, your api key, and backup dir in "ls_runAllBackup.py"
2. Go to your terminal, and type "crontab -e", scroll down to the last row by using arrow button, and enter the configuration at the last row as in "edit_your_crontab.txt"

Notes:
- My cron config is to backup at 12.oopm, Monday-Friday
- Please add backup folder /label_studio/backup/port1 and /label_studio/backup/port2
