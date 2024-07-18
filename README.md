# AI Party Project

Welcome to the AI Party Project repository! This project is designed to simulate a political party with various roles, ministers, and meetings. It includes features for creating prompts for different roles, simulating meetings where positions are drawn, and checking news updates.

## Motivation

- AI party should be more trustworthy than human politicians:
    - You know what you get with AI, but you never know with human politicians
    - AI can be programmed to follow the constitution and party program
    - AI can be more transparent and accountable than human politicians
    - AI can be less prone to corruption and personal interests
    - AI can make decisions based on data and logic rather than emotions and biases
    - AI can work 24/7 without getting tired or distracted
    - AI can be more efficient and effective in governance
Let's make one for Lithuania!

## Important asp

- Grounded on Lithuanian Laws
- Grounded on Data
- Grounded on News
- Clear party program
- Clear roles and responsibilities
- Orchestration of meetings

## Summary
A number of AI agents that are responsible for different areas of governance. They are programmed to follow the constitution and party program, make decisions based on data and logic, and work together to achieve the party's goals. The AI agents are transparent, accountable, and efficient, making them more trustworthy than human politicians. Product of work creation of political positions.

## Tools

- Constitution generation prompt
- Role generation prompt
- Role details generation prompt

## Features

- **Constitution**: View the constitution of the Lithuanian Party of Artificial Intelligence (LPAI). [Constitution](constitution/constitution.md)
- **Positions**: Explore the different roles and positions within the AI party. [Positions](positions)
- **Role Prompts**: Generate unique prompts for different roles within the AI party. [Role](role_instructions)
- **Minister Prompts**: Specific prompts tailored for ministerial positions. [Minister](role_instructions/president.md)
- **Meeting Simulation**: Simulate party meetings where roles and positions are assigned. [Meeting](meeting.py)
- **News Updates**: Check for the latest news relevant to the AI party.
- **Translation with DeepL**: Translate text using the DeepL API.


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

## Links

- https://www.valdosta.edu/pa/documents/polpospa.pdf
- https://en.wikipedia.org/wiki/Position_paper

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
