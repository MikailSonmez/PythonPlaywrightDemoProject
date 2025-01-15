import subprocess

def run_tests():
    subprocess.run(["python", "-m", "behave"])

if __name__ == "__main__":
    run_tests()