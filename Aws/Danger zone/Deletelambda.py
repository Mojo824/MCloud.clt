import boto3
from botocore.exceptions import ClientError

region = input("Enter AWS region (e.g., us-east-1): ")

def list_lambda_functions(region):
    client = boto3.client('lambda', region_name=region)
    paginator = client.get_paginator('list_functions')
    functions = []
    for page in paginator.paginate():
        functions.extend(page['Functions'])
    return functions

def show_functions(functions):
    if not functions:
        print("No Lambda functions found.")
        return
    for idx, fn in enumerate(functions, 1):
        print(f"{idx}. FunctionName: {fn['FunctionName']}")

def delete_function(region, function_name):
    client = boto3.client('lambda', region_name=region)
    try:
        client.delete_function(FunctionName=function_name)
        print(f"Deleted Lambda function {function_name}")
    except ClientError as e:
        print(f"Failed to delete {function_name}: {e}")

def delete_all_in_all_regions():
    ec2 = boto3.client('ec2')
    regions = [r['RegionName'] for r in ec2.describe_regions()['Regions']]
    for reg in regions:
        print(f"\nRegion: {reg}")
        functions = list_lambda_functions(reg)
        for fn in functions:
            delete_function(reg, fn['FunctionName'])

functions = list_lambda_functions(region)
show_functions(functions)

if not functions:
    exit()

print("\nEnter the numbers of the Lambda functions to delete (e.g., 1,3,5), 'all' to delete all in this region, or 'all-regions' to delete all in all regions:")
choice = input("Your choice: ").strip().lower()

if choice == 'all':
    for fn in functions:
        delete_function(region, fn['FunctionName'])
elif choice == 'all-regions':
    delete_all_in_all_regions()
else:
    try:
        indices = [int(x.strip()) for x in choice.split(',') if x.strip().isdigit()]
        for idx in indices:
            if 1 <= idx <= len(functions):
                fn = functions[idx-1]
                delete_function(region, fn['FunctionName'])
            else:
                print(f"Invalid selection: {idx}")
    except Exception as e:
        print(f"Invalid input: {e}")
