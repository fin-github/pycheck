from pycheck import Schema

def UNSAFE_get_rand_int() -> dict: # risky function that may reply invalid format
    res = {"random_number": 1} # insert risky behavior that may return something else
    return res

valid_schema: Schema = Schema(
    {
        "random_number": int
    }
)

unsafe_value: dict = UNSAFE_get_rand_int()
is_safe: bool = valid_schema.check(unsafe_value)

print(f"Is Safe: {is_safe}")