import click
import requests
import os
from .config.definitions import ROOT_DIR

@click.command()
@click.option('--download', 'key', help='Download the patient dataset with the API key.')

def main(key):
    if key:
        click.echo('Downloading dataset...')
        r = requests.get('https://api.patientprogress.ca/api/research', headers={'x-auth-key': key})
        with open(os.path.join(ROOT_DIR, 'data', 'data.json'), "wb") as file:
            file.write(r.content)
        click.echo('Done.')
    


if __name__ == '__main__':
    main()