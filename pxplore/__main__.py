import click
import requests
import os
from .config.definitions import ROOT_DIR
import pandas as pd

@click.command()
@click.option('--download', 'key', help='Download the patient dataset with the API key.')
@click.option('--display', 'attribute', help='Display data about an attribute.')
@click.option('--delete', 'name', help='Deletes the patient record.')

def main(key, attribute, name):
    # Download the dataset from the API
    if key:
        click.echo('Downloading dataset...')
        r = requests.get('https://api.patientprogress.ca/api/research', headers={'x-auth-key': key})
        df = pd.read_json(r.content)
        df.to_json(os.path.join(ROOT_DIR, 'data', 'data.json'))
        click.echo('Done.')
    
    # Check if the file is present
    if not os.path.isfile(os.path.join(ROOT_DIR, 'data', 'data.json')):
        print('Please download the dataset first.')
        exit(1)

    if attribute:
        df = pd.read_json(os.path.join(ROOT_DIR, 'data', 'data.json'))

        if attribute == "info":
            click.echo(df.info())
        
        if attribute == "gender":
            click.echo(df['gender'].value_counts())
    
    if name:
        df = pd.read_json(os.path.join(ROOT_DIR, 'data', 'data.json'))
        prev_len = len(df)
        df = df[df.name != name]
        df.to_json(os.path.join(ROOT_DIR, 'data', 'data.json'))
        curr_len = len(df)
        click.echo(f"Deleted {prev_len - curr_len} records.")

if __name__ == '__main__':
    main()