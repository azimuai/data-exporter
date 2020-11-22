# -*- coding: utf-8 -*-
"""src.src: provides entry point main()."""

__version__ = "0.1"

# from src.bitbucket import bitbucket_runner
from src.git_source import runner as git_runner
from src.utils import get_config, get_logger

logger = get_logger("AzimuGitCLI")


def process_git():
    git_runner.run()


def main():
    process_git()


if __name__ == '__main__':
    main()
