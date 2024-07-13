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