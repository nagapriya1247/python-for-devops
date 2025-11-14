import boto3
from botocore.exceptions import ClientError

try:
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    
    # Filter by instance state (running)
    response = ec2_client.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    print("Running EC2 Instances:\n")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            # Extract tags
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
            
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"Name: {tags.get('Name', 'No Name')}")
            print(f"Type: {instance['InstanceType']}")
            print(f"Public IP: {instance.get('PublicIpAddress', 'N/A')}")
            print(f"Private IP: {instance['PrivateIpAddress']}")
            print(f"Availability Zone: {instance['Placement']['AvailabilityZone']}")
            print(f"Security Groups: {[sg['GroupName'] for sg in instance['SecurityGroups']]}")
            print("=" * 50)

except ClientError as e:
    print(f"AWS Error: {e}")
except Exception as e:
    print(f"Error: {e}")