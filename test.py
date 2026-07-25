from src.core.validator import Validator

validator = Validator()

valid, message = validator.validate(
    "P9899",
    {}
)

print(valid)
print(message)