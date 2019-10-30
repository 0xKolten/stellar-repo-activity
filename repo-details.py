import requests
import time
import json

def get_repo_data(repositories):
    # ---> Loop through repositories & get weekly commits + latest release / date
    for repo in repositories:
        # ---> Get commit details for the past week
        participation = '/stats/participation'
        releases = '/releases'
        p = requests.get(repositories[repo] + participation)
        p_data = p.json()
        print(repo, "commits: ", p_data['all'][51])
        # ---> Get latest release details
        r = requests.get(repositories[repo] + releases)
        r_data = r.json()
        print("Recent release: ", r_data[0]['tag_name'])
        print("Published: ", r_data[0]['published_at'], '\n')

if __name__ == '__main__':
    # ---> List of repositories to go through
    repositories = {
        'Stellar Core': 'https://api.github.com/repos/stellar/stellar-core',
        'Stellar Go Monorepo': 'https://api.github.com/repos/stellar/go',
        'JavaScript SDK': 'https://api.github.com/repos/stellar/js-stellar-base',
        'Python SDK': 'https://api.github.com/repos/StellarCN/py-stellar-base',
        'C# .NET SDK': 'https://api.github.com/repos/elucidsoft/dotnet-stellar-sdk',
        'Java SDK': 'https://api.github.com/repos/stellar/java-stellar-sdk',
        'Scala SDK': 'https://api.github.com/repos/Synesso/scala-stellar-sdk',
        'IOS SDK': 'https://api.github.com/repos/Soneso/stellar-ios-mac-sdk',
        'Ruby SDK': 'https://api.github.com/repos/stellar/ruby-stellar-base'
    }

    get_repo_data(repositories)
