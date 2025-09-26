# per

Tämä on AI/ML-projektin minimirunko.

## Kansiot
- `src/`: Lähdekoodi
- `tests/`: Testit
- `.github/workflows/`: CI/CD-pipeline (GitHub Actions)


## Testien suoritus

Asenna ensin riippuvuudet:

```bash
pip install -r requirements.txt
```

### Aja testit
```bash
pytest tests/ -v
```

### Tarkista koodi linterillä
```bash
flake8 src/
```

### Tarkista turvallisuus
```bash
bandit -r src/
```
