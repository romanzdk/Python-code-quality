# Make

- `sudo apt-get install build-essential` or
- `brew install make` or
- `nix-shell -p gnumake`

# Just

- https://github.com/casey/just?tab=readme-ov-file#installation or
- `brew install just` or
- `nix-shell -p just`

# Task

- https://taskfile.dev/installation/
- `brew install go-task` or
- `nix-shell -p go-task`

# Nox(poetry)

- `poetry add nox-poetry`

# Poe the poet

- https://poethepoet.natn.io/installation.html
- `pip install poethepoet` or
- `nix-shell -p poethepoet` or
- `poetry self add 'poethepoet[poetry_plugin]'`

# SonarQube

1. Start the sonarqube server

   1. `docker run --rm -it --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest`
   1. Wait until logs say "SonarQube is operational"

1. Create project in the SonarQube

1. Access the webserver at https://localhost:9000/ with credentials admin:admin
1. Create new local project named `python_code_quality`

1. Run Sonar scanner CLI

   - Using NIX
     `nix-shell -p sonar-scanner-cli nodejs`

     ```shell
     sonar-scanner \
         -Dsonar.exclusions=project_management/** \
         -Dsonar.projectKey=python_code_quality \
         -Dsonar.sources=. \
         -Dsonar.host.url=http://localhost:9000 \
         -Dsonar.token=sqp_fcd12dcb5e53b2a9290ab9811fffdc5d66fcf72b

     ```

   - Using docker
     ```shell
     docker run \
         --rm \
         -e SONAR_HOST_URL="http://localhost:9000" \
         -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=python_code_quality" \ # replace this
         -e SONAR_TOKEN="sqp_fcd12dcb5e53b2a9290ab9811fffdc5d66fcf72b" \ # replace this
         -v "${PWD}:/usr/src" \
         sonarsource/sonar-scanner-cli
     ```
