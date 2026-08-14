# EdgeVoice — Privacy-First AI Assistant for Arm64

EdgeVoice is a beginner-friendly edge-AI project designed for an Arm optimization hackathon.

It provides:
- A zero-dependency Windows demo mode that runs with Python only.
- An Arm64 benchmark script using Python's standard library.
- A reproducible GitHub Actions workflow for an Arm64 Linux runner.
- A clear place to add a real quantized LLM when Arm hardware/model access is available.

> Important: The included Windows demo is a deterministic demonstration UI. It does **not** claim to contain a full LLM. For a competition submission, run the real-model path and replace the demo benchmark with measured inference results.

## Project structure

```text
EdgeVoice/
├── app/
│   ├── app.py
│   └── config.py
├── benchmark/
│   ├── benchmark.py
│   └── results.md
├── demo/
│   └── demo_script.md
├── models/
│   └── README.md
├── scripts/
│   ├── setup.sh
│   └── download_models.sh
├── .github/
│   └── workflows/
│       └── arm-benchmark.yml
├── .gitignore
├── Dockerfile
├── LICENSE
├── requirements.txt
└── README.md
```

## Windows quick start

No package installation is required for the included demo.

1. Install Python 3.11+.
2. Open Command Prompt inside this repository.
3. Run:

```bash
python app/app.py
```

4. In another Command Prompt, run:

```bash
python benchmark/benchmark.py
```

## What the demo shows

```text
User input
   ↓
Local assistant logic
   ↓
Response
   ↓
Performance benchmark
```

The architecture is intentionally separated so that a real local quantized model can be added later without changing the repository layout.

## Arm64 benchmark

The GitHub Actions workflow runs the standard-library benchmark on an Arm64 Linux environment when an Arm64 runner is available to the repository/account.

The workflow also prints:

- CPU architecture
- Python version
- benchmark latency
- throughput
- memory information when available

Do not present simulated/demo numbers as real LLM inference results.

## Hackathon track

Recommended: **Track 1 — Optimization Output**

For the final submission, the strongest version should include:
1. A real quantized model.
2. Real Arm64 inference.
3. Before/after measurements.
4. Public source code.
5. A short demonstration video.

## License

MIT.
