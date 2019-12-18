from trumpia_Utility import Trumpia
import time

def subscriptions(mobile_number,first_name,last_name):
    trm_obj = Trumpia()
    body = {
        'list_name':'ContactsList',
        'subscriptions':[
            {
                "first_name": first_name,
                "last_name": last_name,
                "mobile":
                {
                    "number":mobile_number,
                    "country_code":"1"
                },
                "voice_device": "mobile"
            }
        ]
    }
    subscription_status = trm_obj.getSearchSubscription(mobile_number)
    if 'MPSE2305' in subscription_status :
        print("PUT SUB")
        request_id = trm_obj.putSubscription(body)
        time.sleep(2)
        subscription_id = trm_obj.getStatusReport(request_id)
        return subscription_id
    elif 'subscription_id_list' in subscription_status:
        print("POST SUB: ")
        subscription_id = subscription_status['subscription_id_list']
        subscription_id = str(subscription_id).strip("['']")
        subscription_data = trm_obj.getSubscription(subscription_id)
        current_mobile_number = subscription_data['mobile']['value']
        if current_mobile_number != mobile_number:
            body = {
                'list_name':'ContactsList',
                'subscriptions':[
                    {
                        "mobile":
                        {
                            "number":mobile_number,
                            "country_code":"1"
                        },
                        "voice_device": "mobile"
                    }
                ]
            }
            request_id = trm_obj.postSubscription(subscription_id,body)
            time.sleep(2)
            subscription_id = trm_obj.getStatusReport(request_id)

        current_list_ids = subscription_data['list_ids']
        if 'first_name' in subscription_data:
            current_first_name = subscription_data['first_name']
            if current_first_name == first_name:
                pass
            else:
                body = {
                    'list_name':'ContactsList',
                    'subscriptions':[
                        {
                            "first_name": first_name,
                        }
                    ]
                }
                request_id = trm_obj.postSubscription(subscription_id,body)
                time.sleep(2)
                subscription_id = trm_obj.getStatusReport(request_id)
        if 'last_name' in subscription_data:
            current_last_name = subscription_data['last_name']
            if current_first_name == first_name:
                pass
            else:
                body = {
                    'list_name':'ContactsList',
                    'subscriptions':[
                        {
                            "last_name": last_name,
                        }
                    ]
                }
                request_id = trm_obj.postSubscription(subscription_id,body)
                time.sleep(2)
                subscription_id = trm_obj.getStatusReport(request_id)
        if 'last_name' not in subscription_data:
            body = {
                'list_name':'ContactsList',
                'subscriptions':[
                    {
                        "last_name": last_name,
                    }
                ]
            }
            request_id = trm_obj.postSubscription(subscription_id,body)
            time.sleep(2)
            subscription_id = trm_obj.getStatusReport(request_id)
    else:
        print(subscription_status)
