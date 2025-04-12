import json
from collections import defaultdict
from tabulate import tabulate

CACHE_PATH = "combo_cache.jsonl"
README_PATH = "README.md"
MARKER_START = "<!-- BEGIN COMBO TABLE -->"
MARKER_END = "<!-- END COMBO TABLE -->"

def get_trait_set(champ_names, champion_pool):
    trait_counter = defaultdict(int)
    for champ in champion_pool:
        if champ["name"] in champ_names:
            for trait in champ["traits"]:
                trait_counter[trait] += 1
    return trait_counter

def get_active_traits(trait_counter, trait_goals):
    return sorted([
        t for t in trait_counter
        if trait_counter[t] >= trait_goals.get(t, 2)
    ])

def generate_table(champion_pool, trait_goals, max_rows=40):
    rows = []
    with open(CACHE_PATH) as f:
        combos = [json.loads(line) for line in f]

    for combo in combos[:max_rows]:
        costs = {i: [] for i in range(1, 6)}
        for name in combo["units"]:
            champ = next(c for c in champion_pool if c["name"] == name)
            costs[champ["cost"]].append(name)

        trait_counter = get_trait_set(combo["units"], champion_pool)
        active_traits = get_active_traits(trait_counter, trait_goals)

        row = [
            ", ".join(sorted(costs[i])) if costs[i] else "" for i in range(1, 6)
        ] + [", ".join(active_traits)]
        rows.append(row)

    headers = ["1-cost", "2-cost", "3-cost", "4-cost", "5-cost", "Traits Active"]
    return tabulate(rows, headers=headers, tablefmt="github")


def update_readme_section(table_md):
    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    if MARKER_START in content and MARKER_END in content:
        before = content.split(MARKER_START)[0]
        after = content.split(MARKER_END)[1]
        new_content = f"{before}{MARKER_START}\n\n{table_md}\n\n{MARKER_END}{after}"
    else:
        # No markers found — just append the table
        print("⚠️ No markers found. Appending combo table to the end of README.")
        new_content = content + f"\n\n{MARKER_START}\n\n{table_md}\n\n{MARKER_END}\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"[✅] README updated with combo table ({'replaced' if MARKER_START in content else 'appended'}).")


def main():
    with open("set_14_units.json") as f:
        champion_pool = json.load(f)
    with open("set_14_traits.json") as f:
        trait_goals = json.load(f)

    table_md = generate_table(champion_pool, trait_goals)
    update_readme_section(table_md)

if __name__ == "__main__":
    main()