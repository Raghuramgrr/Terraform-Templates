import os

def create_folders_and_files(base_path):
    directories = [
        "environments/dev",
        "environments/staging",
        "environments/prod",
        "modules/network",
        "modules/compute",
        "modules/storage"
    ]

    files = {
        "backend.tf": '''
terraform {
  backend "s3" {
    bucket         = "your-bucket-name"
    key            = "path/to/your/terraform.tfstate"
    region         = "us-west-2"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
        ''',
        "main.tf": '''
module "network" {
  source = "./modules/network"
}

module "compute" {
  source = "./modules/compute"
}

module "storage" {
  source = "./modules/storage"
}
        ''',
        "variables.tf": '''
variable "region" {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "us-west-2"
}
        ''',
        "outputs.tf": '''
output "vpc_id" {
  value = module.network.vpc_id
}
        '''
    }

    env_files = {
        "main.tf": '''
provider "aws" {
  region = var.region
}

module "network" {
  source = "../../modules/network"
}

module "compute" {
  source = "../../modules/compute"
}

module "storage" {
  source = "../../modules/storage"
}
        ''',
        "variables.tf": '''
# Define your variables here
        ''',
        "outputs.tf": '''
# Define your outputs here
        ''',
        "terraform.tfvars": '''
region = "us-west-2"
        '''
    }

    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

        if "environments" in dir_path:
            for file_name, content in env_files.items():
                file_path = os.path.join(dir_path, file_name)
                with open(file_path, "w") as file:
                    file.write(content.strip())
                    print(f"Created file: {file_path}")

        if "modules" in dir_path:
            for file_name, content in files.items():
                file_path = os.path.join(dir_path, file_name)
                with open(file_path, "w") as file:
                    file.write(content.strip())
                    print(f"Created file: {file_path}")

    for file_name, content in files.items():
        file_path = os.path.join(base_path, file_name)
        with open(file_path, "w") as file:
            file.write(content.strip())
            print(f"Created file: {file_path}")

if __name__ == "__main__":
    base_path = "terraform-azure"
    create_folders_and_files(base_path)
    print("Terraform project structure has been created.")
