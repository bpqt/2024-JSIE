'''Utilitaires pour télécharger des images'''
import ssl
import urllib.request
from pathlib import Path

import certifi

def download_file(url:str, output_name=None, output_dir="downloads", force=False):
    '''Téléchargement d'un fichier vers un dossier download, si celui-ci n'existe pas encore'''
    if output_name is None:
        output_name = Path(url).name
    response = urllib.request.urlopen(
        url,
        context=ssl.create_default_context(cafile=certifi.where()))
    if output_name is None:
        output_name = response.headers.get_filename()
    output_file = Path(output_dir) / output_name
    # On ne télécharge le fichier que s'il n'existe pas
    if not output_file.exists() or force:
        open(output_file, 'wb').write(response.read())
    # On renvoie le fichier
    return output_file