[English](README.md) | 한국어

# 로봇 손의 정교한 조작을 위한 촉각 센싱: 종합 서베이

촉각 센서, 로봇 핸드 설계, 학습 기반 조작, Physical AI를 아우르는 한국어/영어 이중 언어 기술 서적 및 IEEE 서베이 논문입니다.

**웹사이트**: [terry.artlab.ai/ko/projects/book-robot-hand-tactile-sensor](https://terry.artlab.ai/ko/projects/book-robot-hand-tactile-sensor)

**PDF 다운로드**: [English](https://drive.google.com/file/d/1z5NgFRtOwcWLiZka3bYFnZ-k4Zs7cUa4/view?usp=sharing) | [한글](https://drive.google.com/file/d/1XxPH3N72TOpz2vSSNsrT9C59IUdQpstR/view?usp=sharing) | [ArXiv Paper](https://drive.google.com/file/d/1aF8fDEkFN8vxRfvtyOHLwmz6glowe3f_/view?usp=sharing)

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

## 감사의 글

이 프로젝트는 황민호님의 [Harness](https://github.com/revfactory/harness)(Apache 2.0) 스킬을 이용하여 제작되었으며, 웹사이트 구조는 [AI Trend Onboarding](https://github.com/revfactory/ai-trend-onboarding)([CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ko))의 디자인, 레이아웃 패턴, 에이전트 아키텍처를 본 프로젝트의 도메인에 맞게 변형하여 사용했습니다. 훌륭한 도구를 만들어주신 황민호님께 감사드립니다.

함께 디스커션 해주신 서울대학교 로보틱스 연구실 학생분들께도 감사의 말씀을 전합니다.

이 저작물의 제작에 AI 도구가 활용되었습니다. 문헌 조사, 콘텐츠 생성, 원고 작성에 Claude(Anthropic)를, 그림 생성에 Gemini(Google)를 사용했습니다.

## 라이선스

이 저작물은 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ko) 라이선스를 따릅니다. 출처를 표시하면 비영리 목적으로 자유롭게 공유하고 변경할 수 있습니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
