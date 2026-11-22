from kit import P, UL, OL, topic, callout, flow, chain, cols, tree, table, scale, svg, fig, grid

TITLE = "Week 14: Fever, inflammation, sepsis and rashes"
LEDE = "Why we get fevers and how to work one up at any age, what inflammation does, how sepsis kills, what goes wrong in immunodeficiency, and how to describe and recognize a rash."
LECTURES = ["Fever and hyperthermia (Mohammadi)", "Thermoregulation", "Approach to a paediatric patient with fever (Sirizzotti)", "Approach to fever in older adults (Diachun, Burrell)",
            "Fever in the immunocompromised host (Mohammadi)", "Basics of sepsis (Leeper, Champion)", "Pathology of acute inflammation", "Pathology of chronic inflammation",
            "Immunodeficiency", "Describing the rash (Bustamante)", "Rash ID: infectious diseases perspective (Mohammadi)", "Introduction to allergic rashes (Lee)"]

S_FEV = "Sources: Fever and Hyperthermia (Mohammadi), Thermoregulation, Nicole's Notes p. 127"
S_APP = "Sources: Fever and Hyperthermia (Mohammadi), Paediatric Fever (Sirizzotti), Approach to Fever in Older Adults (Diachun, Burrell), Nicole's Notes p. 128"

SETPOINT = """<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg"><style>.t{font-size:17px;fill:var(--muted)}.b{font-size:17px;font-weight:700}</style>
<line x1="40" y1="250" x2="620" y2="250" stroke="var(--faint)" stroke-width="2"/><line x1="40" y1="40" x2="40" y2="250" stroke="var(--faint)" stroke-width="2"/>
<text x="34" y="234" text-anchor="end" class="t">37°</text><text x="34" y="96" text-anchor="end" class="t">39°</text>
<path d="M40 230 H170 V90 H430 V230 H620" fill="none" stroke="var(--c2)" stroke-width="3" stroke-dasharray="9 7"/>
<path d="M40 230 H170 C230 230 235 95 305 92 H430 C480 92 490 228 565 230 H620" fill="none" stroke="var(--c)" stroke-width="4"/>
<text x="300" y="78" text-anchor="middle" class="b" style="fill:var(--c2)">Set point (dashed)</text>
<text x="300" y="120" text-anchor="middle" class="b" style="fill:var(--c)">Body temperature</text>
<text x="205" y="275" text-anchor="middle" class="t">Body below set point:</text><text x="205" y="295" text-anchor="middle" class="t">chills, shivering</text>
<text x="500" y="275" text-anchor="middle" class="t">Body above set point:</text><text x="500" y="295" text-anchor="middle" class="t">sweating, vasodilation</text>
<text x="170" y="60" text-anchor="middle" class="t">PGE2 raises it</text><text x="430" y="60" text-anchor="middle" class="t">cause removed</text>
</svg>"""

TABS = []

TABS.append(dict(key="fever", label="Fever and temperature",
    lede="How the body holds 37°C, how pyrogens reset the thermostat, and why fever and hyperthermia are different problems.",
    topics=[
    topic("Holding a steady temperature",
        P("Cells work best in a narrow temperature range, so core temperature is a tightly regulated variable. Normal oral temperature is 37°C, with a normal range of 35.5 to 37.7°C. It varies between people and through the day (peak about 2 PM, lowest about 4 AM), and with the menstrual cycle. No single value is the upper limit of normal."),
        P("The body has two thermal compartments: the <b>core</b> (<b>core = internal organs and muscles</b>) and the <b>shell</b> (<b>shell = skin and subcutaneous fat</b>). The shell's temperature swings so the core does not have to."),
        flow(("Sensors", "<b>Thermoreceptors</b> in skin, spinal cord, abdominal viscera and brain"), ("Integrating centre", "Hypothalamus. Anterior handles heat (front, fire). Posterior handles cold (back, brrr)."),
             ("Effectors", "Skin blood flow, sweat glands, muscle (shivering), brown fat, lungs, behaviour"), caption="Negative feedback loop for body temperature"),
        P("The body also uses a <b>Feedforward mechanism</b>: it acts in anticipation of a change, for example putting on a coat before going outside. Thermoregulation reaches adult levels after puberty (girls 13 to 14, boys 17 to 18)."),
        table(["Effector", "To make or keep heat", "To lose heat"],
              ["Brown adipose tissue (thyroid hormone)", "Thermogenesis on", "Off"],
              ["Skin blood flow (autonomic)", "Vasoconstriction", "Vasodilation"],
              ["Sweat glands (acetylcholine)", "Off", "Sweating"],
              ["Lungs", "Off", "Exhale warm air, panting"],
              ["Skeletal muscle", "Shivering (can be suppressed)", "Off"],
              ["Behaviour", "Curl up, seek heat, huddle", "Spread out, seek cool, air conditioning"]),
        P("Each 1°C rise in body temperature raises heart rate by about 4.4 beats per minute."),
        src=S_FEV),
    topic("What makes a fever",
        P("<b>Fever</b> is a raised core temperature from an increase in the hypothalamic set point. It is often, but not always, part of host defence. Fever slows the growth of many microbes, boosts antibody production and stimulates innate and adaptive immunity."),
        flow(("Trigger", "Infection, inflammation (gout, cancer, vasculitis), tissue injury, cell death. <b>Exogenous pyrogens</b> such as LPS (lipid A) from gram-negatives."),
             ("<b>Endogenous pyrogens</b>", "IL-1, IL-6, TNF-α, IFN-γ"),
             ("PGE2", "Made in the hypothalamus. Directly raises the set point."),
             ("Heat conservation", "Vasoconstriction, shivering, heat-seeking, noradrenaline, thyroid hormone"),
             caption="The fever pathway"),
        svg(SETPOINT, caption="When the set point jumps, you feel cold and shiver until your body catches up. When it drops, you sweat.", label="Graph of set point and body temperature over time: set point rises, body temperature lags behind with chills, then set point falls and body temperature drops with sweating."),
        P("<b>Cryogens</b> (anti-inflammatory cytokines, hormones, neuroendocrine products) pull the temperature back down and protect against runaway fever. <strong>Antipyretics</strong> (acetaminophen, NSAIDs such as ibuprofen and aspirin) block cyclooxygenase (COX), so less PGE2 is made and the set point falls."),
        callout("trap", P("The mediator that <strong>directly</strong> raises the set point is <strong>PGE2</strong>, not IL-1 or TNF. The cytokines act upstream by triggering PGE2.")),
        src=S_FEV),
    topic("Fever versus hyperthermia",
        cols(("Fever", UL("Set point is <strong>reset upward</strong>", "Heat production and loss work normally", "Rarely exceeds 41°C", "Responds to antipyretics", "Causes: infection, inflammation, trauma")),
             ("Hyperthermia", UL("Set point is <strong>normal</strong>", "Heat gain beats heat loss: too much heat made or taken in, too little lost", "Can exceed 41°C. No normal daily swing", "No response to antipyretics", "Causes: heat stroke, exercise, drugs")),
             caption="Same thermometer reading, different mechanism"),
        callout("clin", P("Antipyretics are safe at recommended doses. Acetaminophen is hepatotoxic in overdose, NSAIDs cause GI irritation and bleeding. Avoid routine alternating or combining them, which causes dosing errors. Tepid sponging only after medication, and avoid causing shivering. Always look for the cause.")),
        src=S_FEV),
    topic("Defining and classifying fever",
        table(["Who", "Fever is"],
              ["Children", "38.0°C rule of thumb. Rectal is the gold standard"],
              ["Adults", "Early morning (6 AM) oral or tympanic <b>37.2</b>°C or more, or any oral or tympanic <b>37.8</b>°C or more. About 38°C is used clinically"],
              ["Frail older adults", "Single oral above 37.8°C, persistent oral or tympanic 37.2°C or more, or a rise of 1.1°C or more over baseline"]),
        table(["By", "Categories"],
              ["Onset", "Acute (under 7 days): viral, skin, UTI, pneumonia. Subacute (1 to 2 weeks): intra-abdominal abscess. Chronic (over 2 weeks): TB, HIV, cancer, SLE"],
              ["Height", "Low above 37°C, moderate 38 to 39°C, high grade above 39°C"],
              ["Pattern", "Continuous, intermittent, remittent"]),
        P("<b>Fever of unknown origin</b>: 101°F or more on several occasions, with no cause after an appropriate initial workup. Think occult infection, malignancy (lymphoma, leukemia) and connective tissue disease (SLE, vasculitis)."),
        src=S_FEV),
    ],
    notes=[16, 17],
    recall=[("Which mediator directly raises the hypothalamic set point?", "Prostaglandin E2 (PGE2)."),
            ("Fever versus hyperthermia: what happens to the set point?", "Fever raises the set point. In hyperthermia the set point is normal but heat gain beats heat loss."),
            ("Which part of the hypothalamus handles heat?", "Anterior (front, fire). Posterior handles cold."),
            ("Define fever in an adult.", "Early morning oral or tympanic 37.2°C or more, or any 37.8°C or more."),
            ("How do antipyretics work?", "They inhibit COX, so less PGE2 is made."),
            ("Why do you shiver at the start of a fever?", "The set point jumps above your body temperature, so the body conserves and makes heat until it catches up.")]))

TABS.append(dict(key="approach", label="Approach to fever",
    lede="One framework for every febrile patient, then what changes for children, infants and frail older adults.",
    topics=[
    topic("The framework",
        flow(("Safety", "Routine practices plus the right additional precautions and PPE for the suspected pathogen"),
             ("Stable?", "ABCs, vitals, sepsis screen. If unstable: IV fluids, lactate, blood cultures, antibiotics"),
             ("History", "Fever story, localizing symptoms, host factors, exposures"),
             ("Exam", "Head to toe, finish with the infected area"),
             ("Differential", "By site, by context"),
             ("Investigate and treat", "Targeted tests, early management, reassess"), caption="Approach to a patient with fever"),
        cols(("<b>qSOFA</b> (adults)", UL("Respiratory rate 22 or more", "Systolic BP 100 or less", "Altered mentation", "<strong>2 or more = high risk</strong>")),
             ("<b>SIRS</b> (used in paediatrics)", UL("Temperature below 36 or above 38°C", "Heart rate above 90", "Respiratory rate above 20", "WBC above 12,000, below 4,000 or over 10% bands", "<strong>2 or more = SIRS</strong>")),
             caption="Sepsis screens"),
        src=S_APP),
    topic("Taking the history",
        UL("<strong>Fever story</strong>: how high, how measured, how long, pattern, response to antipyretics, rigors, what came with it.",
           "<strong>Localizing symptoms</strong>: cough, dysuria, rash, joint pain, neck stiffness, ear pain.",
           "<strong>General symptoms</strong>: weight loss, night sweats, arthralgia (think malignancy or autoimmune).",
           "<strong>Host factors</strong>: immunocompromise (HIV, splenectomy, steroids, chemo), devices and procedures (lines, catheters).",
           "<strong>Exposures</strong>: sick contacts (daycare counts), food and water (well water, unpasteurized milk, raw meat), travel and chemoprophylaxis, occupation (TB, zoonoses), animals, sexual history, drug use, time of year, MRSA risk factors."),
        P("MRSA risk factors: long-term care, crowded housing, people who inject drugs, men who have sex with men, frequent antibiotics, contact with a carrier, indwelling lines."),
        src=S_APP),
    topic("Fever plus a clue: building the differential",
        table(["Fever plus", "Think of"],
              ["Rash", "Viral exanthems (measles, EBV), meningococcemia, RMSF, syphilis, drug reaction"],
              ["GI symptoms", "Enteric fever, hepatitis, <em>C. difficile</em>, liver abscess, cholangitis, typhlitis"],
              ["Respiratory", "CAP or HAP, TB, influenza, fungal pneumonia (histoplasmosis)"],
              ["Travel", "Malaria, dengue, typhoid, chikungunya, schistosomiasis, leishmaniasis"],
              ["Indwelling device", "CLABSI, CAUTI, VAP, prosthetic joint infection, endocarditis"],
              ["Immunocompromise", "Neutropenic fever, CMV, PJP, invasive candidiasis, HHV-6"],
              ["No source (FUO)", "Occult infection, lymphoma or leukemia, SLE, vasculitis"]),
        cols(("Rash on palms and soles: <b>CaRS</b>", P("<strong>C</strong>oxsackie, <strong>R</strong>ocky Mountain spotted fever, <strong>S</strong>yphilis")),
             ("Fever emergencies", P("RMSF, meningococcemia, necrotizing fasciitis, toxic shock (staph, GAS), endocarditis"))),
        table(["Alarm feature", "Consider"],
              ["Very high fever (over 105.8°F)", "CNS infection, NMS, heat stroke"],
              ["Rash", "Meningitis, bacteremia with septic shock, rickettsia, endocarditis"],
              ["Altered mental status", "Meningitis, encephalitis, NMS, heat stroke, septic shock"],
              ["Dizziness", "Septic shock, adrenal insufficiency, PE"],
              ["Recent chemotherapy", "Neutropenic infection"],
              ["Dyspnea and chest pain", "PE, pneumonia, empyema"]),
        P("Non-infectious causes: inflammatory and malignant disease (SLE, lymphoma), drugs (bleomycin, interferon), thrombosis, thyroid, and factitious fever."),
        src=S_APP),
    topic("Investigations and treatment",
        callout("key", P("<b>ALWAYS SEND 2 SETS FOR BLOOD CULTURES</b>. Then target tests to the history and exam. A well patient with an obvious viral illness may need no tests at all.")),
        cols(("Basic tests", UL("<b>CBC</b>, creatinine, electrolytes, liver enzymes", "<b>C-reactive protein</b> (and ESR), lactate", "Blood cultures × 2", "Urinalysis and culture", "CXR if respiratory symptoms")),
             ("Targeted", UL("LP if altered LOC or meningismus", "Abdominal US or CT if abdominal signs", "PCR or antigen for influenza, RSV, COVID", "Arthrocentesis, paracentesis, bronchoscopy by site", "RF, ANA, ANCA, TSH, dopplers or CTPA if non-infectious"))),
        P("If septic: fluids and empiric antibiotics right after cultures. With a clear source, start narrow. Add supportive care (antipyretics, oxygen, monitoring) and reassess often."),
        callout("clin", P("A 13-year-old has 6 to 7 days of fever and frontal headache despite amoxicillin for sinusitis, with a mildly positive jolt sign. Think meningitis: LP, CT of brain and sinuses, and start meningitis treatment.")),
        src=S_APP),
    topic("Children: not little adults",
        P("Fever is a symptom, not a diagnosis. Most fevers are not dangerous and need treatment only if the child is uncomfortable. Ask parents how they measured it: many rely on touch. Rectal is the gold standard."),
        callout("trap", UL("<strong>When to worry</strong>: the child looks septic, is an infant, has constitutional symptoms, is neutropenic or immunocompromised, or has had fever for 5 days.")),
        P("The history adds prenatal history (TORCH infections: toxoplasma, other such as VZV, parvovirus B19 and HIV, rubella, CMV, HSV), birth history (maternal fever, rupture of membranes over 18 h, chorioamnionitis, GBS status), immunizations and development. Paediatric vitals vary with age, and fever alone raises the heart rate. Examine from afar first, start with the heart while they are quiet, end with the ears."),
        cols(("Kawasaki disease: <b>CRASH & Burn</b>", P("Fever 5 days plus 4 of 5: <strong>C</strong>onjunctivitis (non-purulent), <strong>R</strong>ash, <strong>A</strong>denopathy (cervical, often one side), <strong>S</strong>trawberry tongue, <strong>H</strong>ands (red, swollen palms and soles). Risk: coronary artery aneurysm.")),
             ("MIS-C", P("A post-COVID inflammatory syndrome in children. Fever is the hallmark. Three patterns: fever with hyperinflammation, Kawasaki-like, and shock."))),
        src=S_APP),
    topic("Infants: the full septic workup",
        P("Infants cannot tell you what hurts and often look well with a serious infection, so the threshold for a workup is lower. A febrile UTI in a child is by definition pyelonephritis. Children under 3 with fever and no source need a urinalysis and culture, by catheter or suprapubic aspiration if not toilet trained."),
        flow(("Blood", "Culture + CBC"), ("CSF", "Culture, cell count, glucose, protein, ± viral PCR (HSV, enterovirus)"), ("Urine", "Culture + urinalysis"), ("± CXR", ""),
             ("Empiric antibiotics", "Cover <strong>LEG</strong>: Listeria, E. coli, group B strep"), caption="Full septic workup (FSWU)"),
        callout("clin", P("Skye, a young infant, has fever 38.3°C and 2 days of poor feeding but looks well. Mom was GBS positive. Full septic workup and empiric antibiotics: blood and CSF grew group B strep within 24 h.")),
        src=S_APP),
    topic("Frail older adults: fever may be missing",
        P("Aging weakens barriers (skin, lungs, gut), cellular and humoral immunity, cytokine and antibody production, and vaccine responses. Comorbidities like diabetes add to it. Urethral shortening and vaginal atrophy raise UTI risk."),
        callout("trap", P("<strong>Fever is absent in 30 to 50% of frail older adults with infection</strong>, even serious infection. These patients do worse. No fever does not rule out infection.")),
        UL("Infection often presents atypically, as <strong>delirium or falls</strong>, sometimes with no localizing symptoms.", "Get a collateral history when there is delirium or cognitive impairment.",
           "Ask about pneumococcal, influenza, shingles and COVID vaccines.", "Add functional history (ADLs, IADLs)."),
        callout("key", P("A positive urine culture is not a UTI. Asymptomatic bacteriuria is common in older adults and is not treated unless there are urinary symptoms (dysuria, frequency, urgency, suprapubic pain, fever, CVA tenderness). Nicole's Notes: do not do a urinalysis in patients over 65.")),
        callout("clin", P("Pearl, 89, has 2 days of delirium with T 37.7. The source turns out to be a red, hot, swollen knee after a tooth extraction: aspirate the joint and draw blood cultures. Her E. coli in the urine, without urinary symptoms, is asymptomatic bacteriuria.")),
        src=S_APP),
    ],
    notes=[18],
    recall=[("Name the qSOFA criteria.", "Respiratory rate 22 or more, systolic BP 100 or less, altered mentation. 2 or more is high risk."),
            ("What does CaRS stand for?", "Rashes on palms and soles: Coxsackie, Rocky Mountain spotted fever, syphilis."),
            ("Kawasaki criteria?", "Fever 5 days plus 4 of: conjunctivitis, rash, adenopathy, strawberry tongue, hand changes. Risk of coronary aneurysm."),
            ("What does a full septic workup include?", "Blood culture and CBC, CSF studies, urine culture and urinalysis, ± CXR, then empiric antibiotics for Listeria, E. coli and GBS."),
            ("How often is fever absent in frail older adults with infection?", "30 to 50% of the time."),
            ("How many blood culture sets?", "Always 2.")]))

S_INF = "Sources: Pathology of Acute Inflammation and Pathology of Chronic Inflammation (Walsh), Nicole's Notes pp. 129, 149"
S_SEP = "Sources: The Basics of Sepsis (Champion, Leeper), Nicole's Notes p. 141"

import math, random  # noqa: E402


def _granuloma():
    random.seed(4)
    cx, cy = 210, 160
    o = ['<svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg"><style>.l{font-size:19px;fill:var(--ink)}.s{font-size:16px;fill:var(--muted)}</style>']
    for i in range(64):  # T cell rim
        a = i / 64 * 2 * math.pi + random.random() * .05; r = 138 + random.random() * 10
        o.append(f'<circle cx="{cx+r*math.cos(a):.0f}" cy="{cy+r*math.sin(a):.0f}" r="6" fill="var(--c2)"/>')
    for i in range(26):  # epithelioid histiocytes
        a = i / 26 * 2 * math.pi; r = 100
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        o.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="16" ry="8" transform="rotate({math.degrees(a)+90:.0f} {x:.0f} {y:.0f})" fill="#e9c7b4" stroke="#b9876d" stroke-width="1.2"/>')
    o.append(f'<circle cx="{cx}" cy="{cy}" r="72" fill="#f3e3b5" stroke="#d2b46a" stroke-width="2"/>')
    o.append(f'<text x="{cx}" y="{cy+6}" text-anchor="middle" class="s" style="fill:#6b5310">caseous necrosis</text>')
    gx, gy = cx - 30, cy + 95
    o.append(f'<ellipse cx="{gx}" cy="{gy}" rx="34" ry="20" fill="#e9c7b4" stroke="#b9876d" stroke-width="1.5"/>')
    for k in range(7):
        a = math.pi + k / 6 * math.pi
        o.append(f'<circle cx="{gx+26*math.cos(a):.0f}" cy="{gy+13*math.sin(a)+4:.0f}" r="4" fill="#7a4b9a"/>')
    labels = [((cx + 145, cy - 55), "Rim of T lymphocytes", 60), ((cx + 100, cy - 10), "Epithelioid histiocytes", 140), ((cx + 50, cy + 30), "Central necrosis (TB classic)", 220), ((gx + 34, gy), "Multinucleate giant cell", 285)]
    for (x, y), t, ty in labels:
        o.append(f'<line x1="{x}" y1="{y}" x2="400" y2="{ty-6}" stroke="var(--faint)" stroke-width="1.5"/><text x="408" y="{ty}" class="l">{t}</text>')
    o.append("</svg>")
    return "".join(o)


TABS.append(dict(key="inflam", label="Inflammation",
    lede="Acute inflammation is neutrophils and fluid. Chronic inflammation is macrophages, lymphocytes and repair. Granulomas are a special chronic pattern with a short list of causes.",
    topics=[
    topic("The cardinal signs, and why each happens",
        table(["Sign", "Meaning", "Why"],
              ["<b>Rubor</b>", "Redness", "Vasodilation and more blood flow"],
              ["<b>Calor</b>", "Heat", "Warm core blood reaching the cooler skin"],
              ["<b>Dolor</b>", "Pain", "Chemical mediators stimulate sensory nerve endings"],
              ["<b>Tumor</b>", "Swelling", "Fluid builds up in the tissue"],
              ["<b>Functio laesa</b>", "Loss of function", "Added later by Virchow"]),
        cols(("Under the naked eye", UL("Swelling (edema)", "Pus or exudate", "Congested vessels", "Redness")),
             ("Under the microscope", UL("Neutrophils (pus), recognized by multilobed nuclei", "Neutrophil margination along vessel walls", "Edema")),
             caption="Features of acute inflammation"),
        src=S_INF),
    topic("Four types of acute inflammation",
        tree("Acute inflammation", [("Purulent (suppurative)", "Pus made of neutrophils, from <b>pyogenic bacteria</b> like <em>Staphylococcus</em> that cause liquefactive necrosis. Appendicitis, abscesses."),
                                    ("Fibrinous", "Vessels get leaky enough to let fibrinogen out, so fibrin coats a space: pleura, pericardium, meninges. Pericarditis after MI."),
                                    ("Serous", "Cell-poor fluid. Pleura or pericardium = <b>effusion</b>. Peritoneum = <b>ascites</b>. Skin = <b>bulla/blister</b>."),
                                    ("Ulcer", "A hole through a mucosal surface: skin, mouth (canker sore), stomach and duodenum (peptic ulcer, <em>H. pylori</em>), colon (IBD), diabetic foot.")]),
        P("An <b>Abscess</b> is pus walled off in a cavity made by tissue destruction. Common sites: skin (groin, axilla, perianal), next to teeth, around the bowel (ruptured diverticulum) and lung."),
        callout("key", P("Antibiotics struggle to reach an abscess: it is walled off and its necrotic centre has no blood vessels. Treat skin abscesses with <strong>incision and drainage</strong>. Deep abscesses may need surgery.")),
        P("<b>Fibrinous pericarditis</b> can follow MI (Dressler syndrome) or cardiac surgery, or occur with uremia or SLE."),
        callout("clin", P("Ruby, 26, has periumbilical pain moving to the right lower quadrant, McBurney point tenderness and a WBC of 15.4. CT shows a swollen, fluid-filled appendix: acute (purulent) appendicitis.")),
        src=S_INF),
    topic("Chronic inflammation",
        P("<b>Chronic inflammation</b> has been present for weeks or months and usually comes with attempts at tissue repair. Neutrophils are not usually a feature, although acute and chronic inflammation can coexist."),
        cols(("<b>persistent infection</b> / <b>injury</b>", P("TB")), ("<b>hypersensitivity</b>", P("Rheumatoid arthritis, asthma, IBD")), ("Chronic exposure to <b>toxins</b>", P("Silicosis, atherosclerosis")), caption="Three causes"),
        table(["Cell", "Role", "How to spot it"],
              ["<b>Macrophages</b>", "Dominant cell in many chronic reactions", ""],
              ["<b>Eosinophils</b>", "Allergy and parasites. Major basic protein kills parasites but also damages host epithelium", "Bright red granules, bilobed nucleus"],
              ["<b>Lymphocytes</b>", "T, B and NK cells. Release cytokines that sustain inflammation", "Almost all purple nucleus, thin rim of cytoplasm"],
              ["<b>Plasma cells</b>", "Differentiated B cells that make antibodies", "Eccentric \"clock face\" nucleus"]),
        P("<b>Nasal polyps</b> are soft, painless, benign growths that can follow repeated rhinitis. <b>Allergic rhinitis</b> is a type I, IgE-mediated reaction, so the polyps are full of eosinophils and plasma cells with edematous stroma."),
        src=S_INF),
    topic("Granulomas",
        P("A <b>Granuloma</b> is an aggregation of <b>macrophages surrounded by T lymphocytes</b>. It is the body's attempt to wall off something it cannot clear: a foreign body (talc in IV drug use, sutures), a persistent microbe (TB) or a self antigen."),
        svg(_granuloma(), caption="Anatomy of a caseating granuloma", label="Cross section of a granuloma: central caseous necrosis, a ring of epithelioid histiocytes, a multinucleate giant cell, and an outer rim of T lymphocytes."),
        UL("Activated macrophages fill with cytoplasm and look like epithelial cells: <b>epithelioid histiocytes</b>. Their nuclei can look like footprints in the sand.",
           "Several macrophages can fuse into <b>multinucleate giant cells</b> (<b>Langhan's cells</b>).",
           "The T cell rim releases cytokines that recruit and activate more macrophages.",
           "A chalky, cheesy centre is <strong>caseating (necrotizing)</strong> necrosis from hypoxia and free radical injury. It is classic for TB but not exclusive to it.",
           "Common sites: lungs, lymph nodes, GI tract."),
        cols(("Infectious causes", UL("Mycobacterial (TB)", "Fungal (histoplasmosis)", "Bacterial (cat scratch disease)")),
             ("Non-infectious causes", UL("Sarcoidosis", "Vasculitis", "Crohn's disease", "Foreign body reaction", "Malignancy")),
             caption="Differential for granulomas on a pathology report"),
        callout("trap", P("<b>Make sure the patient does not have TB before starting an immunosuppressive treatment</b> for a non-infectious granulomatous disease.")),
        src=S_INF),
    ],
    notes=[19, 20, 58, 59, 60],
    recall=[("What causes calor?", "Warm core blood entering the cooler skin."),
            ("Pleural effusion is which type of acute inflammation?", "Serous."),
            ("Why drain an abscess instead of relying on antibiotics?", "It is walled off with an avascular necrotic centre, so antibiotics cannot reach it."),
            ("Define a granuloma.", "Activated macrophages (epithelioid histiocytes, giant cells) surrounded by a rim of T lymphocytes."),
            ("List three non-infectious causes of granulomas.", "Sarcoidosis, vasculitis, Crohn's disease, foreign body reaction, malignancy."),
            ("Which cell is NOT typical of chronic inflammation?", "The neutrophil.")]))

TABS.append(dict(key="sepsis", label="Sepsis",
    lede="Sepsis is the body's own response to infection running out of control. It is common, deadly and an emergency. Recognize it early and give antibiotics fast.",
    topics=[
    topic("What sepsis is",
        callout("key", P("<b>Sepsis</b>: a life-threatening organ dysfunction caused by a dysregulated host response to infection (Sepsis-3).")),
        flow(("Infection", "Bacteria, viruses or fungi"), ("Dysregulated response", "Pro- and anti-inflammatory mediators lose balance. Effects go systemic."),
             ("<b>microcirculation dysfunction</b>", "Arteriolar and capillary networks fail, cells are injured"), ("<b>multiple organ dysfunction</b> (<b>MODS</b>)", "Any or all organs"), caption="From infection to organ failure"),
        tree("Organs that fail in sepsis", [("Cardiovascular", "Low BP, high HR, myocardial dysfunction"), ("Respiratory", "Low oxygen, ARDS"), ("Brain", "Confusion, delirium"),
                                            ("Coagulation", "Low platelets, DIC"), ("Kidney", "Oliguria, AKI"), ("Liver, muscle, nerves", "")]),
        P("Organ dysfunction is measured with the SOFA score (Sequential Organ Failure Assessment). Mortality is 30 to 40% or more. Many targeted therapies have failed (activated protein C, anti-TNF, anti-endotoxin, vitamin C and more), so treatment still relies on antibiotics, source control, support and the patient's own immune system."),
        src=S_SEP),
    topic("Septic shock",
        P("<b>Septic shock</b> is low blood pressure that does not respond to fluids. Two things drop the pressure: arterioles <b>vasodilate</b>, and fluid leaks out of vessels into the interstitium. More fluid just leaks out (edema), so vasopressors are added to squeeze the vessels and raise the BP."),
        src=S_SEP),
    topic("Recognizing sepsis",
        cols(("Vital signs", UL("Temperature high or low", "Tachycardia", "Tachypnea", "Low BP", "Warm, flushed skin")),
             ("qSOFA", UL("RR over 22", "Altered mentation", "Systolic BP under 100")),
             ("Find the source", UL("Cough, crackles: pneumonia", "Tender distended abdomen: abdominal sepsis", "Track marks, abscess: bacteremia")),
             caption="Recognize it, then look for the cause"),
        table(["Pillar of early detection", "Clues"],
              ["<b>Physiology</b>", "Tachypnea and hypoxia, tachycardia and hypotension, oliguria"],
              ["<b>Symptomatology</b>", "Rapid decline in function, family is worried, new confusion, looks very unwell"],
              ["<b>High risk factor populations</b>", "Recent surgery, recent chemotherapy, immunosuppressed, elderly"]),
        src=S_SEP),
    topic("The chain of survival",
        flow(("Early recognition", "Have a plan to NOT miss sepsis, wherever you work"),
             ("Early antibiotics", "Broad spectrum, often several drugs. Cultures first only if they will not delay antibiotics"),
             ("Source control", "Find it (exam, CT, US). Fix it: surgery, drainage, remove infected lines or implants"),
             ("Life support", "Vasopressors, inotropes, ventilation, prone positioning, ECMO, dialysis or CRRT, sedation"),
             caption="Four links that save lives"),
        callout("why", P("<strong>Nothing saves lives in sepsis like early, appropriate antibiotics.</strong> From the onset of hypotension, mortality rises about <b>8%</b> for every hour antibiotics are delayed. Do whatever it takes to get the drug into the blood.")),
        P("Life support does not fix the problem. It buys time for antibiotics and source control to work."),
        src=S_SEP),
    topic("Three classic cases",
        table(["Case", "Red flags", "Antibiotics", "Source control and support"],
              ["23-year-old, a scratch while wading in a lake, rapidly spreading hot, red, painful leg. HR 101", "Tachycardia, spread too fast for simple cellulitis. Blood culture: invasive GAS (necrotizing infection)", "Vancomycin + pip-tazo + clindamycin, plus IVIG", "Emergency surgical debridement. Vasopressors for distributive shock, lung-protective ventilation for ARDS"],
              ["63-year-old, day 2 after aortic aneurysm repair, severe LLQ pain, dark bloody stools. HR 120, BP 88/50", "Shock, bloody diarrhea, peritoneal signs (ischemic bowel)", "Piperacillin-tazobactam", "Endoscopy to diagnose, emergency resection. Vasopressors, CRRT for AKI"],
              ["63-year-old smoker, cough and dyspnea. T 39.2, RR 36, BP 96/54, sat 85% on 50% mask", "Tachypnea, hypoxia, hypotension: community-acquired pneumonia", "Ceftriaxone + azithromycin", "Blood cultures, CXR, oxygen and ventilation, vasopressors"]),
        src=S_SEP),
    ],
    notes=[42, 43],
    recall=[("Define sepsis.", "Life-threatening organ dysfunction caused by a dysregulated host response to infection."),
            ("Define septic shock.", "Low blood pressure that does not respond to fluids."),
            ("Why is BP low in septic shock?", "Arteriolar vasodilation and loss of fluid from vessels into the interstitium."),
            ("How much does mortality rise per hour of antibiotic delay after hypotension?", "About 8% per hour."),
            ("Name the four links in the sepsis chain of survival.", "Early recognition, early antibiotics, source control, life support."),
            ("What is the mortality of sepsis?", "30 to 40% or more.")]))

S_IMM = "Sources: Approach to Immunodeficiency (Kuprowski), Fever in the Immunocompromised Host (Mohammadi), Nicole's Notes pp. 143 to 144, 152 to 153"

HIVCOURSE = """<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg"><style>.t{font-size:17px;fill:var(--muted)}.b{font-size:17px;font-weight:700}</style>
<line x1="40" y1="250" x2="620" y2="250" stroke="var(--faint)" stroke-width="2"/>
<line x1="40" y1="30" x2="40" y2="250" stroke="var(--faint)" stroke-width="2"/>
<line x1="130" y1="30" x2="130" y2="250" stroke="var(--line)" stroke-dasharray="4 5"/><line x1="500" y1="30" x2="500" y2="250" stroke="var(--line)" stroke-dasharray="4 5"/>
<line x1="40" y1="200" x2="620" y2="200" stroke="var(--bad)" stroke-width="1.5" stroke-dasharray="6 5"/><text x="612" y="193" text-anchor="end" class="t" style="fill:var(--bad)">CD4 200: PJP risk</text>
<path d="M40 50 C70 50 80 140 100 130 C115 122 125 85 145 80 C250 95 400 150 500 205 C540 225 580 240 620 245" fill="none" stroke="var(--c2)" stroke-width="4"/>
<path d="M40 245 C60 245 75 60 95 55 C110 52 120 150 150 170 C300 175 420 165 500 140 C550 110 590 70 620 50" fill="none" stroke="var(--c)" stroke-width="4"/>
<text x="230" y="112" class="b" style="fill:var(--c2)">CD4 T cells</text><text x="250" y="190" class="b" style="fill:var(--c)">Viral load</text>
<text x="85" y="275" text-anchor="middle" class="t">Acute</text><text x="85" y="295" text-anchor="middle" class="t">~1 month</text>
<text x="315" y="275" text-anchor="middle" class="t">Clinical latency</text><text x="315" y="295" text-anchor="middle" class="t">median ~8 years</text>
<text x="560" y="275" text-anchor="middle" class="t">AIDS</text><text x="560" y="295" text-anchor="middle" class="t">~2 years</text>
</svg>"""

TABS.append(dict(key="immuno", label="Immunodeficiency",
    lede="Spot a patient with too many infections, work out which arm of the immune system is broken from the bugs and the age, then know the secondary causes, HIV and how to handle fever in these patients.",
    topics=[
    topic("When to suspect it",
        P("<b>Immunodeficiency</b> is when the pathways that remove pathogens are disrupted. <strong>Primary</strong> immunodeficiency comes from germline mutations. <strong>Secondary</strong> immunodeficiency comes from infection (HIV), medication (rituximab) or malignancy."),
        P("The clue is <strong>more infections than expected for the patient's age</strong>. Screen with the 10 warning signs. Two or more warrants a closer look."),
        table(["Children (up to 18)", "Adults (18+)"],
              ["4+ new ear infections in 1 year", "2+ new ear infections in 1 year"],
              ["2+ serious sinus infections in 1 year", "2+ new sinus infections in 1 year, <strong>in the absence of allergy</strong>"],
              ["2+ pneumonias in 1 year", "1 pneumonia per year for more than 1 year"],
              ["2+ deep-seated infections, including septicemia", "Recurrent viral infections (colds, herpes, warts, condyloma)"],
              ["2+ months on antibiotics with little effect", "Infection with normally harmless TB-like bacteria"],
              ["Need for IV antibiotics", "Recurrent need for IV antibiotics"],
              ["Infant fails to gain weight or grow", "Chronic diarrhea with weight loss"],
              ["Recurrent deep skin or organ abscesses", "Recurrent deep skin or organ abscesses"],
              ["Persistent thrush or skin fungal infection", "Persistent thrush or skin fungal infection"],
              ["Family history of primary immunodeficiency", "Family history of primary immunodeficiency"], cls="plain"),
        src=S_IMM),
    topic("Which arm is broken? Read the age and the bugs",
        P("Each part of the immune system guards against different microbes, so the pattern of infections points to the defect."),
        cols(("Phagocytes", UL("<strong>Onset</strong>: infancy, early childhood", "<strong>Bugs</strong>: <em>S. aureus</em>, <em>Pseudomonas</em>, <em>Serratia</em>, <em>Klebsiella</em>, <em>Candida</em>, <em>Nocardia</em>, <em>Aspergillus</em>", "<strong>Clues</strong>: abscesses, granulomas, poor wound healing, mouth and anorectal infections")),
             ("Complement", UL("<strong>Onset</strong>: any age", "<strong>Bugs</strong>: <em>Neisseria</em> (meningococcus, gonococcus), encapsulated bacteria", "<strong>Clues</strong>: autoimmunity (RA, lupus, scleroderma)")),
             ("T cells", UL("<strong>Onset</strong>: first 6 months", "<strong>Bugs</strong>: opportunists. Mycobacteria, CMV, EBV, VZV, enterovirus, <em>Candida</em>, PJP", "<strong>Clues</strong>: failure to thrive, thrush, severe eczema, GVHD from mom's T cells, disseminated BCG after vaccination")),
             ("B cells (antibody)", UL("<strong>Onset</strong>: after 6 months (maternal antibody wanes) or adulthood", "<strong>Bugs</strong>: encapsulated bacteria (<em>H. influenzae</em>, pneumococci, streptococci), <em>Giardia</em>, enterovirus", "<strong>Clues</strong>: recurrent sinus, ear and lung infections, chronic diarrhea, autoimmunity")),
             caption="Primary immunodeficiency by arm"),
        callout("key", UL("Most common innate (phagocytic) disorder: <strong>chronic granulomatous disease</strong>.", "Most severe: <strong>T cell</strong> defects (SCID). No T cells means no adaptive immunity.",
                          "Most common overall: <strong>selective IgA deficiency</strong> (1 in 400), and it is the mildest.", "Most common primary immunodeficiencies are humoral, and milder than T cell disorders.", "Most common in practice: <strong>secondary</strong> immunodeficiency.")),
        src=S_IMM),
    topic("Innate defects: phagocytes and complement",
        flow(("Breach", "Bacteria get past the skin"), ("Meet", "Macrophage or neutrophil recognizes it by receptors"), ("Engulf", "Phagosome forms"), ("Kill", "Phagosome fuses with lysosome. NADPH oxidase makes the killing burst."),
             caption="Phagocytosis. A failure at any step causes immunodeficiency"),
        P("<strong>Chronic granulomatous disease (CGD)</strong>: a mutation in the <strong>NADPH oxidase</strong> complex, so phagocytes eat bacteria but cannot destroy them. X-linked (70%, presents in the first 5 years) or autosomal recessive (22%, sometimes found in early adulthood). Severe infections with <strong>catalase-positive</strong> organisms: pneumonia, skin and liver abscesses, lymphadenopathy, osteomyelitis. Test: dihydrorhodamine 123 assay and genetic testing."),
        P("<strong>Complement</strong> kills extracellular pathogens three ways: <strong>opsonization</strong> (tags microbes for phagocytes), <strong>inflammation</strong> (attracts neutrophils) and <strong>lysis</strong> (membrane attack complex, MAC)."),
        table(["Complement deficiency", "Pattern"],
              ["Early components", "Milder infections with encapsulated organisms (<em>Streptococcus</em>, <em>H. influenzae</em>, <em>Neisseria</em>). Most likely to have autoimmunity"],
              ["C3", "Key for opsonization. Infections with encapsulated organisms"],
              ["Terminal (MAC, C5 to C9)", "Most severe. Recurrent systemic <em>Neisseria</em> infections. C9 deficiency is most common"]),
        callout("clin", P("A 19-year-old in residence has fever, photophobia, a stiff neck and pus on LP growing <em>N. meningitidis</em>. Workup shows a terminal complement deficiency.")),
        src=S_IMM),
    topic("Adaptive defects: T cells and B cells",
        P("T cells are the quarterback of adaptive immunity: they help activate B cells, activate NK cells and macrophages, drive memory and control intracellular infection. B cells make antibodies that limit extracellular spread. They make IgM first, then switch to IgG. IgA guards secretions, IgE drives allergy."),
        P("<strong>Severe combined immunodeficiency (SCID)</strong> is the result of primary T cell defects. Infants get severe infections in the first 6 months and die without a bone marrow transplant. It is autosomal recessive or X-linked. Once infections start, transplant is often impossible, so SCID is caught before symptoms on <strong>newborn screening</strong>."),
        flow(("T cell receptor built in thymus", "DNA is cut and edited"), ("Cut-out DNA circles", "T cell receptor excision circles (TRECs)"), ("Newborn screen", "Low TRECs = few T cells = possible SCID"), caption="How newborn screening finds SCID"),
        table(["SCID type", "Mutation"], ["T− B+ NK−", "Common gamma chain, JAK3"], ["T− B+ NK+", "IL-7 receptor"], ["T− B− NK+", "RAG1, RAG2, Artemis"], ["T− B− NK−", "Adenosine deaminase (ADA), PNP"]),
        cols(("Selective IgA deficiency", UL("Most common immunodeficiency, 1 in 400", "Most are asymptomatic: IgG fills in for IgA in secretions", "Often found incidentally", "Symptomatic patients get earlier antibiotics for URTIs")),
             ("Common variable immunodeficiency (CVID)", UL("Most common <strong>symptomatic</strong> primary immunodeficiency in clinic (1 in 10,000 to 50,000)", "Childhood or adulthood", "Recurrent sinopulmonary infections, sometimes chronic diarrhea", "Treat with IgG replacement: monthly IV or weekly subcutaneous"))),
        src=S_IMM),
    topic("Secondary immunodeficiency and immunosuppressive drugs",
        P("This is the immunodeficiency you will see most. Causes: malignancy, immunosuppressive treatment (chemotherapy, biologics), systemic disease (diabetes), chronic infection (HIV), asplenia, malnutrition, extremes of age and environmental stress."),
        tree("Drugs that suppress the immune system", [("Block signalling", ["Anti-TNF: etanercept, infliximab", "CD20 inhibitor: rituximab", "JAK inhibitors"]),
                                                       ("Block immune cells", ["Calcineurin inhibitors: cyclosporine, tacrolimus", "Purine inhibitors: azathioprine, mycophenolate"]),
                                                       ("Many targets", ["Steroids: prednisone"])]),
        P("Management depends on the drug and the reason: antibiotics with each fever or sore throat, regular WBC checks, or chronic prophylaxis against opportunistic infections. Diabetes lowers C4 and impairs cytokine response, chemotaxis, killing and phagocytosis. Uremia impairs antigen presentation, one reason for poor hepatitis B vaccine responses."),
        src=S_IMM),
    topic("HIV",
        P("HIV is a retrovirus that infects and destroys <strong>CD4 T cells</strong>, causing a progressive loss of cell-mediated immunity. It spreads through sexual secretions, blood (shared needles, blood products) and across the placenta. It reverse transcribes its RNA into DNA, integrates into the host genome and makes new virus."),
        svg(HIVCOURSE, caption="Schematic course of untreated HIV", label="Graph of untreated HIV: viral load spikes in acute infection, falls, then rises in AIDS. CD4 count dips, partly recovers, then declines steadily below 200."),
        flow(("Initial infection", "Mono-like illness about 1 month after exposure. Immune response lowers the viral load, symptoms resolve, replication continues"),
             ("Clinical latency", "No symptoms, median 8 years, CD4 cells slowly destroyed"),
             ("AIDS", "Weight loss, lymphadenopathy, fever, opportunistic infections (PJP), malignancy (Kaposi sarcoma). About 2 years, then death"), caption="Untreated HIV"),
        P("Treatment is a combination of antiretrovirals hitting different steps, because error-prone reverse transcriptase mutates quickly. Treated patients live long, symptom-free lives but face more cardiovascular disease, diabetes, renal disease and cancer."),
        src=S_IMM),
    topic("Opportunistic infections",
        P("<b>Opportunistic infections</b> (<b>OIs</b>) occur more often and more severely in immunocompromised people. Risk tracks the CD4 count in HIV: above 500, infections look like everyone else's (and TB). Below 50, think <em>M. avium</em>, CMV retinitis and lymphoma."),
        table(["Organism", "Who is at risk", "Disease", "Treatment"],
              ["<b>Mycobacterium tuberculosis</b>", "Foreign born, TB contacts, Indigenous Canadians, incarceration, elderly. Reactivation with HIV or immunosuppression", "TB: cough over 3 weeks, hemoptysis, constitutional symptoms. 3 sputum samples, one early morning", "Isoniazid + rifampin + ethambutol + pyrazinamide"],
              ["<b>Mycobacterium avium complex</b>", "CF, COPD, bronchiectasis, older women. Disseminated in HIV with CD4 below 50", "MAC lung disease, disseminated disease", "Azithromycin + rifampin + ethambutol"],
              ["<b>Cytomegalovirus</b>", "HIV with CD4 below 100, transplant, chemotherapy", "Reactivation: pneumonia, colitis, retinitis, CMV syndrome", "Ganciclovir, valganciclovir. Letermovir prophylaxis in transplant"],
              ["<b>Cryptococcus spp.</b>", "HIV, long-term steroids, transplant, malignancy", "Meningitis (headache, fever), lung nodules, umbilicated papules", "Amphotericin B + flucytosine, then fluconazole"],
              ["<b>Pneumocystis jirovecii pneumonia</b> (<b>PJP</b>)", "HIV with CD4 below 200, transplant, long-term steroids", "Fever, dyspnea, cough, hypoxemia. High LDH, ground glass on CT", "TMP-SMX (2nd line clindamycin-primaquine), steroids if severe"]),
        src=S_IMM),
    topic("Fever in an immunocompromised patient",
        P("The defect predicts the bugs: cellular (HIV, steroids), humoral (congenital), neutropenia (chemotherapy), barrier breaks (surgery, burns) and other (splenectomy, diabetes). Use the usual differential, then add opportunistic infections and the context. Presentation is often different, and fever may be hidden by cytokine blockers (anakinra, tocilizumab, infliximab, adalimumab)."),
        callout("trap", P("<strong>Neutropenic fever is an emergency.</strong> Patients deteriorate fast even with mild symptoms, opportunists are likely, and delayed treatment carries high mortality. Start antibiotics before culture results.")),
        flow(("Recognize", "Possible neutropenic fever. Vitals, oxygen, hemodynamics"),
             ("Treat now", "Empiric IV broad spectrum: pip-tazo, cefepime or meropenem. Add vancomycin for MRSA concern (line, skin, pneumonia, instability)"),
             ("Investigate", "CBC with differential, blood cultures ≥ 2 sets (one from a central line), urine culture, CXR (CT if needed), site-specific tests"),
             ("Still febrile 4 to 7 days?", "Add an antifungal: echinocandin, voriconazole or liposomal amphotericin B"),
             caption="Neutropenic fever, for example AML on chemotherapy"),
        P("Likely organisms: gram-negatives (<em>Pseudomonas</em>, <em>E. coli</em>, <em>Klebsiella</em>), gram-positives (<em>S. aureus</em>, streptococci), fungi (<em>Candida</em>, and <em>Aspergillus</em> with prolonged neutropenia) and viruses (HSV, CMV)."),
        callout("key", UL("Vaccinate: live vaccines are generally unsafe, so give vaccines before immunosuppression when possible.", "After splenectomy: pneumococcal, meningococcal and <em>H. influenzae</em> type b vaccines.", "Give antimicrobial prophylaxis to HIV and transplant patients for infections with no vaccine.")),
        src=S_IMM),
    ],
    notes=[44, 45, 46, 47, 48, 49, 50, 65, 66],
    recall=[("Recurrent Neisseria infections point to which defect?", "Complement, especially terminal (MAC) deficiency."),
            ("What enzyme is broken in chronic granulomatous disease?", "NADPH oxidase. Phagocytes cannot kill catalase-positive organisms."),
            ("How is SCID found on newborn screening?", "Low T cell receptor excision circles (TRECs)."),
            ("Recurrent sinopulmonary infections starting after 6 months of age suggest which arm?", "Humoral (B cell, antibody). Maternal antibodies have waned."),
            ("Most common immunodeficiency?", "Selective IgA deficiency (1 in 400), usually asymptomatic."),
            ("HIV infects which cell?", "CD4 T cells."),
            ("Below which CD4 count is PJP a risk?", "200 cells/µL."),
            ("Chemo patient, fever 38.5, ANC 300. First step?", "Start empiric broad-spectrum IV antibiotics immediately."),
            ("Fever persists 6 days into antibiotics in a neutropenic patient. Next?", "Add empiric antifungal therapy.")]))

S_RDESC = "Source: Describing the Rash (Bustamante). Not covered in Nicole's Notes"
S_RID = "Sources: Rash from an Infectious Diseases Perspective (Mohammadi), Nicole's Notes p. 128"
S_RALL = "Source: Introduction to Allergic Rashes (Lee). Not covered in Nicole's Notes"


def _lesions():
    items = [("Macule", "flat, &lt;1 cm"), ("Papule", "raised, &lt;1 cm"), ("Plaque", "raised, &gt;1 cm"), ("Nodule", "into dermis"),
             ("Vesicle", "fluid, &lt;1 cm"), ("Bulla", "fluid, &gt;1 cm"), ("Pustule", "pus"), ("Wheal", "edema, &lt;24 h")]
    o = ['<div class="lesions">']
    skin, derm = "#f1d3bf", "#e5bba3"
    for k, (name, sub) in enumerate(items):
        ox, oy = 0, -40
        base = oy + 85
        o.append(f'<div class="les"><svg viewBox="0 0 160 95" xmlns="http://www.w3.org/2000/svg"><rect x="{ox+10}" y="{base}" width="140" height="45" fill="{derm}"/><rect x="{ox+10}" y="{base}" width="140" height="10" fill="{skin}"/>')
        cx = ox + 80
        if name == "Macule":
            o.append(f'<rect x="{cx-22}" y="{base}" width="44" height="6" fill="#a0522d"/>')
        elif name == "Papule":
            o.append(f'<path d="M{cx-18} {base} Q{cx} {base-30} {cx+18} {base}Z" fill="#d98b7a"/>')
        elif name == "Plaque":
            o.append(f'<path d="M{cx-50} {base} L{cx-44} {base-16} H{cx+44} L{cx+50} {base}Z" fill="#d98b7a"/>')
        elif name == "Nodule":
            o.append(f'<ellipse cx="{cx}" cy="{base+18}" rx="28" ry="22" fill="#c27a68"/><path d="M{cx-30} {base} Q{cx} {base-14} {cx+30} {base}" fill="{skin}"/>')
        elif name == "Vesicle":
            o.append(f'<path d="M{cx-16} {base} Q{cx} {base-30} {cx+16} {base}Z" fill="#cfe6f5" stroke="#7aa9c9" stroke-width="2"/>')
        elif name == "Bulla":
            o.append(f'<path d="M{cx-42} {base} Q{cx} {base-55} {cx+42} {base}Z" fill="#cfe6f5" stroke="#7aa9c9" stroke-width="2"/>')
        elif name == "Pustule":
            o.append(f'<path d="M{cx-16} {base} Q{cx} {base-30} {cx+16} {base}Z" fill="#f2df8a" stroke="#c9ad3b" stroke-width="2"/>')
        else:
            o.append(f'<path d="M{cx-55} {base} Q{cx} {base-26} {cx+55} {base}Z" fill="#f2b4b4" opacity=".85"/>')
        o.append(f'</svg><p class="lh">{name}</p><p class="ls">{sub}</p></div>')
    o.append("</div>")
    return "".join(o)


TABS.append(dict(key="rash", label="Rashes",
    lede="Describe a rash before you name it. Then use the pattern, the systemic features and the history to sort infectious from allergic causes.",
    topics=[
    topic("Describe before you diagnose",
        P("Describing a rash systematically narrows the differential before you name anything, the same way you reason through a murmur or a chest film. Build one sentence from four blocks:"),
        chain("1 Noun: primary lesion", "2 Adjectives: size, colour, border, surface", "3 Arrangement: linear, annular, grouped", "4 Distribution: where, symmetric?"),
        callout("clin", P("<strong>Example</strong>: multiple pink, well-demarcated plaques with thick silvery scale, scattered, on symmetric extensor elbows, knees and scalp, with nail pitting. That is plaque psoriasis.")),
        P("Prepare the exam: good light, expose with a gown and drape, look at the <strong>whole skin</strong> including scalp, nails, mouth, palms and soles, then touch (raised or flat, deep or superficial, warm, tender). Ask where it started and what the first lesion looked like. Measure in mm or cm and count."),
        src=S_RDESC),
    topic("Step 1: the primary lesion",
        svg(_lesions(), caption="Primary lesions in cross-section. First question: can you feel it? If not, it is a macule or patch.", label="Eight skin cross sections: macule flat, papule small dome, plaque wide raised, nodule deep, vesicle small fluid blister, bulla large blister, pustule pus-filled, wheal soft edematous swelling."),
        table(["Lesion", "Definition", "Examples"],
              ["Macule / patch", "Flat colour change. A patch is a larger macule", "Freckles, port-wine stain, viral exanthem"],
              ["Papule / plaque", "Raised and palpable. Plaques are broad, often from merging papules", "Warts, lichen planus, psoriasis"],
              ["Nodule / tumor", "Solid, extends into dermis or fat. A tumor is larger", "Dermatofibroma, lipoma"],
              ["Vesicle / bulla", "Clear fluid blister, under or over 1 cm", "HSV, contact dermatitis / pemphigoid, burns"],
              ["Pustule", "Pus-filled blister", "Folliculitis, acne, pustular psoriasis"],
              ["Wheal (hive)", "Itchy edema that moves. Each lasts under 24 h", "Urticaria"],
              ["Others", "Cyst, comedo, burrow, telangiectasia", "Epidermoid cyst, acne, scabies, rosacea"]),
        P("Textbooks disagree on exact size cutoffs, so describe concrete features (size, elevation, depth, colour) rather than leaning on one label."),
        src=S_RDESC),
    topic("Secondary changes: what happened next",
        table(["Change", "What it is", "Example"],
              ["Scale", "Heaped-up dry stratum corneum", "Psoriasis"], ["Crust", "Dried serum, blood or pus", "Impetigo"], ["Fissure", "Linear crack", "Hand eczema"],
              ["Erosion", "Superficial loss of epidermis, heals without scar", "Ruptured vesicle"], ["Ulcer", "Loss into dermis, may scar", "Venous or pressure ulcer"],
              ["Excoriation", "Linear erosion from scratching", "Scabies, eczema"], ["Atrophy", "Thinning", "Chronic steroid use, aging"],
              ["Scar", "Fibrous replacement after injury", "Surgery, acne"], ["Lichenification", "Thick skin with exaggerated markings from rubbing", "Chronic eczema"]),
        src=S_RDESC),
    topic("Steps 3 and 4: arrangement and distribution",
        table(["Arrangement", "Looks like", "Example"],
              ["Linear", "Straight line", "Poison ivy, excoriations"], ["Annular", "Ring with central clearing", "Tinea corporis, granuloma annulare"],
              ["Grouped (herpetiform)", "Clusters", "Herpes simplex"], ["Zosteriform", "Along a dermatome", "Herpes zoster"],
              ["Target (iris)", "Concentric rings", "Erythema multiforme"], ["Serpiginous", "Snake-like track", "Cutaneous larva migrans"],
              ["Reticulated", "Lacy net", "Livedo reticularis"], ["Nummular", "Coin-shaped", "Nummular dermatitis"]),
        P("For distribution ask: one or many, random or patterned, symmetric, sun-exposed, flexor or extensor, and are palms, soles, scalp or mucosa involved?"),
        cols(("Classic sites", UL("Psoriasis: scalp, extensor elbows and knees, umbilicus, gluteal cleft", "Atopic dermatitis (adult): antecubital and popliteal fossae", "Herpes zoster: one dermatome, one side, stops at midline", "Scabies: finger webs, wrists, axillae, waistline, genitalia")),
             ("Do not skip", UL("<strong>Mucosae</strong>: pemphigus, erythema multiforme, SJS. Rash plus mucosa means think severe reaction or blistering disease", "<strong>Palms and soles</strong>: secondary syphilis, erythema multiforme, scabies", "<strong>Nails and scalp</strong>: psoriasis (pitting), lichen planus"))),
        table(["Sign", "What happens", "Classic for"],
              ["Koebner", "New lesions at sites of trauma", "Psoriasis, lichen planus, vitiligo"], ["Nikolsky", "Gentle pressure shears off epidermis", "TEN, pemphigus"],
              ["Auspitz", "Removing scale causes pinpoint bleeding", "Psoriasis"], ["Darier", "Stroking a lesion makes it swell", "Mastocytosis"]),
        callout("trap", UL("\"Maculopapular\" is vague. Say macules, patches, papules or plaques.", "\"Eczema-looking\" is a guess, not a description.", "Palpate. Look everywhere, not only where it hurts. Ask what the first, unscratched lesions looked like.")),
        src=S_RDESC),
    topic("Infectious rashes",
        P("Four patterns: <strong>maculopapular</strong> (flat and raised red lesions), <strong>vesicular</strong> (small blisters), <strong>sandpaper</strong> (fine, rough redness) and <strong>petechial/purpuric</strong> (non-blanching red-purple). Pair the pattern with fever, respiratory symptoms, nodes, mucosal findings and exposure."),
        table(["Infection", "Rash", "Other clues", "Key point"],
              ["Measles", "Maculopapular, face → trunk → limbs", "High fever, cough, coryza, conjunctivitis. Koplik spots", "<strong>Airborne precautions</strong> and public health"],
              ["Rubella", "Maculopapular, starts on face", "Milder. Posterior auricular and suboccipital nodes", "Danger in pregnancy"],
              ["Parvovirus B19 (fifth disease)", "Slapped cheeks, then lacy body rash", "Mild in children", "Danger in pregnancy and hemolytic disorders"],
              ["Roseola (HHV-6)", "Pink maculopapular, starts on trunk", "Under 2 years. Days of high fever, <strong>rash appears as fever resolves</strong>", ""],
              ["Varicella / zoster", "Chickenpox: itchy vesicles in different stages. Zoster: painful grouped vesicles in one dermatome", "", "Precautions, especially disseminated"],
              ["HSV", "Grouped painful vesicles on red base, then erosions", "Oral or genital, recurs", "Severe: eye, CNS, eczema herpeticum"],
              ["Hand, foot and mouth (Coxsackie)", "Mouth ulcers, hands, feet, buttocks", "", "Supportive, hydration"],
              ["Scarlet fever (GAS)", "Fine sandpaper rash", "Fever, sore throat, strawberry tongue", "Think group A strep"],
              ["Meningococcemia", "<strong>Non-blanching petechiae or purpura</strong> that spread fast", "Can deteriorate within hours", "<strong>Emergency</strong>: treat now"],
              ["Secondary syphilis", "Diffuse symmetric maculopapular, <strong>palms and soles</strong>", "Generalized lymphadenopathy", "Take a sexual history"]),
        callout("key", P("Fever with a non-blanching rash is meningococcemia until proven otherwise. Palms and soles: <b>CaRS</b> (Coxsackie, Rocky Mountain spotted fever, syphilis).")),
        src=S_RID),
    topic("Allergic and immune rashes",
        P("Different immune cells give different rashes. <strong>Mast cells</strong> hold histamine, heparin and tryptase. When an antigen (drug, food, venom) cross-links its specific IgE, they degranulate: itch, swelling, redness. <strong>Eosinophils</strong> live in tissues, kill parasites and drive atopic disease. <strong>T cells</strong> cause delayed drug rashes."),
        cols(("Urticaria (hives)", UL("Mast cells in the upper skin", "Itchy wheals, like a mosquito bite", "Each lasts under 24 to 48 h", "Not painful, leaves no mark")),
             ("Morbilliform drug eruption", UL("Most common drug rash, type IV", "Measles-like, symmetric, itchy", "5 to 14 days after starting the drug", "Each spot lasts several days")),
             ("SJS / TEN", UL("Rare, severe type IV: T cells kill epidermal cells", "Painful skin that necroses and detaches", "<strong>Mucosal involvement common</strong>", "Very sick patients")),
             caption="Three drug and allergy rashes, by mechanism"),
        callout("trap", UL("Hives do not equal allergy. Mast cells can be triggered directly (pseudoallergy) or by infection.", "History beats morphology. Hives that start hours after a dose, after days of tolerating the drug, or that last days overall, suggest infection-related or spontaneous hives.")),
        callout("clin", P("A 3-year-old on day 5 of 7 of amoxicillin gets hives 5 hours after his morning dose. Each wheal lasts under an hour, he is well. The delay and days of tolerance point away from true amoxicillin allergy.")),
        cols(("Histamine angioedema", P("Same chemistry as hives, deeper in the dermis. Often comes with hives. Usually benign (spontaneous hives) but can be anaphylaxis.")),
             ("Bradykinin angioedema", P("Rare. No hives. ACE inhibitors, hereditary or acquired angioedema. Can be dangerous.")),
             caption="Angioedema: non-pitting, asymmetric swelling of skin or mucosa that resolves over hours to days"),
        P("<strong>Dermatitis (eczema)</strong> is inflammation of the epidermis and superficial dermis: redness, scale, crust, oozing, from skin barrier failure. Types: atopic, irritant contact, allergic contact, stasis, seborrheic."),
        table(["Mimic of dermatitis", "Clue"], ["Tinea", "Annular plaque with central clearing. Contact-sport athletes"], ["Candida", "Satellite lesions in skin folds"],
              ["Scabies", "Burrows, palm and sole pustules, itchy household contacts"], ["Impetigo", "Honey-coloured crust, usually staph"], ["Eczema herpeticum", "HSV on eczema: painful punched-out crusted clusters"]),
        P("Staph scalded skin syndrome looks like TEN but affects young children and spares the mucosa. RIME (reactive infectious mucocutaneous eruption) follows <em>Mycoplasma</em> or viral infection and mostly spares the skin."),
        src=S_RALL),
    ],
    notes=[],
    recall=[("Name the four parts of a rash description.", "Noun (primary lesion), adjectives, arrangement, distribution."),
            ("Macule versus papule?", "A macule is flat (you cannot feel it). A papule is raised."),
            ("Vesicle versus bulla?", "Both are fluid blisters. Vesicle under 1 cm, bulla over 1 cm."),
            ("Toddler with days of high fever, then a trunk rash as the fever breaks?", "Roseola (HHV-6)."),
            ("Sore throat, strawberry tongue and a sandpaper rash?", "Scarlet fever from group A strep."),
            ("Fever with rapidly spreading non-blanching petechiae?", "Meningococcemia. An emergency."),
            ("Which drug rash appears 5 to 14 days in and is the most common?", "Morbilliform drug eruption (type IV)."),
            ("How do you tell SSSS from TEN?", "SSSS affects young children and spares the mucous membranes.")]))
