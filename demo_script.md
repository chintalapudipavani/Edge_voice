# EdgeVoice Demo Script — Under 3 Minutes

## 0:00–0:15 — Introduction

Show the GitHub repository.

Say:

> EdgeVoice is a privacy-first edge-AI assistant designed for efficient Arm64 inference.

## 0:15–0:45 — Run the application

Run:

```bash
python app/app.py
```

Ask:

```text
What is AI?
```

Then:

```text
Why is edge AI useful?
```

## 0:45–1:15 — Show the benchmark

Run:

```bash
python benchmark/benchmark.py
```

Show the architecture and measured benchmark output.

## 1:15–1:45 — Explain the optimization goal

Show:

```text
Cloud AI
   ↓
Network dependency

EdgeVoice
   ↓
Local inference
   ↓
Arm64 optimization
```

Explain that the final competition version should use a real quantized model and real Arm64 inference measurements.

## 1:45–2:15 — Show repository

Show:
- README
- benchmark
- GitHub Actions workflow
- LICENSE

## 2:15–2:30 — Closing

Say:

> EdgeVoice explores how useful AI can move closer to the user through local inference, quantization, and Arm64-aware optimization.
