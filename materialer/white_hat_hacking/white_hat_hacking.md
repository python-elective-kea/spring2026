# White Hat Hacking with Python

I denne session bruger vi Python til at forstå grundlæggende sikkerhedskoncepter set fra en **ethical hacker** (white hat) vinkel. Vi arbejder udelukkende med teknikker, der er lovlige og etisk forsvarlige — og formålet er at forstå, hvordan angreb virker, så man bedre kan forsvare sig mod dem.

> **Vigtigt**: Alt arbejde i denne session foregår lokalt eller mod systemer, du selv ejer eller har eksplicit tilladelse til at teste. Uautoriseret scanning eller angreb er ulovligt.

## Læringsmål

Efter denne session vil du kunne:

- Forklare forskellen på black hat, grey hat og white hat hacking
- Bruge Pythons `socket`-modul til at forstå netværkskommunikation
- Bygge en simpel port scanner og forstå, hvad den afslører
- Arbejde med hashing og forstå, hvorfor passwords aldrig gemmes i plaintext
- Bruge `requests` til at analysere HTTP-responses og headers
- Reflektere over, hvordan kendte angrebstyper (brute force, enumeration) fungerer — og hvordan man beskytter sig

## Forberedelse

* [Ethical Hacking in 12 Hours – Full Course (freeCodeCamp)](https://www.youtube.com/watch?v=fNzpcB7ODxQ) — se de første 30 minutter som introduktion
* [Python for Cybersecurity – Real Python](https://realpython.com/python-cybersecurity-overview/) — skim artiklen
* Sørg for at have følgende installeret: `requests`, `python-nmap` (valgfrit)

## Dagens emner

### 1. Hvad er White Hat Hacking?

Vi starter med en kort diskussion af:
- CIA-triaden: **Confidentiality, Integrity, Availability**
- Forskellen på **vulnerability**, **exploit** og **payload**
- Hvad en **penetration test** er, og hvad der kræves (scope, tilladelse, rapport)

### 2. Netværk og sockets

```python
import socket

target = "127.0.0.1"
port = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} er åben")
    else:
        print(f"Port {port} er lukket")
```

### 3. Password hashing

```python
import hashlib

password = "hemmeligtPassword123"
hashed = hashlib.sha256(password.encode()).hexdigest()
print(hashed)
```

Vi ser på, hvorfor MD5 ikke er sikkert nok, og hvad `salt` gør for at beskytte mod rainbow table-angreb.

### 4. HTTP header analyse

```python
import requests

response = requests.get("http://example.com")
print(response.headers)
```

Vi kigger på, hvilke headers der afslører information om serveren (f.eks. `Server`, `X-Powered-By`) og hvad **security headers** som `Content-Security-Policy` og `X-Frame-Options` gør.

## Øvelser

### Øvelse 1: Port Scanner

Skriv en port scanner, der scanner de første 1024 porte på `127.0.0.1` (localhost) og udskriver hvilke porte der er åbne.

- Brug `socket`-modulet
- Sæt en kort timeout (f.eks. 0.5 sekunder) så det ikke tager for lang tid
- Udskriv kun åbne porte

**Ekstra**: Brug `concurrent.futures.ThreadPoolExecutor` til at gøre scanningen hurtigere med threads.

### Øvelse 2: Password Strength Checker

Lav en funktion `check_password_strength(password)`, der returnerer en score fra 0–4 baseret på følgende kriterier:

- Mindst 8 tegn
- Indeholder et tal
- Indeholder et stort bogstav
- Indeholder et specialtegn (`!@#$%^&*` osv.)

```python
def check_password_strength(password):
    pass

print(check_password_strength("abc"))          # 0 eller 1
print(check_password_strength("Abc123!?"))     # 4
```

### Øvelse 3: Hash og Dictionary Attack

Du har fundet denne MD5-hash fra en lækket database:

```
5f4dcc3b5aa765d61d8327deb882cf99
```

1. Brug Python til at hashe en liste af common passwords og se om du kan finde et match.
2. Forklar hvad et **dictionary attack** er, og hvorfor lange, unikke passwords beskytter mod det.

```python
import hashlib

common_passwords = ["password", "123456", "qwerty", "letmein", "admin"]
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"

for pw in common_passwords:
    # din kode her
    pass
```

### Øvelse 4: HTTP Header Analyse

Skriv et script, der henter headers fra en liste af websites og checker, om de har følgende security headers:

- `Content-Security-Policy`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Strict-Transport-Security`

Udskriv en rapport for hvert site: hvilke headers er til stede, og hvilke mangler.

```python
import requests

sites = [
    "https://www.kea.dk",
    "https://www.github.com",
    "https://www.python.org",
]

security_headers = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security",
]

for site in sites:
    # din kode her
    pass
```
