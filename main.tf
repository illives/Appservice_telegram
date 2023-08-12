provider "google" {
  credentials = file("C:/Users/DELL LATITUDE 5480/Documents/GCP_SVA/divine-bonbon-395622-8c5ed98cf892.json")
  project     = "divine-bonbon-395622"
  region      = "us-cetral1"
}

resource "google_app_engine_standard_app_version" "app" {
  version_id = "v1"
  service    = "default"
  runtime    = "python310"
  entrypoint = "pytho3 app_service/main.py"
  deployment {
    files = [
      "app_service/main.py",
      "app.yaml",
      "requirements.txt"
    ]
  }
}

resource "google_app_engine_standard_app_version_traffic_split" "app" {
  version_id = google_app_engine_standard_app_version.version_id
  service    = google_app_engine_standard_app_version.app.service
  split {
    percent = 100
  }
}