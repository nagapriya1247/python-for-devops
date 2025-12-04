import sys

# Get command line argument
env = sys.argv[1]  # e.g., "prod" or "dev"

# Print to output
sys.stdout.write(f"Deploying to {env}\n")

# Exit if env is not valid
if env not in ["dev", "prod", "QA"]:
    sys.stderr.write("Invalid environment\n")
    sys.exit(1)

# Print Python version
print(f"Python version: {sys.version}")
