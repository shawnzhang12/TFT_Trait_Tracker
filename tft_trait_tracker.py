import argparse
import json
from collections import defaultdict, Counter
from tabulate import tabulate

def load_champions(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def load_trait_goals(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def find_combos(champions, trait_goals, min_traits_required, max_units, must_include_names, free_traits, cache_path="combo_cache.jsonl"):
    must_include = [c for c in champions if c["name"] in must_include_names]
    pool = [c for c in champions if c["name"] not in must_include_names]
    base_trait_counter = Counter()
    for champ in must_include:
        for trait in champ["traits"]:
            base_trait_counter[trait] += 1
    for trait in free_traits:
        base_trait_counter[trait] += 1

    seen = set()
    saved_combos = []
    max_traits_achieved = 0
    calls = 0

    def count_active_traits(counter):
        return sum(counter[t] >= trait_goals.get(t, 2) for t in counter)

    def save_combo(combo):
        names = sorted(c["name"] for c in combo)
        key = tuple(names)
        if key in seen:
            return
        seen.add(key)
        traits = Counter()
        for champ in combo:
            for t in champ["traits"]:
                traits[t] += 1
        for t in free_traits:
            traits[t] += 1
        cost = sum(c["cost"] for c in combo)
        traits_hit = count_active_traits(traits)
        with open(cache_path, "a") as f:
            f.write(json.dumps({
                "units": names,
                "cost": cost,
                "traits_hit": traits_hit
            }) + "\n")
        saved_combos.append(combo)

    def dfs(path, trait_counter, start):
        nonlocal max_traits_achieved, calls
        calls += 1
        if calls % 100000 == 0:
            print(f"[DFS] {calls} calls, {len(saved_combos)} saved, max traits: {max_traits_achieved}")

        total_units = len(path) + len(must_include)
        if total_units > max_units:
            return

        active = count_active_traits(trait_counter)
        max_traits_achieved = max(max_traits_achieved, active)

        if active >= min_traits_required:
            save_combo(path + must_include)
            return

        for i in range(start, len(pool)):
            champ = pool[i]
            path.append(champ)
            for t in champ["traits"]:
                trait_counter[t] += 1
            dfs(path, trait_counter, i + 1)
            for t in champ["traits"]:
                trait_counter[t] -= 1
            path.pop()

    print("[INFO] Starting DFS...")
    open(cache_path, "w").close()  # clear previous file
    dfs([], base_trait_counter.copy(), 0)
    print(f"[DONE] DFS complete. {len(saved_combos)} combos saved. Max traits achieved: {max_traits_achieved}")
    return saved_combos

def display_combos_as_cost_table(combos, free_traits, trait_goals, must_include, max_results=10):
    if not combos:
        print("\n⚠️ No valid combinations found.\n")
        return

    headers = ["1-cost", "2-cost", "3-cost", "4-cost", "5-cost", "Units", "CONTAINS"]
    table = []
    for combo in combos[:max_results]:
        grouped = defaultdict(list)
        for champ in combo:
            grouped[champ["cost"]].append(champ["name"])
        row = []
        for cost in range(1, 6):
            names = sorted(grouped.get(cost, []))
            row.append(", ".join(names) if names else "")
        row.append(str(len(combo)))
        row.append(", ".join(name.upper() for name in must_include))
        table.append(row)

    print(tabulate(table, headers=headers, tablefmt="grid"))

def main():
    parser = argparse.ArgumentParser(description="TFT Trait Solver")
    parser.add_argument("--champions", type=str, default="set_14_units.json", help="Path to champions JSON file")
    parser.add_argument("--traits", type=str, default="set_14_traits.json", help="Path to trait goals JSON file")
    parser.add_argument("--level", type=int, default=7, help="Max number of units")
    parser.add_argument("--free_traits", nargs="*", default=[], help="Traits from emblems/augments")
    parser.add_argument("--must_include", nargs="*", default=[], help="Champions to lock into the board")
    parser.add_argument("--min_traits", type=int, default=8, help="Minimum number of trait goals to hit")

    args = parser.parse_args()
    champions = load_champions(args.champions)
    trait_goals = load_trait_goals(args.traits)

    combos = find_combos(
        champions=champions,
        trait_goals=trait_goals,
        min_traits_required=args.min_traits,
        max_units=args.level,
        must_include_names=args.must_include,
        free_traits=args.free_traits,
        cache_path="combo_cache.jsonl"
    )

    display_combos_as_cost_table(
        combos=combos,
        free_traits=args.free_traits,
        trait_goals=trait_goals,
        must_include=args.must_include
    )

if __name__ == "__main__":
    main()