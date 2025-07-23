# PokéML ⚡

A modular ELT and ML pipeline designed to extract, load, and model Pokémon data for analytics and insights.

---

## 🚀 Overview

PokéML automates the workflow of:

1. **Extracting** Pokémon data via GraphQL API  
2. **Loading** it into a SQL-ready environment using dbt  
3. **Modeling** with dbt and adding custom transformations  
4. **Exploring** via notebooks and analytical queries  
5. **Testing** with snapshots and unit tests to validate data quality  
6. **Training** machine learning models on Pokémon stats  

Perfect for demonstrating analytics engineering processes and machine learning use cases with open, structured data.

---

## 🗂️ Repo Structure

- `scripts/` – Utilities for data extraction (GraphQL calls, JSON downloads)  
- `seeds/` – Static CSVs ingested into dbt for lookup tables  
- `models/`, `macros/`, `snapshots/` – dbt assets for structured data modeling & incremental logic  
- `analyses/`, `notebooks/` – Exploratory notebooks analyzing Pokémon stats and model behavior  
- `docs/` – Auto-generated documentation from dbt models  
- `tests/` – Data quality checks and snapshot validations  
- `queries/` – SQL files for custom analysis and metric computation  

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+  
- `pip install -r requirements.txt`  
- dbt Core installed (version in `requirements.txt`)  

### Setup & Run

```bash
git clone https://github.com/ChrisAdan/pokemon.git
cd pokemon

# Install dependencies
pip install -r requirements.txt

# Set environment vars (e.g. TARGET, DB connection)
export DBT_TARGET=dev
# or use direnv

# Run models
dbt run

# Run tests
dbt test
```
## 🔍 Explore & Train

- Use `analyses/` or `notebooks/` for EDA on Pokémon stats  
- Build ML models (e.g. predicting Pokémon types or abilities) using models output from dbt  

---

## 📊 Documentation

Generate documentation:

```bash
dbt docs generate  
dbt docs serve
```

---

## 📌 Why PokéML?

- 💡 Showcases full ELT-to-ML workflow with open data  
- ✅ Demonstrates analytics engineering best practices (modularity, testing, docs)  
- 🚀 Great learning tool and portfolio piece for dbt and ML pipelines  

---

## ⚖️ License

MIT – see [LICENSE](LICENSE) for details.

---

## 🙌 Contributions Welcome

Enhance PokéML by:

- Adding tests or snapshot logic  
- Building richer ML models or dashboards  
- Improving documentation  
- Submitting enhancements via PRs or issues  

---

## 🔗 Related Projects

- [BlockStream](https://github.com/ChrisAdan/blockstream) – Automated crypto analytics pipeline with AI insights and dashboard delivery  
- [Patient Risk Simulation](https://github.com/ChrisAdan/fhir) – Full-stack healthcare pipeline using FHIR, dbt, Snowflake, and ML models  
- [ShiftStats](https://github.com/ChrisAdan/shiftstats) – Quick ETL & insight analytics  
- [WeatherStats](https://github.com/ChrisAdan/weather_stats) – Pipeline for weather EDA  

