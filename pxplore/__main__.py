import click
import requests
import os
from .config.definitions import ROOT_DIR

@click.command()
@click.option('--download', is_flag=True)
@click.option('--setkey', 'key', help='Set an API key.')

def main(download, key):
    if download:
        if not key:
            click.echo('Please provide an API key using the --setkey option.')
            exit(1)
        click.echo('Downloading dataset...')
        r = requests.get('https://api.patientprogress.ca/api/research', headers={'x-auth-key': key})
        with open(os.path.join(ROOT_DIR, 'data', 'data.json'), "wb") as file:
            file.write(r.content)
        click.echo('Done.')
    


if __name__ == '__main__':
    main()