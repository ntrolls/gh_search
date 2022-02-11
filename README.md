## GitHub Repository Search Tutorial
This document briefly explains how one can deal with public GitHub repositories that contain course assignment artifacts. These repositories can be used as students to cheat. We will discuss how to use GitHub's search API to identify such repositories: once you find them, you can contact the owners and ask them to either take it down or turn it into a private repo.

### GitHub Search API

GitHub provides a powerful code search API, which is documented [here](https://docs.github.com/en/rest/reference/search#search-code). The API can be used either to write a simple tool that makes the search easier, or even to periodically run the search.

Here is a simple GitHub search script written in Python. As input, it will take 1) a set of keywords that you think specifically appear in the assignment code, and 2) (optional) file extension. If the script finds any repositories that meet the search criteria, it will print out the list of repo URLs. 

### Requirements

We use [PyGitHub](https://github.com/PyGithub/PyGithub) for the sake of convenience. It is documented [here](https://pygithub.readthedocs.io/en/latest/). You can simply install it using `pip`. The script has been tested under Python3.

```bash
$ pip install pygithub
```

You also need an access token to use the GitHub API. To get one, follow the instruction below.

1. Log into your [GitHub](https://github.com) account.
2. Go to your profile setting. You can find the link in the drop-down menu which hides behind your profile picture in the top-right corner, or alternatively can click: [https://github.com/settings/profile](https://github.com/settings/profile).![](step1.png)
3. Go to the developer settings in the left pane menu (at the bottom). Alternatively, click [https://github.com/settings/apps](https://github.com/settings/apps).![](step2.png)
4. Click "Personal access tokens".![](step3.png)
5. Click "Generate new token"![](step4.png)
6. Check `public_repo` because that is what we want to access. Leave a description in the Note field if necessary. Note that GitHub strongly recommends you to set expiration date for your token for security concerns. Once it expires, you need to get a new token. ![](step5.png)
7. You will get a new token. Copy and save the token string somewhere safe.

### Code

Now we are ready to execute the search script. The string `ACCESS_TOKEN` should contain your GitHub access token.

```python
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
```

Here's an example (account names are redacted on purpose):

![](example.png)

### Maintenance & Bug Reports

If you find any issues with the process or the code, please contact [shin.yoo@kaist.ac.kr](mailto:shin.yoo@kaist.ac.kr).