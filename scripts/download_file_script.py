# importing the needed modules
import requests
from typing import Tuple


# creating the download function so I can use it as many times as I like
def download_file(url, filename='') -> Tuple:
    """This function takes at the url you qre trying to download and return none"""

    # try to send a get request and raise an exception if it fails
    try:
        # trying the get the file name
        # if passed do nothing
        if filename:
            pass
        else:
            # if not passed run a get request on the url then get the file name through string parsing
            filename = requests.get(url).url[url.rfind('/')+1:]

        # now that we have the url let's download the file and write it in our directory
        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        return f"{filename} was succefully created", 201

    # raise an exception if there an issue
    except Exception as e:
        print(e)
        return f"{filename} was failed to be created", 200
