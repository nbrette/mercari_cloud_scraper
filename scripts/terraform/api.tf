resource "google_project_service" "iam_api" {
  service                    = "iam.googleapis.com"
  disable_on_destroy         = "false"
  disable_dependent_services = "false"
  project                    = var.project_id
}

resource "google_project_service" "cloudrun_api" {
  service                    = "run.googleapis.com"
  disable_on_destroy         = "false"
  disable_dependent_services = "false"
  project                    = var.project_id
}

resource "google_project_service" "pubsub_api" {
  service                    = "pubsub.googleapis.com"
  disable_on_destroy         = "false"
  disable_dependent_services = "false"
  project                    = var.project_id
}
