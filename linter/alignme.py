#!/usr/bin/python
"""
plz work
"""
from __future__ import print_function
import boto3



def describe_azs():
    """
    docstring
    """
    response = EC2.describe_availability_zones()
    return response


if __name__ == '__main__':

    EC2 = boto3.client('ec2', "us-east-1")
    RESPONSE = describe_azs()
    print (RESPONSE)
