English | [한국어](README_ko.md)

# Tactile Sensing for Dexterous Robot Hand Manipulation: A Comprehensive Survey

A bilingual (Korean/English) book and IEEE survey paper covering tactile sensing, robot hand design, learning-based manipulation, and Physical AI — from foundations to industrial outlook.

**First published**: 2026-04-01 | **Last updated**: 2026-04-07

**Live Website**: [terry.artlab.ai/ko/projects/survey-robot-hand-tactile-sensor](https://terry.artlab.ai/ko/projects/survey-robot-hand-tactile-sensor)

**PDF Download**: [English](https://github.com/terryum/survey-robot-hand-tactile-sensor/raw/main/book/en/tactile_book_en.pdf) | [한글](https://github.com/terryum/survey-robot-hand-tactile-sensor/raw/main/book/ko/tactile_book_ko.pdf) | [ArXiv Paper](https://github.com/terryum/survey-robot-hand-tactile-sensor/raw/main/paper/main.pdf)

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

## Changelog

### 2026-04-11: Image Strategy Overhaul + Hojung Choi Seminar Integration
- **Image strategy**: Shifted from AI-generated illustrations to real paper figures cropped from arXiv PDFs. Downloaded 15 papers, added 25 paper figures across Ch02, Ch03, Ch04, Ch06, Ch07, Ch10.
- **Harness update**: `book-illustrator.md` rewritten as Image Curator (paper figures first, AI generation as supplement). `book-creation-playbook.md` updated.
- **[Dr. Hojung Choi](https://www.hojungchoi.com/) SNU Seminar**: Integrated CoinFT, UMI-FT, ACP content across 5 chapters (Ch02, Ch03, Ch06, Ch07, Ch13). Added 12 seminar-cited papers (Kim 2017, Palli 2014, Fernandez 2021, Winston 2025, Yoshida 2024, Sarac 2022, Adeniji 2025, ALOHA Unleashed, etc.). 12 new BibTeX entries.
- **Ch04 enriched**: LEAP Hand (MCP joint mechanism, 19.5N force), ORCA Hand (poppable joints, 10K cycles, 10.5kg payload, zero-shot RL).
- **Ch02 fix**: F-TAC Hand "100% success" clarified as tactile-adaptation condition only.
- Image ratio: 29% real → 36% real (41 paper figures of 113 total).

### 2026-04-07: Human-to-Robot Transfer Survey Update
Based on a survey of 40+ papers (2024-2026), major updates across 7 chapters:
- **Ch10 (Embodiment Retargeting)**: Restructured from 6 to 8 sections. Added §10.6 Human+Robot Co-training (EgoMimic, EgoScale, AoE, pi0) and §10.7 Teleop-Free Approaches (X-Sim, EgoZero, VidBot, Human2Bot). 14 new papers.
- **Ch06 (Human Hand Data)**: Added TacCap, VTDexManip, AirExo/AirExo-2, NuExo, HumanoidExo, ACE, EgoDex. 8 new papers.
- **Ch13 (Limitations & Future)**: Updated data scarcity limitation with EgoScale scaling law, cross-embodiment progress, egocentric data trends.
- **Ch03, Ch07, Ch08, Ch09**: Added VTDexManip, EgoDex, LAPA, Ye et al., pi0 human transfer, EgoVLA, PhysBrain, DexWM.

### 2026-04-01: Initial Release
First publication with 13 chapters, 146 references, 222 illustrations, IEEE survey paper, and bilingual web viewer.

## Contributors

> Sorted by contribution amount. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute.

<!-- CONTRIBUTORS-START -->
| Avatar | Contributor | Contributions |
|:------:|:-----------:|:-------------|
| <img src="https://github.com/revfactory.png" width="50"> | [@revfactory](https://github.com/revfactory) | :wrench: [Harness](https://github.com/revfactory/harness) agent framework, :art: [Web design](https://github.com/revfactory/ai-trend-onboarding) patterns |
| <img src="https://github.com/sjchoi86.png" width="50"> | [@sjchoi86](https://github.com/sjchoi86) | :book: Ch02: Commercial tactile sensor products & 3 new sensor categories ([`f6f6e59`](https://github.com/terryum/survey-robot-hand-tactile-sensor/commit/f6f6e59)) |
| | [Dr. Hojung Choi (최호중)](https://www.hojungchoi.com/) | :book: CoinFT/UMI-FT/ACP content across Ch02, Ch03, Ch06, Ch07, Ch13 via [SNU Data Science Seminar 2026](https://www.hojungchoi.com/) |
<!-- CONTRIBUTORS-END -->

## Acknowledgment

This project was built using [Harness](https://github.com/revfactory/harness) (Apache 2.0) by Minho Hwang. The website structure was adapted from [AI Trend Onboarding](https://github.com/revfactory/ai-trend-onboarding) ([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)) by Minho Hwang — the design, layout patterns, and agent architecture were modified for this project's domain. Special thanks to Minho Hwang for creating these excellent tools.

This book was seeded from joint research seminar materials between Seoul National University and Cosmax. Special thanks to Junsoo Ha, Jihwan Song, Taejoon Park, and Incheol Jeong (PhD candidates) for preparing the seminars, and to Professors Frank Chongwoo Park, Yong-Lae Park, and Kyujin Cho for their collaboration. Special thanks to **[Dr. Hojung Choi](https://www.hojungchoi.com/)** (Stanford/Sunday Robotics) for his SNU Data Science Seminar (April 2026) on "Multimodal Data for Robot Manipulation" — his presentation on CoinFT, UMI-FT, and Adaptive Compliance Policy provided valuable content that enriched multiple chapters of this report.

AI tools were used in the production of this work: Claude (Opus 4.6) for literature survey, content generation, and manuscript preparation, and [gemini-3-image-generation](https://mcpmarket.com/ko/tools/skills/gemini-3-pro-image-generation) skill (Gemini 3 Pro Image) for figure generation.

## License

This work is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). You are free to share and adapt the material for non-commercial purposes with attribution. See [LICENSE](LICENSE) for details.
