#!/usr/bin/env python3
import sys
import http.client
import requests
import argparse
from bs4 import BeautifulSoup
import threading
import time

# Initialize global variables
dbarray = []
url = ""
useragentdesktop = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Accept-Language": "it"
}
timeoutconnection = 5
pool = None
swversion = "0.5beta-py3"


def hello():
    print("-------------------------------------------")
    print("                Joomla Scan                  ")
    print("    Usage: python3 joomlascan.py -u <target> ")
    print(f"     Version {swversion} - Database Entries {len(dbarray)}")
    print("           created by Andrea Draghetti       ")
    print("-------------------------------------------")


def load_component():
    try:
        with open("comptotestdb.txt", "r") as f:
            for line in f:
                dbarray.append(line.strip())
    except FileNotFoundError:
        print("Error: 'comptotestdb.txt' not found. Please create the database file.")
        sys.exit(1)


def check_url(url, path="/"):
    fullurl = url + path
    try:
        conn = requests.get(fullurl, headers=useragentdesktop, timeout=timeoutconnection)
        # Check content-length header specifically if it exists
        if conn.headers.get("content-length") != "0":
            return conn.status_code
        else:
            return 404
    except Exception:
        return None


def check_url_head_info(url, path="/"):
    """Combined helper to check head status and content length."""
    fullurl = url + path
    try:
        conn = requests.head(fullurl, headers=useragentdesktop, timeout=timeoutconnection)
        length = int(conn.headers.get("content-length", 0))
        return conn.status_code, length
    except Exception:
        return None, 0


def check_readme(url, component):
    paths = [
        f"/components/{component}/README.txt", f"/components/{component}/readme.txt",
        f"/components/{component}/README.md", f"/components/{component}/readme.md",
        f"/administrator/components/{component}/README.txt", f"/administrator/components/{component}/readme.txt",
        f"/administrator/components/{component}/README.md", f"/administrator/components/{component}/readme.md"
    ]
    for p in paths:
        if check_url(url, p) == 200:
            print(f"\t README file found \t > {url}{p}")


def check_license(url, component):
    paths = [
        f"/components/{component}/LICENSE.txt", f"/components/{component}/license.txt",
        f"/administrator/components/{component}/LICENSE.txt", f"/administrator/components/{component}/license.txt",
        f"/components/{component}/{component[4:]}.xml", f"/administrator/components/{component}/{component[4:]}.xml"
    ]
    for p in paths:
        if check_url(url, p) == 200:
            print(f"\t LICENSE file found \t > {url}{p}")


def check_changelog(url, component):
    paths = [
        f"/components/{component}/CHANGELOG.txt", f"/components/{component}/changelog.txt",
        f"/administrator/components/{component}/CHANGELOG.txt", f"/administrator/components/{component}/changelog.txt"
    ]
    for p in paths:
        if check_url(url, p) == 200:
            print(f"\t CHANGELOG file found \t > {url}{p}")


def check_manifest(url, component):
    paths = [
        f"/components/{component}/MANIFEST.xml", f"/components/{component}/manifest.xml",
        f"/administrator/components/{component}/MANIFEST.xml", f"/administrator/components/{component}/manifest.xml"
    ]
    for p in paths:
        if check_url(url, p) == 200:
            print(f"\t MANIFEST file found \t > {url}{p}")


def check_index(url, component):
    paths = [
        f"/components/{component}/index.htm", f"/components/{component}/index.html",
        f"/administrator/components/{component}/INDEX.htm", f"/administrator/components/{component}/INDEX.html"
    ]
    for p in paths:
        status, length = check_url_head_info(url, p)
        if status == 200 and length > 1000:
            print(f"\t INDEX file descriptive found \t > {url}{p}")


def index_of(url, path="/"):
    fullurl = url + path
    try:
        page = requests.get(fullurl, headers=useragentdesktop, timeout=timeoutconnection)
        soup = BeautifulSoup(page.text, "html.parser")
        if soup.title:
            titlepage = soup.title.string
            return titlepage and "Index of /" in titlepage
        return False
    except Exception:
        return False


def scanner(url, component):
    try:
        found = False
        if check_url(url, "/index.php?option=" + component) == 200:
            print(f"Component found: {component}\t > {url}/index.php?option={component}")
            found = True
        elif check_url(url, "/components/" + component + "/") == 200:
            print(f"Component found: {component}\t > {url}/index.php?option={component}")
            print("\t But possibly it is not active or protected")
            found = True
        elif check_url(url, "/administrator/components/" + component + "/") == 200:
            print(f"Component found: {component}\t > {url}/index.php?option={component}")
            print("\t On the administrator components")
            found = True

        if found:
            check_readme(url, component)
            check_license(url, component)
            check_changelog(url, component)
            check_manifest(url, component)
            check_index(url, component)

            if index_of(url, f"/components/{component}/"):
                print(f"\t Explorable Directory \t > {url}/components/{component}/")
            if index_of(url, f"/administrator/components/{component}/"):
                print(f"\t Explorable Directory \t > {url}/administrator/components/{component}/")
    finally:
        pool.release()


def main():
    load_component()
    hello()

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", action="store", dest="url", help="The Joomla URL/domain to scan.")
    parser.add_argument("-t", "--threads", action="store", dest="threads", type=int, default=10,
                        help="The number of threads to use (default: 10).")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {swversion}")

    arguments = parser.parse_args()

    if not arguments.url:
        parser.print_help()
        sys.exit(1)

    target_url = arguments.url
    if not (target_url.startswith("http://") or target_url.startswith("https://")):
        print("You must insert http:// or https:// protocol\n")
        sys.exit(1)

    # Remove trailing slash
    if target_url.endswith("/"):
        target_url = target_url[:-1]

    concurrentthreads = arguments.threads
    global pool
    pool = threading.BoundedSemaphore(concurrentthreads)

    if check_url(target_url) is not None:
        if check_url(target_url, "/robots.txt") == 200:
            print(f"Robots file found: \t \t > {target_url}/robots.txt")
        else:
            print("No Robots file found")

        if check_url(target_url, "/error_log") == 200:
            print(f"Error log found: \t \t > {target_url}/error_log")
        else:
            print("No Error Log found")

        print(f"\nStart scan...with {concurrentthreads} concurrent threads!")

        threads = []
        for component in dbarray:
            pool.acquire(blocking=True)
            t = threading.Thread(target=scanner, args=(target_url, component,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        print("End Scanner")
    else:
        print("Site Down or unreachable, check url please...")


if __name__ == "__main__":
    main()
