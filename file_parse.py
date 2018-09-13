import re

def f_parse(sourcefile):
    emails = re.compile(r'[\w\.-]+@[\w\.-]+')
    ips = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    urls = re.compile(r'\w{1,20}://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    print("""
Emails:
    """)
    for i, line in enumerate(open(sourcefile,'r')):
        for match in re.findall(emails, line):
            print(match)
    print("""
IP Addresses:
        """)
    for i, line in enumerate(open(sourcefile,'r')):
        for match in re.findall(ips, line):
            print(match)
    print("""
URL's:
        """)
    for i, line in enumerate(open(sourcefile,'r')):
        for match in re.findall(urls, line):
            print(match)