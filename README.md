# Uploading an Agent in Weni CLI

## Prerequisites
Before starting, make sure you have Python installed on your machine.

## Step-by-Step Guide

### 1. Clone the Repository
Open your terminal and navigate to the correct repository:
```sh
cd examples-agent-builder
```

### 2. Choose One of the Agents
You can select one of the three available options:
- `books-agentbuilder2`
- `movies-agentbuilder2`
- `news-agentbuilder2`

Example for the books agent:
```sh
cd books-agentbuilder2
```

### 3. Install Weni CLI
Install the correct version of Weni CLI using:
```sh
pip install weni-cli==2.0.3
```

### 4. Authenticate with Weni
Log in to Weni using the following command:
```sh
weni login
```

### 5. Select the Project
To list available projects, use:
```sh
weni project list
```

After identifying the UUID of the desired project, select it with:
```sh
weni project use UUID
```
(Replace `UUID` with the correct project identifier.)

### 6. Test the Agent Execution
Now, run the corresponding agent:

- For the books agent:
```sh
weni run agent_definition.yaml book_agent get_books
```

- For the news agent:
```sh
weni run agent_definition.yaml news_agent get_news
```

- For the movies agent:
```sh
weni run agent_definition.yaml movie_agent_new get_movies_new
```

If the command output does not contain any errors, proceed to the next step.

### 7. Upload the Agent
If the output is incorrect or errors appear, upload the agent using:
```sh
weni project push agent_definition.yaml
```
If the process is successful, the terminal output should match Weni's expected response.

## Final Considerations
This guide applies to any of the three agents. Just change the directory name and execution command as needed.

If you have any doubts or encounter errors, ensure all steps were followed correctly and try again.

