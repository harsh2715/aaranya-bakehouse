#!/usr/bin/env python3
"""Generate Aaranya Bakehouse Project Report PDF (2-3 pages)."""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ── Font Registration ──
pdfmetrics.registerFont(TTFont('TimesNewRoman', '/System/Library/Fonts/Supplemental/Times New Roman.ttf'))
pdfmetrics.registerFont(TTFont('TimesNewRoman-Bold', '/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf'))
pdfmetrics.registerFont(TTFont('TimesNewRoman-Italic', '/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf'))
registerFontFamily('TimesNewRoman', normal='TimesNewRoman', bold='TimesNewRoman-Bold', italic='TimesNewRoman-Italic')

# ── Palette ──
ACCENT = colors.HexColor('#bc253e')
TEXT_PRIMARY = colors.HexColor('#262522')
TEXT_MUTED = colors.HexColor('#7e7b72')
BG_SURFACE = colors.HexColor('#e8e6e2')
BG_PAGE = colors.HexColor('#efeeea')

# ── Styles ──
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'ReportTitle', fontName='TimesNewRoman-Bold', fontSize=22,
    leading=26, alignment=TA_CENTER, textColor=TEXT_PRIMARY,
    spaceAfter=6
)

subtitle_style = ParagraphStyle(
    'ReportSubtitle', fontName='TimesNewRoman', fontSize=13,
    leading=18, alignment=TA_CENTER, textColor=TEXT_MUTED,
    spaceAfter=12
)

heading1_style = ParagraphStyle(
    'ReportH1', fontName='TimesNewRoman-Bold', fontSize=16,
    leading=20, textColor=TEXT_PRIMARY, spaceBefore=14, spaceAfter=6,
    borderWidth=0, borderColor=ACCENT, borderPadding=0
)

heading2_style = ParagraphStyle(
    'ReportH2', fontName='TimesNewRoman-Bold', fontSize=13,
    leading=17, textColor=TEXT_PRIMARY, spaceBefore=10, spaceAfter=4
)

body_style = ParagraphStyle(
    'ReportBody', fontName='TimesNewRoman', fontSize=10.5,
    leading=15, alignment=TA_JUSTIFY, textColor=TEXT_PRIMARY,
    spaceAfter=6
)

bullet_style = ParagraphStyle(
    'ReportBullet', fontName='TimesNewRoman', fontSize=10.5,
    leading=15, alignment=TA_LEFT, textColor=TEXT_PRIMARY,
    leftIndent=18, bulletIndent=8, spaceAfter=3
)

meta_style = ParagraphStyle(
    'ReportMeta', fontName='TimesNewRoman', fontSize=10,
    leading=14, alignment=TA_CENTER, textColor=TEXT_MUTED,
    spaceAfter=4
)

# ── Helpers ──
def add_section(title, content_items):
    """Add a section with heading and content."""
    elements = []
    elements.append(Paragraph(f'<b>{title}</b>', heading1_style))
    elements.append(HRFlowable(width='100%', thickness=1, color=ACCENT, spaceBefore=0, spaceAfter=8))
    for item in content_items:
        if isinstance(item, tuple):
            text, style = item
            elements.append(Paragraph(text, style))
        else:
            elements.append(Paragraph(item, body_style))
    elements.append(Spacer(1, 8))
    return elements

def bullet(text):
    return Paragraph(f'• {text}', bullet_style)

# ── Build Story ──
story = []

# Header info
story.append(Paragraph('Digital Innovation in Business Project Report', title_style))
story.append(Paragraph('Aaranya Bakehouse Website Project', subtitle_style))
story.append(Paragraph('Student: Himani Gupta  |  Roll No.: PGON26108  |  Course Code: 2106', meta_style))
story.append(Spacer(1, 16))
story.append(HRFlowable(width='100%', thickness=2, color=ACCENT, spaceBefore=0, spaceAfter=16))

# 1. Business Overview
story.extend(add_section('1. Business Overview', [
    'Aaranya Bakehouse is a fictional proposed home-based bakery created to offer fresh, personalised and thoughtfully presented baked products for celebrations and gifting. The business focuses on custom cakes, cupcakes, cookies and dessert boxes, with an enquiry-based ordering model rather than direct online checkout. The website serves as the primary online touchpoint, helping customers discover offerings, understand the custom-order process and submit enquiries.',
]))

# 2. Target Audience
story.extend(add_section('2. Target Audience', [
    'Primary audience: People seeking customised baked products for birthdays, anniversaries, celebrations and gifting. These customers typically value fresh preparation, attractive presentation and the ability to personalise their order.',
    'Secondary audience: Customers planning small gatherings or looking for curated dessert gifts. They need a quick understanding of offerings, easy navigation and a simple enquiry process.',
]))

# 3. Website Structure (Sitemap)
story.append(Spacer(1, 4))
story.append(Paragraph('<b>3. Website Structure (Sitemap)</b>', heading1_style))
story.append(HRFlowable(width='100%', thickness=1, color=ACCENT, spaceBefore=0, spaceAfter=8))

sitemap_data = [
    [Paragraph('<b>Page</b>', body_style), Paragraph('<b>Purpose</b>', body_style)],
    [Paragraph('Home', body_style), Paragraph('Introduce the bakery, showcase product categories and guide visitors to enquiry.', body_style)],
    [Paragraph('About Us', body_style), Paragraph('Share the business story, approach and core values.', body_style)],
    [Paragraph('Products / Services', body_style), Paragraph('Display the four core offerings and explain the custom-order process.', body_style)],
    [Paragraph('Contact Us', body_style), Paragraph('Provide contact details and a validated enquiry form.', body_style)],
]

sitemap_table = Table(sitemap_data, colWidths=[160, 330], hAlign='LEFT')
sitemap_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), ACCENT),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'TimesNewRoman-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 10.5),
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
    ('BACKGROUND', (0, 2), (-1, 2), BG_SURFACE),
    ('BACKGROUND', (0, 4), (-1, 4), BG_SURFACE),
    ('GRID', (0, 0), (-1, -1), 0.5, TEXT_MUTED),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))
story.append(sitemap_table)
story.append(Spacer(1, 10))

story.append(Paragraph('Under Products / Services, the website covers: Custom Cakes, Cupcakes, Cookies and Dessert Boxes.', body_style))
story.append(Spacer(1, 8))

# 4. Content Strategy
story.extend(add_section('4. Content Strategy', [
    'The content strategy is designed to communicate the bakery proposition quickly through concise, customer-focused copy. The Home page builds immediate interest with a hero section and four featured categories. The About Us page establishes trust through story, approach and values. The Products / Services page clearly presents each offering and a simple 3-step custom-order process. The Contact Us page invites enquiries with a validated form and clear contact details. Throughout the site, CTAs guide visitors from awareness to enquiry.',
]))

# 5. POEM Strategy
story.extend(add_section('5. POEM Strategy', [
    '<b>Paid Media:</b> Targeted social media advertising to promote custom cakes, celebration products and seasonal dessert boxes to relevant local audiences.',
    '<b>Owned Media:</b> The Aaranya Bakehouse website and business social media profiles are used to publish product visuals, service information and clear enquiry CTAs.',
    '<b>Earned Media:</b> Encouraging genuine customer reviews, recommendations, social media mentions and user-shared celebration photos to build authentic credibility.',
]))

# 6. SEO Keywords
story.extend(add_section('6. SEO Keywords', [
    'The following keywords are incorporated naturally in page titles, meta descriptions, headings and copy: custom cakes, home bakery, custom bakery, celebration cakes, cupcakes, cookies, dessert boxes, personalised cakes, bakery for celebrations, custom dessert boxes. Each page has a unique title and meta description, and internal navigation uses descriptive anchor text.',
]))

# 7. Future Recommendations
story.extend(add_section('7. Future Recommendations', [
    'Add online ordering if business demand grows and operations allow. Expand customer review content as genuine testimonials become available. Improve local SEO when a permanent service location is established. Use website analytics to understand visitor behaviour and optimise the enquiry journey.',
]))

# 8. Learning Outcomes
story.extend(add_section('8. Learning Outcomes', [
    'Through this project, I learned how to plan a small business website from concept to deployment, apply responsive design principles for desktop and mobile, create a cohesive brand identity, write customer-focused content, implement basic on-page SEO and structure a simple POEM-based digital marketing strategy. The process reinforced the importance of aligning design, content and functionality to a clear business objective.',
]))

# Acknowledgement
story.append(Spacer(1, 12))
story.append(HRFlowable(width='100%', thickness=0.5, color=TEXT_MUTED, spaceBefore=0, spaceAfter=6))
story.append(Paragraph('<i>Acknowledgement: AI-assisted drafting tools were used during content creation. The final document has been reviewed and personalised by the student for academic submission.</i>', meta_style))

# ── Build PDF ──
pdf_path = '/Users/harshsinghal/.zcode/workspace/default/aaranya-bakehouse/report.pdf'
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    leftMargin=1.5*cm,
    rightMargin=1.5*cm,
    topMargin=1.5*cm,
    bottomMargin=1.5*cm,
    title='Aaranya Bakehouse Project Report',
    author='Himani Gupta',
    creator='Z.ai',
    subject='Digital Innovation in Business Project Report'
)

doc.build(story)

# Post-processing
import subprocess
pdf_skill = '/Users/harshsinghal/.zcode/cli/plugins/cache/zcode-plugins-official/document-skills/0.1.4/skills/pdf/scripts'

subprocess.run(['python3', f'{pdf_skill}/pdf.py', 'meta.brand', pdf_path], check=False)
subprocess.run(['python3', f'{pdf_skill}/pdf.py', 'pages.clean', pdf_path, '-o', pdf_path], check=False)

print(f'Report generated: {pdf_path}')
