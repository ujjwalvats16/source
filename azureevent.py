import sys
import logging
import datetime
import time
import os
import json

from azure.eventhub import EventHubClient, Sender, EventData

logger = logging.getLogger("azure")

# Address can be in either of these formats:
# "amqps://<URL-encoded-SAS-policy>:<URL-encoded-SAS-key>@<namespace>.servicebus.windows.net/eventhub"
# "amqps://<namespace>.servicebus.windows.net/<eventhub>"
# SAS policy and key are not required if they are encoded in the URL

ADDRESS = "amqps://ronitest1.servicebus.windows.net/ronitest"
USER = "basic"
KEY = "LlCKYylaw5J+d5c2eT1wXMZ6B5S9z4yWjFWEY+Zhz3s="

try:
    if not ADDRESS:
        raise ValueError("No EventHubs URL supplied.")

    # Create Event Hubs client
    client = EventHubClient(ADDRESS, debug=False, username=USER, password=KEY)
    sender = client.add_sender(partition="0")
    client.run()
    try:
        start_time = time.time()
        d="value"+","+"time"+"\n"
        for i in range(5000):
            
            d={"data":str(i)}
            message=d
            print(i)
            
        
            sender.send(EventData(json.dumps(message)))
            print(message)    
    except:
        raise
    finally:
        end_time = time.time()
        client.stop()
        run_time = end_time - start_time
        logger.info("Runtime: {} seconds".format(run_time))

except KeyboardInterrupt:
    pass


