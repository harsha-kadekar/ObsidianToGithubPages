# ObsidianToGithubPages
This is a script which converts obsidian notes to github pages


## Prereq

- This script assumes that you already have your github pages posts and pages are stored in your obsidian vault `blog` folder. 
- The obsidian valut and github pages are in your local disk.
- This is a python based script and hence, it accepts python is already installed in your system.
- This script uses [obyde](https://github.com/notkmhn/obyde) to do the conversion. The script accepts already obyde is installed.

## Execute

Download the script `obsidian_to_githubpages.py` and this can be executed with this command line

```
./obsidian_to_githubpages.py --obsidian_local_vault <local path of the obsidian vault> --github_pages_repo_local <local repository path of github pages>
```

Example - 

```
./obsidian_to_githubpages.py --obsidian_local_vault "/home/myalias/workspace/mypersonalvault" --github_pages_repo_local "/home/myalias/workspace/mypages-blog"
```

