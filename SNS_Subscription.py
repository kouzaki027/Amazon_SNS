import boto3

"""# A session stores configuration state and allows you to create service clients and resources
class boto3.session.Session(aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, region_name=None, botocore_session=None, profile_name=None)[source]"""

#client = boto3.client(
#        "sns",
#        aws_access_key_id="xyz",
#        aws_secret_access_key="xyz",
#        region_name="us-east-1")

response = client.create_topic(Name="topic_name")
topic_arn = response["TopicArn"]

"""
<CreateTopicResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <CreateTopicResult>
        <TopicArn>arn:aws:sns:us-east-2:123456789012:My-Topic</TopicArn>
    </CreateTopicResult>
    <ResponseMetadata>
        <RequestId>a8dec8b3-33a4-11df-8963-01868b7c937a</RequestId>
    </ResponseMetadata>
</CreateTopicResponse>
"""

# uncomment line 27, and add the subscriber's email address
#response = client.subscribe(TopicArn=topic_arn, Protocol="Email", Endpoint="SubscriberEmailAddress@domain.com")
subscription_arn = response["SubscriptionArn"]
