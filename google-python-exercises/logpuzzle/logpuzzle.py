#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

# Custom function to sort on last word of image file name
def lastword(url):
  match = re.findall(r'.*-(\w+)\.', url)
  return match[0]
  
def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  hostname = re.search('_(\S+)', filename).group(1)

  f = open(filename, 'r')
  text = f.read()
  f.close()

  all_urls = re.findall('GET (\S+puzzle\S+)', text)
  unique_urls = []
  for url in all_urls:
    if not url in unique_urls:
      unique_urls.append(url)

  for i in range(len(unique_urls)):
    unique_urls[i] = 'http://' + hostname + unique_urls[i]

  return sorted(unique_urls, key=lastword)
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  # download image slices
  for i in range(len(img_urls)):
    print 'retrieving', img_urls[i], '...'
    urllib.urlretrieve(img_urls[i], os.path.join(dest_dir, 'img'+str(i))) 
  
  # create a HTML file
  f = open(dest_dir + r'\index.html', 'w')
  f.write('<verbatim>\n<html>\n<body>\n')

  for i in range(len(img_urls)):
    # Strangely this doesn't work in FireFox but works in IE
    # f.write('<img src="' + os.path.abspath(os.path.join(dest_dir, 'img'+str(i))) + '">')
    f.write('<img src="img' + str(i) + '">')
  
  f.write('\n</body>\n</html>')

  f.close()
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
