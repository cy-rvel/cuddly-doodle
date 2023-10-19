import subprocess

FAST_DOWNWARD_PATH = "/Users/rick/downward/fast-downward.py"
VALIDATE_PATH = "/Users/rick/VAL/build/bin/validate"

def run_validator(domain_file, problem_file, plan_file):
    cmd = [VALIDATE_PATH, domain_file, problem_file, plan_file]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

domain_path = "/Users/rick/PycharmProjects/pddl_planning/domain.pddl"
problem_path = "/Users/rick/PycharmProjects/pddl_planning/problem.pddl"
validation_output = run_validator(domain_path, problem_path, "plan.txt")
print(validation_output)