


mydict = {}

with open("/tmp/ips.txt","r") as f:
    for line in f:
        (ip, port) = line.split(",")
        print ip
        print port

