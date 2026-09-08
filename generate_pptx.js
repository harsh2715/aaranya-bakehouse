const pptxgen = require("pptxgenjs");
const pres = new pptxgen();

pres.layout = "LAYOUT_WIDE";
pres.author = "Himani Gupta";
pres.title = "Aaranya Bakehouse Website Project";

const W = 13.33, H = 7.5, M = 0.5;

// Brand colors
const BG_DARK = "4A2C2A";
const BG_LIGHT = "FFF8F0";
const PRIMARY = "4A2C2A";
const ACCENT = "C97B5D";
const MUTED = "7e7b72";
const SURFACE = "F2E8DC";

function addDarkSlide() {
  const slide = pres.addSlide();
  slide.background = { color: BG_DARK };
  return slide;
}

function addLightSlide() {
  const slide = pres.addSlide();
  slide.background = { color: BG_LIGHT };
  return slide;
}

// ===== SLIDE 1: TITLE =====
const s1 = addDarkSlide();
s1.addText("Digital Innovation in Business", {
  x: M, y: 1.8, w: W - 2*M, h: 1.2,
  fontSize: 40, fontFace: "Georgia", color: "FFFFFF", bold: true, align: "center"
});
s1.addText("Aaranya Bakehouse Website Project", {
  x: M, y: 3.0, w: W - 2*M, h: 0.9,
  fontSize: 28, fontFace: "Georgia", color: "F2E8DC", align: "center"
});
s1.addText([
  { text: "Name: Himani Gupta", options: { breakLine: true } },
  { text: "Roll No.: PGON26108", options: { breakLine: true } },
  { text: "Course Code: 2106" }
], {
  x: M, y: 4.2, w: W - 2*M, h: 1.5,
  fontSize: 16, fontFace: "Calibri", color: "D7CCC8", align: "center", lineSpacingMultiple: 1.5
});
s1.addNotes("Good morning/afternoon. Today I will present my Digital Innovation in Business project: a website designed for a fictional home-based bakery called Aaranya Bakehouse. I will walk you through the business concept, the website structure, design decisions, content strategy, SEO and future improvements.");

// ===== SLIDE 2: BUSINESS INTRODUCTION =====
const s2 = addLightSlide();
s2.addShape(pres.shapes.RECTANGLE, { x: M, y: M, w: W - 2*M, h: 0.08, fill: { color: ACCENT } });
s2.addText("Business Introduction", {
  x: M, y: 0.25, w: W - 2*M, h: 0.7,
  fontSize: 32, fontFace: "Georgia", color: PRIMARY, bold: true
});
s2.addText("Aaranya Bakehouse", {
  x: M, y: 1.1, w: W - 2*M, h: 0.6,
  fontSize: 22, fontFace: "Georgia", color: ACCENT, bold: true
});
s2.addText([
  { text: "Business concept: ", options: { bold: true, color: PRIMARY } },
  { text: "A proposed home-based bakery offering fresh, personalised baked products for celebrations and gifting.", options: { color: PRIMARY } }
], { x: M, y: 1.8, w: W - 2*M, h: 0.5, fontSize: 16, fontFace: "Calibri", color: PRIMARY });
s2.addText([
  { text: "Core offerings: ", options: { bold: true, color: PRIMARY } },
  { text: "Custom cakes, cupcakes, cookies and dessert boxes.", options: { color: PRIMARY } }
], { x: M, y: 2.35, w: W - 2*M, h: 0.5, fontSize: 16, fontFace: "Calibri", color: PRIMARY });
s2.addText([
  { text: "Target customers: ", options: { bold: true, color: PRIMARY } },
  { text: "People looking for customised bakes for birthdays, anniversaries, small events and gifting.", options: { color: PRIMARY } }
], { x: M, y: 2.9, w: W - 2*M, h: 0.5, fontSize: 16, fontFace: "Calibri", color: PRIMARY });
s2.addText([
  { text: "Business purpose: ", options: { bold: true, color: PRIMARY } },
  { text: "To provide a simple, warm and enquiry-based online presence that helps customers discover offerings and connect easily.", options: { color: PRIMARY } }
], { x: M, y: 3.45, w: W - 2*M, h: 0.5, fontSize: 16, fontFace: "Calibri", color: PRIMARY });
s2.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: M, y: 4.3, w: 3.5, h: 1.6, fill: { color: SURFACE },
  shadow: { type: "outer", color: "000000", blur: 4, offset: 2, angle: 135, opacity: 0.1 }
});
s2.addText("Home-based\nCustom bakery\nCelebration focus", {
  x: M + 0.2, y: 4.4, w: 3.1, h: 1.2,
  fontSize: 14, fontFace: "Calibri", color: PRIMARY, align: "center", valign: "middle"
});
s2.addNotes("Aaranya Bakehouse is a fictional home-based bakery. It offers custom cakes, cupcakes, cookies and dessert boxes. The target audience includes people planning birthdays, anniversaries and small celebrations. The business purpose is to provide a simple online presence where customers can discover products and send an enquiry.");

// ===== SLIDE 3: WEBSITE STRUCTURE =====
const s3 = addLightSlide();
s3.addShape(pres.shapes.RECTANGLE, { x: M, y: M, w: W - 2*M, h: 0.08, fill: { color: ACCENT } });
s3.addText("Website Structure", {
  x: M, y: 0.25, w: W - 2*M, h: 0.7,
  fontSize: 32, fontFace: "Georgia", color: PRIMARY, bold: true
});

const siteData = [
  [{ text: "Page", options: { fill: { color: PRIMARY }, color: "FFFFFF", bold: true, fontSize: 15 } },
   { text: "Purpose", options: { fill: { color: PRIMARY }, color: "FFFFFF", bold: true, fontSize: 15 } }],
  [{ text: "Home", options: { fontSize: 14 } }, { text: "Introduce the bakery, showcase categories and guide visitors to enquiry.", options: { fontSize: 14 } }],
  [{ text: "About Us", options: { fontSize: 14 } }, { text: "Share the business story, approach and core values.", options: { fontSize: 14 } }],
  [{ text: "Products / Services", options: { fontSize: 14 } }, { text: "Display the four core offerings and the 3-step custom-order process.", options: { fontSize: 14 } }],
  [{ text: "Contact Us", options: { fontSize: 14 } }, { text: "Provide contact details and a validated enquiry form.", options: { fontSize: 14 } }]
];
s3.addTable(siteData, {
  x: M, y: 1.2, w: W - 2*M,
  colW: [3.5, 8.5],
  border: { pt: 0.5, color: MUTED },
  fill: { color: "FFFFFF" },
  rowH: [0.5, 0.6, 0.6, 0.6, 0.6],
  fontFace: "Calibri", fontSize: 14, color: PRIMARY
});
s3.addText("Product categories under Products / Services: Custom Cakes, Cupcakes, Cookies, Dessert Boxes", {
  x: M, y: 4.4, w: W - 2*M, h: 0.5,
  fontSize: 14, fontFace: "Calibri", color: MUTED, italic: true
});
s3.addNotes("The website has four main pages: Home, About Us, Products/Services and Contact Us. The Home page introduces the brand and product categories. About Us tells the story and values. Products/Services explains each offering and a simple 3-step order process. Contact Us provides details and an enquiry form. The four product categories are Custom Cakes, Cupcakes, Cookies and Dessert Boxes.");

// ===== SLIDE 4: WEBSITE DEMONSTRATION =====
const s4 = addLightSlide();
s4.addShape(pres.shapes.RECTANGLE, { x: M, y: M, w: W - 2*M, h: 0.08, fill: { color: ACCENT } });
s4.addText("Website Demonstration", {
  x: M, y: 0.25, w: W - 2*M, h: 0.7,
  fontSize: 32, fontFace: "Georgia", color: PRIMARY, bold: true
});
s4.addText("Key pages and interactions shown in the completed website:", {
  x: M, y: 1.1, w: W - 2*M, h: 0.4,
  fontSize: 16, fontFace: "Calibri", color: MUTED
});

const demoData = [
  [{ text: "Page / Feature", options: { fill: { color: SURFACE }, bold: true, fontSize: 14 } },
   { text: "What to show", options: { fill: { color: SURFACE }, bold: true, fontSize: 14 } }],
  [{ text: "Home", options: { fontSize: 14 } }, { text: "Hero headline, featured categories and CTAs.", options: { fontSize: 14 } }],
  [{ text: "Navigation", options: { fontSize: 14 } }, { text: "Sticky header with working links on desktop and mobile.", options: { fontSize: 14 } }],
  [{ text: "Products / Services", options: { fontSize: 14 } }, { text: "Four product cards and the 3-step order process.", options: { fontSize: 14 } }],
  [{ text: "Contact / Enquiry", options: { fontSize: 14 } }, { text: "Contact details plus validated enquiry form.", options: { fontSize: 14 } }],
  [{ text: "Mobile view", options: { fontSize: 14 } }, { text: "Hamburger menu and responsive layout.", options: { fontSize: 14 } }]
];
s4.addTable(demoData, {
  x: M, y: 1.7, w: W - 2*M,
  colW: [3.5, 8.5],
  border: { pt: 0.5, color: MUTED },
  fill: { color: "FFFFFF" },
  rowH: [0.5, 0.55, 0.55, 0.55, 0.55, 0.55],
  fontFace: "Calibri", fontSize: 14, color: PRIMARY
});
s4.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: M, y: 4.7, w: W - 2*M, h: 1.0, fill: { color: SURFACE }
});
s4.addText("Note: Actual screenshots from the live website should be inserted here during final presentation preparation.", {
  x: M + 0.2, y: 4.85, w: W - 2*M - 0.4, h: 0.7,
  fontSize: 13, fontFace: "Calibri", color: MUTED, italic: true, align: "center", valign: "middle"
});
s4.addNotes("This slide should show actual screenshots from the live website. I will navigate through Home, Products/Services and Contact Us to demonstrate the CTAs, navigation and form. On mobile, the hamburger menu opens the navigation and the layout remains readable without horizontal scrolling.");

// ===== SLIDE 5: DESIGN DECISIONS =====
const s5 = addLightSlide();
s5.addShape(pres.shapes.RECTANGLE, { x: M, y: M, w: W - 2*M, h: 0.08, fill: { color: ACCENT } });
s5.addText("Design Decisions", {
  x: M, y: 0.25, w: W - 2*M, h: 0.7,
  fontSize: 32, fontFace: "Georgia", color: PRIMARY, bold: true
});

const designItems = [
  ["Colour palette", "Warm cream, cocoa brown, terracotta accent and soft beige. Used consistently for backgrounds, text and CTAs."],
  ["Typography", "Georgia for headings and Calibri for body text. Strong readability and clear hierarchy."],
  ["Logo / branding", "Simple original SVG wordmark with a warm bakery-inspired mark. Repeated in header and footer."],
  ["Visual hierarchy", "Clear hero section, card-based product display and numbered process steps."],
  ["Responsive design", "Mobile-first breakpoints, hamburger menu and fluid grids for tablet and phone."],
  ["CTA placement", "Primary CTAs placed in hero, product cards and final sections to guide users toward enquiry."]
];

let yPos = 1.15;
designItems.forEach(([title, desc]) => {
  s5.addShape(pres.shapes.OVAL, { x: M + 0.1, y: yPos + 0.05, w: 0.35, h: 0.35, fill: { color: ACCENT } });
  s5.addText(title, {
    x: M + 0.6, y: yPos, w: 3.2, h: 0.45,
    fontSize: 15, fontFace: "Calibri", color: PRIMARY, bold: true, valign: "middle"
  });
  s5.addText(desc, {
    x: M + 3.9, y: yPos, w: W - 2*M - 4.0, h: 0.45,
    fontSize: 14, fontFace: "Calibri", color: "3E2723", valign: "middle"
  });
  yPos += 0.65;
});
s5.addNotes("The colour palette uses warm cream, cocoa brown and terracotta to match a handcrafted bakery feel. Georgia and Calibri keep the typography readable and elegant. The logo is a simple SVG mark. Layouts use cards and clear sections. The site is responsive with a hamburger menu on mobile. CTAs are placed prominently to drive enquiry.");

// ===== SLIDE 6: CONTENT STRATEGY + POEM =====
const s6 = addLightSlide();
s6.addShape(pres.shapes.RECTANGLE, { x: M, y: M, w: W - 2*M, h: 0.08, fill: { color: ACCENT } });
s6.addText("Content Strategy & POEM", {
  x: M, y: 0.25, w: W - 2*M, h: 0.7,
  fontSize: 32, fontFace: "Georgia", color: PRIMARY, bold: true
});

s6.addText("Content Strategy", {
  x: M, y: 1.1, w: W - 2*M, h: 0.5,
  fontSize: 20, fontFace: "Georgia", color: ACCENT, bold: true
});
s6.addText([
  { text: "Concise, customer-focused copy across all pages.\n", options: { breakLine: true } },
  { text: "Four core categories presented clearly.\n", options: { breakLine: true } },
  { text: "Warm brand tone with enquiry-oriented CTAs.", options: {} }
], { x: M, y: 1.65, w: W - 2*M, h: 1.0, fontSize: 15, fontFace: "Calibri", color: PRIMARY });

s6.addText("POEM Strategy", {
  x: M, y: 2.8, w: W - 2*M, h: 0.5,
  fontSize: 20, fontFace: "Georgia", color: ACCENT, bold: true
});

const poemData = [
  [{ text: "Paid", options: { fill: { color: PRIMARY }, color: "FFFFFF", bold: true, fontSize: 14 } },
   { text: "Owned", options: { fill: { color: PRIMARY }, color: "FFFFFF", bold: true, fontSize: 14 } },
   { text: "Earned", options: { fill: { color: PRIMARY }, color: "FFFFFF", bold: true, fontSize: 14 } }],
  [{ text: "Targeted social media ads for local celebration audiences.", options: { fontSize: 14 } },
   { text: "Website and social profiles with product visuals and enquiry CTAs.", options: { fontSize: 14 } },
   { text: "Genuine reviews, recommendations and customer-shared celebration photos.", options: { fontSize: 14 } }]
];
s6.addTable(poemData, {
  x: M, y: 3.35, w: W - 2*M,
  colW: [4.1, 4.1, 4.1],
  border: { pt: 0.5, color: MUTED },
  fill: { color: "FFFFFF" },
  rowH: [0.5, 1.0],
  fontFace: "Calibri", fontSize: 14, color: PRIMARY
});
s6.addNotes("The content strategy uses concise, customer-focused copy and keeps the tone warm. CTAs guide visitors toward enquiry. The POEM strategy covers Paid media through targeted social ads, Owned media via the website and social profiles, and Earned media through genuine reviews and customer recommendations.");

// ===== SLIDE 7: SEO CONSIDERATIONS =====
const s7 = addLightSlide();
s7.addShape(pres.shapes.RECTANGLE, { x: M, y: M, w: W - 2*M, h: 0.08, fill: { color: ACCENT } });
s7.addText("SEO Considerations", {
  x: M, y: 0.25, w: W - 2*M, h: 0.7,
  fontSize: 32, fontFace: "Georgia", color: PRIMARY, bold: true
});

const seoItems = [
  ["Page titles", "Unique titles for each page, e.g., 'Aaranya Bakehouse | Custom Cakes & Celebration Bakes'."],
  ["Meta descriptions", "Concise descriptions summarising each page's purpose and offerings."],
  ["Headings", "One clear H1 per page with logical H2/H3 structure."],
  ["Keywords", "Natural use of target keywords: custom cakes, home bakery, cupcakes, dessert boxes, etc."],
  ["Internal links", "Descriptive navigation and CTA links across all pages."],
  ["Alt text", "Descriptive alt text for meaningful images and illustrations."]
];

yPos = 1.15;
seoItems.forEach(([title, desc]) => {
  s7.addShape(pres.shapes.OVAL, { x: M + 0.1, y: yPos + 0.05, w: 0.35, h: 0.35, fill: { color: ACCENT } });
  s7.addText(title, {
    x: M + 0.6, y: yPos, w: 2.8, h: 0.45,
    fontSize: 15, fontFace: "Calibri", color: PRIMARY, bold: true, valign: "middle"
  });
  s7.addText(desc, {
    x: M + 3.5, y: yPos, w: W - 2*M - 3.6, h: 0.45,
    fontSize: 14, fontFace: "Calibri", color: "3E2723", valign: "middle"
  });
  yPos += 0.65;
});
s7.addNotes("SEO was implemented through unique page titles, meta descriptions, semantic headings and natural keyword usage. Target keywords include custom cakes, home bakery, celebration cakes, cupcakes, cookies and dessert boxes. Internal navigation uses descriptive links, and meaningful images include descriptive alt text.");

// ===== SLIDE 8: FUTURE IMPROVEMENTS =====
const s8 = addLightSlide();
s8.addShape(pres.shapes.RECTANGLE, { x: M, y: M, w: W - 2*M, h: 0.08, fill: { color: ACCENT } });
s8.addText("Future Improvements & Learning", {
  x: M, y: 0.25, w: W - 2*M, h: 0.7,
  fontSize: 32, fontFace: "Georgia", color: PRIMARY, bold: true
});

s8.addText("Future Improvements", {
  x: M, y: 1.1, w: W - 2*M, h: 0.45,
  fontSize: 20, fontFace: "Georgia", color: ACCENT, bold: true
});
s8.addText([
  { text: "Add online ordering if demand grows.\n", options: { breakLine: true } },
  { text: "Expand customer review content as testimonials become available.\n", options: { breakLine: true } },
  { text: "Improve local SEO when a permanent service location is established.\n", options: { breakLine: true } },
  { text: "Use analytics to understand visitor behaviour.", options: {} }
], { x: M, y: 1.6, w: W - 2*M, h: 1.2, fontSize: 15, fontFace: "Calibri", color: PRIMARY });

s8.addText("Key Learning", {
  x: M, y: 2.9, w: W - 2*M, h: 0.45,
  fontSize: 20, fontFace: "Georgia", color: ACCENT, bold: true
});
s8.addText("I learned how to plan and build a small business website with responsive design, consistent branding, customer-focused content and basic SEO. The project also helped me understand how to structure a simple POEM-based digital marketing strategy around a clear enquiry journey.", {
  x: M, y: 3.4, w: W - 2*M, h: 1.1,
  fontSize: 15, fontFace: "Calibri", color: PRIMARY
});

s8.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: M, y: 4.7, w: W - 2*M, h: 1.0, fill: { color: SURFACE },
  shadow: { type: "outer", color: "000000", blur: 4, offset: 2, angle: 135, opacity: 0.1 }
});
s8.addText("Thank you! Questions welcome.", {
  x: M + 0.2, y: 4.85, w: W - 2*M - 0.4, h: 0.7,
  fontSize: 22, fontFace: "Georgia", color: PRIMARY, bold: true, align: "center", valign: "middle"
});
s8.addNotes("Future improvements include online ordering, customer reviews, local SEO and analytics. The main learning from this project was end-to-end website planning: from brand identity and responsive design to content strategy, SEO and a simple POEM marketing framework. Thank you for your time. I welcome any questions.");

// ===== SAVE =====
pres.writeFile({ fileName: "/Users/harshsinghal/.zcode/workspace/default/aaranya-bakehouse/presentation.pptx" })
  .then(() => console.log("Presentation created: presentation.pptx"))
  .catch(err => console.error(err));
