variable "project_id" {}
variable "service_name" {}
variable "service_sac_name" {}
variable "service_image_url" {}
variable "region" {}
variable "pubsub_topic" {}
variable "port" {}

data "google_project" "project" {}
