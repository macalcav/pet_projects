import json
import requests

def create_slack_image_block(markdown_text_title,image_url,image_alt_plain_text):
    
    image_block='''
    {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*'''+markdown_text_title+'''*"
                }
            },
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "'''+image_alt_plain_text+'''",
                    "emoji": true
                },
                "image_url": "'''+image_url+'''",
                "alt_text": "'''+image_alt_plain_text+'''"
            }
        ]
    }
    '''
    return image_block
    
    
def create_slack_message_block(slack_message_text):

    message_block='''
    {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "'''+slack_message_text+'''"
                }
            },
        ]
    }
    '''  
    return message_block

def send_slack_block(url,slack_block):
    r = requests.post(url, data=slack_image_block)
    return r.text
