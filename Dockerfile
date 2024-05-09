# https://docs.docker.com/engine/reference/builder/

FROM python:3.12

ENV GRADIO_SERVER_NAME="0.0.0.0"
ENV GRADIO_SERVER_PORT="7860"

EXPOSE 7860

COPY app.py .
RUN pip install --no-cache-dir gradio
CMD ["python", "app.py"]
