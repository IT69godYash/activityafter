import os
import random
import datetime

# Replace this with your local repository path
repo_path = "C:/path/to/your/repo"

# Replace with your GitHub repository URL
repo_url = "https://github.com/yourusername/your-repo.git"

# Set the branch to push changes
branch_name = "main"

# Change to your repository directory
os.chdir(repo_path)

# Get today's date
today = datetime.datetime.now()
weekday = today.weekday()

# Check if today is a weekday (0 = Monday, 4 = Friday)
if weekday < 5:  # Exclude weekends (Saturday, Sunday)
    # Randomize number of commits (1–5 per day)
    commits = random.randint(1, 5)

    for i in range(commits):
        # Generate a random timestamp for today
        commit_time = today.replace(hour=random.randint(9, 17), minute=random.randint(0, 59))
        commit_date = commit_time.strftime("%Y-%m-%d %H:%M:%S")

        # Create an empty commit with a timestamp
        os.system(f'git commit --allow-empty -m "Organic contribution on {commit_date}" --date="{commit_date}"')

    # Push changes to the repository
    os.system(f"git push origin {branch_name}")

print("Today's contributions have been added and pushed to the repository.")
