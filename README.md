# Estonian Morphological Analyzer

This script processes an Estonian noun dataset and analyzes the morphological patterns across **nominative singular**, **genitive singular**, and **partitive singular** forms. It groups lexemes by **string differences** and **meta-patterns** of stem alternation, and explores the **phonological and syllabic rules** underlying case marking.

---

## What the Script Does

1. **Parses the Dataset**
   - Loads lexemes and their inflected forms into a dictionary
   - Handles malformed or incomplete entries gracefully

2. **Extracts String Differences**
   - Compares the suffixes of `nom_sg`, `gen_sg`, and `part_sg`
   - Identifies what is *added, dropped, or changed* across forms
   - Example: `pidu/peo/pidu` → `u/eo/u` → stored as a string diff pattern

3. **Groups Lexemes by Morphological Pattern**
   - Groups lexemes by shared string differences
   - Further abstracts into **meta-patterns** using:
     - `C` = consonant
     - `V` = vowel
     - `∅` = null/empty suffix

4. **Outputs Results**
   - Prints out:
     - Each string difference class and its members
     - Each meta-pattern and the string patterns it contains

---


## Requirements

- Python 3.6+
- Uses only built-in libraries: `re`, `json`, `os`, `collections`

---

## Extendable Ideas

- Export results to CSV/JSON
- Add support for other Estonian cases (illative, elative, etc.)
- Integrate with phonological feature extraction (e.g., vowel harmony)
- Add visualization (e.g., plot number of lexemes per meta-pattern)

---

## Notes

- `%` symbol in input marks superheavy syllables (e.g., `l%õug`)
- Script assumes tab-separated format between tags (`nom_sg`, etc.) and forms
- Handles malformed or incomplete entries without crashing

