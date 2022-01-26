#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:39:38 2022

@author: macalcav@us.ibm.com
https://developer.pagerduty.com/api-reference/b3A6Mjc0ODE2Mw-list-all-of-the-on-calls

Returns an object with the following information:
--------------------------------------------------
'PD SCHEDULE':parsed_response['oncalls'][0]['schedule']['name'],
'PD SCHEDULE URL':parsed_response['oncalls'][0]['schedule']['html_url'],
'PD ONCALL NAME':parsed_response['oncalls'][0]['user']['summary'],
'PD ONCALL ID':parsed_response['oncalls'][0]['user']['id'],
'PD ONCALL EMAIL':get_user_email(parsed_response['oncalls'][0]['user']['id']),
'PD ONCALL URL':parsed_response['oncalls'][0]['user']['html_url'],
'PD ONCALL START':parsed_response['oncalls'][0]['start'],
'PD ONCALL END':parsed_response['oncalls'][0]['end']
"""

import http.client
import json

PAGERDUTY_TOKEN='<YOUR_TOKEN>'
SCHEDULE_ID='<SCHEDULE_ID>'

def get_user_email(pd_id):
    
    conn = http.client.HTTPSConnection("api.pagerduty.com")
    
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': "Token token={pd_token}".format(pd_token=PAGERDUTY_TOKEN)
        }
    
    resource='users'

    conn.request("GET", "/{resource_type}/{pd_user_id}?include%5B%5D=contact_methods".format(resource_type=resource,pd_user_id=pd_id), headers=headers)
    
    res = conn.getresponse()
    
    data = res.read()
    
    parsed_response=json.loads(data.decode("utf-8"))
    #print(json.dumps(parsed_response, indent=4, sort_keys=True))
    
    return parsed_response['user']['email']



def get_oncall_person(pagerduty_schedule_id):
    
    conn = http.client.HTTPSConnection("api.pagerduty.com")
    
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/vnd.pagerduty+json;version=2",
        'Authorization': "Token token={pd_token}".format(pd_token=PAGERDUTY_TOKEN)
        }
    
    resource='oncalls'
    
    conn.request("GET", "/{resource_type}?limit=1&include%5B%5D=schedules&schedule_ids%5B%5D={schedule_id}".format(resource_type=resource,schedule_id=pagerduty_schedule_id), headers=headers)
    
    res = conn.getresponse()
    
    data = res.read()
    
    parsed_response=json.loads(data.decode("utf-8"))
    #print(json.dumps(parsed_response, indent=4, sort_keys=True))
    
    pd_sched_name=parsed_response['oncalls'][0]['schedule']['name']
    pd_sched_url=parsed_response['oncalls'][0]['schedule']['html_url']
    pd_oncall_person_name=parsed_response['oncalls'][0]['user']['summary']
    pd_oncall_person_profile_url=parsed_response['oncalls'][0]['user']['html_url']
    pd_oncall_sched_start=parsed_response['oncalls'][0]['start']
    pd_oncall_sched_end=parsed_response['oncalls'][0]['end']
        
    pd_oncall_person_record=(
        {
            'PD SCHEDULE':parsed_response['oncalls'][0]['schedule']['name'],
            'PD SCHEDULE URL':parsed_response['oncalls'][0]['schedule']['html_url'],
            'PD ONCALL NAME':parsed_response['oncalls'][0]['user']['summary'],
            'PD ONCALL ID':parsed_response['oncalls'][0]['user']['id'],
            'PD ONCALL EMAIL':get_user_email(parsed_response['oncalls'][0]['user']['id']),
            'PD ONCALL URL':parsed_response['oncalls'][0]['user']['html_url'],
            'PD ONCALL START':parsed_response['oncalls'][0]['start'],
            'PD ONCALL END':parsed_response['oncalls'][0]['end']
        }
    )
    
    return pd_oncall_person_record




oncall_person=get_oncall_person(SCHEDULE_ID)
print('{} is on call for {} from {} until {}'.format(oncall_person['PD ONCALL EMAIL'],oncall_person['PD SCHEDULE'],oncall_person['PD ONCALL START'],oncall_person['PD ONCALL END']))
