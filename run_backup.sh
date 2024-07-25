#!/bin/bash

# Source Conda initialization script
source ~path/to/conda

# Activate Conda environment (adjust the environment name as per your setup)
conda activate nconda

# Verify Conda activation
echo "Conda environment activated: $(conda info --envs | grep '*' | awk '{print $1}')" >> /path/to/label_studio/backup_log.txt

# Function to perform the backup
perform_backup() {
    # Run the Python backup script
    $PYTHON /path/to/label_studio/ls_runAllBackup.py
    exit_status=$?

    if [ $exit_status -eq 0 ]; then
        echo "$(date +'%Y-%m-%d %H:%M:%S') - Backup successful" >> /label_studio/backup_log.txt
    else
        echo "$(date +'%Y-%m-%d %H:%M:%S') - Backup failed with exit code $exit_status" >> /label_studio/backup_log.txt
    fi

    return $exit_status
}

# Function to delete backups older than a week (multiple ports)
delete_oldest_backup() {
    for BACKUP_DIR in /path/to/label_studio/backup/port1 /path/to/label_studio/backup/port2; do
        # Calculate the date of one week ago
        old_date=$(date -d '7 days ago' +'%Y-%m-%d')
        old_backup_dir="$BACKUP_DIR/$old_date"

        if [ -d "$old_backup_dir" ]; then
            rm -rf "$old_backup_dir"
            echo "$(date +'%Y-%m-%d %H:%M:%S') - Deleted old backup: $old_backup_dir" >> /path/to/label_studio/backup_log.txt
        else
            echo "$(date +'%Y-%m-%d %H:%M:%S') - No backup found for date: $old_date in $BACKUP_DIR" >> /path/to/label_studio/backup_log.txt
        fi
    done
}

# Execute the functions
perform_backup
delete_oldest_backup
