# GitHub Activity CLI

A simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal.

Built as a solution for the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) project on roadmap.sh.

## Features

- **Fetch User Activity**: Retrieves the latest public events for any GitHub user.
- **Aggregated Output**: Groups repetitive events (like multiple commits to the same repo) into concise summary lines.
- **Event Support**: Handles various GitHub event types including:
  - `PushEvent` (aggregated by commit count)
  - `IssueCommentEvent` (aggregated by comment count)
  - `PullRequestEvent` (aggregated by action count)
  - `MemberEvent` (aggregated by rule modification count)
  - `CreateEvent` (branches/tags)
  - `DeleteEvent` (branches/tags)
  - `ForkEvent`, `WatchEvent`, `IssuesEvent`

## Prerequisites

- Python 3.6+
- Internet connection (to access GitHub API)

## Usage

Run the script from the command line by providing a GitHub username:

```bash
python github-activity.py <username>
```

### Example

```bash
python github-activity.py dhh
```

**Output:**

```text
Fetching activity for : dhh
Output:
- Pushed 23 commit(s) to basecamp/omarchy
- Left 5 issue comment(s) in basecamp/omarchy
- Deleted 1 branch(es)/tag(s) in basecamp/omarchy
- Made 1 pull request actions in basecamp/omarchy
```

## How it Works

The script fetches JSON data from the GitHub API (`https://api.github.com/users/<username>/events`) and parses it using Python's standard `urllib` and `json` libraries. It assumes no external dependencies are installed.
