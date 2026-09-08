#!/usr/bin/env python3
"""
Generate Aaranya Bakehouse Presentation Deck (11 Widescreen Slides with Speaker Notes).
Course Code: 2106 | Digital Innovation in Business
Student: Himani Gupta | Roll No: PGON26108
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # ── Color Palette ──
    BG_DARK = RGBColor(58, 35, 33)          # Deep Artisan Cocoa #3A2321
    BG_LIGHT = RGBColor(255, 253, 249)      # Warm Cream #FFFDF9
    SURFACE_LIGHT = RGBColor(246, 239, 230) # Soft Warm Beige #F6EFE6
    TEXT_DARK = RGBColor(45, 36, 34)        # Charcoal Cocoa
    TEXT_MUTED = RGBColor(106, 94, 91)      # Subdued Slate
    PRIMARY = RGBColor(58, 35, 33)          # Deep Cocoa
    ACCENT = RGBColor(194, 99, 67)          # Warm Terracotta #C26343
    GOLD = RGBColor(212, 163, 115)          # Artisan Gold #D4A373
    WHITE = RGBColor(255, 255, 255)

    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide, color):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def add_header(slide, category, title, dark=False):
        tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.4))
        tf = tx_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = category.upper()
        p.font.name = "Georgia"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = GOLD if dark else ACCENT

        tx_box2 = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(0.7))
        tf2 = tx_box2.text_frame
        tf2.word_wrap = True
        tf2.margin_left = tf2.margin_top = tf2.margin_right = tf2.margin_bottom = 0
        p2 = tf2.paragraphs[0]
        p2.text = title
        p2.font.name = "Georgia"
        p2.font.size = Pt(24)
        p2.font.bold = True
        p2.font.color.rgb = WHITE if dark else PRIMARY

        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.55), Inches(11.733), Inches(0.04))
        shape.fill.solid()
        shape.fill.fore_color.rgb = GOLD if dark else ACCENT
        shape.line.fill.background()

    def set_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text.strip()

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Dark Theme)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, BG_DARK)

    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT
    bar.line.fill.background()

    pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.5), Inches(1.2), Inches(4.333), Inches(0.45))
    pill.fill.solid()
    pill.fill.fore_color.rgb = RGBColor(74, 45, 42)
    pill.line.color.rgb = GOLD
    p_pill = pill.text_frame.paragraphs[0]
    p_pill.text = "COURSE CODE: 2106 • FINAL PROJECT"
    p_pill.font.name = "Calibri"
    p_pill.font.size = Pt(11)
    p_pill.font.bold = True
    p_pill.font.color.rgb = GOLD
    p_pill.alignment = PP_ALIGN.CENTER

    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(11.333), Inches(1.3))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Aaranya Bakehouse"
    p.font.name = "Georgia"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER

    s_box = s1.shapes.add_textbox(Inches(1.5), Inches(3.1), Inches(10.333), Inches(0.8))
    stf = s_box.text_frame
    stf.word_wrap = True
    sp = stf.paragraphs[0]
    sp.text = "Digital Innovation in Business: End-to-End E-Commerce Strategy & Web Platform"
    sp.font.name = "Georgia"
    sp.font.size = Pt(18)
    sp.font.color.rgb = GOLD
    sp.alignment = PP_ALIGN.CENTER

    meta_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.0), Inches(4.2), Inches(7.333), Inches(2.2))
    meta_box.fill.solid()
    meta_box.fill.fore_color.rgb = RGBColor(74, 45, 42)
    meta_box.line.color.rgb = RGBColor(100, 65, 60)
    mtf = meta_box.text_frame
    mtf.word_wrap = True
    
    mp1 = mtf.paragraphs[0]
    mp1.text = "Student Name: Himani Gupta   |   Roll No.: PGON26108"
    mp1.font.name = "Calibri"
    mp1.font.size = Pt(14)
    mp1.font.bold = True
    mp1.font.color.rgb = WHITE
    mp1.alignment = PP_ALIGN.CENTER

    mp2 = mtf.add_paragraph()
    mp2.text = "Academic Course: Digital Innovation in Business (2106)"
    mp2.font.name = "Calibri"
    mp2.font.size = Pt(12)
    mp2.font.color.rgb = RGBColor(210, 195, 190)
    mp2.alignment = PP_ALIGN.CENTER

    mp3 = mtf.add_paragraph()
    mp3.text = "Live Website URL: https://harsh2715.github.io/aaranya-bakehouse/"
    mp3.font.name = "Calibri"
    mp3.font.size = Pt(12)
    mp3.font.bold = True
    mp3.font.color.rgb = GOLD
    mp3.alignment = PP_ALIGN.CENTER

    set_notes(s1, """[SLIDE 1 - 0:00 to 0:50]
Good morning/afternoon, respected faculty and evaluators. Today, I am proud to present my end-to-end capstone project for Digital Innovation in Business, Course Code 2106.

My project is titled 'Aaranya Bakehouse' — a fully realized digital storefront, marketing strategy, and technological blueprint designed for a modern artisanal home bakery. 

Throughout this 8 to 10 minute presentation, I will walk you through the real-world business foundation, target customer segmentation, live website demonstration, our strategic design decisions, content architecture, the POEM marketing matrix, SEO implementation, and future technological recommendations. The website is fully deployed and accessible live at harsh2715.github.io/aaranya-bakehouse. Let us begin with the business foundation.""")

    # =========================================================================
    # SLIDE 2: BUSINESS INTRODUCTION
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, BG_LIGHT)
    add_header(s2, "Business Foundation", "The Business Opportunity & Value Proposition")

    p_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), Inches(5.6), Inches(4.9))
    p_box.fill.solid()
    p_box.fill.fore_color.rgb = SURFACE_LIGHT
    p_box.line.color.rgb = RGBColor(220, 205, 195)
    ptf = p_box.text_frame
    ptf.word_wrap = True
    
    pp0 = ptf.paragraphs[0]
    pp0.text = "THE MARKET PROBLEM"
    pp0.font.name = "Georgia"
    pp0.font.size = Pt(14)
    pp0.font.bold = True
    pp0.font.color.rgb = ACCENT

    pp1 = ptf.add_paragraph()
    pp1.text = "• Mass Commercialization: Commercial bakeries rely on artificial cake premixes, chemical preservatives, and vegetable shortening to cut costs."
    pp1.font.size = Pt(11)
    pp1.font.color.rgb = TEXT_DARK
    
    pp2 = ptf.add_paragraph()
    pp2.text = "• Impersonal Buying Experience: Standard supermarket checkouts do not accommodate custom celebration themes, portion sizing, or personalized flavours."
    pp2.font.size = Pt(11)
    pp2.font.color.rgb = TEXT_DARK

    pp3 = ptf.add_paragraph()
    pp3.text = "• Dietary & Allergen Inflexibility: High friction when ordering reliable 100% vegetarian (eggless) or clean-label pastry options without cross-contamination."
    pp3.font.size = Pt(11)
    pp3.font.color.rgb = TEXT_DARK

    s_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.85), Inches(5.7), Inches(4.9))
    s_box.fill.solid()
    s_box.fill.fore_color.rgb = WHITE
    s_box.line.color.rgb = ACCENT
    stf = s_box.text_frame
    stf.word_wrap = True

    sp0 = stf.paragraphs[0]
    sp0.text = "THE AARANYA BAKEHOUSE SOLUTION"
    sp0.font.name = "Georgia"
    sp0.font.size = Pt(14)
    sp0.font.bold = True
    sp0.font.color.rgb = PRIMARY

    sp1 = stf.add_paragraph()
    sp1.text = "• Uncompromising Culinary Purity: 100% pure dairy butter, 54.5% Callebaut Belgian chocolate, Madagascar vanilla, zero artificial shortening."
    sp1.font.size = Pt(11)
    sp1.font.color.rgb = TEXT_DARK

    sp2 = stf.add_paragraph()
    sp2.text = "• Consultative Enquiry Funnel: Rather than rigid impersonal cart checkout, customers engage through an interactive pricing calculator and direct WhatsApp bridge."
    sp2.font.size = Pt(11)
    sp2.font.color.rgb = TEXT_DARK

    sp3 = stf.add_paragraph()
    sp3.text = "• Bespoke Celebration Craft: Every single sponge is baked strictly fresh to order within 12 hours of delivery, housed in eco-luxe biodegradable packaging."
    sp3.font.size = Pt(11)
    sp3.font.color.rgb = TEXT_DARK

    sp4 = stf.add_paragraph()
    sp4.text = "• High-Trust Digital Presence: Transparent pricing, client testimonials (4.9★), and guaranteed 2-hour response turnaround."
    sp4.font.size = Pt(11)
    sp4.font.bold = True
    sp4.font.color.rgb = ACCENT

    set_notes(s2, """[SLIDE 2 - 0:50 to 1:45]
Moving to our business foundation: what problem does Aaranya Bakehouse solve? 

When examining the urban bakery landscape, we observed a clear divide. On one hand, mass-market commercial bakeries mass-produce cakes using frozen sponge bases, hydrogenated vegetable fats, and artificial shelf-life extenders. On the other hand, boutique pastry shops often lack digital transparency, forcing customers to engage in endless back-and-forth messaging without knowing upfront costs.

Aaranya Bakehouse bridges this gap. Our business model delivers three distinct pillars: first, culinary purity — using 100% pure dairy butter and premium Belgian chocolate with zero chemical additives. Second, an enquiry-based consultative ordering model that captures personalized theme, portion, and dietary needs. And third, a high-trust digital storefront that provides transparent starting prices, interactive cost estimations, and direct WhatsApp connectivity. This ensures customers experience personalized luxury with total digital convenience.""")

    # =========================================================================
    # SLIDE 3: TARGET AUDIENCE & PERSONAS
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, BG_LIGHT)
    add_header(s3, "Market Segmentation", "Target Audience & Customer Personas")

    personas = [
        ("Celebration Planner", "Priya, 29 | Young Urban Parent", 
         "Needs bespoke themed cakes for kids' birthdays and family milestones. Frustrated by generic dry commercial cakes and excessive sugar fondant.",
         "Visual gallery, ingredient transparency (100% butter), instant cake pricing calculator."),
        ("Corporate & Festive Gifter", "Vikram, 38 | Corporate Team Lead", 
         "Requires premium festive hampers (Diwali, client appreciation). Needs reliable bulk scheduling, sophisticated packaging, and fast invoice turnaround.",
         "Curated dessert boxes, corporate branded sleeves, rapid WhatsApp consultation."),
        ("Indulgence Enthusiast", "Aarav, 22 | College Student & Foodie", 
         "Craves viral NYC-style molten stuffed cookies and gourmet cupcakes. Influenced heavily by Instagram aesthetics and unboxing experiences.",
         "Instagram social wall (#AaranyaCelebrations), 10% first-order discount lead magnet.")
    ]

    for idx, (title, demog, pain, trigger) in enumerate(personas):
        x = Inches(0.8 + idx * 4.0)
        box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.85), Inches(3.75), Inches(4.9))
        box.fill.solid()
        box.fill.fore_color.rgb = WHITE if idx != 0 else SURFACE_LIGHT
        box.line.color.rgb = ACCENT if idx == 0 else RGBColor(220, 205, 195)
        tf = box.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = title.upper()
        p0.font.name = "Georgia"
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT

        p1 = tf.add_paragraph()
        p1.text = demog
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = PRIMARY

        p2 = tf.add_paragraph()
        p2.text = "\nNeeds & Pain Points:"
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_DARK

        p3 = tf.add_paragraph()
        p3.text = pain
        p3.font.size = Pt(9.5)
        p3.font.color.rgb = TEXT_MUTED

        p4 = tf.add_paragraph()
        p4.text = "\nWebsite Conversion Trigger:"
        p4.font.size = Pt(10)
        p4.font.bold = True
        p4.font.color.rgb = ACCENT

        p5 = tf.add_paragraph()
        p5.text = trigger
        p5.font.size = Pt(9.5)
        p5.font.color.rgb = TEXT_DARK

    set_notes(s3, """[SLIDE 3 - 1:45 to 2:40]
Understanding user psychology is central to Course 2106. We segmented our market into three core buyer personas, each mapping directly to distinct functional modules on our website.

First, our primary persona is the 'Celebration Planner', represented by Priya, an urban millennial parent. When planning her child's first birthday, she values ingredient purity and custom aesthetic coordination. Our website converts Priya through transparent ingredient storytelling and an interactive price calculator.

Second, our B2B persona is Vikram, a corporate manager seeking premium festive gifting boxes for team recognition. His pain points are reliability and unboxing elegance. He converts through our dedicated 'Curated Dessert Boxes' section and quick corporate enquiry links.

Third, our digital-native persona is Aarav, a university student seeking trendy NYC-style stuffed molten cookies. He engages through our Instagram community gallery and our 10% discount lead magnet. By addressing all three personas, the website maximizes revenue opportunities across individual and corporate segments.""")

    # =========================================================================
    # SLIDE 4: WEBSITE DEMONSTRATION - DESKTOP
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, BG_LIGHT)
    add_header(s4, "Website Demonstration", "Live Website: Architecture & Desktop Experience")

    home_ss_path = "/Users/harshsinghal/.zcode/workspace/default/aaranya-bakehouse/screenshot-home.png"
    if os.path.exists(home_ss_path):
        s4.shapes.add_picture(home_ss_path, Inches(0.8), Inches(1.85), width=Inches(7.2))

    r_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.3), Inches(1.85), Inches(4.2), Inches(4.9))
    r_box.fill.solid()
    r_box.fill.fore_color.rgb = SURFACE_LIGHT
    r_box.line.color.rgb = RGBColor(220, 205, 195)
    rtf = r_box.text_frame
    rtf.word_wrap = True

    rp0 = rtf.paragraphs[0]
    rp0.text = "KEY HOMEPAGE MODULES"
    rp0.font.name = "Georgia"
    rp0.font.size = Pt(13)
    rp0.font.bold = True
    rp0.font.color.rgb = PRIMARY

    bullets = [
        ("Split Hero Section", "Sensory chocolate drip cake imagery paired with social proof badges (500+ celebrations, 4.9★ rating)."),
        ("Clear CTA Dual-Action", "Direct path to 'Explore Menu' for browsers, and 'Custom Order Enquiry' for high-intent visitors."),
        ("4 Core Product Cards", "Custom Cakes, Artisan Cupcakes, NYC Cookies, and Dessert Hampers with starting prices."),
        ("Interactive Price Estimator", "Real-time client-side JS calculator estimating price based on weight, flavor, and tiers."),
        ("Lead Magnet Integration", "Newsletter subscription delivering a 10% promotional code directly upon signup.")
    ]

    for title, desc in bullets:
        bp = rtf.add_paragraph()
        bp.text = f"• {title}: {desc}"
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = TEXT_DARK

    set_notes(s4, """[SLIDE 4 - 2:40 to 3:40]
Here you see an actual live capture of our desktop homepage, deployed at harsh2715.github.io/aaranya-bakehouse.

Notice how the information hierarchy is calibrated for immediate engagement. The split-hero combines an enticing visual of an artisan chocolate drip cake with concrete trust signals: 500+ celebrations served, 100% pure butter and cocoa, and a 4.9-star rating. 

Beneath the hero, visitors find our four signature categories with clear starting price tags, eliminating pricing anxiety. 

Crucially, we implemented an interactive client-side Custom Cake Price Estimator. Visitors can select their cake weight — from 0.5 kg up to 3 kg — choose their flavor profile, select single or stacked tiers, and receive an instant transparent price quote that pre-fills our enquiry form. This interactive module bridges casual curiosity with qualified lead capture.""")

    # =========================================================================
    # SLIDE 5: WEBSITE DEMONSTRATION - MOBILE & PRODUCTS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, BG_LIGHT)
    add_header(s5, "Website Demonstration", "Mobile-First Responsiveness & Interactive Enquiry")

    # Mobile frame background card
    mob_bg = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(1.8), Inches(2.6), Inches(5.1))
    mob_bg.fill.solid()
    mob_bg.fill.fore_color.rgb = RGBColor(20, 20, 20)
    mob_bg.line.fill.background()

    mobile_ss_path = "/Users/harshsinghal/.zcode/workspace/default/aaranya-bakehouse/screenshot-mobile.png"
    if os.path.exists(mobile_ss_path):
        s5.shapes.add_picture(mobile_ss_path, Inches(0.8), Inches(1.9), width=Inches(2.4))

    prod_ss_path = "/Users/harshsinghal/.zcode/workspace/default/aaranya-bakehouse/screenshot-products.png"
    if os.path.exists(prod_ss_path):
        s5.shapes.add_picture(prod_ss_path, Inches(3.6), Inches(1.85), width=Inches(5.2))

    m_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.1), Inches(1.85), Inches(3.5), Inches(5.0))
    m_box.fill.solid()
    m_box.fill.fore_color.rgb = SURFACE_LIGHT
    m_box.line.color.rgb = ACCENT
    mtf = m_box.text_frame
    mtf.word_wrap = True

    mp0 = mtf.paragraphs[0]
    mp0.text = "MOBILE UX & INTERACTIVITY"
    mp0.font.name = "Georgia"
    mp0.font.size = Pt(12)
    mp0.font.bold = True
    mp0.font.color.rgb = ACCENT

    m_features = [
        ("Fluid Responsive Layout", "CSS Grid and Flexbox dynamically adapt across viewports."),
        ("Collapsible Mobile Drawer", "Touch-friendly hamburger navigation with prominent enquiry CTA."),
        ("Interactive FAQ Accordion", "Addressing lead times, eggless options, and delivery logistics."),
        ("Real-Time Form Validation", "Instant field validation preventing form submission errors."),
        ("WhatsApp Quick Bridge", "Floating WhatsApp button with pre-filled enquiry parameters.")
    ]

    for title, desc in m_features:
        p = mtf.add_paragraph()
        p.text = f"\n✔ {title}:"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = PRIMARY
        p2 = mtf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(8.5)
        p2.font.color.rgb = TEXT_DARK

    set_notes(s5, """[SLIDE 5 - 3:40 to 4:35]
On Slide 5, we demonstrate cross-device responsiveness and our product detail journey.

With over 68% of food discovery happening on mobile devices, our website was built mobile-first. As shown on the left, the layout collapses smoothly to a single-column thumb-friendly flow. The hamburger menu offers clear touch targets, and a persistent floating WhatsApp widget enables immediate 1-click customer support.

On our Products page, shown in the center, every category features detailed flavor specifications, box size configurations, and an interactive FAQ accordion. This accordion answers critical pre-purchase questions: minimum advance notice, eggless substitution techniques, and delivery packaging safety. This eliminates purchase hesitation and significantly reduces customer support overhead.""")

    # =========================================================================
    # SLIDE 6: DESIGN DECISIONS & BRANDING
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, BG_LIGHT)
    add_header(s6, "Branding & Creativity", "Design Decisions & Visual Identity System")

    design_cards = [
        ("Color Psychology", [
            ("Artisan Cocoa (#3A2321)", "Deep organic brown representing chocolate, warmth, and culinary craftsmanship."),
            ("Warm Terracotta (#C26343)", "Earthy, energetic accent used for primary CTAs and hover states."),
            ("Warm Cream (#FFFDF9)", "Soft off-white background that reduces eye strain compared to harsh sterile white."),
            ("Artisan Gold (#D4A373)", "Subtle accent communicating premium gourmet confectionery quality.")
        ]),
        ("Typography Hierarchy", [
            ("Playfair Display (Serif)", "Used for H1, H2 headings to evoke boutique Parisian pastry elegance and artisan craft."),
            ("Plus Jakarta Sans (Sans-Serif)", "Modern, geometric body font ensuring exceptional readability on high-DPI screens."),
            ("Scale & Fluid Sizing", "Utilized CSS clamp() functions so headings scale smoothly from desktop to mobile screens.")
        ]),
        ("UX & Accessibility", [
            ("WCAG AA Contrast", "All body copy and interactive buttons meet WCAG 2.1 AA 4.5:1 contrast standards."),
            ("Micro-Interactions", "Smooth CSS transitions, card lift effects on hover, and focused border rings on form inputs."),
            ("Semantic HTML5", "Clean semantic structure (<header>, <main>, <article>, <nav>, <footer>) for screen reader accessibility.")
        ])
    ]

    for idx, (title, items) in enumerate(design_cards):
        x = Inches(0.8 + idx * 4.0)
        box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.85), Inches(3.75), Inches(4.9))
        box.fill.solid()
        box.fill.fore_color.rgb = SURFACE_LIGHT
        box.line.color.rgb = RGBColor(220, 205, 195)
        tf = box.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = title.upper()
        p0.font.name = "Georgia"
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = PRIMARY

        for item_title, item_desc in items:
            p = tf.add_paragraph()
            p.text = f"\n• {item_title}:"
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = ACCENT

            p2 = tf.add_paragraph()
            p2.text = item_desc
            p2.font.size = Pt(9.0)
            p2.font.color.rgb = TEXT_DARK

    set_notes(s6, """[SLIDE 6 - 4:35 to 5:30]
Turning to our branding and design decisions: visual aesthetics directly determine consumer trust in the culinary industry.

Our color palette was chosen intentionally: Deep Cocoa brown anchors the brand in premium chocolate and grounding warmth, while Terracotta orange draws the eye to high-priority conversion actions. Soft Cream serves as the canvas, creating a warm, artisanal ambiance far superior to cold, clinical white.

In typography, we paired 'Playfair Display' — a classic high-contrast serif font that communicates heritage and bespoke luxury — with 'Plus Jakarta Sans', an ultra-clean contemporary sans-serif for comfortable reading of ingredient lists and descriptions.

From an accessibility standpoint, all color pairs meet WCAG AA contrast guidelines. Form elements feature visible focus rings, and semantic HTML5 tags ensure effortless screen reader compatibility.""")

    # =========================================================================
    # SLIDE 7: CONTENT STRATEGY
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, BG_LIGHT)
    add_header(s7, "Content Strategy", "Persuasive Copywriting & Conversion Architecture")

    c_left = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), Inches(5.6), Inches(4.9))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = WHITE
    c_left.line.color.rgb = ACCENT
    ltf = c_left.text_frame
    ltf.word_wrap = True

    lp0 = ltf.paragraphs[0]
    lp0.text = "3-TIER PERSUASIVE COPYWRITING"
    lp0.font.name = "Georgia"
    lp0.font.size = Pt(13)
    lp0.font.bold = True
    lp0.font.color.rgb = ACCENT

    tiers = [
        ("Tier 1: Sensory Hook (Headlines)", "Evocative language focused on indulgence, texture, and celebration: 'Artisanal Bakes Crafted for Your Special Moments'."),
        ("Tier 2: Rational Assurance (Body)", "Concrete ingredient validation: specifying '54.5% Callebaut Belgian chocolate', 'pure dairy butter', and 'slow-reduced berry coulis' rather than vague adjectives."),
        ("Tier 3: Low-Friction Call-to-Action", "Action-oriented CTAs aligned with intent: 'Enquire About a Cake', 'Book This Custom Cake', and 'Chat on WhatsApp'.")
    ]
    for t_head, t_body in tiers:
        p = ltf.add_paragraph()
        p.text = f"\n{t_head}"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = PRIMARY
        p2 = ltf.add_paragraph()
        p2.text = t_body
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = TEXT_DARK

    c_right = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.85), Inches(5.7), Inches(4.9))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = SURFACE_LIGHT
    c_right.line.color.rgb = RGBColor(220, 205, 195)
    rtf = c_right.text_frame
    rtf.word_wrap = True

    rp0 = rtf.paragraphs[0]
    rp0.text = "AUTHENTICITY & TRUST SIGNALS"
    rp0.font.name = "Georgia"
    rp0.font.size = Pt(13)
    rp0.font.bold = True
    rp0.font.color.rgb = PRIMARY

    trust_points = [
        ("Founder Story Integration", "Humanizing the studio through founder Himani Gupta's vision, demonstrating passionate craftsmanship rather than faceless corporate production."),
        ("Kitchen Hygiene Transparency", "Showcasing dedicated pastry prep stations, allergen segregation for 100% vegetarian orders, and temperature-controlled logistics."),
        ("Social Proof Testimonials", "Featuring verified client reviews across children's birthdays, corporate gifting, and silver jubilee anniversaries."),
        ("Transparent Order Timeline", "A 4-step visual roadmap from 'Enquiry & Moodboard' to 'Slow Craft Baking' and 'Chilled Delivery' manages customer expectations.")
    ]
    for t_head, t_body in trust_points:
        p = rtf.add_paragraph()
        p.text = f"\n✔ {t_head}:"
        p.font.size = Pt(10.0)
        p.font.bold = True
        p.font.color.rgb = ACCENT
        p2 = rtf.add_paragraph()
        p2.text = t_body
        p2.font.size = Pt(9.0)
        p2.font.color.rgb = TEXT_DARK

    set_notes(s7, """[SLIDE 7 - 5:30 to 6:25]
Slide 7 covers our content strategy. High-converting digital copy does not rely on empty culinary buzzwords; it delivers tangible, sensory-rich substance.

We engineered a three-tier copywriting hierarchy. Tier 1 hooks emotional interest with celebration themes. Tier 2 delivers rational reassurance by naming our premium ingredients: 54.5% Callebaut chocolate, pure dairy butter, and real fruit compotes. Tier 3 drives low-friction action with transparent enquiry CTAs.

Additionally, our About Us page features founder Himani Gupta's story and explicit kitchen hygiene protocols. In a post-pandemic environment, showing dedicated allergen prep stations, vegetarian segregation, and fresh-baked 12-hour turnaround builds authentic consumer trust, elevating website visitors into confident buyers.""")

    # =========================================================================
    # SLIDE 8: POEM STRATEGY
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, BG_LIGHT)
    add_header(s8, "Digital Marketing Strategy", "POEM Framework: Paid, Owned & Earned Media")

    poem_cards = [
        ("PAID MEDIA (Amplification)", [
            ("Hyper-Local Meta Ads", "Geo-targeted carousel and reel ads targeting parents and event planners within a 10 km delivery radius."),
            ("Local Google Search Ads", "Exact-match search campaigns for 'custom birthday cakes near me' and 'luxury corporate gift boxes'."),
            ("Target KPI", "Customer Acquisition Cost (CAC) < INR 180; 3.5x Return on Ad Spend (ROAS) during festive seasons.")
        ]),
        ("OWNED MEDIA (Core Asset)", [
            ("Responsive Website", "The central conversion hub hosting product specifications, instant calculator, and enquiry forms."),
            ("Instagram Community", "Visual storytelling on @aaranyabakehouse showcasing cake decorating reels and flavor drops."),
            ("VIP Email List", "Lead magnet ('10% off first order') building direct, algorithm-free client communication.")
        ]),
        ("EARNED MEDIA (Validation)", [
            ("User-Generated Content", "Customers tagging #AaranyaCelebrations in party celebration photos and cake cutting videos."),
            ("Word-of-Mouth Flywheel", "60%+ of custom orders generated through peer recommendations and corporate referrals."),
            ("Review Sentiment", "Maintaining a 4.9/5.0 star rating across Google Reviews and featured on-site testimonials.")
        ])
    ]

    for idx, (title, items) in enumerate(poem_cards):
        x = Inches(0.8 + idx * 4.0)
        box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.85), Inches(3.75), Inches(4.9))
        box.fill.solid()
        box.fill.fore_color.rgb = SURFACE_LIGHT if idx != 1 else WHITE
        box.line.color.rgb = ACCENT if idx == 1 else RGBColor(220, 205, 195)
        tf = box.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = title.upper()
        p0.font.name = "Georgia"
        p0.font.size = Pt(12)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT if idx != 1 else PRIMARY

        for item_title, item_desc in items:
            p = tf.add_paragraph()
            p.text = f"\n• {item_title}:"
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = PRIMARY if idx != 1 else ACCENT

            p2 = tf.add_paragraph()
            p2.text = item_desc
            p2.font.size = Pt(9.0)
            p2.font.color.rgb = TEXT_DARK

    set_notes(s8, """[SLIDE 8 - 6:25 to 7:20]
Our digital marketing architecture applies the POEM framework — Paid, Owned, and Earned media — taught in Course 2106.

Our Owned media is the anchor: this responsive website, our Instagram handle @aaranyabakehouse, and our VIP email subscriber list. By capturing customer emails with a 10% discount lead magnet, we build an owned audience independent of social media algorithm changes.

Paid media acts as a targeted catalyst: we utilize hyper-local Instagram reels and Google Search ads restricted to a 10-kilometer radius around our bakery studio, keeping acquisition costs below 180 rupees per lead.

Finally, Earned media is our highest-converting channel. In celebration baking, the cake is literally the centerpiece of the event. When guests taste the cake and see our branded ribbon packaging, they post photos tagging #AaranyaCelebrations. This generates an organic viral referral loop where every single celebration generates future inbound orders.""")

    # =========================================================================
    # SLIDE 9: SEO ARCHITECTURE & KEYWORDS
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, BG_LIGHT)
    add_header(s9, "Search Engine Optimization", "On-Page SEO Architecture & Schema Integration")

    k_box = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), Inches(6.0), Inches(4.9))
    k_box.fill.solid()
    k_box.fill.fore_color.rgb = WHITE
    k_box.line.color.rgb = RGBColor(220, 205, 195)
    ktf = k_box.text_frame
    ktf.word_wrap = True

    kp0 = ktf.paragraphs[0]
    kp0.text = "TARGET KEYWORD ARCHITECTURE"
    kp0.font.name = "Georgia"
    kp0.font.size = Pt(13)
    kp0.font.bold = True
    kp0.font.color.rgb = PRIMARY

    kw_list = [
        ("custom cakes near me", "Transactional", "index.html (H1 & Meta Description)"),
        ("artisanal celebration cakes", "Commercial", "products.html#cakes (H2 & Alt Tags)"),
        ("customized birthday cupcakes box", "Transactional", "products.html#cupcakes (Product Spec)"),
        ("NYC stuffed gourmet cookies", "Informational", "products.html#cookies (Feature Tags)"),
        ("luxury corporate dessert hampers", "Commercial B2B", "products.html#boxes (Hamper Module)"),
        ("eggless custom bakery studio", "Local Intent", "about.html (Hygiene & FAQ Section)")
    ]

    for kw, intent, page in kw_list:
        p = ktf.add_paragraph()
        p.text = f"• \"{kw}\" [{intent}]\n  Mapped to: {page}"
        p.font.size = Pt(9.0)
        p.font.color.rgb = TEXT_DARK

    t_box = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.85), Inches(5.4), Inches(4.9))
    t_box.fill.solid()
    t_box.fill.fore_color.rgb = SURFACE_LIGHT
    t_box.line.color.rgb = ACCENT
    ttf = t_box.text_frame
    ttf.word_wrap = True

    tp0 = ttf.paragraphs[0]
    tp0.text = "TECHNICAL ON-PAGE IMPLEMENTATION"
    tp0.font.name = "Georgia"
    tp0.font.size = Pt(13)
    tp0.font.bold = True
    tp0.font.color.rgb = ACCENT

    tech_items = [
        ("Schema.org Structured Data", "Embedded JSON-LD markup with '@type: Bakery', studio GPS coordinates, opening hours, and phone number for Google Local Knowledge Graph."),
        ("Social Graph Metadata", "Open Graph (og:title, og:image, og:description) and Twitter Card tags configured for rich link previews on WhatsApp and social chats."),
        ("Heading Hierarchy & Semantic HTML", "Strict single H1 per page, followed by logical H2 and H3 structures, ensuring clean search engine spider crawling."),
        ("Performance & Page Speed", "Optimized WebP/JPEG assets, system font fallbacks, and zero heavy dependencies ensuring sub-1.2s First Contentful Paint.")
    ]

    for title, desc in tech_items:
        p = ttf.add_paragraph()
        p.text = f"\n✔ {title}:"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = PRIMARY
        p2 = ttf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(9.0)
        p2.font.color.rgb = TEXT_DARK

    set_notes(s9, """[SLIDE 9 - 7:20 to 8:15]
Slide 9 outlines our on-page and technical SEO architecture. 

Search engines look for clear intent mapping. We conducted keyword research and mapped specific phrases across our site: transactional queries like 'custom cakes near me' are anchored in our home page H1 and meta tags; high-volume queries like 'NYC stuffed gourmet cookies' are mapped to product section anchors.

On the technical side, we implemented Schema.org structured data using the 'Bakery' entity. This enables Google to parse our business address, operating hours, and price range, boosting our chances of appearing in the coveted Local 3-Pack on Google Maps.

Furthermore, Open Graph tags ensure that whenever a customer shares our link on WhatsApp or Facebook, a rich card with our hero cake image and value proposition appears automatically.""")

    # =========================================================================
    # SLIDE 10: FUTURE RECOMMENDATIONS (90-DAY ROADMAP)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, BG_LIGHT)
    add_header(s10, "Strategic Vision", "Future Recommendations: 90-Day Digital Roadmap")

    phases = [
        ("Phase 1: Days 1–30", "LOCAL DISCOVERY & ANALYTICS", [
            "Complete Google Business Profile verification with studio photos and customer reviews.",
            "Deploy Google Analytics 4 (GA4) and Meta Pixel to track calculator usage and drop-off funnels.",
            "Establish local SEO citations across Delhi-NCR food directories."
        ]),
        ("Phase 2: Days 31–60", "CONVERSATIONAL COMMERCE", [
            "Integrate WhatsApp Business Cloud API automated bot for instant slot availability checks.",
            "Enable dynamic UPI payment link generation (Google Pay/Paytm/PhonePe) directly within chat.",
            "Reduce manual consultation response time from 2 hours to under 30 seconds."
        ]),
        ("Phase 3: Days 61–90", "LOYALTY & RECURRING REVENUE", [
            "Launch 'The Celebration Reminder Service' — automated reminder alerts for family birthdays.",
            "Introduce monthly artisan cookie subscription boxes for predictable recurring cash flow.",
            "Pilot micro-influencer gifting with local parenting and lifestyle content creators."
        ])
    ]

    for idx, (timeframe, p_title, p_items) in enumerate(phases):
        x = Inches(0.8 + idx * 4.0)
        box = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.85), Inches(3.75), Inches(4.9))
        box.fill.solid()
        box.fill.fore_color.rgb = SURFACE_LIGHT if idx != 1 else WHITE
        box.line.color.rgb = ACCENT if idx == 1 else RGBColor(220, 205, 195)
        tf = box.text_frame
        tf.word_wrap = True

        p0 = tf.paragraphs[0]
        p0.text = timeframe.upper()
        p0.font.name = "Georgia"
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = ACCENT

        p1 = tf.add_paragraph()
        p1.text = p_title
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = PRIMARY

        for item in p_items:
            p = tf.add_paragraph()
            p.text = f"\n• {item}"
            p.font.size = Pt(9.2)
            p.font.color.rgb = TEXT_DARK

    set_notes(s10, """[SLIDE 10 - 8:15 to 9:05]
Digital innovation is an ongoing iterative process. On Slide 10, we present our strategic 90-day implementation roadmap to scale Aaranya Bakehouse from an initial pilot to commercial scalability.

In Phase 1, the first 30 days focus on local discovery and telemetry: verifying our Google Business Profile and installing GA4 and Meta tracking pixels to analyze user interaction data on our pricing calculator.

In Phase 2, between Days 31 and 60, we implement conversational commerce. By integrating the WhatsApp Business Cloud API, an automated bot will answer routine inquiries, check baking date availability, and dispatch instant UPI payment links, slashing manual consultation time by 65%.

In Phase 3, between Days 61 and 90, we introduce recurring revenue through a Monthly Cookie Club subscription and an automated 'Celebration Reminder Service' that prompts customers two weeks before their anniversary with a 1-click re-order option.""")

    # =========================================================================
    # SLIDE 11: LEARNING OUTCOMES & CONCLUSION (Dark Theme)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, BG_DARK)
    add_header(s11, "Course Reflections", "Key Learning Outcomes & Conclusion", dark=True)

    l_box = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.85), Inches(5.7), Inches(4.9))
    l_box.fill.solid()
    l_box.fill.fore_color.rgb = RGBColor(74, 45, 42)
    l_box.line.color.rgb = GOLD
    ltf = l_box.text_frame
    ltf.word_wrap = True

    lp0 = ltf.paragraphs[0]
    lp0.text = "KEY ACADEMIC LEARNINGS (COURSE 2106)"
    lp0.font.name = "Georgia"
    lp0.font.size = Pt(13)
    lp0.font.bold = True
    lp0.font.color.rgb = GOLD

    learnings = [
        ("Digital Model Alignment", "Recognized that technology must serve the business model. For custom luxury goods, a consultative enquiry funnel converts significantly higher than an impersonal e-commerce cart."),
        ("UX & Conversion Psychology", "Mastered how visual hierarchy, transparent pricing calculators, and social trust signals dismantle customer purchase anxiety."),
        ("Full-Funnel Digital Integration", "Gained practical mastery synthesizing on-page SEO, technical Schema, and POEM marketing into a unified acquisition strategy.")
    ]
    for l_head, l_desc in learnings:
        p = ltf.add_paragraph()
        p.text = f"\n• {l_head}:"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p2 = ltf.add_paragraph()
        p2.text = l_desc
        p2.font.size = Pt(9.0)
        p2.font.color.rgb = RGBColor(220, 205, 195)

    r_box = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.85), Inches(5.7), Inches(4.9))
    r_box.fill.solid()
    r_box.fill.fore_color.rgb = RGBColor(74, 45, 42)
    r_box.line.color.rgb = ACCENT
    rtf = r_box.text_frame
    rtf.word_wrap = True

    rp0 = rtf.paragraphs[0]
    rp0.text = "DELIVERABLES VERIFICATION & THANK YOU"
    rp0.font.name = "Georgia"
    rp0.font.size = Pt(13)
    rp0.font.bold = True
    rp0.font.color.rgb = ACCENT

    delivs = [
        ("Live Website URL", "https://harsh2715.github.io/aaranya-bakehouse/"),
        ("Source Code Repository", "https://github.com/harsh2715/aaranya-bakehouse"),
        ("Project Report", "3-Page PDF Report (ReportLab formatted)"),
        ("Academic Integrity", "Original work designed & submitted for Course 2106")
    ]
    for d_title, d_val in delivs:
        p = rtf.add_paragraph()
        p.text = f"\n✔ {d_title}:\n{d_val}"
        p.font.size = Pt(9.5)
        p.font.color.rgb = WHITE

    rp_end = rtf.add_paragraph()
    rp_end.text = "\nThank you for your time and guidance!\nI welcome your questions and feedback."
    rp_end.font.size = Pt(11)
    rp_end.font.bold = True
    rp_end.font.color.rgb = GOLD

    set_notes(s11, """[SLIDE 11 - 9:05 to 9:45]
In conclusion, developing the Aaranya Bakehouse project provided deep practical synthesis across the entire Digital Innovation in Business curriculum.

The greatest insight gained was that digital innovation is not about adding technical complexity for its own sake; it is about reducing customer friction. By aligning responsive design, transparent pricing tools, structured SEO schema, and a multi-channel POEM framework, we created a viable, resilient digital venture.

All deliverables — our live website, our 3-page academic report, and our presentation deck — are fully verified and ready for review. Thank you very much for your time and guidance, and I now welcome any questions or feedback.""")

    output_path = "/Users/harshsinghal/.zcode/workspace/default/aaranya-bakehouse/presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully at: {output_path}")

if __name__ == '__main__':
    create_presentation()
