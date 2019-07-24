"""
Write a program calculate how long it will take to download the Python 3.7.3
installer from https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe
over my crappy ADSL internet connection.  I typically get ~11Mbps down.
"""
import urllib.request

try:
    file_size_bytes = urllib.request.urlopen(
        "https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe"
    ).length
except Exception:
    print("Failed to get file size! Using default value.")
    file_size_bytes = 26190920

# The code above gets the file size but as beginners you weren't expected
# to do it this way.  Instead, we thought you'd look on the site or download
# it to see how big it was and just use something like line 16 in your
# code!

BANDWIDTH = 11.0

file_size_bits = file_size_bytes * 8
bandwidth_bits_per_sec = BANDWIDTH * 1024 ** 2
estimated_download_time = file_size_bits / bandwidth_bits_per_sec

print(
    "It would take about",
    round(estimated_download_time),
    "second(s) to download the file.",
)
