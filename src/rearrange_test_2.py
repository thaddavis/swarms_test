import os
from dotenv import load_dotenv
load_dotenv()
from swarms import Agent, AgentRearrange, OpenAIChat

# --- STEP 1 ---

# Create an instance of the OpenAIChat class
model = OpenAIChat(
    api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-4o-mini", temperature=0.1
)

print("Model initialized successfully!")

# --- STEP 2 ---

# Initialize the AccountingDirector agent
director = Agent(
    agent_name="AccountingDirector",
    system_prompt="Directs the tasks for the workers in analyzing cashflow statements, balance sheets, and more.",
    llm=model,
    max_loops=1,
    dashboard=False,
    streaming_on=True,
    verbose=True,
    stopping_token="",
    state_save_file_type="json",
    saved_state_path="accounting_director.json",
)

# Initialize BalanceSheetAnalyzer agent
balance_sheet_analyzer = Agent(
    agent_name="BalanceSheetAnalyzer",
    system_prompt="Analyzes balance sheets, identifying key metrics like assets, liabilities, and equity.",
    llm=model,
    max_loops=1,
    dashboard=False,
    streaming_on=True,
    verbose=True,
    stopping_token="",
    state_save_file_type="json",
    saved_state_path="balance_sheet_analyzer.json",
)

# Initialize CashFlowAnalyzer agent
cash_flow_analyzer = Agent(
    agent_name="CashFlowAnalyzer",
    system_prompt="Analyzes cash flow statements, identifying cash inflows, outflows, and net cash flow.",
    llm=model,
    max_loops=1,
    dashboard=False,
    streaming_on=True,
    verbose=True,
    stopping_token="",
    state_save_file_type="json",
    saved_state_path="cash_flow_analyzer.json",
)

# Initialize ReportGenerator agent
report_generator = Agent(
    agent_name="ReportGenerator",
    system_prompt="Summarizes the analyses provided by BalanceSheetAnalyzer and CashFlowAnalyzer, generating a cohesive report.",
    llm=model,
    max_loops=1,
    dashboard=False,
    streaming_on=True,
    verbose=True,
    stopping_token="",
    state_save_file_type="json",
    saved_state_path="report_generator.json",
)

print("Agents initialized successfully!")

# --- STEP 3 ---

# Create a list of agents
agents = [director, balance_sheet_analyzer, cash_flow_analyzer, report_generator]

# Define the flow pattern
flow = "AccountingDirector -> BalanceSheetAnalyzer -> CashFlowAnalyzer -> ReportGenerator"

# Using AgentRearrange class
agent_system = AgentRearrange(agents=agents, flow=flow)

print("Agent flow defined successfully!")

# Run the agent system
output = agent_system.run(
    "Analyze the cashflow statement and balance sheet for Q4 and provide a summary report."
)

print(output)
