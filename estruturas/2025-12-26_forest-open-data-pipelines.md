# Estrutura do Projeto: forest-open-data-pipelines

Gerado em: 26/12/2025 09:13:32
Este documento descreve a hierarquia de pastas e arquivos.

```text
forest-open-data-pipelines/
├── .github
│   └── worflows
│       └── daily_sync.yml
├── configs
│   ├── datasets
│   │   └── cvm_fi_inf_diario.yml
│   ├── schedules
│   │   └── daily_0900_brt.yml
│   └── app.yml
├── data
├── docs
├── logs
├── scripts
│   ├── backfill_cvm_inf_diario.py
│   └── run_local.sh
├── src
│   └── forest_pipelines
│       ├── datasets
│       │   ├── cvm
│       │   │   ├── __init__.py
│       │   │   └── fi_inf_diario.py
│       │   └── __init__.py
│       ├── manifests
│       │   ├── __init__.py
│       │   └── build_manifest.py
│       ├── registry
│       │   ├── __init__.py
│       │   └── datasets.py
│       ├── storage
│       │   ├── __init__.py
│       │   └── supabase_storage.py
│       ├── utils
│       │   ├── __init__.py
│       │   ├── dates.py
│       │   └── hashing.py
│       ├── __init__.py
│       ├── cli.py
│       ├── http.py
│       ├── logging_.py
│       └── settings.py
├── .env.example
├── .gitignore
├── Makefile
├── pyproject.toml
└── README.md
```
