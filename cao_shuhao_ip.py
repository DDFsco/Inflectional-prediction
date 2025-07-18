filename = 'Estonian.txt'
with open(filename, 'r') as f:
    lines = f.read().splitlines()

print(f"Loaded {len(lines)} lines from {filename}")

lexeme_dict = {}
i = 0

while i < len(lines):
    # Skip empty lines
    if not lines[i].strip():
        i += 1
        continue

    lexeme = lines[i].strip()
    i += 1

    forms = {}

    # Read the following lines until an empty line or a new lexeme is encountered
    while i < len(lines) and lines[i].strip() and "\t" in lines[i]:
        parts = lines[i].strip().split()
        if len(parts) >= 2:
            key = parts[0]
            value = parts[1]  # Take only the first value
            forms[key] = value
        else:
            print(f"Warning: malformed line at {i}: {lines[i]}")
        i += 1

    # Store the parsed forms for this lexeme
    lexeme_dict[lexeme] = forms

print(f"Collected {len(lexeme_dict)} lexemes.")

def strip_percent(word):
    return word.replace('%', '')

def get_string_diff(nom, gen, part):
    nom_clean = strip_percent(nom)
    gen_clean = strip_percent(gen)
    part_clean = strip_percent(part)

    # Find the longest common prefix
    min_len = min(len(nom_clean), len(gen_clean), len(part_clean))
    i = 0
    while i < min_len and nom_clean[i] == gen_clean[i] == part_clean[i]:
        i += 1

    # Get suffixes
    nom_suffix = nom_clean[i:]
    gen_suffix = gen_clean[i:]
    part_suffix = part_clean[i:]

    # Use ∅ to indicate empty suffix
    nom_diff = nom_suffix if nom_suffix else '∅'
    gen_diff = gen_suffix if gen_suffix else '∅'
    part_diff = part_suffix if part_suffix else '∅'

    return f"{nom_diff}/{gen_diff}/{part_diff}"

from collections import defaultdict

string_diff_dict = defaultdict(list)

# For three-way string differences among the three forms
required_keys = ['nom_sg', 'gen_sg', 'part_sg']

for lexeme, forms in lexeme_dict.items():
    if all(k in forms for k in required_keys):
        diff = get_string_diff(forms['nom_sg'], forms['gen_sg'], forms['part_sg'])
        string_diff_dict[diff].append(lexeme)
    else:
      # Skip for non three-way string
      continue
        # print(f"Skipping {lexeme} due to missing forms: {set(required_keys) - set(forms.keys())}")
# print
for i, (diff, lexemes) in enumerate(string_diff_dict.items(), 1):
    print(f"Class {i} with string difference pattern {diff} has {len(lexemes)} members, which are: {lexemes}\n")

vowels = set('aeiou')

meta_dict = defaultdict(lambda: defaultdict(list))

for diff, lexemes in string_diff_dict.items():
    meta_pattern = []

    for ch in diff:
        if ch in vowels:
            meta_pattern.append('V')
        elif ch == '/':
            meta_pattern.append('/')
        elif ch == '∅':
            meta_pattern.append('∅')
        else:
            meta_pattern.append('C')

    meta_key = ''.join(meta_pattern)

    # Store
    meta_dict[meta_key][diff] = lexemes

# Print meta-patterns sorted alphabetically
for meta_key in sorted(meta_dict.keys()):
    print(f"Meta-pattern {meta_key} contains string diffs {list(meta_dict[meta_key].keys())}")
    for diff, words in meta_dict[meta_key].items():
        print(f"{diff}: {words}")
    print()

"""a. (.75) If the meta-pattern that includes pidu 'party' turns out to be different from the meta-pattern that includes madu "snake", suppose that we unify the two groups. Write a maximally general rule that predicts the genitive from the nominative for every lexeme in this unified group. Refer to vowel features high, mid, front, back and low.

  - In this unified group (e.g., pidu, madu), the high vowels in the final syllable lower to mid vowels in the genitive (e.g., pidu → peo, madu → mao).
  - Also, there is no vowel harmony involved. The vowels in the genitive do not necessarily match front/back features from the nominative.
Additionally, the initial consonant of the stem is not deleted in the genitive; it remains intact.

b. (.75) Explain why the genitive singular of all these forms needs to have a superheavy syllable.
  - Superheavy syllables ensure the prosodic licensing necessary for case marking. The added vowel or diphthong provides that weight.That is due to syllable weight constraints in the language.

c. (.75) The string difference pattern that includes kapsas 'dung' and the pattern that includes kutsikas 'puppy' both have final /s in the nominative singular. Apart from the number of syllables in each word, what other differences between the stems in each group might help predict which of the two groups a lexeme belongs in? Think about heavy versus light syllables, and where in the word they occur, where a heavy syllable contains either a coda, a long vowel or a diphthong.
  - Kapsas has a heavy penult syllable (VC), e.g., kap-sas. Kutsikas has light syllables, e.g., ku-tsi-kas (mostly CV). Heavy syllables often correlate with shorter stem changes, while light stems tend to require heavier inflectional additions to mark case, which may determine which group a lexeme fits.

d. (.75) Look at the meta-class that includes the second lexeme in the data set l%õug 'jaw'. If we exclude words that look like loanwords such as 'blank%ett',  'tabl%ett', 'ball%ett', 'krev%ett',  'rak%ett',  'brűn%ett', 'tual%ett', and 'ress%urss', exactly what kind of syllable structure do all the nominative singular forms share? Think about number of syllables and light vs. heavy vs. superheavy syllables.
  - If we excluding loanwords, nominative singular forms in this class all share: One syllable, or a superheavy syllable: typically CVVC or CVC with long vowels/diphthongs or codas. Also, the superheaviness is marked via % (e.g., l%õug, j%alg, k%ord)
  - So, they are monosyllabic superheavy stems.

e. (.75) Why do the genitive singular forms of that class "not need" a superheavy syllable? (Assume that three consecutive vowels cannot all be in the same syllable.)

  - The genitive singular is built from an underlying stem, and the prosodic requirements for the genitive are satisfied independently of whether the nominative is superheavy or not. The genitive does not rely on the surface shape of the nominative for its syllable structure.
  - Additionally, since Estonian avoids trivocalic syllables, gen.sg. forms like lõua split the vowels across syllables, keeping the weight distributed.

f. (.75) If we were to write a maximally general rule that derives two of the forms of that meta-class from one of them, which of the three forms would a speaker need to know in order to predict the forms of the other two, and what would that rule be without referring to any specific vowels or consonants?

	- The speaker needs to know the genitive singular form in order to predict the other two forms.
	- Rule:
	  - From gen.sg., derive nom.sg. by adding back the final consonant (typically a plosive like g or k).
	  - From gen.sg., derive part.sg. by inserting the final consonant + a, forming a superheavy CVVC or CVCVC form.

	- Example with lõua (gen.sg.):
		- nom.sg. → lõug (restore final g)
	  - part.sg. → lõuga (add back g + a)
      - String difference: g/a/ga
      - Meta-pattern: C/V/CV

g. (.75) If we look just at nom.sg., gen.sg. and part.sg. forms and look for where superheavy syllables occur or don't occur in each, what robust patterns do we see? For example, how many other nouns pattern like  l%õug 'jaw', how many like k%ahtlus 'suspicion' and how many like kapsas 'dung'? (You may find that some patterns like the one in koti 'bag' is not very robust and can be considered an outlier.)

	- k%ahtlus-like (∅/e/t): Superheavy across all three forms. Extremely robust—hundreds of lexemes.
	- l%õug-like (g/a/ga): Superheavy in nom.sg. only, gen.sg. lightens. Moderately robust (~10–20 monosyllabic lexemes).
	- kapsas-like (C/∅/st or ∅/∅/∅): Non-superheavy across forms. Medium robustness; common among trisyllabic nouns with CVC roots.

h. (.75) What correlation can you find between membership in one of these classes and the endings of their partitive singular forms?

  - There is a correlation between the syllable weight pattern (presence or absence of Q3 syllables) across the three forms and the partitive singular ending:
	  - If the part.sg. ends in -ga, it tends to mark monosyllabic, Q3 nominative forms like l%õug.
	  - If the part.sg. ends in -t, it typically belongs to nouns that are Q3 across all forms, like k%ahtlus.
	  - If the part.sg. ends in -st, it often corresponds to non-Q3 stems, such as kapsas.

  - These endings reflect morphological patterns and prosodic requirements that help identify the class membership of a lexeme.

g'. What regex command could you use with a text editor on the file Estonian.txt to find lexemes that have the same pattern as kõrvits 'pumpkin'?

h'. How might you guess that a lexeme in the ∅/u/ku string difference class belongs to that class without knowing what all three forms are?


"""