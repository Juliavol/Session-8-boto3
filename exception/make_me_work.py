#!/usr/bin/python3

import argparse
import boto3


def args_parser():
    """ validate arguments and return them """
    parser = argparse.ArgumentParser(add_help=True, description="VPC Arguments")
    parser.add_argument("--region", "-r", help="Get region",
                        required=True)
    parser.add_argument("--vpcid", "-i", help="Get vpc id",
                        required=True)
    return parser.parse_args()


def create_tags(ec2, vpc_id):
    """
    Changes the name of the VPC to opsschool

    :param ec2: Boto EC2 Service Client Instance
    :param vpc_id: String
    :return: None
    """
    ec2.create_tags(
        Resources=[
            vpc_id,
        ],
        Tags=[
            {
                'Key': 'Name',
                'Value': 'opsschool'
            },
        ]
    )


def main():
    args = args_parser()
    ec2 = boto3.client('ec2', args.region)
    create_tags(ec2, args.vpcid)


if __name__ == '__main__':
    main()
