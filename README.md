# GitHub Pull Request Monitor
This tool makes it easy to track pull requests and send Slack notification for public GitHub repositories that are not under your control.
# Requirements
Set the variables such as:

owner = "GITHUB_USERNAME" (GitHub username of repo owner. e.g `arddluma`)

repo = "GITHUB_REPO" (GitHub repo name. e.g `gh-pull-request-monitor`)

api_key = "GITHUB_API_KEY" (Recommended: Create fine-grained token with `Public Repositories (read-only)` access or use `Tokens(classic)` *(not recommended)*)

slack_webhook_url = "SLACK_WEBHOOK_URL" (Slack incoming webhook webhook url)

Optional: time.sleep(60) = Change API polling period (in seconds)

# Run
Clone:
`git clone https://github.com/arddluma/gh-pull-request-monitor.git`

Script should run in background

*There are multiple ways to run python script in background, here is the list of some of them*

Use [pm2](https://www.npmjs.com/package/pm2) process manager

`pm2 start --name "PRMonitor" monitor.py  --interpreter=python3`

or
`python3 monitor.py &`

or
`nohup python3 monitor.py &`

or
`screen python3 monitor.py`
