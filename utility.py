import re

def contains(list, filter):
    for x in list:
        if filter(x):
            return x
    return False

def add_site_to_hosts(host, ip):
	hosts = open("example", "a")
	hosts.write("%s\t%s\n" % (ip, host))
	hosts.close()

def remove_site_from_hosts(host):
	hosts = open("example", "r+")
	removed = False
	pattern = ".*" + host
	for line in hosts:
		print(line)
		if(re.match(pattern, line)):
			print('find')
			line = hosts.replace(line, "")
			hosts.write(line)
			removed = True
			break

	hosts.close()
	return removed

def alert(string):
	print('\033[91m\t' + string + '\033[0m')