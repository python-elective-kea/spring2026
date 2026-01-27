# Copilot Instructions: Introduktion til Python Spring 2026

## Project Overview

This is an educational repository for a Danish-language elective course "Introduktion til Python" (Introduction to Python) for Spring 2026. The repository contains teaching materials structured by session/topic, with a combination of Markdown documentation and interactive Jupyter notebooks.

**Key Context:**
- 16-week course covering Python fundamentals through advanced topics
- Bilingual workflow: Markdown/README in Danish, code comments and documentation flexible
- Course culminates in exam preparation and final project work
- Two mandatory assignments (obligatorisk) and weekly practice exercises

## Repository Structure

```
root/
├── README.md                          # Course schedule and overview (Danish)
├── materialer/                        # Teaching materials (organized by topic)
│   ├── introduktion/                  # Session 1 materials (currently developed)
│   │   ├── introduktion.md           # Session notes with learning objectives
│   │   ├── kode_fra_undervisning.ipynb # Classroom code examples
│   │   ├── list1/2.ipynb             # Exercise notebooks
│   │   └── string1/2.ipynb           # Exercise notebooks
│   ├── formalia/                      # Administrative info
│   │   ├── about_this_elective.md    # Course description
│   │   └── exam.md                    # Exam requirements
│   └── [future topics]/               # Modules, vectors, frameworks, etc.
└── test/                              # Miscellaneous testing files
```

## Material Creation Patterns

### Markdown Session Files (`materialer/{topic}/{topic}.md`)
- **Structure**: Learning objectives → preparation/setup → classroom activities → exercises
- **Sections**: "Læringsmål" (learning goals), "Forberedelse" (prep), "Dagen i dag" (today's lesson)
- **Linking**: Cross-reference to notebooks and external resources (RealPython glossary links common)
- **Language**: Danish with embedded English resource links

### Jupyter Notebooks
- **Classroom notebooks** (`kode_fra_undervisning.ipynb`): Instructor examples showing Python concepts
- **Exercise notebooks** (`string1.ipynb`, `list1.ipynb`, etc.): Student practice with progressive complexity
- **Pattern**: Mix markdown headers for concept explanation + code cells + output demonstration
- **No external deps**: Use only Python stdlib initially (pandas/numpy/matplotlib added in later sessions)

### Exercise Organization
- Exercises grouped by topic (strings, lists, functions, etc.)
- Multiple levels per topic (e.g., `string1.ipynb`, `string2.ipynb`) for progressive difficulty
- Numbered exercises guide students through problem-solving

## Development Workflow

### When Adding New Session Content:

1. **Create session markdown file**: `materialer/{topic}/{topic}.md`
   - Follow structure from [introduktion.md](materialer/introduktion/introduktion.md)
   - List learning objectives first
   - Include external reference links (RealPython, Python docs common sources)
   - Section "Dagen i dag" describes in-class work

2. **Create classroom notebook**: `{topic}/kode_fra_undervisning.ipynb`
   - Live coding demonstration of concepts
   - Document with markdown headers explaining each code section
   - Include expected outputs for reference

3. **Create exercise notebooks**: `{topic}/{topic}N.ipynb` (where N is 1, 2, etc.)
   - Progressive difficulty levels
   - Clear instructions in markdown cells
   - Leave space for student code (skeleton with comments)

4. **Update README.md**: Add row to lesson table with link to new session materials

### Testing Notebooks:
- Manually test all code cells execute without errors
- Verify outputs match educational intent (clarity > performance)
- Save executed state so outputs visible when shared

## Key Project Conventions

- **Language flexibility**: Markdown docs in Danish; code comments, variable names, and explanations can be bilingual or English (context-dependent)
- **Resource linking**: Favor external links (RealPython glossary, Python docs) rather than duplicating explanations
- **Notebook cell organization**: Use markdown cells for explanations + small focused code cells for each concept
- **Python version**: No explicit constraints visible; assume Python 3.9+ (modern stdlib)
- **No build/test system**: This is an educational repo, not a package. No `pytest`, `setup.py`, or CI/CD pipeline.

## Critical Files for Agents

- [README.md](README.md) — Course structure and session overview
- [materialer/introduktion/introduktion.md](materialer/introduktion/introduktion.md) — Template for session design
- [materialer/introduktion/kode_fra_undervisning.ipynb](materialer/introduktion/kode_fra_undervisning.ipynb) — Notebook pattern example
- [materialer/formalia/exam.md](materialer/formalia/exam.md) — Exam scope and expectations (check this for content planning)

## Common Tasks

### Adding a new lesson:
- Create `materialer/{new_topic}/{new_topic}.md` following introduktion.md structure
- Create accompanying `.ipynb` notebooks in same directory
- Update lesson table in README.md with link and date

### Fixing/updating exercise notebooks:
- Execute all cells to verify outputs
- Update markdown explanations if concepts need clarification
- Save notebook with current kernel state

### Ensuring content consistency:
- Check that learning objectives align across markdown and notebooks
- Verify external resource links are still active
- Compare exercise progression between topics (similar pacing expected)
