"""Periodic check of domain"""
from time import sleep


import dns_updater
from utils import get_host_ip, get_public_ip


def scheduler(domain, no_net_interval, no_change_interval):
    """Test IP value and try to update as needed."""

    while True:
        try:
            if get_public_ip() != get_host_ip(domain):
                print('IP has changed, updating DNS')
                response = dns_updater.run()
                result = dns_updater.parse_response(response)
                if result != "Ok":
                    print(result)
                    break
                sleep(90)
            else:
                print('IP has not changed, waiting for next check')
                sleep(no_change_interval)
        except KeyboardInterrupt:
            print('\nKeyboard interrupt. Exiting.')
            break
        except BaseException:
            print('No internet connection, waiting for next check')
            sleep(no_net_interval)
    exit(-1)


if __name__ == '__main__':
    import configuration as config
    scheduler(config.DOMAIN, config.NO_NET_INTERVAL, config.NO_CHANGE_INTERVAL)
