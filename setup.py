import requests
import json
import argparse


def initialize_thread(ids, token, name):
    headers = {"Authorization": "Bearer {}".format(token),
               'content-type': 'application/json'}
    url = "https://graph.facebook.com/me/messages"
    data = {
        'message': {'text': "Initializing new thread"},
        'recipient': {'ids': ids}
    }
    resp = requests.post(url, headers=headers, data=json.dumps(data)).json()
    print(resp)
    tid = resp['thread_key']
    url2 = "https://graph.facebook.com/{}/threadname".format(tid)
    data2 = {"name": name}
    resp2 = requests.post(url2, headers=headers, data=json.dumps(data2)).json()
    print(resp2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t",
                        "--token",
                        help="fb access token",
                        default=None,
                        required=True)

    parser.add_argument("-n", "--name", help="name to use for thread",
                        default=None,
                        required=True)

    parser.add_argument("-u", "--userids", help="list of workplace userids",
                        default=None,
                        nargs='+',
                        required=True)

    args = parser.parse_args()
    initialize_thread(args.userids, args.token, args.name)
