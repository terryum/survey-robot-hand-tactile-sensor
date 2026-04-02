#!/usr/bin/env python3
"""Build static HTML site from markdown chapters."""

import re
import os
import json

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(BASE, 'docs')
BOOK_KO = os.path.join(BASE, 'book', 'ko')
BOOK_EN = os.path.join(BASE, 'book', 'en')

# Chapter metadata
CHAPTERS_KO = {
    1: {"title": "왜 촉각인가 — 로봇에게 손의 감각을", "part": "Part I: 촉각의 기초", "part_num": 1},
    2: {"title": "촉각 센서 기술 — 로봇의 피부", "part": "Part I: 촉각의 기초", "part_num": 1},
    3: {"title": "촉각 데이터: 표현과 수집", "part": "Part I: 촉각의 기초", "part_num": 1},
    4: {"title": "로봇 핸드 설계 — 잡기 위한 기계", "part": "Part II: 로봇 핸드와 인간 손", "part_num": 2},
    5: {"title": "지능형 메커니즘 — 물리적 지능", "part": "Part II: 로봇 핸드와 인간 손", "part_num": 2},
    6: {"title": "사람 손 데이터 수집 — 시연으로 가르치기", "part": "Part II: 로봇 핸드와 인간 손", "part_num": 2},
    7: {"title": "조작 학습 — 만지며 배우기", "part": "Part III: 학습과 전이", "part_num": 3},
    8: {"title": "VLA 모델 — 보고 듣고 행동하기", "part": "Part III: 학습과 전이", "part_num": 3},
    9: {"title": "Sim-to-Real 전이 — 가상에서 현실로", "part": "Part III: 학습과 전이", "part_num": 3},
    10: {"title": "사람에서 로봇으로 — Embodiment Retargeting", "part": "Part III: 학습과 전이", "part_num": 3},
    11: {"title": "시스템 통합 — 연구적 관점", "part": "Part IV: 통합과 전망", "part_num": 4},
    12: {"title": "Physical AI와 산업적 전망", "part": "Part IV: 통합과 전망", "part_num": 4},
    13: {"title": "한계와 미래 — Physical AI for Manufacturing", "part": "Part IV: 통합과 전망", "part_num": 4},
}

CHAPTERS_EN = {
    1: {"title": "Why Tactile Sensing — Giving Robots the Sense of Touch", "part": "Part I: Foundations of Touch", "part_num": 1},
    2: {"title": "Tactile Sensor Technology — The Skin of Robots", "part": "Part I: Foundations of Touch", "part_num": 1},
    3: {"title": "Tactile Data: Representation and Collection", "part": "Part I: Foundations of Touch", "part_num": 1},
    4: {"title": "Robot Hand Design — Machines Built to Grasp", "part": "Part II: Hands — Robot and Human", "part_num": 2},
    5: {"title": "Intelligent Mechanisms — Physical Intelligence", "part": "Part II: Hands — Robot and Human", "part_num": 2},
    6: {"title": "Human Hand Data Collection — Teaching by Demonstration", "part": "Part II: Hands — Robot and Human", "part_num": 2},
    7: {"title": "Learning to Manipulate — Learning by Touch", "part": "Part III: Learning and Transfer", "part_num": 3},
    8: {"title": "Vision-Language-Action Models — See, Speak, Act", "part": "Part III: Learning and Transfer", "part_num": 3},
    9: {"title": "Sim-to-Real Transfer — From Virtual to Reality", "part": "Part III: Learning and Transfer", "part_num": 3},
    10: {"title": "From Human to Robot — Embodiment Retargeting", "part": "Part III: Learning and Transfer", "part_num": 3},
    11: {"title": "Research Integration — Toward Unified Systems", "part": "Part IV: Integration and Outlook", "part_num": 4},
    12: {"title": "Physical AI and the Industrial Outlook", "part": "Part IV: Integration and Outlook", "part_num": 4},
    13: {"title": "Limitations and Future — Toward Physical AI for Manufacturing", "part": "Part IV: Integration and Outlook", "part_num": 4},
}


def parse_frontmatter(md):
    """Extract YAML frontmatter and body."""
    meta = {}
    body = md
    if md.startswith('---'):
        parts = md.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            for line in fm.strip().split('\n'):
                if ':' in line and not line.strip().startswith('-'):
                    key, val = line.split(':', 1)
                    meta[key.strip().strip('"')] = val.strip().strip('"')
    return meta, body


def build_citation_map(md_text):
    """Build a mapping from Author-Year citations to sequential numbers.

    Parses the reference list at the end of a chapter markdown to create
    a lookup from citation keys like 'Johansson & Flanagan, 2009' to
    sequential numbers [1], [2], etc.
    """
    # Find the references section
    ref_section = None
    for marker in ['## 참고문헌', '## References']:
        idx = md_text.find(marker)
        if idx != -1:
            ref_section = md_text[idx:]
            break

    if not ref_section:
        return {}, []

    # Parse numbered references: "1. Author, A., Author, B. (Year). Title..."
    refs = []
    for line in ref_section.split('\n'):
        line = line.strip()
        match = re.match(r'^\d+\.\s+(.+)', line)
        if match:
            ref_text = match.group(1)
            refs.append(ref_text)

    # Build citation key -> number mapping
    cite_map = {}
    for i, ref_text in enumerate(refs, 1):
        # Extract year from reference
        year_match = re.search(r'\((\d{4})\)', ref_text)
        if not year_match:
            continue
        year = year_match.group(1)

        # Extract author last name(s) from the beginning
        # Format: "LastName, F., LastName2, F. (Year)..."
        author_part = ref_text[:ref_text.find(f'({year})')].strip().rstrip(',').strip()

        # Get first author's last name
        first_author = author_part.split(',')[0].strip()

        # Generate possible citation keys that might appear in text
        # Single author: [LastName, Year]
        cite_map[f'{first_author}, {year}'] = i
        cite_map[f'{first_author} ({year})'] = i

        # With et al.: [LastName et al., Year]
        cite_map[f'{first_author} et al., {year}'] = i
        cite_map[f'{first_author} et al. ({year})'] = i

        # Two authors: [Last1 & Last2, Year]
        authors_list = [a.strip() for a in author_part.split(',')]
        # Filter out initials (single letter + period)
        last_names = [a for a in authors_list if len(a) > 2 and not re.match(r'^[A-Z]\.\s*$', a.strip())]
        if len(last_names) == 2:
            cite_map[f'{last_names[0]} & {last_names[1]}, {year}'] = i
            cite_map[f'{last_names[0]} and {last_names[1]}, {year}'] = i

        # Map bold-stripped first author (handles **bold** in md)
        first_author_clean = first_author.replace('**', '').strip()
        if first_author_clean != first_author:
            cite_map[f'{first_author_clean}, {year}'] = i
            cite_map[f'{first_author_clean} et al., {year}'] = i

        # Map organization names (e.g., "Physical Intelligence", "Google DeepMind")
        org_part = author_part.replace('**', '').strip().rstrip('.')
        if org_part:
            cite_map[f'{org_part}, {year}'] = i
            cite_map[f'{org_part} ({year})'] = i
            cite_map[f'{org_part} [{year}]'] = i

        # Map keywords found in the full reference text (title, etc.)
        # This catches "pi0", "pi0.6", "RECAP", "Octo", "OpenVLA", etc.
        ref_lower = ref_text.lower()
        # Extract notable keywords from the reference
        for keyword in re.findall(r'(?:pi\*?\d[\d.]*|RECAP|Octo|OpenVLA|GR00T|Helix|DIGIT|GelSight|LEAP|MANO|ALOHA|DexCap|DeXtreme|Sparsh|UniTouch|ForceVLA|Tactile-VLA|OSMO|DexUMI|DEXOP|ExoStart|NeuralFeels|RoboPaint|DiffTactile|FARM|TLA|F-TAC|Mobile ALOHA|RT-1|RT-2|Gemini Robotics|X-Embodiment|Flow Matching|Diffusion Policy|ACT|VTDexManip|AnyTouch|AnySkin|ReSkin|Bunny-VisionPro|AnyTeleop|DexPilot|DexH2R|DOGlove|UniTacHand|ImMimic|X-Sim|Isaac|MuJoCo|RGMC|Robot Synesthesia|PP-Tac|DexForce|ForceMimic)', ref_text, re.IGNORECASE):
            kw_lower = keyword.lower()
            cite_map[f'{keyword} [{year}]'] = i
            cite_map[f'{keyword}, {year}'] = i
            cite_map[f'{keyword} ({year})'] = i
            # Store for contextual matching
            cite_map[f'_kw_{kw_lower}_{year}'] = i

    # Build year-only map (only if unique year in refs)
    year_count = {}
    for ref_text in refs:
        ym = re.search(r'\((\d{4})\)', ref_text)
        if ym:
            yr = ym.group(1)
            year_count[yr] = year_count.get(yr, 0) + 1
    # Only map year-only for unambiguous years
    for i, ref_text in enumerate(refs, 1):
        ym = re.search(r'\((\d{4})\)', ref_text)
        if ym:
            yr = ym.group(1)
            if year_count[yr] == 1 and yr not in cite_map:
                cite_map[yr] = i

    return cite_map, refs


def replace_citations_with_links(html_text, cite_map, ch_num, ref_list=None):
    """Replace [Author, Year] citations in HTML with superscript links.

    Converts inline citations to clickable superscript numbers that
    link to the reference list at the bottom of the chapter.
    """
    if not cite_map:
        return html_text
    if ref_list is None:
        ref_list = []

    # Build a reverse lookup: year → list of (author_keyword, ref_num)
    year_refs = {}
    for key, num in cite_map.items():
        year_match = re.search(r'\d{4}', key)
        if year_match:
            yr = year_match.group()
            author = key.replace(yr, '').strip(' ,[]()').lower()
            if yr not in year_refs:
                year_refs[yr] = []
            year_refs[yr].append((author, num))

    def make_link(num, title):
        return f'<sup><a class="cite-link" href="#ch{ch_num}-ref-{num}" title="{title}">[{num}]</a></sup>'

    def citation_replacer(match):
        """Replace a single [citation] with a superscript link."""
        full_match = match.group(0)
        inner = match.group(1)

        # Skip if this looks like a markdown link [text](url)
        end_pos = match.end()
        if end_pos < len(html_text) and html_text[end_pos] == '(':
            return full_match

        # Skip things that aren't citations (e.g., [보충 필요], [PASS], [Link])
        if not re.search(r'\d{4}', inner):
            return full_match

        inner_clean = inner.strip()

        # Direct lookup
        if inner_clean in cite_map:
            return make_link(cite_map[inner_clean], inner_clean)

        # Fuzzy matching: years match + author substring
        inner_year = re.search(r'\d{4}', inner_clean)
        if inner_year:
            yr = inner_year.group()
            inner_lower = inner_clean.lower()

            # Try cite_map keys
            for key, num in cite_map.items():
                key_year = re.search(r'\d{4}', key)
                if key_year and key_year.group() == yr:
                    key_author = key.replace(yr, '').strip(' ,[]()').lower()
                    if key_author and key_author in inner_lower:
                        return make_link(num, inner_clean)
                    if inner_lower.replace(yr, '').strip(' ,[]()') in key_author and len(inner_lower) > 4:
                        return make_link(num, inner_clean)

            # Year-only citation [2025]: look for context before the bracket
            if inner_clean == yr and yr in cite_map:
                return make_link(cite_map[yr], inner_clean)

        return full_match

    # First pass: replace [Author et al., Year] and [Year] patterns
    result = re.sub(r'\[([^\]]+)\](?!\()', citation_replacer, html_text)

    # Second pass: find "Name [Year]" patterns where [Year] wasn't matched
    # e.g., "pi0.6 [2025]" or "Octo [2024]" — match word(s) before [year]
    def contextual_replacer(match):
        prefix = match.group(1)  # e.g., "pi0.6" or "Octo"
        year = match.group(2)    # e.g., "2025"

        # Check if already replaced (contains cite-link)
        if 'cite-link' in prefix:
            return match.group(0)

        prefix_clean = re.sub(r'<[^>]+>', '', prefix).strip()
        prefix_lower = prefix_clean.lower()

        # Try keyword matching first (most precise)
        kw_key = f'_kw_{prefix_lower}_{year}'
        if kw_key in cite_map:
            return f'{prefix}{make_link(cite_map[kw_key], prefix_clean + " " + year)}'

        # Try direct key match
        for pattern in [f'{prefix_clean} [{year}]', f'{prefix_clean}, {year}', f'{prefix_clean} ({year})']:
            if pattern in cite_map:
                return f'{prefix}{make_link(cite_map[pattern], prefix_clean + " " + year)}'

        # Fuzzy: check if prefix appears in any cite_map key with same year
        for key, num in cite_map.items():
            if key.startswith('_kw_'):
                continue
            key_year = re.search(r'\d{4}', key)
            if key_year and key_year.group() == year:
                key_lower = key.lower()
                if prefix_lower and len(prefix_lower) > 2 and prefix_lower in key_lower:
                    return f'{prefix}{make_link(num, prefix_clean + " " + year)}'

        # Search in full reference text for the prefix keyword
        if ref_list:
            for idx, ref_text in enumerate(ref_list, 1):
                ref_year = re.search(r'\((\d{4})\)', ref_text)
                if ref_year and ref_year.group(1) == year:
                    ref_lower = ref_text.lower()
                    if prefix_lower and len(prefix_lower) > 2:
                        # Exact substring match
                        if prefix_lower in ref_lower:
                            return f'{prefix}{make_link(idx, prefix_clean + " " + year)}'
                        # Prefix match for versioned names (pi0.6 → pi0.5, pi0)
                        prefix_base = re.sub(r'[\d.]+$', '', prefix_lower)
                        if prefix_base and len(prefix_base) > 1 and prefix_base in ref_lower:
                            return f'{prefix}{make_link(idx, prefix_clean + " " + year)}'

        # Fallback: year-only match (only if unambiguous)
        if year in cite_map:
            return f'{prefix}{make_link(cite_map[year], year)}'

        return match.group(0)

    result = re.sub(r'(\S+)\s*\[(\d{4})\](?!\()', contextual_replacer, result)

    return result


def build_references_list_html(refs, ch_num):
    """Build the chapter-level reference list as a proper numbered list with anchors."""
    if not refs:
        return ''

    items = []
    for i, ref_text in enumerate(refs, 1):
        # Process inline formatting
        ref_html = ref_text
        ref_html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', ref_html)
        ref_html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', ref_html)
        items.append(f'  <li id="ch{ch_num}-ref-{i}" value="{i}">{ref_html}</li>')

    return '<ol class="references-list">\n' + '\n'.join(items) + '\n</ol>'


def md_to_html_content(md_text, ch_num, lang):
    """Convert markdown body to HTML sections."""
    lines = md_text.strip().split('\n')
    html_parts = []
    in_table = False
    in_code = False
    in_list = False
    in_blockquote = False
    list_type = None
    current_section_id = None
    bq_lines = []

    def flush_blockquote():
        nonlocal bq_lines, in_blockquote
        if bq_lines:
            content = '\n'.join(bq_lines)
            # Check if key paper
            css_class = 'key-paper' if any(k in content for k in ['핵심 논문', 'Key Paper', '핵심 연구']) else ''
            html_parts.append(f'<blockquote class="{css_class}">{process_inline(content)}</blockquote>')
            bq_lines = []
            in_blockquote = False

    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            tag = 'ol' if list_type == 'ol' else 'ul'
            html_parts.append(f'</{tag}>')
            in_list = False
            list_type = None

    def process_inline(text):
        """Process inline markdown."""
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        # Code
        text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
        # Links
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        # Cross-references like (→ Chapter N)
        def chapter_ref(m):
            ref_text = m.group(1)
            ch_match = re.search(r'Chapter\s+(\d+)', ref_text)
            if ch_match:
                ch = ch_match.group(1).zfill(2)
                return f'(<a href="ch{ch}.html">{ref_text}</a>)'
            return m.group(0)
        text = re.sub(r'\(→\s*([^)]+)\)', chapter_ref, text)
        return text

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Code blocks
        if stripped.startswith('```'):
            if in_code:
                html_parts.append('</code></pre>')
                in_code = False
            else:
                flush_blockquote()
                flush_list()
                lang_match = re.match(r'```(\w+)', stripped)
                code_lang = lang_match.group(1) if lang_match else ''
                html_parts.append(f'<pre><code class="language-{code_lang}">')
                in_code = True
            continue

        if in_code:
            html_parts.append(line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
            continue

        # Skip frontmatter-like content
        if stripped.startswith('---') and not in_table:
            flush_blockquote()
            flush_list()
            html_parts.append('<hr>')
            continue

        # Blockquotes
        if stripped.startswith('>'):
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            content = stripped.lstrip('>').strip()
            if not in_blockquote:
                in_blockquote = True
                bq_lines = [content]
            else:
                bq_lines.append(content)
            continue
        elif in_blockquote:
            flush_blockquote()

        # Empty lines
        if not stripped:
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            continue

        # H1 - Chapter title (skip, we handle it in header)
        if stripped.startswith('# ') and not stripped.startswith('## '):
            continue

        # H2 - Section headers
        if stripped.startswith('## '):
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            title = stripped[3:].strip()
            # Generate section ID
            sec_match = re.match(r'(\d+\.\d+)', title)
            if sec_match:
                sec_id = f'sec-{sec_match.group(1).replace(".", "-")}'
            else:
                sec_id = f'sec-{title.lower().replace(" ", "-")[:30]}'

            if current_section_id is not None:
                html_parts.append('</section>')

            current_section_id = sec_id
            html_parts.append(f'<section id="{sec_id}" class="content-section">')
            html_parts.append(f'<h2>{process_inline(title)}</h2>')
            continue

        # H3 - Subsection
        if stripped.startswith('### '):
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            title = stripped[4:].strip()
            html_parts.append(f'<h3>{process_inline(title)}</h3>')
            continue

        # H4
        if stripped.startswith('#### '):
            flush_list()
            if in_table:
                html_parts.append('</tbody></table>')
                in_table = False
            title = stripped[5:].strip()
            html_parts.append(f'<h4>{process_inline(title)}</h4>')
            continue

        # Images
        img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', stripped)
        if img_match:
            flush_list()
            caption = img_match.group(1)
            src = img_match.group(2)
            # Fix path: ../../assets/figures/ -> ../assets/figures/
            src = src.replace('../../assets/figures/', '../assets/figures/')
            # Use darkmode version if available
            src_dark = src.replace('_technical.png', '_darkmode.png')
            html_parts.append(f'<figure>')
            html_parts.append(f'  <img src="{src_dark}" alt="{caption}" loading="lazy" onerror="this.src=\'{src}\'">')
            html_parts.append(f'  <figcaption>{process_inline(caption)}</figcaption>')
            html_parts.append(f'</figure>')
            continue

        # Tables
        if '|' in stripped and stripped.startswith('|'):
            if not in_table:
                flush_list()
                in_table = True
                html_parts.append('<table class="styled-table">')
                # Parse header
                cells = [c.strip() for c in stripped.split('|')[1:-1]]
                html_parts.append('<thead><tr>')
                for c in cells:
                    html_parts.append(f'<th>{process_inline(c)}</th>')
                html_parts.append('</tr></thead><tbody>')
            elif re.match(r'\|[\s\-:|]+\|', stripped):
                # Separator row, skip
                continue
            else:
                cells = [c.strip() for c in stripped.split('|')[1:-1]]
                html_parts.append('<tr>')
                for c in cells:
                    html_parts.append(f'<td>{process_inline(c)}</td>')
                html_parts.append('</tr>')
            continue
        elif in_table:
            html_parts.append('</tbody></table>')
            in_table = False

        # Unordered list
        if re.match(r'^[-*]\s', stripped):
            content = re.sub(r'^[-*]\s+', '', stripped)
            if not in_list or list_type != 'ul':
                flush_list()
                html_parts.append('<ul>')
                in_list = True
                list_type = 'ul'
            html_parts.append(f'<li>{process_inline(content)}</li>')
            continue

        # Ordered list
        ol_match = re.match(r'^(\d+)\.\s+(.+)', stripped)
        if ol_match:
            content = ol_match.group(2)
            if not in_list or list_type != 'ol':
                flush_list()
                html_parts.append('<ol>')
                in_list = True
                list_type = 'ol'
            html_parts.append(f'<li>{process_inline(content)}</li>')
            continue

        # Regular paragraph
        flush_list()
        html_parts.append(f'<p>{process_inline(stripped)}</p>')

    # Close open elements
    flush_blockquote()
    flush_list()
    if in_table:
        html_parts.append('</tbody></table>')
    if in_code:
        html_parts.append('</code></pre>')
    if current_section_id is not None:
        html_parts.append('</section>')

    return '\n'.join(html_parts)


def extract_sections(md_text, ch_num):
    """Extract section titles for sidebar navigation."""
    sections = []
    for line in md_text.split('\n'):
        line = line.strip()
        if line.startswith('## ') and not line.startswith('### '):
            title = line[3:].strip()
            sec_match = re.match(r'(\d+\.\d+)', title)
            if sec_match:
                sec_id = f'sec-{sec_match.group(1).replace(".", "-")}'
            else:
                sec_id = f'sec-{title.lower().replace(" ", "-")[:30]}'
            sections.append({"id": sec_id, "title": title})
    return sections


def build_sidebar(sections, part_num):
    """Build sidebar navigation HTML."""
    if not sections:
        return ''
    dots = []
    for i, sec in enumerate(sections):
        active = ' active' if i == 0 else ''
        label = sec['title']
        if len(label) > 35:
            label = label[:35] + '...'
        dots.append(f'    <a class="nav-dot{active}" data-section="{sec["id"]}">\n'
                     f'      <span class="dot"></span>\n'
                     f'      <span class="label">{label}</span>\n'
                     f'    </a>')
    return f'  <nav class="sidebar-nav part-{part_num}">\n' + '\n'.join(dots) + '\n  </nav>'


def build_chapter_html(ch_num, lang, chapters_meta, book_dir, lang_code):
    """Build a complete chapter HTML page."""
    md_path = os.path.join(book_dir, f'ch{ch_num:02d}.md')
    if not os.path.exists(md_path):
        print(f"  WARNING: {md_path} not found, skipping")
        return None

    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    meta, body = parse_frontmatter(md)
    ch_meta = chapters_meta[ch_num]
    part_num = ch_meta['part_num']
    part_label = ch_meta['part']
    title = ch_meta['title']

    date = meta.get('date', '2026-04-01')
    last_updated = meta.get('last_updated', '2026-04-01')

    # Extract sources from frontmatter
    sources = []
    in_sources = False
    for line in md.split('---')[1].split('\n') if '---' in md else []:
        if 'sources:' in line:
            in_sources = True
            continue
        if in_sources:
            if line.strip().startswith('-'):
                sources.append(line.strip().lstrip('- ').strip('"').strip("'"))
            else:
                in_sources = False

    # Build chapter navigation (needed before content assembly)
    if lang_code == 'ko':
        date_label = '집필일'
        updated_label = '최종수정일'
        toc_label = '목록'
    else:
        date_label = 'Written'
        updated_label = 'Last updated'
        toc_label = 'Index'

    if ch_num > 1:
        prev_link = f'<a href="ch{ch_num-1:02d}.html" class="prev">&larr; Ch.{ch_num-1}</a>'
    else:
        prev_link = '<span class="placeholder"></span>'

    toc_link = f'<a href="./" class="toc-link">{toc_label}</a>'

    if ch_num < 13:
        next_link = f'<a href="ch{ch_num+1:02d}.html" class="next">Ch.{ch_num+1} &rarr;</a>'
    else:
        next_link = '<span class="placeholder"></span>'

    chapter_nav_html = f'''      <nav class="chapter-nav">
        {prev_link}
        {toc_link}
        {next_link}
      </nav>'''

    # Build citation map from references in this chapter
    cite_map, ref_list = build_citation_map(body)

    # Split body: content before references section, and references section
    ref_marker = None
    body_content = body
    for marker in ['## 참고문헌', '## References']:
        idx = body.find(marker)
        if idx != -1:
            ref_marker = marker
            body_content = body[:idx]
            break

    # Convert body (without references section)
    content_html = md_to_html_content(body_content, ch_num, lang)

    # Replace citations with superscript links
    content_html = replace_citations_with_links(content_html, cite_map, ch_num, ref_list)

    # Build proper references list HTML
    ref_section_title = '참고문헌' if lang == 'ko' else 'References'
    ref_html = ''
    if ref_list:
        ref_html = f'<section id="sec-references" class="content-section">\n'
        ref_html += f'<h2>{ref_section_title}</h2>\n'
        ref_html += build_references_list_html(ref_list, ch_num)
        ref_html += '\n</section>'

    # Navigation before references + references + navigation after
    content_html = content_html + '\n' + chapter_nav_html + '\n' + ref_html

    sections = extract_sections(body, ch_num)
    sidebar_html = build_sidebar(sections, part_num)

    # Navigation variables already defined above (before citation processing)

    # Sources section removed per user request
    sources_html = ''

    html = f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter {ch_num}: {title}</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body{' class="lang-en"' if lang_code == 'en' else ''}>
  <canvas id="particle-canvas"></canvas>

  <header id="site-header"></header>
  <script src="../js/header.js"></script>

  <main class="chapter-page part-{part_num}">
{sidebar_html}

    <article class="chapter-content">
      <header class="chapter-header">
        <span class="part-label">{part_label}</span>
        <h1>Chapter {ch_num}: {title}</h1>
        <div class="chapter-meta">
          <span>{date_label}: {date}</span>
          <span>{updated_label}: {last_updated}</span>
        </div>
      </header>

{content_html}

{chapter_nav_html}
    </article>
  </main>

  <footer id="site-footer"></footer>
  <script src="../js/footer.js"></script>

  <script src="../js/main.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
  <script src="../js/chapter.js"></script>
</body>
</html>'''

    return html


def build_glossary_html(lang_code, book_dir):
    """Build glossary page."""
    md_path = os.path.join(book_dir, 'glossary.md')
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    meta, body = parse_frontmatter(md)

    if lang_code == 'ko':
        page_title = '용어집 (Glossary)'
        other_lang_path = '../en/glossary.html'
    else:
        page_title = 'Glossary'
        other_lang_path = '../ko/glossary.html'

    # Parse glossary entries
    content_lines = []
    for line in body.strip().split('\n'):
        stripped = line.strip()
        if stripped.startswith('# '):
            continue  # Skip main title
        if stripped.startswith('## '):
            letter = stripped[3:].strip()
            content_lines.append(f'<h2 class="glossary-letter">{letter}</h2>')
        elif stripped.startswith('- **'):
            # Glossary item
            text = stripped[2:]  # Remove "- "
            text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
            content_lines.append(f'<div class="glossary-item">{text}</div>')
        elif stripped:
            content_lines.append(f'<p>{stripped}</p>')

    content = '\n'.join(content_lines)

    html = f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body{' class="lang-en"' if lang_code == 'en' else ''}>
  <canvas id="particle-canvas"></canvas>

  <header id="site-header"></header>
  <script src="../js/header.js"></script>

  <main>
    <div class="glossary-section">
      <header class="chapter-header">
        <h1>{page_title}</h1>
      </header>
{content}
    </div>
  </main>

  <footer id="site-footer"></footer>
  <script src="../js/footer.js"></script>

  <script src="../js/main.js"></script>
</body>
</html>'''

    return html


def parse_bib(bib_path):
    """Parse BibTeX file into list of references."""
    refs = []
    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into entries
    entries = re.findall(r'@\w+\{([^,]+),([^@]+)', content)
    for key, body in entries:
        ref = {'key': key.strip()}
        for field in ['title', 'author', 'year', 'journal', 'booktitle', 'url']:
            match = re.search(rf'{field}\s*=\s*\{{(.+?)\}}', body)
            if match:
                ref[field] = match.group(1).strip()
        if 'title' in ref:
            refs.append(ref)

    return refs


def build_references_html(lang_code, bib_path):
    """Build references page."""
    refs = parse_bib(bib_path)

    if lang_code == 'ko':
        page_title = '통합 참고문헌 (References)'
    else:
        page_title = 'Consolidated References'

    ref_items = []
    for i, ref in enumerate(refs, 1):
        authors = ref.get('author', 'Unknown')
        year = ref.get('year', '')
        title = ref.get('title', '')
        venue = ref.get('journal', ref.get('booktitle', ''))
        url = ref.get('url', '')

        url_html = f' <a href="{url}" target="_blank" rel="noopener">[Link]</a>' if url else ''

        ref_items.append(
            f'<div class="ref-item" id="ref-{ref["key"]}">'
            f'<span class="ref-id">[{i}]</span> '
            f'{authors} ({year}). <strong>{title}</strong>. <em>{venue}</em>.{url_html}'
            f'</div>'
        )

    content = '\n'.join(ref_items)

    html = f'''<!DOCTYPE html>
<html lang="{lang_code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body{' class="lang-en"' if lang_code == 'en' else ''}>
  <canvas id="particle-canvas"></canvas>

  <header id="site-header"></header>
  <script src="../js/header.js"></script>

  <main>
    <div class="references-section">
      <header class="chapter-header">
        <h1>{page_title}</h1>
        <p class="chapter-summary">{len(refs)} references</p>
      </header>
{content}

      <section class="acknowledgment-section">
        <h2>{'감사의 글' if lang_code == 'ko' else 'Acknowledgment'}</h2>
        <p>{'이 책은 서울대학교와 코스맥스의 공동연구 세미나 자료를 초기 Seed로 하여 만들어졌습니다. 세미나를 준비해주신 하준수, 송지환, 박태준, 정인철 박사과정과 공동연구를 함께해주신 박종우(Frank C. Park), 박용래(Yong-Lae Park), 조규진(Kyujin Cho) 교수님께 감사의 말씀 드립니다.' if lang_code == 'ko' else 'This work was seeded from joint research seminar materials between Seoul National University and Cosmax. Special thanks to Junsoo Ha, Jihwan Song, Taejoon Park, and Incheol Jeong (PhD candidates) for preparing the seminars, and to Professors Frank Chongwoo Park, Yong-Lae Park, and Kyujin Cho for their collaboration.'}</p>
        <p>{'이 프로젝트는 황민호님의 <a href="https://github.com/revfactory/harness">Harness</a> 스킬을 이용하여 제작되었으며, 웹사이트 구조는 <a href="https://github.com/revfactory/ai-trend-onboarding">AI Trend Onboarding</a>을 참고하였습니다.' if lang_code == 'ko' else 'This project was built using the <a href="https://github.com/revfactory/harness">Harness</a> skill by Minho Hwang, and the site structure was adapted from <a href="https://github.com/revfactory/ai-trend-onboarding">AI Trend Onboarding</a> by Minho Hwang.'}</p>
        <p>{'이 저작물의 제작에 AI 도구가 활용되었습니다. 문헌 조사, 콘텐츠 생성, 원고 작성에 Claude(Opus 4.6)를, 그림 생성에 /gemini-3-image-generation 스킬(Gemini 3 Pro Image)을 사용하였습니다.' if lang_code == 'ko' else 'AI tools were used in the production of this work: Claude (Opus 4.6) for literature survey, content generation, and manuscript preparation, and the gemini-3-image-generation skill (Gemini 3 Pro Image) for figure generation.'}</p>
      </section>
    </div>
  </main>

  <footer id="site-footer"></footer>
  <script src="../js/footer.js"></script>

  <script src="../js/main.js"></script>
</body>
</html>'''

    return html


def main():
    bib_path = os.path.join(BASE, 'book', 'references.bib')

    # Build KO chapters
    print("Building Korean chapters...")
    for ch in range(1, 14):
        html = build_chapter_html(ch, 'ko', CHAPTERS_KO, BOOK_KO, 'ko')
        if html:
            out_path = os.path.join(DOCS, 'ko', f'ch{ch:02d}.html')
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  Created: ko/ch{ch:02d}.html")

    # Build EN chapters
    print("Building English chapters...")
    for ch in range(1, 14):
        html = build_chapter_html(ch, 'en', CHAPTERS_EN, BOOK_EN, 'en')
        if html:
            out_path = os.path.join(DOCS, 'en', f'ch{ch:02d}.html')
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  Created: en/ch{ch:02d}.html")

    # Build Glossaries
    print("Building glossaries...")
    for lang_code, book_dir in [('ko', BOOK_KO), ('en', BOOK_EN)]:
        html = build_glossary_html(lang_code, book_dir)
        out_path = os.path.join(DOCS, lang_code, 'glossary.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: {lang_code}/glossary.html")

    # Build References
    print("Building references...")
    for lang_code in ['ko', 'en']:
        html = build_references_html(lang_code, bib_path)
        out_path = os.path.join(DOCS, lang_code, 'references.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  Created: {lang_code}/references.html")

    # Copy figures
    print("Copying figures...")
    import shutil
    src_figures = os.path.join(BASE, 'assets', 'figures')
    dst_figures = os.path.join(DOCS, 'assets', 'figures')
    if os.path.exists(src_figures):
        if os.path.exists(dst_figures):
            shutil.rmtree(dst_figures)
        shutil.copytree(src_figures, dst_figures)
        print(f"  Copied figures to docs/assets/figures/")

    print("\nBuild complete!")
    # Count files
    total = 0
    for root, dirs, files in os.walk(DOCS):
        total += len([f for f in files if f.endswith('.html')])
    print(f"Total HTML files: {total}")


if __name__ == '__main__':
    main()
