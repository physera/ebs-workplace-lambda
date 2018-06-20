from botocore.vendored import requests
import os


def parse_message(message):
    foo = [x.split(": ") for x in filter(None, message.split("\n"))]
    if len(foo) > 0:
        return dict(foo)
    else:
        return {}


def lambda_handler(event, context):
    headers = {"Authorization": "Bearer {}".format(os.environ['FB_API_TOKEN'])}
    url = "https://graph.facebook.com/{}/feed".format(
        os.environ['FB_GROUP_ID']
    )

    message = event['Records'][0]['Sns']['Message']
    fields = parse_message(message)

    if 'Application' in fields and 'Environment' in fields and \
       'Environment URL' in fields and 'Message' in fields:
        app = fields.get("Application", "App")
        post = ["# [{} ({})]({})".format(app,
                                         fields["Environment"],
                                         fields["Environment URL"])]
        post.append("{}".format(fields["Message"]))
    else:
        post = ["# {}".format(message)]

    data = {
        'formatting': 'MARKDOWN',
        'message': '\n'.join(post)
    }
    resp = requests.post(url, headers=headers, data=data).json()
    print(resp)
