provider "aws" {
  region = "eu-central-1"
}

resource "aws_s3_bucket" "data_bucket" {
  bucket = "gp-data-engineer-excel-pipeline"
  acl    = "private"
}