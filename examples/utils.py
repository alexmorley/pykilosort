import os
import urllib.request

S3_BUCKET_BASE_URL = 'https://static.alexmorley.me/pykilosort/test-recording/'

def create_test_directory(test_dir_path):
    try:
        os.makedirs(test_dir_path)
    except FileExistsError:
        pass

    print(f"Downloading test files from {S3_BUCKET_BASE_URL} ...")
    for file_ in ['xc.npy', 'yc.npy', 'test.bin']:
        url = S3_BUCKET_BASE_URL + file_
        filename = test_dir_path + file_
        print(url)
        urllib.request.urlretrieve(url, filename)
    print("Done")
