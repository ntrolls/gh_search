from github import Github

ACCESS_TOKEN="****************" // Your personal GitHub access token

if __name__ == '__main__':
    keywords = input("Enter keywords separated by spaces [e.g. pintos kaist]:")
    extensions = input("Enter specific file extensions you target, if you have any [e.g. py java scala]:")

    keywords = [s.strip() for s in keywords.split(" ")]
    extensions = [s.strip() for s in extensions.split(" ")]
    q = "+".join(keywords) + "+in:name+in:description+in:file"
    if len(extensions) > 0:
        q = q + "+" + "+".join("extension:" + x for x in extensions)
    
    g = Github(ACCESS_TOKEN)
    res = g.search_repositories(q)
    print(q)
    print(f'Found {res.totalCount} repo(s)')
    for repo in res:
        print(repo.clone_url)
