# DevOps Python Project

A containerized Python application featuring a fully automated CI/CD pipeline with automated testing and Docker Hub deployment via GitHub Actions.

## Features
- **Automated Testing:** Runs `pytest` automatically on every push to the `main` branch before building.
- **Containerization:** Packaged as a lightweight Docker container.
- **CI/CD Automation:** Automatically builds and pushes the latest container image to Docker Hub upon passing tests.

## CI/CD Pipeline Workflow
1. **Test Job:** Checks out code, sets up Python, installs dependencies, and runs `pytest`.
2. **Build & Push Job:** Triggers only after tests pass, logs into Docker Hub securely using secrets, and pushes the updated image.
