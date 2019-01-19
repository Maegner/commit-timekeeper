import json, subprocess
import CommitData as cdata
import os, operator

PROPERTIES_FILE_NAME = 'gitProperties.json'
SPLITTER = '-()-'
CMD_BRANCH = 'git log --branches  --source --pretty=oneline --author="{}" --after="{}"  --no-merges --no-decorate'
CMD_DATE = 'git log --branches --author="{}" --after="{}" --format="format:%H-()-%cd" --no-merges --date="unix"'

def parseGitProperties():
    with open(PROPERTIES_FILE_NAME) as f:
        configs = json.load(f)
        return configs['repositories'], configs['user']

def log_repository(path,cmd_branch,cmd_date):
    os.chdir(path)
    commits_by_branch = subprocess.getoutput('{}'.format(cmd_branch)).split('\n')
    commits_by_date = subprocess.getoutput('{}'.format(cmd_date)).split('\n')
    info = {}
    for commit_branch, commit_date in zip(commits_by_branch,commits_by_date):
            hash_branch_infos = commit_branch.split()
            hash_date_infos = commit_date.split(SPLITTER)
            if not hash_branch_infos or not hash_date_infos:
                    continue
            commit = info.get( hash_branch_infos[0],cdata.CommitData(hash_branch_infos[1]) )
            commit.set_date(hash_date_infos[1])
            info[hash_branch_infos[0]] = commit
    return store_path_commit_data_to_list(info)

def store_path_commit_data_to_list(dictionary):
        info_list = []
        for _,value in dictionary.items():
                info_list.append(value)
        return info_list

def log_all(since):
        paths,user = parseGitProperties()
        cmd_date = CMD_DATE.format(user,since)
        cmd_branch = CMD_BRANCH.format(user,since)
        commits = []
        for path in paths:
                commits += log_repository(path,cmd_branch,cmd_date)
        return sorted(commits,key=operator.attrgetter('date'))