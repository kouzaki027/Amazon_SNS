import boto3

# uncomment lines 4 through 8 and add your AWS Access Key and AWS Secret Access Key
#client = boto3.client(
#        "sns",
#        aws_access_key_id="xyz",
#        aws_secret_access_key="xyz",
#        region_name="us-east-1")

response = client.create_topic(Name="topic_name_here")
topic_arn = response["TopicArn"]

# Publish to topic
client.publish(TopicArn=topic_arn, 
            Message="Thank you for subscribing using AWS! ;)", 
            Subject="Your Email Subject Name")

'''# List all subscriptions
response = client.list_subscriptions()
subscriptions = response["Subscriptions"]
print ( subscriptions ) 

topics = client.list_topics().get('Topics')

for topic in topics:
    subscriptions = client.list_subscriptions_by_topic(TopicArn=topic.get('TopicArn')).get('Subscriptions')
    for subscription in subscriptions:
        print(subscription.get('SubscriptionArn'))
        print(subscription.get('Endpoint'))'''
       
print ("Finished")
#sys.exit("Finished")   
        
