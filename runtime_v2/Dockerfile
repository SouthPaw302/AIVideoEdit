FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg git ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY runtime_v2/requirements.txt /tmp/runtime-v2-requirements.txt
RUN python -m pip install -r /tmp/runtime-v2-requirements.txt

COPY . /app

RUN useradd --create-home --uid 10001 aivideo \
    && mkdir -p /state/jobs /state/studio /app/.aivideoedit/models \
    && chown -R aivideo:aivideo /state /app/.aivideoedit

USER aivideo

ENV PORT=8787 \
    BRIDGE_WORKSPACE_ROOT=/state/jobs \
    AIVIDEOEDIT_REPO_ROOT=/app

EXPOSE 8787

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import json,urllib.request; json.load(urllib.request.urlopen('http://127.0.0.1:8787/health', timeout=3))"

CMD ["python", "-m", "runtime_v2.serve"]
