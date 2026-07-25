from src.core.validators.validator import Validator

validator = Validator()


def test(title, routine, parameters, option=None):

    print("=" * 70)
    print(title)

    try:

        valid, errors = validator.validate(
            routine,
            parameters,
            option
        )

        print("Valid :", valid)

        if errors:

            print("Errors:")

            for error in errors:
                print(" -", error)

        else:

            print("No errors.")

    except Exception as e:

        print(type(e).__name__)
        print(e)


# =====================================================
# P9834 - Surface (VALID)
# =====================================================

test(
    "P9834 - Surface",
    "P9834",
    {
        "Z": 10,
        "T": 5
    },
    "Surface"
)


# =====================================================
# P9834 - Angled surface (VALID)
# =====================================================

test(
    "P9834 - Angled surface",
    "P9834",
    {
        "A": 30,
        "Z": 10,
        "B": 0
    },
    "Angled surface"
)


# =====================================================
# P9834 - Angled surface using invalid optional (INVALID)
# =====================================================

test(
    "P9834 - Invalid optional parameter",
    "P9834",
    {
        "A": 30,
        "Z": 10,
        "T": 5
    },
    "Angled surface"
)


# =====================================================
# P9814 - Bore (VALID)
# =====================================================

test(
    "P9814 - Bore",
    "P9814",
    {
        "D": 20
    },
    "Bore"
)