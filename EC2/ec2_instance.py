'''
@Author: Swapnil Bhoyar
@Date: 2021-08-31
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-08-31
@Title : Program for creating ec2 instance using boto3.
'''
import boto3
from Log import logger

def create_ec2_instance():
    """
    Description:
        fucntion for creating instance.
    """
    try:
        print ("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-0c1a7f89451184c8b",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="EC2-mumbai-key-pair"
        )
    except Exception as e:
        logger.info(e)


def describe_ec2_instance():
    """
    Description:
        fucntion for describing instance.
    """
    try:
        print ("Describing EC2 instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        logger.info(e)


def reboot_ec2_instance():
    """
    Description:
        fucntion for rebooting instance.
    """
    try:
        print ("Reboot EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.reboot_instances(InstanceIds=[instance_id]))
    except Exception as e:
        logger.info(e)


def stop_ec2_instance():
    """
    Description:
        fucntion for sptoing instance.
    """
    try:
        print ("Stop EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as e:
        logger.info(e)


def start_ec2_instance():
    """
    Description:
        fucntion for starting instance.
    """
    try:
        print ("Start EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.start_instances(InstanceIds=[instance_id]))
    except Exception as e:
        logger.info(e)


def terminate_ec2_instance():
    """
    Description:
        fucntion for trrminating instance.
    """
    try:
        print ("Terminate EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        logger.info(e)


create_ec2_instance()
describe_ec2_instance()
reboot_ec2_instance()
stop_ec2_instance()
start_ec2_instance()
terminate_ec2_instance()