import platform
import time
from config import PROJECT_NAME, VERSION

RESPONSES = {
    "hello": "Hello! I am EdgeVoice, a local edge-AI demonstration.",
    "hi": "Hi! EdgeVoice is ready.",
    "what is ai": "Artificial intelligence is the field of building systems that perform tasks that normally require human intelligence.",
    "what is arm": "Arm is a processor architecture widely used in mobile, embedded, and edge devices.",
    "privacy": "A local AI assistant can keep sensitive input on the device instead of sending it to a remote service.",
    "edge ai": "Edge AI means running AI inference near the user or device instead of relying entirely on a cloud server.",
}

def answer(text: str) -> str:
    cleaned = " ".join(text.lower().strip().split())
    for key, value in RESPONSES.items():
        if key in cleaned:
            return value
    return (
        "EdgeVoice received your request locally. "
        "In the full competition version, this interface is connected "
        "to a quantized language model running on Arm64."
    )

def main():
    print("=" * 64)
    print(f"{PROJECT_NAME} v{VERSION}")
    print("=" * 64)
    print("Architecture:", platform.machine())
    print("Mode: local demonstration")
    print("Pipeline: Input -> local inference interface -> response")
    print("\nType 'exit' to stop.\n")

    while True:
        try:
            text = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nEdgeVoice stopped.")
            break

        if text.lower() in {"exit", "quit"}:
            print("EdgeVoice stopped.")
            break

        if not text:
            continue

        start = time.perf_counter()
        response = answer(text)
        elapsed_ms = (time.perf_counter() - start) * 1000

        print("EdgeVoice:", response)
        print(f"[local response time: {elapsed_ms:.3f} ms]\n")

if __name__ == "__main__":
    main()
