resource "google_compute_network" "vpc_network" {
  name = var.vpc_network_name
  auto_create_subnetworks = true
}

resource "google_compute_firewall" "firewall" {
  name = var.firewall_name
  network = google_compute_network.vpc_network.name

  allow {
    protocol = "tcp"
    ports = ["22","25","53","80","110","143","443","993","995","8080","8081","8000"]
  }

  source_ranges = var.source_ranges
}

