import click
import CommitData as cdata
from utils import *

@click.group()
def main():
    pass

@main.command("git_history",help="- Shows the work you have done in the given repositories after the given date")
@click.option("--since",default="1 week ago")
def git_history(since):
    for x in log_all(since):
        print(x)

if __name__ == "__main__":
    main()