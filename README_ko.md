[English](README.md) | 한국어

# 로봇 손의 정교한 조작을 위한 촉각 센싱: 종합 서베이

촉각 센서, 로봇 핸드 설계, 학습 기반 조작, Physical AI를 아우르는 한국어/영어 이중 언어 기술 서적 및 IEEE 서베이 논문입니다.

**최초 발행**: 2026-04-01 | **최종 업데이트**: 2026-04-07

**웹사이트**: [terry.artlab.ai/ko/projects/survey-robot-hand-tactile-sensor](https://terry.artlab.ai/ko/projects/survey-robot-hand-tactile-sensor)

**PDF 다운로드**: [English](https://github.com/terryum/survey-robot-hand-tactile-sensor/raw/main/book/en/tactile_book_en.pdf) | [한글](https://github.com/terryum/survey-robot-hand-tactile-sensor/raw/main/book/ko/tactile_book_ko.pdf) | [ArXiv Paper](https://github.com/terryum/survey-robot-hand-tactile-sensor/raw/main/paper/main.pdf)

## 산출물

| 산출물 | 형식 | 경로 |
|--------|------|------|
| 한국어 책 | 마크다운 (13챕터) | `book/ko/` |
| 영어 책 | 마크다운 (13챕터) | `book/en/` |
| IEEE 서베이 논문 | LaTeX (IEEEtran, ~14페이지) | `paper/` |
| 웹 뷰어 | 정적 HTML/CSS/JS (다크 모드) | `docs/` |
| 일러스트 | 222개 PNG (technical/darkmode/academic) | `assets/figures/` |
| 참고문헌 | BibTeX (146편) | `book/references.bib` |

## 목차

### Part I: 촉각의 기초
1. **왜 촉각인가** — 로봇에게 손의 감각을
2. **촉각 센서 기술** — 로봇의 피부
3. **촉각 데이터: 표현과 수집**

### Part II: 로봇 핸드와 인간 손
4. **로봇 핸드 설계** — 잡기 위한 기계
5. **지능형 메커니즘** — 물리적 지능 (VSA, Underactuation)
6. **사람 손 데이터 수집** — 시연으로 가르치기

### Part III: 학습과 전이
7. **조작 학습** — 만지며 배우기
8. **VLA 모델** — 보고 듣고 행동하기
9. **Sim-to-Real 전이** — 가상에서 현실로
10. **Embodiment Retargeting** — 사람에서 로봇으로

### Part IV: 통합과 전망
11. **시스템 통합** — 연구적 관점
12. **Physical AI와 산업적 전망**
13. **한계와 미래** — Physical AI for Manufacturing을 향해

## 주요 수치

- **146편 참고문헌** — 중요도 점수(1-5) 포함
- **222개 일러스트** — Gemini 3 Pro Image로 생성, 각 3가지 스타일
- **13개 챕터** — 7개 연구 카테고리 포괄
- **96개 인용** — IEEE 논문 내 5개 비교표 포함
- **11개 기업** 산업 동향 조사 (NVIDIA, Figure AI, Tesla 등)
- **시장 전망**: $29억(2025) → $153억(2030), CAGR 39.2%

## 기술 스택

- **책**: 마크다운 + YAML frontmatter, APA 인용
- **IEEE 논문**: LaTeX (IEEEtran.cls), [Tectonic](https://tectonic-typesetting.github.io/)으로 컴파일
- **웹사이트**: 순수 HTML/CSS/JS, GSAP ScrollTrigger, Canvas 파티클 배경
- **일러스트**: [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/imagen)
- **빌드**: `python3 build_site.py` (마크다운 → HTML, 인용 링크 자동 생성)
- **배포**: Vercel (정적)
- **저작**: Claude Code 에이전트 팀 (researcher, book-writer, illustrator, reference-checker)

## 로컬 실행

```bash
# 웹사이트 로컬 확인
cd docs && python3 -m http.server 8000
# → http://localhost:8000

# 마크다운에서 HTML 재빌드
python3 build_site.py

# IEEE 논문 PDF 컴파일
cd paper && tectonic main.tex

# 책 PDF 생성
bash scripts/build_pdf.sh ko
bash scripts/build_pdf.sh en
```

## 프로젝트 구조

```
├── book/
│   ├── ko/          # 한국어 챕터 + 용어집
│   ├── en/          # 영어 챕터 + 용어집
│   └── references.bib
├── paper/
│   ├── main.tex     # IEEE 서베이 논문
│   ├── sections/    # LaTeX 섹션
│   └── references.bib
├── docs/            # 정적 웹사이트 (Vercel)
│   ├── ko/          # 한국어 페이지
│   ├── en/          # 영어 페이지
│   ├── css/         # 다크 모드 glassmorphism 스타일
│   └── js/          # 파티클, GSAP, 공통 헤더
├── assets/figures/  # 222개 일러스트 (ch01-ch13)
├── build_site.py    # 마크다운 → HTML 빌더
├── scripts/         # PDF 생성, 이미지 생성
└── .claude/         # 에이전트 정의 + 스킬 (하네스)
    ├── agents/      # 7개 에이전트 (researcher, writer, illustrator 등)
    └── skills/      # 7개 스킬 (literature-research, web-build 등)
```

## 변경 이력

### 2026-04-07: Human-to-Robot Transfer 서베이 업데이트
2024-2026년 40+편 논문 서베이를 기반으로 7개 챕터 대규모 업데이트:
- **Ch10 (Embodiment Retargeting)**: 6절 → 8절로 재구성. §10.6 Human+Robot Co-training (EgoMimic, EgoScale, AoE, pi0), §10.7 Teleop-Free 접근 (X-Sim, EgoZero, VidBot, Human2Bot) 신규. 14편 추가.
- **Ch06 (사람 손 데이터 수집)**: TacCap, VTDexManip, AirExo/AirExo-2, NuExo, HumanoidExo, ACE, EgoDex 추가. 8편 추가.
- **Ch13 (한계와 미래)**: EgoScale 스케일링 법칙으로 데이터 부족 한계 업데이트, cross-embodiment 진전, egocentric 데이터 트렌드.
- **Ch03, Ch07, Ch08, Ch09**: VTDexManip, EgoDex, LAPA, Ye et al., pi0 human transfer, EgoVLA, PhysBrain, DexWM 추가.

### 2026-04-01: 최초 릴리스
13챕터, 146편 참고문헌, 222개 일러스트, IEEE 서베이 논문, 이중 언어 웹 뷰어 최초 공개.

## Contributors

> 기여량 순 정렬. 기여 방법은 [CONTRIBUTING_ko.md](CONTRIBUTING_ko.md)를 참고하세요.

<!-- CONTRIBUTORS-START -->
| Avatar | Contributor | Contributions |
|:------:|:-----------:|:-------------|
| <img src="https://github.com/revfactory.png" width="50"> | [@revfactory](https://github.com/revfactory) | :wrench: [Harness](https://github.com/revfactory/harness) 에이전트 프레임워크, :art: [웹 디자인](https://github.com/revfactory/ai-trend-onboarding) 패턴 |
| <img src="https://github.com/sjchoi86.png" width="50"> | [@sjchoi86](https://github.com/sjchoi86) | :book: Ch02: 상용 촉각 센서 제품 정보 및 3개 신규 센서 카테고리 ([`f6f6e59`](https://github.com/terryum/survey-robot-hand-tactile-sensor/commit/f6f6e59)) |
| | Hojung Choi (최호정) | :book: CoinFT/UMI-FT/ACP 콘텐츠 — Ch02, Ch03, Ch06, Ch07, Ch13 ([SNU Data Science Seminar 2026](https://www.hojungchoi.com/)) |
<!-- CONTRIBUTORS-END -->

## 감사의 글

이 프로젝트는 황민호님의 [Harness](https://github.com/revfactory/harness)(Apache 2.0) 스킬을 이용하여 제작되었으며, 웹사이트 구조는 [AI Trend Onboarding](https://github.com/revfactory/ai-trend-onboarding)([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ko))의 디자인, 레이아웃 패턴, 에이전트 아키텍처를 본 프로젝트의 도메인에 맞게 변형하여 사용했습니다. 훌륭한 도구를 만들어주신 황민호님께 감사드립니다.

이 책은 서울대학교와 코스맥스의 공동연구 세미나 자료를 초기 Seed로 하여 만들어졌습니다. 세미나를 준비해주신 하준수, 송지환, 박태준, 정인철 박사과정과 공동연구를 함께해주신 박종우, 박용래, 조규진 교수님께 감사의 말씀 드립니다. **최호정** 박사(Stanford/Sunday Robotics)의 SNU Data Science Seminar (2026년 4월) "Multimodal Data for Robot Manipulation" 발표에 감사드립니다 — CoinFT, UMI-FT, Adaptive Compliance Policy에 대한 발표 내용이 이 책의 여러 챕터를 풍부하게 했습니다.

이 저작물의 제작에 AI 도구가 활용되었습니다. 문헌 조사, 콘텐츠 생성, 원고 작성에 Claude(Opus 4.6)를, 그림 생성에 /gemini-3-image-generation 스킬(Gemini 3 Pro Image)을 사용하였습니다.

## 라이선스

이 저작물은 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ko) 라이선스를 따릅니다. 출처를 표시하면 비영리 목적으로 자유롭게 공유하고 변경할 수 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
