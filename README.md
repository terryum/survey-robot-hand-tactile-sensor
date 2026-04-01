English | [한국어](README_ko.md)

# Tactile Sensing for Dexterous Robot Hand Manipulation: A Comprehensive Survey

A bilingual (Korean/English) book and IEEE survey paper covering tactile sensing, robot hand design, learning-based manipulation, and Physical AI — from foundations to industrial outlook.

**Live Website**: [book-robot-hand-tactile-sensor.vercel.app](https://book-robot-hand-tactile-sensor.vercel.app)

## Outputs

| Output | Format | Path |
|--------|--------|------|
| Korean Book | Markdown (13 chapters) | `book/ko/` |
| English Book | Markdown (13 chapters) | `book/en/` |
| IEEE Survey Paper | LaTeX (IEEEtran, ~14 pages) | `paper/` |
| Web Viewer | Static HTML/CSS/JS (dark mode) | `docs/` |
| Illustrations | 222 PNGs (technical/darkmode/academic) | `assets/figures/` |
| References | BibTeX (146 entries) | `book/references.bib` |

## Table of Contents

### Part I: Foundations of Touch
1. **Why Tactile Sensing** — Giving Robots the Sense of Touch
2. **Tactile Sensor Technology** — The Skin of Robots
3. **Tactile Data: Representation and Collection**

### Part II: Hands — Robot and Human
4. **Robot Hand Design** — Machines Built to Grasp
5. **Intelligent Mechanisms** — Physical Intelligence (VSA, Underactuation)
6. **Human Hand Data Collection** — Teaching by Demonstration

### Part III: Learning and Transfer
7. **Learning to Manipulate** — Learning by Touch
8. **Vision-Language-Action Models** — See, Speak, Act
9. **Sim-to-Real Transfer** — From Virtual to Reality
10. **Embodiment Retargeting** — From Human to Robot

### Part IV: Integration and Outlook
11. **Research Integration** — Toward Unified Systems
12. **Physical AI and the Industrial Outlook**
13. **Limitations and Future** — Toward Physical AI for Manufacturing

## Key Numbers

- **146 references** with importance scoring (1-5)
- **222 illustrations** generated with Gemini 3 Pro Image, each in 3 styles
- **13 chapters** covering 7 research categories
- **96 citations** in IEEE paper with 5 comparison tables
- **11 companies** surveyed for industry outlook (NVIDIA, Figure AI, Tesla, etc.)
- **Market projection**: $2.9B (2025) → $15.3B (2030), CAGR 39.2%

## Tech Stack

- **Book**: Markdown with YAML frontmatter, APA citations
- **IEEE Paper**: LaTeX (IEEEtran.cls), compiled with [Tectonic](https://tectonic-typesetting.github.io/)
- **Website**: Vanilla HTML/CSS/JS, GSAP ScrollTrigger, Canvas particle background
- **Illustrations**: [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/imagen)
- **Build**: `python3 build_site.py` (Markdown → HTML with citation linking)
- **Deploy**: Vercel (static)
- **Authoring**: Claude Code agent team (researcher, book-writer, illustrator, reference-checker)

## Local Development

```bash
# View website locally
cd docs && python3 -m http.server 8000
# → http://localhost:8000

# Rebuild HTML from markdown
python3 build_site.py

# Compile IEEE paper PDF
cd paper && tectonic main.tex

# Generate book PDFs
bash scripts/build_pdf.sh ko
bash scripts/build_pdf.sh en
```

## Project Structure

```
├── book/
│   ├── ko/          # Korean chapters + glossary
│   ├── en/          # English chapters + glossary
│   └── references.bib
├── paper/
│   ├── main.tex     # IEEE survey paper
│   ├── sections/    # LaTeX sections
│   └── references.bib
├── docs/            # Static website (Vercel)
│   ├── ko/          # Korean pages
│   ├── en/          # English pages
│   ├── css/         # Dark mode glassmorphism styles
│   └── js/          # Particles, GSAP, shared header
├── assets/figures/  # 222 illustrations (ch01-ch13)
├── build_site.py    # Markdown → HTML builder
├── scripts/         # PDF generation, image generation
└── .claude/         # Agent definitions + skills (harness)
    ├── agents/      # 7 agents (researcher, writer, illustrator, etc.)
    └── skills/      # 7 skills (literature-research, web-build, etc.)
```

## Author

**Terry Taewoong Um** — Cosmax
- Website: [terry.artlab.ai](https://terry.artlab.ai)
- Email: terry.t.um@gmail.com

## Acknowledgment

This work was conducted with the assistance of AI tools, including Claude (Anthropic) for literature survey, content generation, and manuscript preparation, and Gemini (Google) for figure generation.

## License

This work is intended for educational and research purposes.
