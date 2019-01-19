# commit-timekeeper
Python script to help you fill out work timekeeping forms

## Configuration

First, you will need to configure the gitProperties.example.json file.
1. rename the file to gitProperties.json
2. add the path form root to all the git repositories you want to, under the property repositories
3. add your git email under the property user


## Usage

The script is really simple to use it has only one command,`git-history` and that command has only one option `--since` which tells the script the day since when you need the data.
```sh
    $ python3 main.py git_history --since="2019-01-14"
      >>>> 2019-01-14 17:08:14 - bugfix/branch-you-commited-to
      ....
```

## Disclaimer

This script was built for personal use and as of now only supports happy paths so it will not react very well to bad input data, like repository paths that don't have .git files inside.
