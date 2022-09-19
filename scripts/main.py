# importing the needed modules
from download_file_script import download_file

# creating the initial filenames
string_urls = "1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11 - 12 - 13 - 14 - 15 - 16 - 17 - 18 - 19 - 2A - 2B - 21 - 22 - 23 - 24 - 25 - 26 - 27 - 28 - 29 - 30 - 31 - 32 - 33 - 34 - 35 - 36 - 37 - 38 - 39 - 40 - 41 - 42 - 43 - 44 - 45 - 46 - 47 - 48 - 49 - 50 - 51 - 52 - 53 - 54 - 55 - 56 - 57 - 58 - 59 - 60 - 61 - 62 - 63 - 64 - 65 - 66 - 67 - 68 - 69 - 70 - 71 - 72 - 73 - 74 - 75 - 76 - 77 - 78 - 79 - 80 - 81 - 82 - 83 - 84 - 85 - 86 - 87 - 88 - 89 - 90 - 91 - 92 - 93 - 94 - 95"
list_urls = string_urls.split(" - ")


# starting to download the files
original_download_url = "https://files.data.gouv.fr/ademe/dpe-departements/"

# Iterate over all links and download them
for number in list_urls:
    # creating the urls needed to take from them the files
    final_url = original_download_url + f"{number}.zip"
    # printing and calling the download function
    print(download_file(final_url))

