'''
@Author: Swapnil Bhoyar
@Date: 2021-08-31
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-08-31
@Title : Program for creating s3 bucket using boto3.
'''
import boto3
from Log import logger
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

resource_s3 = boto3.resource(
            service_name='s3',
            region_name='ap-south-1',
            aws_access_key_id=env['ACCESS_KEY'],
            aws_secret_access_key=env['SECRETE_ACCESS_KEY']
        )

client_s3 = boto3.client(
            service_name='s3',
            region_name='ap-south-1',
            aws_access_key_id=env['ACCESS_KEY'],
            aws_secret_access_key=env['SECRETE_ACCESS_KEY']
        )

def create_bucket():
    """
    Description:
        fucntion for creating bucket.
    """
    try:
        print ("creating bucket")
        location = {'LocationConstraint': 'ap-south-1'}
        client_s3.create_bucket(
        Bucket='swapniltest12',
        CreateBucketConfiguration=location)

    except Exception as e:
        logger.info(e)

def get_bucket_list():
    """
    Description:
        fucntion for getting bucket list.
    """
    try:
        print ("Creating bucket list")
        for bucket in resource_s3.buckets.all():
            print(bucket.name)
    except Exception as e:
        logger.info(e)

def upload_file():
    """
    Description:
        fucntion for uploading file.
    """
    try:
        print ("uploding file")
        resource_s3.Bucket('swapniltest1').upload_file(Filename='user_data.csv', Key='user_data.csv')
    except Exception as e:
        logger.info(e)

def get_files_in_bucket():
    """
    Description:
        fucntion for getting files in bucket.
    """
    try:
        print ("file list:")
        for obj in resource_s3.Bucket('swapniltest1').objects.all():
            print(obj)

    except Exception as e:
        logger.info(e)

def download_files_in_bucket():
    """
    Description:
        fucntion for downloading file from bucket.
    """
    try:
        print ("Downloading bucket")
        resource_s3.Bucket('swapniltest1').download_file(Key='user_data.csv', Filename='user_data_download.csv')
    except Exception as e:
        logger.info(e)

if __name__=="__main__":
    create_bucket()
    get_bucket_list()
    upload_file()
    get_files_in_bucket()
    download_files_in_bucket()