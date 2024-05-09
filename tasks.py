"""Tasks for the project."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

# %% CONFIGS

DOCKER_IMAGE = "cloud-run-chatbot-demo"
DOCKER_TAG = "latest"

# %% TASKS


@task
def install(ctx: Context) -> None:
    """Install the project."""
    ctx.run("poetry install")


@task
def reset(ctx: Context) -> None:
    """Reset the installation."""
    ctx.run("rm -rf .venv/")
    ctx.run("rm -f poetry.lock")


@task
def serve(ctx: Context) -> None:
    """Serve the application."""
    ctx.run("poetry run gradio app.py")


@task
def build(ctx: Context) -> None:
    """Build the docker image."""
    ctx.run(f"docker build -t {DOCKER_IMAGE}:{DOCKER_TAG} .")


@task(pre=[build])
def run(ctx: Context) -> None:
    """Run the docker image."""
    ctx.run(f"docker run --rm -p 7860:7860 {DOCKER_IMAGE}:{DOCKER_TAG}")