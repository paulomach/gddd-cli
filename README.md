# Google Domains Dynamic DNS Client 

Scripts to configure dynamic DNS.

## Configuration

Configure Env vars on `.env` or environment as:

```shell
GENERATED_USER="<your user>"
GENERATED_PASS="<your pass>"

DOMAIN="<your domain>"

SERVICE="domains.google.com/nic/update"
USER_AGENT="Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"

NO_NET_INTERVAL=300
NO_CHANGE_INTERVAL=600
```

## Dependencies

Install with `pip install -r requirements.txt`

## Run

```shell
python src/scheduler.py
```

## Test/Lint

Using tox:
```shell
tox 
```

### Single run

```shell
tox -e run
```

## Motivation

I use this to update my home ip updated for my home automation toy projects.

## References

[Google Documentation](https://support.google.com/domains/answer/6147083?hl=en#zippy=%2Cset-up-a-client-program-on-your-gateway-host-or-server%2Cuse-the-api-to-update-your-dynamic-dns-record)