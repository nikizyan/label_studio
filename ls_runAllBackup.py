import os
import requests
import json
from datetime import datetime

# Label Studio configurations
label_studio_configs = [
    {
        'url': 'http://YOUR.IP.ADDRESS:PORT1',
        'api_key': 'YOUR_API_KEY_PORT_1',
        'backup_dir': '/path/to/label_studio/backup/port1'
    },
    {
        'url': 'http://YOUR.IP.ADDRESS:PORT2',
        'api_key': 'YOUR_API_KEY_PORT_2',
        'backup_dir': '/path/to/label_studio/backup/port2'
    }
]

def export_projects_to_json(label_studio_url, api_key, backup_dir):
    headers = {
        'Authorization': f'Token {api_key}',
        'Content-Type': 'application/json'
    }

    print(f"Starting export process for {label_studio_url}...")
    # Get list of projects from Label Studio API
    projects_url = f'{label_studio_url}/api/projects?page=1'
    print(f"Fetching projects from: {projects_url}")
    response = requests.get(projects_url, headers=headers)
    print(f'Response status code: {response.status_code}')
    if response.status_code == 200:
        projects = response.json()
        if isinstance(projects, dict) and 'results' in projects:
            projects = projects['results']  # Adjust according to the actual response structure
        print(f'Fetched {len(projects)} projects')
        for project in projects:
            project_id = project['id']
            project_name = project['title']
            export_url = f'{label_studio_url}/api/projects/{project_id}/export'

            # Export project to JSON
            print(f"\nExporting project {project_name} from: {export_url}")
            export_response = requests.get(export_url, headers=headers)
            if export_response.status_code == 200:
                timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
                date = datetime.now().strftime('%Y-%m-%d')

                backup_dir_date = os.path.join(backup_dir, date)
                if not os.path.exists(backup_dir_date):
                    os.makedirs(backup_dir_date)

                filename = f'{backup_dir_date}/{project_name}-at-{timestamp}.json'
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(export_response.json(), f, ensure_ascii=False, indent=4)
                print(f'Exported project {project_name} to {filename}')
            else:
                print(f'Failed to export project {project_name}. Export API response status code: {export_response.status_code}')
    else:
        print("Failed to fetch projects from Label Studio API")

    print(f"Export process for {label_studio_url} completed.")

if __name__ == '__main__':
    for config in label_studio_configs:
        export_projects_to_json(config['url'], config['api_key'], config['backup_dir'])
