# 🧠 TFT Trait Solver (Set 14)

This tool helps you find **champion combinations** that activate a desired number of traits in **Teamfight Tactics**.

It's designed to:
- ✅ Identify all valid trait combinations for a given level
- ✅ Consider free traits from emblems/augments
---

## ⚙️ How to Use

1. Prepare your data:
   - `set_14_units.json` → champion list with name, traits, and cost
   - `set_14_traits.json` → trait activation thresholds (e.g., "Bastion": 2)

2. Run the trait solver to generate combos:
   ```bash
   python tft_trait_solver.py --level 7 --min_traits 8
    ```

---

## 🧪 Example Usage

To find all valid champion combinations for **level 7** that activate at least **8 traits**, and include both Ziggs and Ekko with a bonus emblem for Techie:

```bash
python tft_trait_solver.py \
  --level 7 \
  --min_traits 8 \
  --must_include Ziggs Ekko \
  --free_traits Techie
```

## 📊 7 Units, 8 Trait Combos

<!-- BEGIN COMBO TABLE -->

| 1-cost                    | 2-cost                  | 3-cost                               | 4-cost            | 5-cost          | Traits Active                                                                       |
|---------------------------|-------------------------|--------------------------------------|-------------------|-----------------|-------------------------------------------------------------------------------------|
| Alistar, Dr Mundo, Poppy  | Rhaast, Shyvana, Veigar | Jarvan IV                            |                   |                 | Bastion, Bruiser, Cyberboss, Divinicorp, Golden Ox, Slayer, Techie, Vanguard        |
| Alistar, Dr Mundo         | Ekko, Rhaast            | Jarvan IV, Yuumi                     |                   | Samira          | A.M.P., Bruiser, Divinicorp, Golden Ox, Slayer, Strategist, Street Demon, Vanguard  |
| Alistar, Dr Mundo         | Rhaast                  | Jarvan IV, Yuumi                     | Neeko             | Samira          | A.M.P., Bruiser, Divinicorp, Golden Ox, Slayer, Strategist, Street Demon, Vanguard  |
| Alistar, Dr Mundo         | Shyvana, Skarner        | Fiddlesticks, Jarvan IV              |                   | Renekton        | Bastion, BoomBots, Bruiser, Divinicorp, Golden Ox, Slayer, Techie, Vanguard         |
| Alistar, Jax, Morgana     | Jhin, Shyvana           | Mordekaiser                          | Aphelios          |                 | Bastion, Bruiser, Divinicorp, Dynamo, Exotech, Golden Ox, Marksman, Techie          |
| Alistar, Kindred, Morgana | Jhin                    | Mordekaiser                          | Zeri              | Viego           | Bruiser, Divinicorp, Dynamo, Exotech, Golden Ox, Marksman, Rapidfire, Techie        |
| Alistar, Morgana          | Jhin, Shyvana           | Mordekaiser                          | Aphelios, Sejuani |                 | Bastion, Bruiser, Divinicorp, Dynamo, Exotech, Golden Ox, Marksman, Techie          |
| Alistar                   | Skarner, Veigar         | Fiddlesticks, Jarvan IV, Senna       |                   | Kobuko          | BoomBots, Bruiser, Cyberboss, Divinicorp, Golden Ox, Slayer, Techie, Vanguard       |
| Dr Mundo, Jax             | Rhaast                  | Jarvan IV, Mordekaiser               | Sejuani           | Viego           | Bastion, Bruiser, Divinicorp, Exotech, Golden Ox, Slayer, Techie, Vanguard          |
| Dr Mundo, Kindred, Kogmaw | Rhaast                  | Jarvan IV                            | Aphelios, Chogath |                 | BoomBots, Bruiser, Divinicorp, Golden Ox, Marksman, Rapidfire, Slayer, Vanguard     |
| Dr Mundo, Kindred, Kogmaw | Skarner                 | Gragas, Jarvan IV                    | Aphelios          |                 | BoomBots, Bruiser, Divinicorp, Golden Ox, Marksman, Rapidfire, Slayer, Vanguard     |
| Dr Mundo, Morgana         | Jhin, Skarner           | Jarvan IV                            | Aphelios, Chogath |                 | BoomBots, Bruiser, Divinicorp, Dynamo, Golden Ox, Marksman, Slayer, Vanguard        |
| Dr Mundo, Poppy           | Rhaast, Shyvana         | Jarvan IV                            |                   | Kobuko, Viego   | Bastion, Bruiser, Cyberboss, Divinicorp, Golden Ox, Slayer, Techie, Vanguard        |
| Dr Mundo, Zyra            | Graves, Rhaast          | Jarvan IV, Mordekaiser, Rengar       |                   |                 | Bruiser, Divinicorp, Executioner, Golden Ox, Slayer, Street Demon, Techie, Vanguard |
| Dr Mundo, Zyra            | Rhaast                  | Jarvan IV, Jinx, Mordekaiser         | Aphelios          |                 | Bruiser, Divinicorp, Golden Ox, Marksman, Slayer, Street Demon, Techie, Vanguard    |
| Dr Mundo, Zyra            | Rhaast                  | Jarvan IV, Mordekaiser               | Annie             | Samira          | A.M.P., Bruiser, Divinicorp, Golden Ox, Slayer, Street Demon, Techie, Vanguard      |
| Dr Mundo                  | Ekko, Rhaast            | Jarvan IV, Mordekaiser               | Neeko             | Viego           | Bruiser, Divinicorp, Golden Ox, Slayer, Strategist, Street Demon, Techie, Vanguard  |
| Dr Mundo                  | Graves, Rhaast          | Fiddlesticks, Jarvan IV, Mordekaiser |                   | Urgot           | BoomBots, Bruiser, Divinicorp, Executioner, Golden Ox, Slayer, Techie, Vanguard     |
| Dr Mundo                  | Graves, Rhaast          | Jarvan IV, Mordekaiser, Rengar       | Brand             |                 | Bruiser, Divinicorp, Executioner, Golden Ox, Slayer, Street Demon, Techie, Vanguard |
| Dr Mundo                  | Graves, Skarner         | Fiddlesticks, Jarvan IV, Mordekaiser | Vex               |                 | BoomBots, Bruiser, Divinicorp, Executioner, Golden Ox, Slayer, Techie, Vanguard     |
| Dr Mundo                  | Rhaast                  | Jarvan IV, Jinx, Mordekaiser         | Aphelios, Brand   |                 | Bruiser, Divinicorp, Golden Ox, Marksman, Slayer, Street Demon, Techie, Vanguard    |
| Dr Mundo                  | Rhaast                  | Jarvan IV, Mordekaiser               | Annie, Brand      | Samira          | A.M.P., Bruiser, Divinicorp, Golden Ox, Slayer, Street Demon, Techie, Vanguard      |
| Dr Mundo                  | Rhaast                  | Jarvan IV, Yuumi                     | Annie, Ziggs      | Kobuko          | A.M.P., Bruiser, Cyberboss, Divinicorp, Golden Ox, Slayer, Strategist, Vanguard     |
| Dr Mundo                  | Shyvana, Skarner        | Jarvan IV                            | Chogath           | Renekton, Viego | Bastion, BoomBots, Bruiser, Divinicorp, Golden Ox, Slayer, Techie, Vanguard         |
| Dr Mundo                  | Skarner                 | Jarvan IV, Mordekaiser               | Vex               | Urgot, Viego    | BoomBots, Bruiser, Divinicorp, Executioner, Golden Ox, Slayer, Techie, Vanguard     |
| Jax, Kindred              | Jhin, Shyvana           | Elise, Gragas, Mordekaiser           |                   |                 | Bastion, Bruiser, Divinicorp, Dynamo, Exotech, Marksman, Nitro, Techie              |
| Kindred, Kogmaw           | Jhin, Shyvana           | Elise, Fiddlesticks                  |                   | Renekton        | Bastion, BoomBots, Divinicorp, Dynamo, Marksman, Nitro, Rapidfire, Techie           |
| Kindred, Morgana          | Jhin, Veigar            | Mordekaiser                          | Zeri              | Kobuko          | Bruiser, Cyberboss, Divinicorp, Dynamo, Exotech, Marksman, Rapidfire, Techie        |
| Kindred, Morgana          | Jhin                    | Fiddlesticks, Mordekaiser            | Chogath, Zeri     |                 | BoomBots, Bruiser, Divinicorp, Dynamo, Exotech, Marksman, Rapidfire, Techie         |
| Kindred                   | Jhin, Shyvana           | Elise, Gragas, Mordekaiser           | Sejuani           |                 | Bastion, Bruiser, Divinicorp, Dynamo, Exotech, Marksman, Nitro, Techie              |
| Kindred                   | Jhin, Shyvana           | Elise, Gragas, Mordekaiser           | Zeri              |                 | Bruiser, Divinicorp, Dynamo, Exotech, Marksman, Nitro, Rapidfire, Techie            |
| Kindred                   | Jhin, Shyvana           | Elise, Mordekaiser                   | Zeri              | Renekton        | Bastion, Divinicorp, Dynamo, Exotech, Marksman, Nitro, Rapidfire, Techie            |

<!-- END COMBO TABLE -->