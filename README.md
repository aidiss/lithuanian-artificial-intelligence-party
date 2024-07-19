# AI Party Project

Welcome to the AI Party Project repository! This project is designed to simulate a political party with various roles, ministers, and meetings. It includes features for creating prompts for different roles, simulating meetings where positions are drawn, and checking news updates.

## Motivation

AI party should be more trustworthy than human politicians, because
- You know what you get with AI, but you never know with human politicians
- AI can be programmed to follow the constitution and party program
- AI can be more transparent and accountable than human politicians
- AI can be less prone to corruption and personal interests
- AI can make decisions based on data and logic rather than emotions and biases
- AI can work 24/7 without getting tired or distracted
- AI can be more efficient and effective in governance
Let's make one for Lithuania!


## Features

- Grounded on Lithuanian Constitution
- Clear and transparent Party Constitution
- Clear and transparent Roles
- Role responsibilities based on https://www.lrvalstybe.lt/valstybines-institucijos/ministerijos-ir-departamentai
- Position paper creation meetings.

## Tools

- Party Constitution generation prompt
- Role generation prompt (Head of Economy, ...)
- Role details generation prompt

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.12+
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aidiss/lithuanian-artificial-intelligence-party.git
    cd aiparty
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script to start the simulation:
    ```bash
    python main.py
    ```

2. Follow the prompts to generate roles, simulate meetings, and check news updates.

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

## ToDo 

- [x] Simulate discussion on a topic
- [x] Ability to create a position statement based on the discussion
- [x] Create role description prompts
- [x] Create party constitution
- [ ] Create party constitution creation prompt
- [ ] Opening statement
- [ ] Handle provided urls as context
- [ ] Ground on Lithuanian Constitution
- [ ] Ground on Party Constitution
- [ ] Add ability to find and use important context like news and statistical data
- [ ] Add support for multiple discussion rounds
- [ ] Add ability to create legislation proposals
- [ ] Create Chair that would use "tool use"/Agentic flow

## Links

- https://www.valdosta.edu/pa/documents/polpospa.pdf
- https://en.wikipedia.org/wiki/Position_paper

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
