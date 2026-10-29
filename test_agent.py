# Import the helper function we wrote in agent.py
from agent import ask_agent

print("--- Starting Agent Tests ---\n")

# Test 1: No tool needed (Direct LLM response)
print("Test 1: Hello! What can you do?")
print("Result:", ask_agent("Hello! What can you do?"))
print("-" * 30)

# Test 2: Calculator tool
print("Test 2: What is 15% of 240?")
print("Result:", ask_agent("What is 15% of 240?"))
print("-" * 30)

# Test 3: Weather tool (API call)
print("Test 3: What is the weather in Tokyo right now?")
print("Result:", ask_agent("What is the weather in Tokyo right now?"))
print("-" * 30)

# Test 4: Multi-tool chaining (Weather + Calculator)
print("Test 4: What is the weather in London, and what is that temperature multiplied by 2?")
print("Result:", ask_agent("What is the weather in London, and what is that temperature multiplied by 2?"))
print("-" * 30)

print("\n--- Tests Complete ---")