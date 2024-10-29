import click
from  github import userGithub
@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', required = True, prompt='Username: ', help="Enter GitHub username")
def getUserGithub(name):
    userGithub(name)




if __name__ == '__main__':
    cli()