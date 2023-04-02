import requests
import time
import json
import datetime

owner = "GITHUB_USERNAME"
repo = "GITHUB_REPO"
api_key = "GITHUB_API_KEY"
slack_webhook_url = "SLACK_WEBHOOK_URL"

url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

latest_pull_request_number = None

while True:
    response = requests.get(url, auth=(api_key, ""))
    
    if response.status_code == 200:
        data = response.json()
        print("Waiting for new PRs", datetime.datetime.now())
        
        if data:
            if latest_pull_request_number is not None and latest_pull_request_number != data[0]["number"]:
                new_pull_requests = [pull_request for pull_request in data if pull_request["number"] > latest_pull_request_number]
                
                if len(new_pull_requests) > 0:
                    message = f"{len(new_pull_requests)} new pull request(s) opened in {owner}/{repo}:\n"
                    for pull_request in new_pull_requests:
                        message += f"<{pull_request['html_url']}|{pull_request['title']}>\n"
                
                    payload = {
                        "text": message
                    }
                    response = requests.post(slack_webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
                
                    print(f"Slack message sent with status code {response.status_code}")
                
                    latest_pull_request_number = data[0]["number"]
            
            else:
                latest_pull_request_number = data[0]["number"]
        
        else:
            if latest_pull_request_number is not None:
                print(f"No open pull requests in {owner}/{repo}")
            latest_pull_request_number = None
    
    else:
        print(f"Error: {response.status_code}")
    
    time.sleep(60)
