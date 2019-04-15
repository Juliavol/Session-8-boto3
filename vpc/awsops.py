s#!/usr/bin/env python3

from . import config
import boto3


class AwsOperation():

    def __init__(self):
        self.ec2 = boto3.client('ec2', region_name=config.REGION)

    def create_vpc(self):
        self.ec2.create_vpc(CidrBlock=config.CIDR, InstanceTenancy=config.TENANCY)

