import requests
import json
import zipfile
import io,os,re
from config import DRIVER_PATH, STABLE_VERSION_URL, ZIP_DOWNLOAD_URL

def extract_version_registry(output):
    try:
        google_version = ''
        for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
            if letter != '\n':
                google_version += letter
            else:
                break
        return(google_version.strip())
    except TypeError:
        return

def extract_version_folder():
    # Check if the Chrome folder exists in the x32 or x64 Program Files folders.
    for i in range(2):
        path = 'C:\\Program Files' + (' (x86)' if i else '') +'\\Google\\Chrome\\Application'
        if os.path.isdir(path):
            paths = [f.path for f in os.scandir(path) if f.is_dir()]
            for path in paths:
                filename = os.path.basename(path)
                pattern = '\d+\.\d+\.\d+\.\d+'
                match = re.search(pattern, filename)
                if match and match.group():
                    # Found a Chrome version.
                    return match.group(0)
                
def get_local_version():
    try:
        # Try registry key.
        stream = os.popen('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
        output = stream.read()
        local_version = extract_version_registry(output)
    except Exception as ex:
        # Try folder path.
        local_version = extract_version_folder()
    return local_version

def get_current_stable_version():
    stable_version_url=STABLE_VERSION_URL
    resp=requests.get(stable_version_url)
    stable_version=json.loads(resp.text)['channels']['Stable']['version']
    print(f"Current stable version is {stable_version}")
    return stable_version

def get_zip_download_url(current_stable_version):
    download_link_url=ZIP_DOWNLOAD_URL
    resp=requests.get(download_link_url)
    versions=json.loads(resp.text)['versions']
    for version in versions:
        if version['version'] == current_stable_version:
            zip_url=version['downloads']['chromedriver'][-1]['url']
            print(f"Download link of the version is {zip_url}")
    return zip_url

def extract_zip(zip_url):
    r=requests.get(zip_url)
    z=zipfile.ZipFile(io.BytesIO(r.content))
    extract_path=os.getcwd()+"\src"
    z.extractall(extract_path)
    print(f"Chrome driver is extracted to {os.path.dirname(DRIVER_PATH)}")
