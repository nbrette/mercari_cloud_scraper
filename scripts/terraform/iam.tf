resource "google_service_account" "sac_mercari_scraper" {
  account_id   = var.service_sac_name
  display_name = var.service_sac_name
  project      = var.project_id

  depends_on = [google_project_service.iam_api]
}

resource "google_project_iam_member" "cloudrun_invoker_roles" {
  role    = "roles/run.invoker"
  member  = "serviceAccount:${google_service_account.sac_mercari_scraper.email}"
  project = var.project_id
}

resource "google_project_iam_member" "cloudbuild_sac_permissions" {
  for_each = toset([
    "roles/run.admin",
    "roles/iam.serviceAccountUser",
  ])
  role    = each.key
  member  = "serviceAccount:${data.google_project.project.number}@cloudbuild.gserviceaccount.com"
  project = var.project_id
}
