import boto3

def create_rds_instance():
    print("RDS Instance Deployment (Free Tier Eligible)")

    region = input("Enter AWS region [default: us-east-1]: ") or "us-east-1"
    identifier = input("Enter DB instance identifier: ")
    engine = input("Choose engine (mysql/postgres) [mysql]: ") or "mysql"
    username = input("Enter master username: ")
    password = input("Enter master password (min 8 characters): ")

    if len(password) < 8:
        print("❌ Password must be at least 8 characters.")
        return

    port = 3306 if engine == "mysql" else 5432

    rds = boto3.client("rds", region_name=region)

    try:
        response = rds.create_db_instance(
            DBInstanceIdentifier=identifier,
            AllocatedStorage=20,
            DBInstanceClass="db.t3.micro",
            Engine=engine,
            MasterUsername=username,
            MasterUserPassword=password,
            BackupRetentionPeriod=7,
            Port=port,
            PubliclyAccessible=True,
            MultiAZ=False
        )
        print(f"🚀 RDS instance '{identifier}' is being created in {region}...")
    except Exception as e:
        print("❌ Error creating RDS instance:", e)

if __name__ == "__main__":
    print ("                      +++ Rds DB Tool MCloud +++")
    create_rds_instance()