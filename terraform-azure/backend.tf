terraform {
  backend "s3" {
    bucket         = "your-bucket-name"
    key            = "path/to/your/terraform.tfstate"
    region         = "us-west-2"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}