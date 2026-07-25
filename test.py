from src.core.validator import Validator

validator = Validator()


def run_test(title, routine, parameters):

    print(f"\n=== {title} ===")

    valid, errors = validator.validate(routine, parameters)

    print(f"Valid: {valid}")

    if errors:
        print("Errors:")
        for error in errors:
            print(f" - {error}")
    else:
        print("No errors.")


# 1 - Rotina válida
run_test(
    "Test 1 - Valid routine",
    "P9811",
    {
        "Z": 0
    }
)

# 2 - Rotina inexistente
run_test(
    "Test 2 - Unknown routine",
    "P9999",
    {
        "Z": 0
    }
)

# 3 - Parâmetro inexistente
run_test(
    "Test 3 - Unknown parameter",
    "P9811",
    {
        "ABC": 10
    }
)

# 4 - Falta parâmetro obrigatório (one_of)
run_test(
    "Test 4 - Missing required parameter",
    "P9811",
    {
        "F": 1
    }
)

# 5 - Parâmetro não permitido
run_test(
    "Test 5 - Parameter not allowed",
    "P9811",
    {
        "Z": 0,
        "C": 1
    }
)

# 6 - Múltiplos erros
run_test(
    "Test 6 - Multiple errors",
    "P9999",
    {
        "ABC": 10
    }
)