import sys
import json
import urllib.request

def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User not found.")
        else:
            print(f"HTTP Error: {e.code}")
    except Exception as e:
        print(f"Error: {e}")
        return None

def process_uncountable(event):
    event_type = event['type']
    repo_name = event['repo']['name']
    event_count = []
        
    if event_type == "ForkEvent":
        return f"- Forked {repo_name}"
    elif event_type == "WatchEvent":
        return f"- Starred {repo_name}"
    else:
        return f"- {event_type} in {repo_name}"

def process_countable(events):
    commits_count = {}
    memberEvent_count = {}
    createEvent_count = {}
    issueCommentEvent_count = {}
    deleteEvent_count = {}
    pullRequestEvent_count = {}

    for event in events:
        repo_name = event['repo']['name']
        if event['type'] == 'PushEvent':
            commits_count[repo_name] = commits_count.get(repo_name, 0) + 1
        elif event['type'] == 'MemberEvent':
            memberEvent_count[repo_name] = memberEvent_count.get(repo_name, 0) + 1
        elif event['type'] == 'CreateEvent':
            createEvent_count[repo_name] = createEvent_count.get(repo_name, 0) + 1
        elif event['type'] == 'IssueCommentEvent':
            issueCommentEvent_count[repo_name] = issueCommentEvent_count.get(repo_name, 0) + 1
        elif event['type'] == 'DeleteEvent':
            deleteEvent_count[repo_name] = deleteEvent_count.get(repo_name, 0) + 1
        elif event['type'] == 'PullRequestEvent':
            pullRequestEvent_count[repo_name] = pullRequestEvent_count.get(repo_name, 0) + 1
        
    print("Output:")
    for repo, count in commits_count.items():
        print(f"- Pushed {count} commit(s) to {repo}")
    
    for repo, count in memberEvent_count.items():
        print(f"- Modified {count} member rule(s) in {repo}")
    
    for repo, count in createEvent_count.items():
        print(f"- Created {count} branch(es)/tag(s) in {repo}")
    
    for repo, count in issueCommentEvent_count.items():
        print(f"- Left {count} issue comment(s) in {repo}")

    for repo, count in deleteEvent_count.items():
        print(f"- Deleted {count} branch(es)/tag(s) in {repo}")

    for repo, count in pullRequestEvent_count.items():
        print(f"- Made {count} pull request actions in {repo}")

    return ['PushEvent', 
            'MemberEvent', 
            'CreateEvent', 
            'IssueCommentEvent', 
            'DeleteEvent',
            'PullRequestEvent']
            

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python github-activity.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Fetching activity for : {username}")
    
    events = fetch_activity(username)
    if events:
        handled_types = process_countable(events)

        for event in events:
            if event['type'] not in handled_types:
                print(process_uncountable(event))
