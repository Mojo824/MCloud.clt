# ☁️ MCloud – AWS & Azure Cloud Automation Suite

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20S3%20%7C%20VPC-orange)
![Azure](https://img.shields.io/badge/Azure-Support%20Coming%20Soon-blue)
![Status](https://img.shields.io/badge/Project-Active%20Development-informational)
![License](https://img.shields.io/badge/License-MIT-green)

**MCloud** is a modular, CLI-based automation suite for **AWS** and **(upcoming)** Azure services. Built with Python and `boto3`, this toolkit is ideal for DevOps learners, cloud practitioners, and portfolio builders.

---

## 🚀 Features

### ✅ AWS Modules (Available Now)

#### 🖥️ Compute
- Launch and manage EC2 instances with custom input
- Choose AMI, instance type, key pair, subnet, and security group
- Wait-for-instance ready logic
- List instances with public IP, state, and security groups

#### 🧱 Network
- Create/view/manage:
  - VPCs with CIDR, tenancy, and name
  - Subnets with custom CIDR, AZ, and tags
  - Security Groups with interactive inbound/outbound rule prompts

#### 🗃️ Storage
- Create and configure S3 buckets
  - Set ACLs (with recommendations)
  - Enable versioning
  - Control public access settings
- List buckets with ACL, versioning, and public access status

#### 📊 View/Inventory
- List EC2, VPCs, Subnets, S3 buckets, and Security Groups
- Choose single, multiple, or all AWS regions for viewing

---

### 🔵 Azure Support (Coming Soon)

Azure modules will include:
- VM deployment
- Resource group creation
- NSG rule handling
- Azure Blob Storage setup

---

## ⚙️ Tools & Tech Stack

- 🐍 Python 3.9+
- ☁️ AWS SDK (`boto3`)
- 🧩 CLI Shell Interface (Python)
- 🔐 IAM-authenticated operations
- 🔜 Azure SDK (`azure-cli` + `azure-identity`)

---

## 📦 Installation

### 🔧 Option 1: Clone via Git
```bash
git clone https://github.com/Mojo824/MCloud.git
cd MCloud
python Install_MCloud.py  # to run the tool (Windows only)
```
#And Enjoy using the tool by just typing MCloud to your Terminal or CMD
### 📥 Option 2: ZIP Download
- Download ZIP: [Click here](https://github.com/Mojo824/MCloud/archive/refs/heads/main.zip)
- Unzip and run:
```bash
cd MCloud-main
python MCloud.py  # Windows only
```

### 🚀 Option 3: Global Command (Windows Only)
To run `MCloud` from anywhere in your command prompt:
```bash
python install_mcloud.py
```
> **Run as Administrator!**

After installation, just type `MCloud` in any command prompt to launch the tool.

> ✅ **Before you begin**, ensure you’ve run:
```bash
aws configure
```

---

## 🧰 Use Cases

- 🔐 DevSecOps learning and labs
- ☁️ Infrastructure setup and teardown
- 🔄 Region-based automation testing
- 🧪 AWS & Azure multi-cloud exploration
- 📊 Cloud inventory reporting

---

## 📁 Folder Overview

```text
MCloud/
├── Aws/
│   ├── aws.py
│   ├── Compute/
│   ├── Network/
│   ├── Storage/
│   ├── View/
│
├── Azure/              <-- Azure modules will go here
│   ├── azure.py
│   ├── Compute/
│   ├── Network/
│   ├── Storage/
│
├── MCloud.py           <-- Main launcher (Windows only)
├── install_mcloud.py   <-- Windows installer for global command
├── LICENSE
└── README.md
```

---

## 👥 Contributions Welcome

Want to contribute AWS or Azure modules? PRs and feedback are highly welcome.

1. Fork the repo
2. Create a new branch
3. Push & submit a PR

---

## 🛡️ License

MIT License — see the `LICENSE` file.

---

## 👨‍💻 Author
#Mojo824#
Crafted with ☁️ by [**Mojo824**](https://github.com/Mojo824)
