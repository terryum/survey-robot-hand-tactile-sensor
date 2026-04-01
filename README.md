English | [한국어](README_ko.md)

# Tactile Sensing for Dexterous Robot Hand Manipulation: A Comprehensive Survey

A bilingual (Korean/English) book and IEEE survey paper covering tactile sensing, robot hand design, learning-based manipulation, and Physical AI — from foundations to industrial outlook.

**Live Website**: [terry.artlab.ai/ko/projects/book-robot-hand-tactile-sensor](https://terry.artlab.ai/ko/projects/book-robot-hand-tactile-sensor)

**PDF Download**: [English](https://drive.google.com/file/d/1z5NgFRtOwcWLiZka3bYFnZ-k4Zs7cUa4/view?usp=sharing) | [한글](https://drive.google.com/file/d/1XxPH3N72TOpz2vSSNsrT9C59IUdQpstR/view?usp=sharing) | [ArXiv Paper](https://drive.google.com/file/d/1aF8fDEkFN8vxRfvtyOHLwmz6glowe3f_/view?usp=sharing)

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

## Acknowledgment

This project was built using [Harness](https://github.com/revfactory/harness) (Apache 2.0) by Minho Hwang. The website structure was adapted from [AI Trend Onboarding](https://github.com/revfactory/ai-trend-onboarding) ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)) by Minho Hwang — the design, layout patterns, and agent architecture were modified for this project's domain. Special thanks to Minho Hwang for creating these excellent tools.

This book was seeded from joint research seminar materials between Seoul National University and Cosmax. Special thanks to Junsoo Ha, Jihwan Song, Taejoon Park, and Incheol Jeong (PhD candidates) for preparing the seminars, and to Professors Frank Chongwoo Park, Yong-Lae Park, and Kyujin Cho for their collaboration.

AI tools were used in the production of this work: Claude (Opus 4.6) for literature survey, content generation, and manuscript preparation, and [gemini-3-image-generation](https://mcpmarket.com/ko/tools/skills/gemini-3-pro-image-generation) skill (Gemini 3 Pro Image) for figure generation.

## License

This work is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). You are free to share and adapt the material for non-commercial purposes with attribution. See [LICENSE](LICENSE) for details.
