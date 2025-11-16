import boto3
import json

def list_instances():
    """Return list of simple dicts: InstanceId, State, Name"""
    ec2 = boto3.client("ec2")
    resp = ec2.describe_instances()
    out = []
    for r in resp.get("Reservations", []):
        for i in r.get("Instances", []):
            out.append({
                "InstanceId": i.get("InstanceId"),
                "State": i.get("State", {}).get("Name"),
                "Name": next((t["Value"] for t in i.get("Tags", []) if t["Key"] == "Name"), None)
            })
    return out

def get_instance_details(instance_id):
    """Return a few useful fields for one instance or an error dict"""
    ec2 = boto3.client("ec2")
    try:
        resp = ec2.describe_instances(InstanceIds=[instance_id])
    except Exception as e:
        return {"error": str(e)}
    for r in resp.get("Reservations", []):
        for i in r.get("Instances", []):
            return {
                "InstanceId": i.get("InstanceId"),
                "State": i.get("State", {}).get("Name"),
                "InstanceType": i.get("InstanceType"),
                "PublicIp": i.get("PublicIpAddress"),
                "PrivateIp": i.get("PrivateIpAddress"),
                "LaunchTime": str(i.get("LaunchTime")),
                "Tags": {t["Key"]: t["Value"] for t in i.get("Tags", [])}
            }
    return {"error": "Instance not found"}

def main():
    print("Listing EC2 instances...")
    instances = list_instances()
    if not instances:
        print("No instances found.")
        return
    for i in instances:
        print(i["InstanceId"], "-", i["State"], "-", i.get("Name"))
    iid = input("\nEnter one InstanceId to view details (or Enter to exit): ").strip()
    if not iid:
        return
    details = get_instance_details(iid)
    print("\nDetails:")
    print(json.dumps(details, indent=2))

if __name__ == "__main__":
    main()