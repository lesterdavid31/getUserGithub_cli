import requests

def userGithub(user):
    url = f'https://api.github.com/users/{user}/events'
    response = requests.get(url)
    
    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        events = response.json()
        for event in events:
            if event['type'] == 'IssueCommentEvent':
                print(f"Comento sobre el problema {event['payload']['issue']['number']}\n")
            elif event['type'] == 'PushEvent':
                print(f"Pushed to {event['repo']['name']}\n")
            elif event['type'] == 'IssuesEvent':
                print(f"Created issue {event['payload']['issue']['number']}\n")
            elif event['type'] == 'WatchEvent':
                print(f"Starred {event['repo']['name']}\n")
            elif event['type'] == 'PullRequestEvent':
                print(f"Created pull request {event['payload']['pull_request']['number']}\n")
            elif event['type'] == 'PullRequestReviewEvent':
                print(f"Reviewed pull request {event['payload']['pull_request']['number']}\n")
            elif event['type'] == 'PullRequestReviewCommentEvent':
                print(f"Comented on pull request {event['payload']['pull_request']['number']}\n")
            elif event['type'] == 'CreateEvent':
                print(f"Created {event['payload']['ref_type']} {event['payload']['ref']}\n")
            else:
                print(f"{event['type']}\n")
    else:
        print(f"Error {response.status_code}: {response.json()}")

# userGithub('lesterdavid31')

