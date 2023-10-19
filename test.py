import subprocess

FAST_DOWNWARD_PATH = "/Users/rick/downward/fast-downward.py"
VALIDATE_PATH = "/Users/rick/VAL/build/bin/validate"

def run_validator(domain_file, problem_file, plan_file):
    cmd = [VALIDATE_PATH, domain_file, problem_file, plan_file]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def run_fast_downward(domain_file, problem_file):
    cmd = [FAST_DOWNWARD_PATH, domain_file, problem_file, "--heuristic", "h=ff()", "--search", "astar(h)"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


if __name__ == "__main__":
    domain_path = "/Users/rick/PycharmProjects/pddl_planning/domain.pddl"
    problem_path = "/Users/rick/PycharmProjects/pddl_planning/problem.pddl"

    output = run_fast_downward(domain_path, problem_path)

    # 保存计划到文件
    with open("plan.txt", "w") as f:
        f.write(output)

    # 使用验证器验证计划
    validation_output = run_validator(domain_path, problem_path, "plan.txt")
    print(validation_output)
