"""Update DNS script."""
import configuration as cfg
import utils


def run():
    """Main function."""
    public_ip = utils.get_public_ip()
    headers = utils.build_request_headers(cfg.USER_AGENT)
    request_url = utils.build_request_url(
        cfg.SERVICE,
        cfg.DOMAIN,
        cfg.GENERATED_USER,
        cfg.GENERATED_PASS,
        public_ip)

    response = utils.dyndns_updated_request(request_url, headers)

    return response


def parse_response(response):
    """Parse response."""
    code = response.split()[0]
    if code in ['good', 'nochg']:
        return "Ok"
    elif code == 'badauth':
        return 'Invalid username or password'
    elif code == 'notfqdn':
        return 'Domain name is not fully qualified'
    elif code == 'nohost':
        return 'Domain name does not exist'
    elif code == 'badagent':
        return 'User agent is invalid'
    elif code == 'abuse':
        return 'Domain name is blocked due to abuse'
    elif code == '911':
        return 'Domain name is blocked due to a system problem'


if __name__ == "__main__":
    run()
