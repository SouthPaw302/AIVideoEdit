"""Development entrypoint: python -m runtime_v2.bridge"""

import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "runtime_v2.bridge.app:app",
        host="127.0.0.1",
        port=8787,
        reload=False,
    )
