# 업데이트 요약: 최호정 SNU Data Science Seminar (2026-04-11)

## 원본 자료
- **세미나**: "Multimodal Data for Robot Manipulation: From Tactile Sensing to Scalable Human Demonstrations" — 최호정 (Stanford/Sunday Robotics)
- **날짜**: 2026년 4월 8일, SNU Data Science Seminar
- **데이터 파일**: `docs/revise-source/seminar-hojung-choi/`
- **참고**: Sunday Robotics 고유 콘텐츠 및 개인 작업 섹션은 지침에 따라 제외함.

---

## 챕터별 업데이트

### Chapter 2: 촉각 센서 기술 (한/영)

**추가 내용:**
1. **2.1.2절 (정전용량식)**: CoinFT를 주목할 만한 정전용량식 센서 설계로 소개
   - 스펙: 두께 2 mm, 무게 2 g, 재료비 <$10, ~360 Hz, 6축, 오픈소스
   - 기둥(pillar) 직경 조절을 통한 감도 튜닝
   - 비구조 환경을 위한 해머 충격 내성

2. **2.1.6절 (스트레인 게이지)**: 상용 F/T 센서 가격 정보 추가
   - ATI >$7,000, Mitsumi >$1,000, Resense >$5,000
   - 취약성 및 수리 비용 문제

3. **2.3절 (다축 센싱)**: "CoinFT 사례 연구" 새 하위 섹션
   - 비교표: CoinFT vs ATI Nano17 vs Mitsumi vs 세미나 2 센서
   - 핵심 논문 인용 추가

**새 이미지:**
- `assets/figures/seminar/coinft_design.png` — CoinFT PCB 설계 (슬라이드 20)
- `assets/figures/seminar/ft_sensor_comparison_table.png` — 상용 F/T 센서 비교 (슬라이드 34)

**새 참고문헌:**
- Choi, H., Kim, A., & Cutkosky, M. R. (2024). CoinFT. *IEEE Sensors Journal*.
- Choi, H. (2026). SNU Data Science Seminar.

---

### Chapter 3: 촉각 데이터 (한/영)

**추가 내용:**
1. **3.4.4절 (신규 — 휴대형 시연 장치)**: UMI-FT 방법론
   - 하드웨어: UMI + iPhone + 손가락별 CoinFT
   - 수집 모달리티: 비전, 자세, 손가락 수준 6축 F/T
   - 태스크 결과: 화이트보드 닦기, 전구 삽입
   - 학습 파이프라인: 멀티모달 Diffusion Policy + 하위 컨트롤러

2. **3.5절 (공개 데이터셋)**: 데이터 규모 비교 단락 추가
   - LLaMA 3: 34,000 인간-년의 텍스트
   - Generalist AI: 57 인간-년의 로봇 데이터 (비전+위치만)
   - 학계 촉각 데이터: <1 인간-년

3. **수집 파이프라인 비교표**: "휴대형 장치" 행 추가 (UMI-FT)

**새 이미지:**
- `assets/figures/seminar/umift_three_components.png` — UMI-FT 3대 구성요소 (슬라이드 48)
- `assets/figures/seminar/data_scale_comparison.png` — 데이터 규모 비교 (슬라이드 9)

**새 참고문헌:**
- Choi, H., et al. (2025). UMI-FT. *arXiv preprint*.
- Choi, H. (2026). SNU Data Science Seminar.

---

### Chapter 6: 인간 손 데이터 수집 (한/영)

**추가 내용:**
1. **6.6절 (원격 조작)**: 원격 조작 비교표 앞에 UMI-FT 비교 단락 추가
   - 독특한 포지셔닝: 휴대형 + 자연스러운 햅틱 + 6축 F/T + 확장 가능
   - 로봇 없이 수백 명이 매일 데이터 수집 가능
   - 그리퍼 형태 모방으로 작은 체화 격차(embodiment gap)

**새 이미지:**
- `assets/figures/seminar/in_wild_generalization.png` — In-the-wild vs. in-lab 결과 (슬라이드 65)

---

### Chapter 7: 조작 학습 (한/영)

**추가 내용:**
1. **7.4절 (DexForce)**: CoinFT 통합 세부사항으로 확장
   - Allegro Hand 손가락에 CoinFT 센서 장착
   - 태스크 결과: F/T + 컴플라이언스 없이 ~0% → 있으면 >90% 성공

2. **7.4절 (신규 — Adaptive Compliance Policy)**: ACP 전체 하위 섹션
   - 인간 시연에서 학습한 방향별 선택적 컴플라이언스
   - ~500 Hz 하위 컨트롤러 vs ~10 Hz 상위 정책
   - 인간 감각운동 계층 비유 (뇌 vs. 반사)
   - 태스크별 결과: 화이트보드 닦기, 전구 삽입

**새 이미지:**
- `assets/figures/seminar/dexforce_coinft_dexterous.png` — Allegro Hand의 DexForce (슬라이드 37)

**새 참고문헌:**
- Choi, H. (2024). CoinFT. *IEEE Sensors Journal*.
- Choi, H. (2025). UMI-FT. *arXiv preprint*.

---

### Chapter 13: 한계와 미래 방향 (한/영)

**추가 내용:**
1. **13.2.A절 (센싱과 인지)**: 저가 소형 F/T 센서 방향 추가
   - CoinFT 성과 + 남은 과제 (인장력 취약성, 표준화)

2. **13.4절 (삼각 통합)**: 축 2, 축 3 설명 강화
   - 축 2: CoinFT ~360 Hz + ACP ~500 Hz 시간 해상도 근거
   - 축 3: UMI-FT in-the-wild 100% vs in-lab 20% 검증

**새 이미지:**
- `assets/figures/seminar/tactile_hierarchy_architecture.png` — 계층적 제어 아키텍처 (슬라이드 84)

---

## 공통 변경사항

### 참고문헌 (references.bib)
3개 BibTeX 항목 추가:
- `choi2024coinft` — CoinFT 논문
- `choi2025umift` — UMI-FT 논문
- `choi2026snuseminar` — SNU 세미나 인용

### README.md + README_ko.md
- **Contributors 테이블**: 최호정(Hojung Choi) 추가 — Ch02, Ch03, Ch06, Ch07, Ch13 기여
- **감사의 글**: SNU Data Science Seminar 기여에 대한 감사 문구 추가

### 이미지 자산
세미나 PDF에서 3840x2160 해상도로 15개 슬라이드 이미지 크롭:
- `assets/figures/seminar/` 디렉토리에 저장

---

## 전체 새 이미지 목록

| 이미지 | 원본 슬라이드 | 사용 챕터 |
|-------|-------------|----------|
| `coinft_design.png` | 슬라이드 20 | Ch02 |
| `coinft_performance.png` | 슬라이드 25 | (미사용, 필요시 활용 가능) |
| `coinft_tunability.png` | 슬라이드 26 | (미사용, 필요시 활용 가능) |
| `ft_sensor_comparison_table.png` | 슬라이드 34 | Ch02 |
| `commercial_ft_sensors.png` | 슬라이드 17 | (미사용, 필요시 활용 가능) |
| `ft_sensor_platform_constraints.png` | 슬라이드 18 | (미사용, 필요시 활용 가능) |
| `dexforce_coinft_dexterous.png` | 슬라이드 37 | Ch07 |
| `vision_models_incomplete.png` | 슬라이드 43 | (미사용, 필요시 활용 가능) |
| `umift_three_components.png` | 슬라이드 48 | Ch03 |
| `umift_learning_pipeline.png` | 슬라이드 50 | (미사용, 필요시 활용 가능) |
| `whiteboard_wipe_baseline.png` | 슬라이드 61 | (미사용, 필요시 활용 가능) |
| `in_wild_generalization.png` | 슬라이드 65 | Ch06 |
| `data_scale_comparison.png` | 슬라이드 9 | Ch03 |
| `anesthetized_finger_demo.png` | 슬라이드 8 | (미사용, 필요시 활용 가능) |
| `tactile_hierarchy_architecture.png` | 슬라이드 84 | Ch13 |

---

## 통계
- **수정된 챕터**: 5개 (Ch02, Ch03, Ch06, Ch07, Ch13)
- **언어**: 한/영 모두
- **새 참고문헌**: BibTeX 12개 + 챕터별 참고문헌 목록 추가
- **새 이미지**: 15개 크롭, 7개 본문 참조
- **README 업데이트**: 2개 (한/영) — contributors + 감사의 글

---

## 2차 보강: 세미나 인용 논문 기반 추가 (2026-04-11)

세미나에서 구체적으로 인용된 논문들을 체계적으로 추출하고, 각 논문의 실제 내용을 조사하여 책에 반영.

### 논문 조사 결과

**이미 책에 있던 논문 (5건)**: Chen 2025 (DexForce), Hou 2025 (ACP/UMI-FT), Chi 2024 (UMI), Zhao 2025 (F-TAC Hand), Huang 2024 (3D-ViTac)

**새로 추가한 논문 (9건)**:

| # | 논문 | 핵심 내용 | 추가 위치 |
|---|------|----------|----------|
| 1 | **Kim et al. 2017** | 광전자식 6축 F/T 센서 (*IEEE/ASME Trans. Mechatronics*) | Ch02 §2.1.6 |
| 2 | **Palli et al. 2014** | Cross-beam + photodetector 6축 F/T (*Sensors & Actuators A*) | Ch02 §2.1.6 |
| 3 | **Fernandez et al. 2021** | Visiflex — 비전 기반 소형 F/T 손가락 끝 센서 (*IEEE RA-L*) | Ch02 §2.1.6, §2.2 |
| 4 | **Winston et al. 2025** | Fourigami — CoinFT 활용 4-DoF 종이접기 햅틱 장치 (*IEEE T-RO*) | Ch02 §2.3 |
| 5 | **Yoshida et al. 2024** | CoinFT로 전완부 방향성 전단 햅틱 큐 (*IEEE T-Haptics*) | Ch02 §2.3 |
| 6 | **Sarac et al. 2022** | CoinFT로 웨어러블 햅틱 브레이슬릿 연구 (*IEEE RA-L*) | Ch02 §2.3 |
| 7 | **Zhao et al. 2024** | ALOHA Unleashed — 대규모 양손 접촉 풍부 조작 (*CoRL 2024*) | Ch07 §7.1 |
| 8 | **Adeniji et al. 2025** | Feel the Force — 촉각 글로브 zero-shot 인간→로봇 전이, 77% 성공 | Ch07 §7.4 |
| 9 | **Flexiv / OnRobot** | 산업용 F/T 센싱 활용 협동로봇 (상용 맥락) | Ch02 §2.1.6 |

### Ch02 보강 상세

1. **§2.1.6 (스트레인 게이지)**: Kim 2017, Palli 2014, Fernandez 2021을 6축 F/T 센서 설계 다양성의 근거로 추가. Flexiv/OnRobot을 산업 응용 맥락으로 추가.
2. **§2.2 (비전 기반)**: Visiflex (Fernandez 2021)를 photometric stereo와 다른 비전 기반 F/T 접근법으로 별도 소개.
3. **§2.3 (CoinFT 사례)**: Winston 2025, Yoshida 2024, Sarac 2022를 CoinFT의 연구실 밖 채택 사례로 추가 — 햅틱, 웨어러블, 인간 지각 연구 분야.

### Ch07 보강 상세

1. **§7.1 (모방학습)**: Zhao 2024 ALOHA Unleashed — 양손 접촉 풍부 조작의 스케일업 사례.
2. **§7.4 (힘 기반 학습)**: Adeniji 2025 "Feel the Force" — 인간 촉각 글로브에서 로봇으로 zero-shot 전이, UMI-FT/DexForce와 같은 맥락이나 로봇 데이터 없이 달성.

### references.bib 추가

9건 BibTeX 항목 추가: kim2017optoelectronic, palli2014optoelectronic, fernandez2021visiflex, winston2025fourigami, yoshida2024shear, sarac2022haptic, zhao2024aloha_unleashed, adeniji2025feel
