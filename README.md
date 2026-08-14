# Models

The repository intentionally does not store large model files.

For the final competition version, place or download a properly licensed quantized model here.

Recommended final structure:

```text
models/
└── your-model-file.gguf
```

Before using a model:
- Verify its license.
- Verify redistribution rights.
- Record the model name and version in README.md.
- Benchmark it on the target Arm64 environment.
- Never commit large model binaries unless the repository and hackathon rules permit it.
