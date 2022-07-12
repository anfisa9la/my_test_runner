import asyncio
import requests
import auth

request_string = "http://appserver12:{}/api/"
server_ports = [5100]


def request_url(port):
    return request_string.format(port)


def get_loop():
    return asyncio.get_event_loop()


def test_request(port):
    return lambda: requests.get(
        request_url(port),
        headers={
            "Authorization": "Bearer " + auth.adminToken(port)
        }
    )


async def test():
    loop = get_loop()

    futures = [
        loop.run_in_executor(None, test_request(port))
        for port in server_ports * 2
    ]

    for response in await asyncio.gather(*futures):
        print(response)


loop = get_loop()
loop.run_until_complete(test())
