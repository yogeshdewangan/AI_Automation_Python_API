from agents import test_generator_agent, test_execution_agent, log_analysis_agent

if __name__ == "__main__":
    print("🚧 Generating test cases with AI...")
    api_description = "GET request to https://jsonplaceholder.typicode.com/users/1"
    test_code = test_generator_agent.generate_test_code(api_description)
    test_generator_agent.save_test(test_code)

    print("🚀 Running tests...")
    test_execution_agent.run_pytest()

    print("📊 Analyzing logs...")
    log_analysis_agent.analyze_logs()