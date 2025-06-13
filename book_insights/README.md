# 📚 Book Price Dashboard

A data visualization web app that presents an interactive dashboard for exploring book pricing, ratings, genres, and stock availability. Built with **Dash**, **Plotly**, and **Flask**, and powered by a cleaned dataset from a companion **book scraper project**.

---

## 📦 Features

- 📈 **Price Distribution by Genre** – Box plots to spot expensive/affordable genres.
- ⭐ **Average Rating by Genre** – Bar chart showing quality by category.
- 📊 **Smoothed Price vs. Rating Trend** – Trend line (LOWESS) + raw data scatter.
- 📚 **Book Count by Genre** – Which genres dominate the dataset?
- 🧮 **Stock Availability by Genre** – Total book stock per genre.
- 🔌 **REST API** – `/api/stats` endpoint for programmatic access to average price/rating per genre.

---

## 🛠 Technologies Used

- **Dash** – Web interface for interactive Python dashboards.
- **Plotly** – Rich, interactive plotting.
- **Flask** – REST API backend.
- **Pandas** – Data transformation and grouping.
- **Statsmodels** – LOWESS smoothing for visual trend clarity.
- **Docker** – Containerization for reproducible deployment.
- **GitHub Codespaces** – Optional no-install dev environment in the cloud.

---

## 🗂️ Dataset

This dashboard uses the file: books_ascii_clean.csv

...which is the result of a previous scraper project that collected:
- Title, Genre, Rating, Price
- Stock availability
- Book descriptions

---

## 🚀 Running the App

### ✅ Option 1: GitHub Codespaces (No Setup Required)

1. Click **Code → Codespaces → Create codespace on main**.
2. It builds and runs the app inside a cloud VM.
3. When ready, click the forwarded **Port 8050** to open the app.

---

### 🐳 Option 2: Docker (Recommended for Deployment)

#### 1. Clone the repo

```bash
git clone https://github.com/viktor-july/book_dashboard.git
cd book_dashboard