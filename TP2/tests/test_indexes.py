import json

def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def normalize_index(index):
    return {key: sorted(value) for key, value in index.items()}

def test_index(name):
    generated = normalize_index(load(f"output/{name}_index.json"))
    expected = normalize_index(load(f"output/expected_{name}_index.json"))

    if generated == expected:
        print(f"[PASS] {name} index matches expected output")
        return True
    else:
        print(f"[FAIL] {name} index does NOT match expected output")
        gen_keys = set(generated.keys())
        exp_keys = set(expected.keys())
        extra_keys = gen_keys - exp_keys
        missing_keys = exp_keys - gen_keys
        if extra_keys:
            print(f"  Extra tokens in generated index: {list(extra_keys)[:10]} ...")
        if missing_keys:
            print(f"  Missing tokens from generated index: {list(missing_keys)[:10]} ...")
        return False

if __name__ == "__main__":
    all_passed = True
    for name in ["title", "description", "brand", "origin", "reviews"]:
        result = test_index(name)
        all_passed = all_passed and result

    if all_passed:
        print("\nAll indexes passed!")
    else:
        print("\nSome indexes did NOT match expected output. See above for details.")
