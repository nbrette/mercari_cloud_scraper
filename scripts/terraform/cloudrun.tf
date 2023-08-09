resource "google_cloud_run_service" "mercari_scraper" {
  name     = var.service_name
  location = var.region
  project  = var.project_id

  lifecycle {
    ignore_changes = [
      template[0].metadata[0].annotations["run.googleapis.com/client-name"],
      template[0].metadata[0].annotations["run.googleapis.com/client-version"],
      template[0].spec[0].containers[0].env
    ]
  }

  autogenerate_revision_name = true

  template {
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale"  = 2
        "client.knative.dev/user-image"     = var.service_image_url
        "run.googleapis.com/client-name"    = "gcloud"
        "run.googleapis.com/client-version" = "404.0.0"
      }
      labels = {}
    }
    spec {
      container_concurrency = 4
      containers {
        env {
          name  = "PROJECT_ID"
          value = var.project_id
        }
        env {
          name  = "PUBSUB_TOPIC"
          value = var.pubsub_topic
        }
        env {
          name  = "PORT"
          value = var.port
        }
        image = var.service_image_url
        resources {
          limits = {
            cpu    = "1000m"
            memory = "256M"
          }
          requests = {}
        }
      }
      service_account_name = google_service_account.sac_mercari_scraper.email
    }
  }
}
