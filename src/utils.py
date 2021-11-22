"""Utilities."""
import socket

import requests


def get_host_ip(domain):
    """Get IP address for a domain."""
    return socket.gethostbyname(domain)


def get_public_ip():
    """Get public IP address."""
    try:
        r = requests.get('https://api.ipify.org?format=json')
        return r.json()['ip']
    except Exception as e:
        return e


def dyndns_updated_request(request_url, headers):
    """Send a request to the google domains service to update the IP address."""
    try:
        print(request_url)
        r = requests.get(
            request_url,
            headers=headers,
        )
        return r.text
    except Exception as e:
        print(e)
        return None


def build_request_headers(user_agent):
    """Build the request headers to update the IP address."""
    return {
        'User-Agent': user_agent,
    }


def build_request_url(service, domain, username, password, ip):
    """
    Build the request url to update the IP address.

    params:
        service: The service to update the IP address (e.g. google)
        domain: The domain to update the IP address (e.g. example.com)
        username: The username to update the IP address
        password: The password to update the IP address
        ip: The IP address
    """
    return f'https://{username}:{password}@{service}?hostname={domain}&myip={ip}'
