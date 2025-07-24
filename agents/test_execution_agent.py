import subprocess
import warnings, os
warnings.filterwarnings('ignore')
def run_pytest():
    log_file = "logs/test_failures.log"
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Clear existing log content (optional)
    with open(log_file, "w") as f:
        f.write("")
    result = subprocess.run(["pytest", "tests/", "--tb=short", "--capture=tee-sys", "--log-file=logs/test_failures.log"])
    print("\n✅ Test execution completed.")
    return result.returncode