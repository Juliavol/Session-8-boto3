#!/usr/bin/env python3

from . import config
import boto3

client = boto3.client('ec2')
vpc = client.Vpc('id')
ec2 = boto3.resource('ec2')
internet_gateway = ec2.InternetGateway('id')

class awsOperations():


    def __init__(self, region):
	self.ec2 = boto3.client('ec2', region_name=config.REGION)

    def describe_vpcs(self):
        """ Return description of all vpcs in region """
        response = self.ec2.create_vpc(CidrBlock=config.CIDR, InstanceTenancy=config.TENANCY)

    def create_internet_gateway(self):
        """ Return description of created internet gateway """
        response = self.ec2.create_internet_gateway()
        return response


    def create_dhcp_options(self):
        """ Return description of created dhcp options """
        response = self.ec2.create_dhcp_options(
            DhcpConfigurations=config.DHCP_CONFIGURATION
        )
        return response


    def attach_internet_gateway(self, vpc_id, igw_id):
        """ Attach a given igw to a given vpc """
        response = internet_gateway.attach_to_vpc(
            VpcId='string'
        )


    def associate_dhcp_options(self, vpc_id, dhcp_options_id):
        """ Associate a given dhcp_options to a given vpc """
        response = self.ec2.associate_dhcp_options(
            DhcpOptionsId=dhcp_options_id,
            VpcId=vpc_id,
        )
        return response

