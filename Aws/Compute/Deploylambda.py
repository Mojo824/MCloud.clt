import boto3

def deploy_lambda():
    print("                 +++ Lambda Deployment Tool MCloud +++")

    region = input("Enter AWS region (e.g. us-east-1): ").strip()
    function_name = input("Enter Lambda function name: ").strip()
    zip_path = input("Path to zipped Lambda code (.zip): ").strip()
    role_arn = input("Enter IAM Role ARN (Lambda execution role): ").strip()

    client = boto3.client('lambda', region_name=region)

    try:
        with open(zip_path, 'rb') as f:
            zip_code = f.read()

        response = client.create_function(
            FunctionName=function_name,
            Runtime="python3.9",
            Role=role_arn,
            Handler="lambda_function.lambda_handler",
            Code={'ZipFile': zip_code},
            Timeout=15,
            MemorySize=128,
            Publish=True
        )

        print(f"Lambda '{function_name}' created successfully!")
        print(f"ARN: {response['FunctionArn']}")

    except client.exceptions.ResourceConflictException:
        print(f" Function '{function_name}' already exists.")
    except Exception as e:
        print("Deployment failed:", e)

if __name__ == "__main__":
    deploy_lambda()
