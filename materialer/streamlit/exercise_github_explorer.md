# Øvelse: GitHub Explorer

Byg en Streamlit app der bruger [GitHub API](https://api.github.com) til at søge efter GitHub-brugere og vise information om dem og deres repositories.

GitHub´s API kræver ingen API-nøgle ved GET forespørgsler til `public` repositories.

---

## Del 1: Bruger-søgning

Lav en side (`app.py`) der:

1. Har et `st.text_input` felt hvor man kan skrive et GitHub-brugernavn
2. Henter brugerens profil fra API'et: `https://api.github.com/users/{username}`
3. Viser følgende information:
   - Avatar (brug `st.image`)
   - Navn og bio
   - Antal followers og following (brug `st.metric`)
   - Antal public repositories (brug `st.metric`)

**Tip:** Husk at håndtere fejl — hvad sker der hvis brugeren ikke eksisterer?

---

## Del 2: Repositories

Udvid din app så den også viser brugerens repositories hentet fra:
`https://api.github.com/users/{username}/repos`

For hvert repository skal du vise:
- Navn (som et link til GitHub)
- Beskrivelse (hvis der er en)
- Primært programmeringssprog
- Antal stjerner

**Tip:** Brug `st.markdown` til at lave klikbare links med `[tekst](url)` syntaksen.

---

## Del 3: Filtrering og sortering

Tilføj mulighed for at filtrere og sortere repositories:

- En `st.selectbox` til at vælge sortering: mest stjerner, nyeste, alfabetisk
- En `st.multiselect` til at filtrere på programmeringssprog (vis kun de sprog der faktisk bruges)

---

## Del 4: Flere sider (valgfri)

Omstrukturér din app til at have flere sider:

```
github_explorer/
├── app.py          ← Forside med søgefelt
└── pages/
    ├── repos.py    ← Repository-oversigt
    └── compare.py  ← Sammenlign to brugere
```

På `compare.py` kan du sammenligne to brugere side om side med `st.columns`.

---

## Nyttige Streamlit-komponenter

| Komponent | Brug |
|---|---|
| `st.text_input()` | Søgefelt |
| `st.image()` | Avatar |
| `st.metric()` | Tal med label |
| `st.selectbox()` | Sorteringsvalg |
| `st.multiselect()` | Sprogfilter |
| `st.columns()` | Side om side layout |
| `st.spinner()` | Loading-indikator mens API kaldes |
| `st.error()` | Fejlbesked |

---

## Kom i gang

```python
import streamlit as st
import requests

st.title("GitHub Explorer")

username = st.text_input("Søg efter GitHub-bruger")

if username:
    response = requests.get(f"https://api.github.com/users/{username}")

    if response.status_code == 200:
        user = response.json()
        st.write(user)  # Start her — hvad returnerer API'et?
    else:
        st.error(f"Bruger '{username}' blev ikke fundet")
```

Kør din app med:

```bash
streamlit run app.py
```
