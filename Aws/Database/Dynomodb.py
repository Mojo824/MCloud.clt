#!/usr/bin/env python3

import boto3
import json
import time

def list_tables(dynamodb):
    print("Available DynamoDB Tables:")
    tables = dynamodb.list_tables().get("TableNames", [])
    for i, table in enumerate(tables, 1):
        print(f"{i}. {table}")
    return tables

def create_table(dynamodb):
    table_name = input("Enter table name: ")
    pk_name = input("Enter name for Primary Key attribute: ")
    pk_type = input("Enter type for Primary Key (S=String, N=Number): ").upper()

    billing_mode = input("Choose billing mode (on_demand/provisioned) [on_demand]: ") or "on_demand"
    if billing_mode not in ["on_demand", "provisioned"]:
        billing_mode = "on_demand"

    try:
        params = {
            'TableName': table_name,
            'KeySchema': [{'AttributeName': pk_name, 'KeyType': 'HASH'}],
            'AttributeDefinitions': [{'AttributeName': pk_name, 'AttributeType': pk_type}],
            'BillingMode': 'PAY_PER_REQUEST' if billing_mode == 'on_demand' else 'PROVISIONED'
        }

        if billing_mode == 'provisioned':
            read_units = int(input("Read Capacity Units (RCU): "))
            write_units = int(input("Write Capacity Units (WCU): "))
            params['ProvisionedThroughput'] = {
                'ReadCapacityUnits': read_units,
                'WriteCapacityUnits': write_units
            }

        table = dynamodb.create_table(**params)
        print(" Creating table...")
        table.wait_until_exists()
        print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        print("❌ Error:", e)

def insert_item(dynamodb):
    table_name = input("Enter table name to insert item into: ")
    table = dynamodb.Table(table_name)

    key = input("Enter primary key name: ")
    value = input("Enter primary key value: ")

    try:
        table.put_item(Item={key: value})
        print("Item inserted successfully.")
    except Exception as e:
        print("❌ Failed to insert item:", e)

def main():
    region = input("Enter AWS region [default: us-east-1]: ") or "us-east-1"
    session = boto3.Session(region_name=region)
    dynamodb = session.client('dynamodb')
    dynamodb_resource = session.resource('dynamodb')

    print("\n🔸 DynamoDB Manager")
    print("1. List Tables")
    print("2. Create Table")
    print("3. Insert Sample Item")
    choice = input("Choose an option: ")

    if choice == '1':
        list_tables(dynamodb)
    elif choice == '2':
        create_table(dynamodb_resource)
    elif choice == '3':
        insert_item(dynamodb_resource)
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()