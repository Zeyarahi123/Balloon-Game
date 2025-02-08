# Balloon Blast Game Application

## Prerequisites

Before running the application, ensure that you have the following installed:

- **Python**: Version `>=3.9` and `<4.0`
- **Poetry**: Version `2.0.1`

You can install Poetry by following the instructions in the [official documentation](https://python-poetry.org/docs/#installation).

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:Zeyarahi123/Balloon-Game.git
    cd Balloon-Game
    ```

2. Install **Poetry** (if not already installed):

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Install project dependencies using Poetry:

    ```bash
    poetry install -vv
    ```

4. Update project dependencies if needed:

    ```bash
    poetry update -vv
    ```

## Running the Balloon Blast Game

1. Start the FastAPI server:

    ```bash
    poetry run balloon-game
    ```

2. Once the game launches, follow these rules:

    - Pop a balloon to earn **one point**.
    - If you miss **five balloons**, the game **ends**.
