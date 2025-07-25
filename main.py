from agents import test_generator_agent, test_execution_agent, log_analysis_agent

if __name__ == "__main__":
    endpoints = {}
    endpoints["GET"] = "https://jsonplaceholder.typicode.com/users/1"
    endpoints["POST"] = "https://reqres.in/api/users"


    for method, endpoint in endpoints.items():
        print(f"🚧 Generating test cases with AI...for endpoint {endpoint}")
        api_description = f"{method} request to {endpoint}"
        test_code = test_generator_agent.generate_test_code(api_description)
        test_generator_agent.save_test(test_code, f"tests/test_generated_{method}.py")

        print("🚀 Running tests...")
        test_execution_agent.run_pytest()

        print("📊 Analyzing logs...")
        log_analysis_agent.analyze_logs()