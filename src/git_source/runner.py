#! /usr/bin/env python

import os
import sys

import json
import requests

from git import Repo
from src.git_source.commit import get_commit_payload
from src.git_source.ref import get_ref_info
from src.git_source.repository import get_repository_info
from src.utils import get_logger

logger = get_logger("GitSource Logger")
BATCH_SIZE = 100
AUTH_TOKEN = os.environ.get('AZIMU_API_TOKEN')
HOST = os.environ.get("AZIMU_API_HOST")
PATH = os.environ.get("AZIMU_EXPORTER_REPO_DIR")

logger.debug(f'AUTH_TOKEN: {AUTH_TOKEN}')
logger.debug(f'HOST: {HOST}')
logger.debug(f'PATHPATH: {PATH}')

def run():
    url = f"https://{HOST}/data/git"
    for repo in __get_repos(PATH):
        __process_repository(repo, url)
        __process_commits(repo, url)

def __get_repos(path=''):
    path = os.path.abspath(path)
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            yield Repo(item_path)



def __process_repository(repo, url):
    table_name = 'git_repository'
    repo_info = vars(get_repository_info(repo))
    logger.debug("Git repository - {}".format(repo_info))
    logger.debug(f'{url}/{table_name}')
    r = requests.post(f'{url}/{table_name}',
                      json={"repository": json.dumps(repo_info, sort_keys=True, default=str)},
                      headers={"AUTHENTICATION": AUTH_TOKEN})


def __process_commits(repo, url):
    table_name = 'git_commit'
    commits = []
    for commit in repo.iter_commits():
        commit_info = get_commit_payload(commit)
        commit_info.message = commit_info.message[:1000]
        logger.debug("Git commit - {}".format(commit_info))
        commits.append(vars(commit_info))
        if len(commits) == BATCH_SIZE:
            r = requests.post(f'{url}/{table_name}',
                              json={"data": json.dumps(commits, sort_keys=True, default=str)},
                              headers={"AUTHENTICATION": AUTH_TOKEN})
            if r.status_code != 200:
                logger.debug(commits)
            commits = []
    if commits:
        r = requests.post(f'{url}/{table_name}', 
                          json={"data": json.dumps(commits, sort_keys=True, default=str)},
                          headers={"AUTHENTICATION": AUTH_TOKEN})


def __process_refs(repo, url):
    table_name = 'git_ref'
    for ref in repo.refs:
        try:
            ref_info = vars(get_ref_info(ref))
            if ref_info:
                logger.debug("Git ref - {}".format(ref_info))
                r = requests.post(f'{url}/{table_name}',
                                  json={"ref": json.dumps(ref_info, sort_keys=True, default=str)},
                                  headers={"AUTHENTICATION": AUTH_TOKEN})
                if r.status_code != 200:
                    logger.debug(ref_info)
        except Exception as e:
            logger.debug(e)
            logger.debug("No remote branch for the next ref: {}".format(ref))




if __name__ == '__main__':
    run()
