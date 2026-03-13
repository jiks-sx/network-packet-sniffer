import socket

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"

def get_dns(ip):
    try:
        return socket.getfqdn(ip)
    except:
        return "Unknown"

def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"
