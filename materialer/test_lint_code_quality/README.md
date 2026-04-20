## Testing, Linting, Code Quality
I dag kigger vi på et repository vi har arbejdet med tidligere på dette semester: https://github.com/python-elective-kea/mistral-vibe. 

Fokus vil være på hvordan projektet bruger unit-tests, Linting, static code ananlysis og i det hele taget har fokus på code quality. 

Formålet er at i får et indblik i hvordan emnerne håndteres i et velfungerende pythonprojekt. 

Fokus er på analyse, ikke på at skrive kode. I opfordres til at bruge mistral-vibe, eller et andet cli tool, til at hjælpe med analysen, og til at skrive den kode der er nødvendig. 

## Læringsmål
* Forstå hvordan et fungerende open source python projekt gør brug af unittests, linting og sikre god kode kvalitet.
* Kunne bruge værktøjerne: `uv`, `ruff`, `pytest`, `pyright` og `pre-commit`

## Forberedels 
Læs følgende dokumenter.
* https://github.com/mistralai/mistral-vibe/blob/main/CONTRIBUTING.md
* https://github.com/mistralai/mistral-vibe/blob/main/README.md

## Dagen i dag
Lav en fork af [dette projekt](https://github.com/python-elective-kea/mistral-vibe) og `clone` det og `checkout ek-edition` nu er du på den branch vi bruger i dag. lav yderligere en `checkout -b <dit_navn>` for at lave en ny branch og skifte til den. Du kan nu gå i gang med at ændre i koden uden at skabe merge konflikter.

Vi analysere først dette rpositories brug af testing og linting tools. 

Herefter kigger vi overordnet på hvordan disse værektøjer kan bruges i nogle meget simple eksempler ved tavlen:  
* `uv`
* `ruff`
* `pytest`
* `pyright`
* `pre-commit`

## Materialer
I kan læse mere om dagens værktøjer i denne dokumentation. Dette er ikke obligatorisk læsning.

* [ruff](https://docs.astral.sh/ruff/tutorial/)
* [uv](https://docs.astral.sh/uv/)
* [pytest](https://docs.pytest.org/en/stable/)
* [pyright](https://github.com/microsoft/pyright)
* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

### Øvelser
#### Tilføj en ny feature
**Feature**: "Tæl antalet af Emojis i en tekst streng"    
**Mål**: Tilføj en `function` der tæller antallet af emojis i en tekst streng (feks.: "Hello 😊 world 🚀" → 2).
 
1. Tilføj funktionen (man kunne godt se denne type af function som en `utility`)

<details>
  <summary>Hint (Tænk over problemt inden du ser hint og løsning)</summary>

* Lav en ny fil: `vibe/core/utils/emoji_counter.py`

```
def count_emojis(text: str) -> int:
    """Count the number of emojis in a string."""
    # Simple heuristic: count characters outside ASCII range (emojis are multi-byte)
    return sum(1 for char in text if ord(char) > 127)
```
</details>

2. Tilføj en `Test`

<details>
  <summary>Hint (Tænk over problemt inden du ser hint og løsning)</summary>

* Opret: `tests/test_emoji_counter.py`:

```
from vibe.core.utils.emoji_counter import count_emojis

def test_count_emojis():
    assert count_emojis("Hello 😊 world 🚀") == 2
    assert count_emojis("No emojis here") == 0
    assert count_emojis("🔥🔥🔥") == 3
``` 
</details>

3. Enforce Quality Checks

<details>
  <summary>Hint (Tænk over problemt inden du ser hint og løsning)</summary>
```
uv run ruff check .
uv run pytest tests/test_emoji_counter.py -v 
uv run pre-commit run --all-files
``` 
</details>

4. Integrer dette i Mistral Vibe´s CLI  

"Hvordan ville du integrere dette i Mistral Vibe’s CLI?" (Hint: Tilføj en kommando til vibe/cli/.

<details>
  <summary>Hint (Tænk over problemt inden du ser hint og løsning)</summary>

Modificer `vibe/cli/clipboard.py` tilføj dette til funktionen: `_copy_to_clipboard`:

```
from vibe.core.utils.emoji_counter import count_emojis

def copy_to_clipboard(text: str) -> None:
    emoji_count = count_emojis(text)
    if emoji_count > 0:
        print(f"🎉 Copied text with {emoji_count} emoji(s)!")
    # ... rest of the existing copy logic

```  
</details>

5. Test det

Kopier teksten: "Hello 😊"
Din terminal skal gerne vise:

🎉 Copied text with 1 emoji(s)!

