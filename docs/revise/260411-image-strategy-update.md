# 이미지 전략 전환 업데이트 (2026-04-11)

## 배경
기존 보고서의 이미지는 대부분 Gemini AI 생성 일러스트였으나, 실제 논문 figure를 크롭/인용하는 것이 교육적 가치가 높다는 판단에 따라 이미지 전략을 전환함.

## 하네스 설정 변경

### `.claude/agents/book-illustrator.md` 전면 개편
- **이전**: Gemini 생성 중심, 3종 변형(technical/academic/darkmode) 생성
- **이후**: 논문 figure 크롭/인용 우선, AI 생성은 보조(챕터당 0-2개)
- 이미지 우선순위: 논문 원본 > 세미나/발표자료 > 상용 사진 > AI 생성

### `book-creation-playbook.md` 수정
- 입문서 프로젝트: "Gemini API" → "논문 figure 크롭 우선, AI 생성 보조"
- 연구 전략서 프로젝트: "AI 생성 아님" → "논문 figure 우선, AI 생성 보조 가능"
- image-curator 에이전트 설명: "AI 생성 금지" → "논문 figure 우선, 보조적 AI 생성 허용"

## 논문 PDF 다운로드 및 Figure 크롭

15개 논문 arXiv PDF 다운로드 → 25개 figure 크롭 (Page 1 teaser + Page 2 detail)

| 논문 | arXiv ID | 크롭 figure | 삽입 챕터 |
|------|----------|-----------|----------|
| LEAP Hand | 2309.06440 | teaser + design detail | Ch04 |
| ORCA Hand | 2504.04259 | teaser + design detail | Ch04 |
| Digit 360 | 2411.02479 | overview + modalities | Ch02 |
| ReSkin | 2111.00071 | overview | Ch02 |
| AnySkin | 2409.08276 | overview | Ch02 |
| F-TAC Hand | 2412.14482 | overview + sensor layout | Ch02 |
| Diffusion Policy | 2303.04137 | overview + architecture | Ch07 |
| ACT/ALOHA | 2304.13705 | overview + architecture | Ch07 |
| Mobile ALOHA | 2401.02117 | overview | Ch07 |
| DexForce | 2501.10356 | overview | Ch07 |
| PP-Tac | 2504.16649 | overview | Ch07 |
| OSMO | 2512.08920 | overview + hardware | Ch06 |
| DexUMI | 2505.21864 | overview + pipeline | Ch06 |
| UMI-FT | 2601.09988 | overview + pipeline | Ch03 |
| EgoMimic | 2410.24221 | overview + pipeline | Ch10 |

## 챕터별 변경 사항

### Ch02 (촉각 센서 기술) — 에이전트 작업 중
- Digit 360, ReSkin, AnySkin, F-TAC Hand 실물 사진 추가 예정

### Ch03 (촉각 데이터)
- UMI-FT 논문 Fig.1, Fig.2 삽입 (기존 세미나 크롭 이미지 대체)

### Ch04 (로봇 핸드 설계)
- LEAP Hand Fig.1 (teaser) + Fig.2 (MCP 관절 설계) 삽입
- ORCA Hand Fig.1 (teaser) + Fig.2 (poppable joint, 텐던 라우팅) 삽입
- LEAP Hand: MCP 관절 보편적 내전/외전 메커니즘, 19.5N 당김력, 조작성 타원체 추가
- ORCA Hand: FSR 기반 이진 촉각, poppable pin joint, 자동 교정, 10K+ 연속 운전 사이클, 10.5kg 하중, zero-shot sim-to-real RL 추가

### Ch06 (인간 손 데이터 수집)
- OSMO 글로브 논문 Fig.1 + Fig.2 삽입 (기존 생성 이미지 대체)
- DexUMI Fig.1 + Fig.2 삽입 (기존 생성 이미지 대체)

### Ch07 (조작 학습)
- Diffusion Policy Fig.1 + Fig.3 (아키텍처) 삽입
- ACT/ALOHA Fig.1 + Fig.3 (아키텍처) 삽입
- Mobile ALOHA Fig.1 삽입
- PP-Tac Fig.1 삽입
- DexForce Fig.1 삽입
- 기존 생성 figure 6개 모두 유지

### Ch10 (체현 리타게팅)
- EgoMimic Fig.1 + Fig.2 삽입

### Ch01, Ch05, Ch08-09, Ch11-13
- 대부분 개념적 내용이므로 현재 생성 이미지 유지 (적절함)
- 추후 필요시 개별 교체 가능

## 이미지 통계 변화

| 항목 | 이전 | 이후 | 변화 |
|------|------|------|------|
| 생성 이미지 | 74개 | 72개 | -2 |
| 실제 논문 figure | 30개 | 41개 | **+11** |
| 실제 이미지 비율 | 29% | **36%** | +7%p |
| 총 이미지 | 104개 | **113개** | +9 |

## 미완료 항목 (추후 세션)
- Ch02 에이전트 작업 완료 대기 중
- Ch08 pi0 아키텍처 논문 figure (pi0 PDF 접근 필요)
- Ch09 DeXtreme ADR 파이프라인 (이미 생성 이미지로 충분할 수 있음)
- Ch11 Mobile ALOHA 시스템 사진 (Ch07에 이미 추가됨)
- Shadow Hand, Allegro Hand 실물 사진 (Ch04 — 기존 설명이 충분히 간략하여 시급하지 않음)
