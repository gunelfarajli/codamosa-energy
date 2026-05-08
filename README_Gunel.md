### Running CodaMOSA with Energy Modifications

This artefact summarises the changes made to the original CodaMOSA repository and the instructions for replication.

- Clone the repository:
```bash
git clone https://github.com/your-username/codamosa-energy
cd codamosa-energy
```

- Build the Docker image (only needed once):
```bash
docker build -t codamosa-energy .
```

- Remove any existing output to avoid appending to previous results:
```bash
rm -rf codamosa_energy_runs/*
rm -f emissions/energy_breakdown.csv
```

- Run CodaMOSA across all 50 modules:
```bash
./scripts/run_50_modules.sh test-apps/selected_50_modules.csv codamosa/codamosa_runs/ config-args/codamosa-0.8-uninterp 180 --auth <api_key_path>
```

- The test outputs can be found in the `codamosa/codamosa_runs/` directory and the energy measurements for original project experiment at `replication/emissions/energy_breakdown_uk_ci_applied.csv` and for replication at `replication/emissions/energy_breakdown.csv`.

# All the edited/added files for the experiment are listed below:
- `Dockerfile`
- `config-args/codamosa-0.8-uninterp`
- `scripts/run_50_modules.sh`
- `pynguin/languagemodels/model.py`
- `pynguin/generation/algorithms/codamosastrategy.py`
- `test-apps/selected_50_modules.csv`
- `codamosa/codamosa_runs/`
- `emissions/energy_breakdown.csv`
