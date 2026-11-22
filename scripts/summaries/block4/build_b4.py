"""Build the Block 4 weekly summary pages (week-13/14/15-summary.html).

Notes cards come from cards.json (convert.py, Nicole's Notes PDF pages 119-153), with
Nicole's bold kept as <b> and shown highlighted. Lecture cards are hand-written from
the week's lecture slides and tagged "From the lectures".
"""
import json, html, re, pathlib, shutil

HERE = pathlib.Path(__file__).parent
SITE = pathlib.Path("/home/claude/med-notes/quartz/static/pages")
CARDS = json.loads((HERE / "cards.json").read_text())
FIGDIR = "b4figs"


def N(*idx):
    return [("notes", i) for i in idx]


def LEC(title, body, src):
    return ("lecture", {"title": title, "body": body, "src": src})


def ul(*xs):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"


def table(head, *rows):
    h = '<div class="tw"><table><tr>' + "".join(f"<th>{c}</th>" for c in head) + "</tr>"
    for r in rows:
        h += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return h + "</table></div>"


# ------------------------------------------------------------------ lecture cards
RASH_FRAME = LEC("Describing a rash: the framework", ul(
    "Describe before you diagnose. One sentence, four building blocks: <em>noun</em> (primary or secondary lesion), <em>adjective</em> (size, colour, texture, border, surface), <em>arrangement</em> (linear, annular, grouped), <em>distribution</em> (symmetric, sun-exposed, dermatomal).",
    "Prepare the exam: good light, expose with dignity (quadrants with gown and drape), examine the whole skin including scalp, nails, mucosae, palms and soles.",
    "Look, then touch: raised or flat, superficial or deep, firm, soft, warm, tender.",
    "Ask the story: where it started, what the first lesion looked like, what changed, itch or pain.",
    "Measure it in mm or cm, and count: single, few or many.",
), "Describing the Rash (Bustamante)")

RASH_PRIMARY = LEC("Primary lesions", table(
    ["Lesion", "Definition", "Examples"],
    ["Macule / patch", "Flat, non-palpable colour change. Macule under 1 cm, patch over 1 cm", "Freckles, port-wine stain, viral exanthem"],
    ["Papule / plaque", "Raised, palpable. Papule under 1 cm, plaque over 1 cm, often flat-topped", "Warts, lichen planus, psoriasis"],
    ["Nodule / tumor", "Solid lesion extending into the dermis or subcutis. A tumor is larger", "Dermatofibroma, lipoma"],
    ["Vesicle / bulla", "Fluid-filled blister. Vesicle under 1 cm, bulla over 1 cm", "HSV, contact dermatitis / bullous pemphigoid, burns"],
    ["Pustule", "Pus-filled superficial lesion", "Folliculitis, acne, pustular psoriasis"],
    ["Wheal (hive)", "Transient, edematous raised lesion, each lasting under 24 h", "Urticaria"],
    ["Cyst / comedo", "Encapsulated cavity / follicular plug (open or closed)", "Epidermoid cyst / acne vulgaris"],
    ["Burrow / telangiectasia", "Thin winding tract / visible dilated superficial vessels", "Scabies / rosacea, systemic sclerosis"],
) + ul("First question: can you feel it? If not, it is a macule or patch.", "Time is a clue: wheals come and go within hours. A lesion fixed for days is not a wheal.",
       "Textbooks disagree on exact size cutoffs, so describe size, elevation, depth and colour rather than leaning on one label."),
    "Describing the Rash (Bustamante)")

RASH_SECONDARY = LEC("Secondary lesions", table(
    ["Lesion", "Definition", "Example"],
    ["Scale", "Heaped-up, dry exfoliation of the stratum corneum", "Psoriasis, ichthyosis"],
    ["Crust (scab)", "Dried serum, blood or pus over injured epithelium", "Impetigo, excoriation"],
    ["Fissure", "A linear crack in the skin", "Atopic dermatitis, hand eczema"],
    ["Erosion", "Superficial loss of epidermis, heals without a scar", "Ruptured vesicle, impetigo"],
    ["Ulcer", "Loss of epidermis into dermis, may scar", "Venous ulcer, pressure ulcer"],
    ["Excoriation", "A linear erosion from scratching", "Pruritus, scabies, eczema"],
    ["Atrophy", "Thinning of skin", "Chronic steroid use, aging"],
    ["Scar", "Fibrotic replacement after injury or inflammation", "Surgery, trauma, acne"],
    ["Lichenification", "Thickened skin with accentuated markings from chronic rubbing", "Chronic eczema, lichen simplex"],
), "Describing the Rash (Bustamante)")

RASH_PATTERN = LEC("Arrangement, distribution and signs",
    "<p class=\"cap\">Configuration</p>" + ul(
        "Linear: contact dermatitis (poison ivy), excoriations.", "Annular: ring with central clearing, as in tinea corporis.",
        "Grouped / herpetiform: herpes simplex. Zosteriform: along a dermatome, as in herpes zoster.",
        "Target (iris): erythema multiforme. Serpiginous: cutaneous larva migrans. Reticulated: livedo reticularis. Nummular: coin-shaped.")
    + "<p class=\"cap\">Classic distributions</p>" + ul(
        "Psoriasis: scalp, extensor elbows and knees, umbilicus, gluteal cleft.", "Lichen planus: wrists, forearms, genitalia, lower legs.",
        "Vitiligo: periorificial and acral. Discoid lupus: sun-exposed face.", "Herpes zoster: strictly unilateral, one dermatome. Adult atopic dermatitis: flexural.",
        "Rash with mucosal involvement (mouth, eyes, genitalia): think severe reaction or blistering disease. Secondary syphilis involves palms and soles.")
    + "<p class=\"cap\">Signs</p>" + ul(
        "Koebner: new lesions at sites of trauma (psoriasis, lichen planus, vitiligo).", "Nikolsky: gentle lateral pressure shears off epidermis (TEN, pemphigus).",
        "Auspitz: removing scale causes pinpoint bleeding (psoriasis).", "Darier: stroking a lesion causes swelling (mastocytosis).")
    + "<p class=\"cap\">Traps</p>" + ul("Saying \"maculopapular\" instead of describing.", "Naming (\"eczema-looking\") instead of describing.", "Skipping palpation.",
        "Looking only where it hurts.", "Forgetting mucosae, palms and soles.", "Describing a scratched rash. Ask what the first lesions looked like."),
    "Describing the Rash (Bustamante)")

RASH_ID = LEC("Infectious rashes", table(
    ["Infection", "Rash", "Key clue"],
    ["Measles", "Maculopapular, face → trunk → extremities. Koplik spots", "High fever, cough, coryza, conjunctivitis. Airborne precautions and public health"],
    ["Rubella", "Maculopapular, often starts on the face. Milder than measles", "Posterior auricular and suboccipital nodes. Major concern in pregnancy"],
    ["Parvovirus B19 (fifth disease)", "Slapped cheeks, then a lacy, reticular body rash", "Concern in pregnancy and hemolytic disorders"],
    ["Roseola", "Pink maculopapular rash starting on the trunk", "Under 2 years. High fever for days, rash appears as fever resolves"],
    ["Varicella zoster", "Chickenpox: itchy vesicles in different stages. Zoster: painful grouped vesicles in one dermatome", "Precautions, especially for disseminated disease"],
    ["Herpes simplex", "Grouped painful vesicles on a red base, becoming erosions", "Oral or genital, recurs. Severe: ocular, CNS, eczema herpeticum"],
    ["Hand-foot-and-mouth", "Oral vesicles or ulcers, rash on hands, feet, buttocks", "Supportive care, hydration"],
    ["Scarlet fever", "Fine red sandpaper rash, strawberry tongue", "Fever and sore throat. Group A Streptococcus"],
    ["Meningococcemia", "Petechiae or purpura, non-blanching, spreads fast", "Medical emergency. Can deteriorate within hours"],
    ["Secondary syphilis", "Diffuse symmetric maculopapular rash, palms and soles", "Generalized lymphadenopathy. Take a sexual history"],
), "Rash from an Infectious Diseases Perspective (Mohammadi)")

RASH_ALLERGY = LEC("Allergic and drug rashes", ul(
    "Mast cell granules hold histamine, heparin and tryptase. Antigen binding to specific IgE triggers degranulation. Eosinophils kill ectoparasites and drive asthma and atopic dermatitis.",
    "<em>Urticaria</em>: mast cell activation in the upper skin. Itchy red wheals, each lasting under 24 to 48 h on the same spot, not painful, leaving no mark or bruise.",
    "Hives do not equal allergy. History beats morphology. A delay of several hours after a drug, tolerance for days in the same course, or hives lasting days suggest a spontaneous or infection-related cause.",
    "<em>Angioedema</em>: localized swelling of skin or mucosa. Resolves over hours to days, asymmetric, non-pitting, not gravity dependent. Histamine-mediated (same as hives, deeper) or bradykinin-mediated (ACE inhibitors, hereditary or acquired angioedema).",
    "<em>Dermatitis</em>: inflammation of the epidermis and superficial dermis with erythema, scale, crust and oozing. Types: atopic, irritant or allergic contact, stasis, seborrheic. Mimics: tinea (central clearing), candida (satellite lesions), scabies (burrows, household contacts), impetigo (honey crust), eczema herpeticum (punched-out painful clusters).",
    "<em>Morbilliform drug eruption</em>: the most common drug rash. Measles-like, symmetric, itchy, appears 5 to 14 days after exposure. Type IV hypersensitivity.",
    "<em>SJS/TEN</em>: rare, severe type IV reaction. Drug-specific cytotoxic T cells kill epidermal cells, causing necrosis and detachment, painful skin and mucosal involvement. Staph scalded skin syndrome affects young children and spares the mucosa.",
    "<em>RIME</em>: post-infectious mucositis after Mycoplasma or a virus, sparing the rest of the skin.",
), "Introduction to Allergic Rashes (Lee)")

FEVER_OLDER = LEC("Fever in older adults", ul(
    "Higher infection risk: weaker barriers, lower cellular and humoral immunity, weaker vaccine response, comorbidities such as diabetes.",
    "Fever thresholds in a frail older adult: a single oral temperature over 37.8°C, a persistent oral or tympanic temperature of 37.2°C or more, or a rise of 1.1°C or more above baseline.",
    "Fever is absent in 30 to 50% of frail older adults with infection, even serious infection. These patients do worse. No fever does not rule out infection.",
    "Delirium and falls are common atypical presentations of infection. Get collateral history. Localizing symptoms may be absent despite a focal infection.",
    "Ask about pneumococcal, influenza, shingles and COVID vaccines.",
    "Use the same approach: safe and stable, history, exam, differential, investigations.",
), "Approach to Fever in Older Adults (Diachun, Burrell)")

# ------------------------------------------------------------------ recall
R = {}
R["lab"] = [("When should specimens be collected relative to antibiotics?", "Before antibiotics are given."),
            ("What is the most critical factor for a blood culture?", "The volume of blood collected."),
            ("What is the specimen of choice for a skin and soft tissue infection?", "A biopsy of the advancing margin of the lesion."),
            ("An isolate has an MIC of 4 or less and a zone of 20 or more. Which category is it?", "Susceptible.")]
R["dx"] = [("What colour are gram-positive and gram-negative bacteria?", "Gram-positive purple, gram-negative pink."),
           ("What colour is an acid-fast positive organism?", "Red. Acid-fast negative is blue."),
           ("How do IgM and IgG serology differ?", "IgM needs a single acute serum. IgG needs acute and convalescent sera."),
           ("Why are gram-negatives resistant to penicillin?", "Their thick outer membrane.")]
R["bugs"] = [("Which bacterial endotoxin engages TLR4, and which engages TLR2?", "Lipopolysaccharide (gram-negative) engages TLR4. Lipoteichoic acid (gram-positive) engages TLR2."),
             ("Which E. coli adhesins cause pyelonephritis and cystitis?", "PapG binds glycolipids in pyelonephritis. FimH binds mannose in cystitis."),
             ("What makes up a nucleocapsid?", "The capsid plus the genome.")]
R["viro"] = [("Which receptor does SARS-CoV-2 use, and which does influenza use?", "ACE2 for SARS-CoV-2. Sialic acid for influenza."),
             ("What share of human fungal infections do yeasts cause, and which yeasts matter?", "70%. Candida and Cryptococcus."),
             ("Where is C. gattii found?", "Tropical areas and the Pacific Northwest of North America.")]
R["biome"] = [("What is the difference between a commensal and dysbiosis?", "A commensal is a microbe in its usual habitat. Dysbiosis is a change in the composition, diversity or metabolites of the microbiome."),
              ("Name the normally sterile sites.", "Bladder, bloodstream, CSF and lower respiratory tract.")]
R["abx"] = [("Which antibiotic group is safest in pregnancy?", "β-lactams."),
            ("When should carbapenems be used?", "For serious, life-threatening infections or multi-drug resistant organisms."),
            ("How do oseltamivir and zanamivir work?", "They inhibit neuraminidase, which releases virus from infected cells."),
            ("What do azoles target, and what is the main caution?", "CYP450 lanosterol 14-α-demethylase, blocking ergosterol synthesis. Watch for drug interactions."),
            ("Which patients should never be challenged with the drug again?", "Those with severe type II, III or IV reactions.")]
R["ipac"] = [("What is the single most important measure for infection control?", "Hand hygiene."),
             ("How do droplet and airborne particles differ?", "Droplets are 5 microns or more and travel under 2 m. Airborne particles are under 5 microns."),
             ("What is herd immunity?", "When enough of a population is resistant that the few susceptible people are protected, because the pathogen is unlikely to find them.")]
R["outbreak"] = [("How do antigenic drift and shift differ?", "Drift is slow point mutations in one virus and may cause an epidemic. Shift is reassortment between two viruses and may cause a pandemic."),
                 ("How do isolation and quarantine differ?", "Isolation separates sick people. Quarantine restricts people who were exposed, to see if they get sick."),
                 ("What does an incubation period measure?", "The time from exposure to the first symptoms.")]
R["fever"] = [("What defines a fever?", "An early morning oral or tympanic temperature of 37.2°C or more, or any temperature of 37.8°C or more."),
              ("What are the qSOFA criteria?", "Respiratory rate 22 or more, BP 100/60 or less, altered mentation. 2 or more points means high risk."),
              ("How often is fever absent in frail older adults with infection?", "30 to 50% of the time.")]
R["inflam"] = [("Name the five cardinal signs of inflammation.", "Rubor, calor, dolor, tumor and functio laesa."),
               ("What is a granuloma?", "An aggregation of macrophages surrounded by T lymphocytes."),
               ("What must you rule out before immunosuppressive treatment?", "TB.")]
R["sepsis"] = [("Define sepsis.", "Life-threatening organ dysfunction caused by a dysregulated host response to infection."),
               ("What is the mortality rate of sepsis?", "30 to 40%.")]
R["immuno"] = [("What is the most common innate immunodeficiency?", "Phagocytic disorders."),
               ("Which newborn screen detects SCID?", "T cell receptor excision circles (TRECs). Low or absent levels suggest SCID."),
               ("How do you approach fever in an immunocompromised host?", "The same differential, plus opportunistic infections, plus the context.")]
R["rash"] = [("Macule or papule: what is the first question?", "Can you feel it? If not, it is a macule or patch."),
             ("How long does each hive last?", "Under 24 to 48 h on the same spot, with no mark left behind."),
             ("When does a morbilliform drug eruption appear?", "5 to 14 days after exposure. It is type IV."),
             ("Which petechial rash is a medical emergency?", "Meningococcemia.")]
R["hyper"] = [("Name the four hypersensitivity types.", "I IgE mediated, II antibody-mediated cell death, III immune complex, IV delayed."),
              ("What is the anaphylaxis dose of epinephrine in the notes?", "IM epinephrine 0.01 mg/kg of 1:1000, max 0.3 mg, repeated every 5 to 15 min as needed."),
              ("In the hygiene hypothesis, which T helper state protects against allergy?", "Th1 protects. Th2 promotes allergy.")]
R["allergy"] = [("How do type A and type B drug reactions differ?", "Type A is predictable (toxicity, side effects, interactions). Type B is unpredictable (intolerance, idiosyncrasy, allergy)."),
                ("What does RAST testing measure?", "Specific IgE antibodies in the blood.")]
R["auto"] = [("What is immune tolerance?", "Antigen-specific unresponsiveness to self-antigens."),
             ("Where does central tolerance happen?", "In the bone marrow and thymus, where immature self-reactive lymphocytes are deleted.")]
R["vax"] = [("What is the time window for an AEFI?", "Within 6 weeks of immunization."),
            ("Define vaccine hesitancy.", "Delay in accepting, or refusing, vaccines despite available services."),
            ("Which program supports people with serious vaccine injuries?", "The Vaccine Injury Support Program (VISP).")]

# ------------------------------------------------------------------ pages
PAGES = {
    13: dict(title="Week 13: Microbes, antimicrobials and infection control",
             tabs=[("lab", "Micro lab", N(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)),
                   ("dx", "Diagnostics", N(11)),
                   ("bugs", "Bacteria", N(12, 13, 14)),
                   ("viro", "Viruses and fungi", N(28, 61, 62, 63)),
                   ("biome", "Microbiome", N(15)),
                   ("abx", "Antimicrobials", N(22, 23, 24, 25, 26, 27, 40, 41, 64)),
                   ("ipac", "Infection control", N(21, 36, 37, 38)),
                   ("outbreak", "Outbreaks", N(29, 34, 35, 39))]),
    14: dict(title="Week 14: Fever, inflammation, sepsis and rashes",
             tabs=[("fever", "Fever", N(16, 17, 18) + [FEVER_OLDER]),
                   ("inflam", "Inflammation", N(19, 20, 58, 59, 60)),
                   ("sepsis", "Sepsis", N(42, 43)),
                   ("immuno", "Immunodeficiency", N(44, 45, 46, 47, 48, 49, 50, 65, 66)),
                   ("rash", "Rashes", [RASH_FRAME, RASH_PRIMARY, RASH_SECONDARY, RASH_PATTERN, RASH_ID, RASH_ALLERGY])]),
    15: dict(title="Week 15: Allergy, autoimmunity and vaccines",
             tabs=[("hyper", "Hypersensitivity", N(51, 52, 53)),
                   ("allergy", "Allergies and testing", N(54, 55, 56)),
                   ("auto", "Autoimmunity", N(57)),
                   ("vax", "Vaccines", N(30, 31, 32, 33))]),
}
LECTURES = {13: ["Utilizing the microbiology lab", "Interpreting micro tests", "Classification of microbes", "Understanding the human microbiome",
                 "Antibiotics", "Antifungal and antiviral agents", "Basics of transmission", "Introduction to infection control", "Outbreak management"],
            14: ["Approach to a patient with fever", "Thermoregulation", "Paediatric fever", "Fever in older adults", "Fever in immunocompromised patients",
                 "Basics of sepsis", "Acute and chronic inflammation", "Immunodeficiency", "Describing the rash", "Rash ID", "Allergic rashes"],
            15: ["Allergy", "Understanding allergy testing", "Approach to allergy through different lenses", "Autoimmunity", "Approach to autoimmune disease",
                 "Vaccine adverse events", "Vaccine hesitancy"]}

CSS = """
:root{--bg:#f5f6f8;--surface:#fff;--ink:#15181d;--muted:#4d5560;--faint:#6b7380;--line:#d5dae1;--soft:#eef0f3;
  --c:#a35f08;--cbg:#f8eedf;--hl:#fbe3b4;--lec:#245b9a;--lec-bg:#e6eef8;
  --font:"Atkinson Hyperlegible Next","Segoe UI",system-ui,-apple-system,sans-serif}
:root[data-theme="dark"]{--bg:#14161a;--surface:#1b1e24;--ink:#eceef2;--muted:#b3bac5;--faint:#8d95a1;--line:#353b45;--soft:#23272e;
  --c:#e3a548;--cbg:#2a2110;--hl:#5a3f12;--lec:#93b9ec;--lec-bg:#16212f;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);font-size:16px;line-height:1.5;
  padding:20px max(16px,env(safe-area-inset-right,0px)) 56px max(16px,env(safe-area-inset-left,0px))}
.wrap{max-width:820px;margin:0 auto;display:flex;flex-direction:column;gap:16px}
h1,h2,h3,p,ul,ol{margin:0}
header h1{font-size:clamp(24px,4vw,30px);line-height:1.15}
header .lede{color:var(--muted);margin-top:6px}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:10px;font-size:14px;color:var(--muted);align-items:center}
.legend b{font-weight:700}
.chip{display:inline-block;font-size:12px;font-weight:700;border-radius:4px;padding:1px 6px;white-space:nowrap;color:var(--lec);background:var(--lec-bg)}
details.lectures{font-size:14px;color:var(--muted);margin-top:8px}
details.lectures summary{cursor:pointer;font-weight:700}
details.lectures ul{margin-top:4px;padding-left:20px}
.bar{position:sticky;top:0;z-index:5;background:var(--bg);padding:8px 0 10px;border-bottom:1px solid var(--line);display:flex;flex-direction:column;gap:8px}
.search{display:flex;gap:8px;align-items:center}
.search input{flex:1;min-width:0;font:inherit;font-size:15px;padding:8px 12px;border:1.5px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}
.search input:focus{outline:2px solid var(--c);outline-offset:1px;border-color:var(--c)}
.count{font-size:13px;color:var(--faint);white-space:nowrap}
.tabs{display:flex;flex-wrap:wrap;gap:6px}
.tabs button{font:inherit;font-size:14px;font-weight:700;color:var(--muted);background:var(--surface);border:1.5px solid var(--line);border-radius:999px;padding:5px 12px;cursor:pointer}
.tabs button[aria-selected="true"]{color:var(--c);border-color:var(--c);background:var(--cbg)}
button:focus-visible,summary:focus-visible{outline:2px solid var(--c);outline-offset:2px}
.panel{display:flex;flex-direction:column;gap:10px}.panel[hidden]{display:none}
.phead{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
.phead h2{font-size:22px;color:var(--c)}
.linkbtn{font:inherit;font-size:14px;font-weight:700;color:var(--c);background:none;border:0;padding:0;cursor:pointer;text-decoration:underline;text-underline-offset:3px}
.keys{background:var(--cbg);border-radius:8px;padding:12px 14px}
.keys h3{font-size:15px;margin-bottom:6px}
.keys ul{padding-left:18px;display:flex;flex-direction:column;gap:3px;font-size:15px}
details.card{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--c);border-radius:8px}
details.card.lec{border-left-color:var(--lec)}
details.card>summary{list-style:none;cursor:pointer;padding:12px 40px 12px 14px;display:flex;align-items:center;flex-wrap:wrap;gap:4px 10px;font-weight:700;font-size:16.5px;position:relative}
details.card>summary::-webkit-details-marker{display:none}
details.card>summary::after{content:"";position:absolute;right:16px;top:18px;width:8px;height:8px;border-right:2px solid var(--faint);border-bottom:2px solid var(--faint);transform:rotate(45deg);transition:transform .15s}
details.card[open]>summary::after{transform:rotate(-135deg)}
.src{font-size:12.5px;font-weight:400;color:var(--faint)}
.body{padding:0 14px 14px;display:flex;flex-direction:column;gap:8px;font-size:15.5px}
.body ul{padding-left:20px;display:flex;flex-direction:column;gap:3px}
.body li.sub{margin-left:18px;list-style:circle}
.body b{font-weight:700;background:linear-gradient(transparent 55%,var(--hl) 55%);padding:0 1px}
.body th b{background:none}
.body .cap{font-size:13.5px;font-weight:700;color:var(--muted);margin-top:4px}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:6px}
.tw table{border-collapse:collapse;width:100%;font-size:14px;min-width:520px}
.tw th,.tw td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}
.tw tr:last-child td{border-bottom:0}
.tw th{background:var(--soft);font-weight:700}
.tw td:first-child{font-weight:700}
figure{margin:0;text-align:center}
figure img{max-width:100%;height:auto;border-radius:6px;border:1px solid var(--line);background:#fff}
.recall{background:var(--surface);border:1px dashed var(--line);border-radius:8px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.recall h3{font-size:16px}.recall .hint{font-size:14px;color:var(--muted)}
.qa{border-top:1px solid var(--line);padding-top:8px}
.qa button{font:inherit;font-size:15px;text-align:left;width:100%;color:var(--ink);background:none;border:0;padding:0;cursor:pointer;display:flex;gap:10px;align-items:flex-start}
.qa button::before{content:"Show";flex:none;font-size:12px;font-weight:700;color:var(--c);border:1.5px solid var(--c);border-radius:5px;padding:1px 6px;margin-top:2px}
.qa button[aria-expanded="true"]::before{content:"Hide"}
.qa .ans{margin-top:6px;padding:8px 10px;background:var(--cbg);border-radius:6px;font-size:15px}
.qa .ans[hidden]{display:none}
body.searching .keys,body.searching .recall,body.searching .phead .linkbtn{display:none}
body.searching .panel{display:flex !important}
.empty{color:var(--muted);font-size:15px}
.hidden{display:none !important}
@media (max-width:620px){.tw table{min-width:440px}
  .tabs{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;margin:0 -16px;padding:0 16px 2px;-webkit-overflow-scrolling:touch}
  .tabs::-webkit-scrollbar{display:none}.tabs button{flex:none}}
figure a{display:block}
figure figcaption{font-size:12.5px;color:var(--faint);margin-top:4px}
@media (prefers-reduced-motion:reduce){details.card>summary::after{transition:none}}
"""

JS = """
(function(){
  const tabs=[...document.querySelectorAll('.tabs [role="tab"]')], panels=[...document.querySelectorAll('.panel')];
  const KEY="differential-b4-tab-"+document.body.dataset.w, q=document.getElementById("q"), count=document.getElementById("count");
  function show(t,focus){ tabs.forEach(x=>{ const on=x===t; x.setAttribute("aria-selected",on); x.tabIndex=on?0:-1;
    document.getElementById(x.getAttribute("aria-controls")).hidden=!on; }); if(focus) t.focus(); t.scrollIntoView({block:"nearest",inline:"nearest"}); try{ localStorage.setItem(KEY,t.id); }catch(e){} }
  tabs.forEach((t,i)=>{ t.onclick=()=>{ q.value=""; search(); show(t); };
    t.onkeydown=e=>{ const d=e.key==="ArrowRight"?1:e.key==="ArrowLeft"?-1:0; if(d){ e.preventDefault(); show(tabs[(i+d+tabs.length)%tabs.length],true); } }; });
  try{ const s=document.getElementById(localStorage.getItem(KEY)); if(s && tabs.includes(s)) show(s); }catch(e){}
  document.querySelectorAll("[data-all]").forEach(b=>{ const cards=[...b.closest(".panel").querySelectorAll("details.card")];
    const sync=()=>{ b.textContent=cards.every(c=>c.open)?"Close all":"Open all"; };
    b.onclick=()=>{ const open=!cards.every(c=>c.open); cards.forEach(c=>c.open=open); sync(); };
    cards.forEach(c=>c.addEventListener("toggle",sync)); sync(); });
  document.querySelectorAll(".qa button").forEach(b=>{ b.onclick=()=>{ const a=b.nextElementSibling, open=a.hidden; a.hidden=!open; b.setAttribute("aria-expanded",open); }; });
  const cards=[...document.querySelectorAll("details.card")];
  function search(){
    const s=q.value.trim().toLowerCase();
    if(!s){ document.body.classList.remove("searching"); cards.forEach(c=>c.classList.remove("hidden"));
      panels.forEach(p=>p.querySelector(".phead").classList.remove("hidden")); count.textContent="";
      const cur=tabs.find(t=>t.getAttribute("aria-selected")==="true")||tabs[0]; show(cur); return; }
    document.body.classList.add("searching"); let n=0;
    cards.forEach(c=>{ const hit=c.dataset.text.includes(s); c.classList.toggle("hidden",!hit); if(hit){ n++; c.open=true; } });
    panels.forEach(p=>p.querySelector(".phead").classList.toggle("hidden",!p.querySelector("details.card:not(.hidden)")));
    count.textContent=n?`${n} card${n===1?"":"s"}`:"No matches";
  }
  q.addEventListener("input",search);
})();
"""

THEME = """(function(){const r=document.documentElement;function theme(){let t=null;try{t=localStorage.getItem("theme");}catch(e){}
r.dataset.theme=t||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light");}theme();addEventListener("storage",theme);})();"""


def plain(h):
    return html.unescape(re.sub(r"<[^>]+>", " ", h))


def keylist(card_html):
    """Bullets that open with a bold term then a colon: Nicole's definitions."""
    out = []
    for m in re.finditer(r"<li>(<b>[^<]{2,60}</b>\s*(?:\([^)]*\)\s*)?:\s*.*?)</li>", card_html):
        t = m.group(1)
        if len(plain(t)) < 240:
            out.append(t)
    return out


def card_block(item, open_):
    kind, x = item
    if kind == "notes":
        c = CARDS[x]
        body = c["html"].replace("FIGDIR", FIGDIR)
        # This header cell sits outside the table area in the PDF, so pdfplumber misses it
        body = body.replace("<th><b>COVID-19 Vaccine Hesitancy Factor</b></th><th></th>", "<th><b>COVID-19 Vaccine Hesitancy Factor</b></th><th><b>Reasoning</b></th>")
        # Tap a figure to open it full size
        body = re.sub(r'<figure><img src="([^"]+)"([^>]*)></figure>', r'<figure><a href="\1" target="_blank" rel="noopener"><img src="\1"\2></a><figcaption>Tap to enlarge</figcaption></figure>', body)
        head = html.escape(c["heading"].rstrip(":"))
        src = f'<span class="src">Nicole\'s Notes p. {c["page"]}</span>'
        cls = "card"
        text = (c["heading"] + " " + c["text"]).lower()
    else:
        body, head = x["body"], html.escape(x["title"])
        src = f'<span class="chip">From the lectures</span><span class="src">{html.escape(x["src"])}</span>'
        cls = "card lec"
        text = (x["title"] + " " + plain(x["body"])).lower()
    text = re.sub(r"\s+", " ", text).replace('"', "&quot;")
    return f'<details class="{cls}" data-text="{text}"{" open" if open_ else ""}><summary>{head} {src}</summary><div class="body">{body}</div></details>'


def render(w, pg):
    o = ['<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
         f"<title>Week {w} Summary</title>",
         '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@400;600;700&display=swap">',
         "<!-- Generated by scripts/summaries/build_b4.py from Nicole's Notes and the week's lectures. Edit that script, not this file. -->",
         f"<style>{CSS}</style></head><body data-w=\"{w}\">", f"<script>{THEME}</script>", '<div class="wrap">',
         f'<header><h1>{pg["title"]}</h1><p class="lede">Every topic from Nicole\'s Notes and the Week {w} lectures. Pick a topic, open a card, then test yourself with the quick recall at the end.</p>'
         '<div class="legend"><span><b style="background:linear-gradient(transparent 55%,var(--hl) 55%)">Highlighted</b> = bold in Nicole\'s Notes</span><span><span class="chip">From the lectures</span> = not in Nicole\'s Notes</span></div>'
         f'<details class="lectures"><summary>Lectures this week</summary><ul>' + "".join(f"<li>{html.escape(l)}</li>" for l in LECTURES[w]) + "</ul></details></header>",
         '<div class="bar"><div class="search"><input id="q" type="search" placeholder="Search this week, e.g. qSOFA or acyclovir" aria-label="Search this week"><span class="count" id="count" aria-live="polite"></span></div>',
         '<div class="tabs" role="tablist" aria-label="Topics">' + "".join(
             f'<button role="tab" id="t-{k}" aria-controls="p-{k}" aria-selected="{str(i == 0).lower()}"{"" if i == 0 else " tabindex=\"-1\""}>{html.escape(lbl)}</button>'
             for i, (k, lbl, _) in enumerate(pg["tabs"])) + "</div></div>"]
    for i, (k, lbl, items) in enumerate(pg["tabs"]):
        o.append(f'<section class="panel" id="p-{k}" role="tabpanel" aria-labelledby="t-{k}"{"" if i == 0 else " hidden"}>')
        o.append(f'<div class="phead"><h2>{html.escape(lbl)}</h2><button class="linkbtn" data-all>Open all</button></div>')
        keys = []
        for it in items:
            if it[0] == "notes":
                keys += keylist(CARDS[it[1]]["html"])
        if keys:
            o.append('<div class="keys"><h3>Key definitions</h3><ul>' + "".join(f"<li>{x}</li>" for x in keys[:10]) + "</ul></div>")
        for j, it in enumerate(items):
            o.append(card_block(it, j == 0))
        if R.get(k):
            o.append('<div class="recall"><h3>Quick recall</h3><p class="hint">Answer in your head, then check.</p>' + "".join(
                f'<div class="qa"><button aria-expanded="false">{html.escape(a)}</button><p class="ans" hidden>{html.escape(b)}</p></div>' for a, b in R[k]) + "</div>")
        o.append("</section>")
    o.append(f"</div><script>{JS}</script></body></html>\n")
    return "\n".join(o)


if __name__ == "__main__":
    (SITE / FIGDIR).mkdir(exist_ok=True)
    for f in (HERE / "figs").glob("*.webp"):  # figures already live in quartz/static/pages/b4figs
        shutil.copy(f, SITE / FIGDIR / f.name)
    used = set()
    for w, pg in PAGES.items():
        (SITE / f"week-{w}-summary.html").write_text(render(w, pg))
        for _, _, items in pg["tabs"]:
            used |= {i for k, i in items if k == "notes"}
        print("wrote", f"week-{w}-summary.html")
    missing = [f"{i} {CARDS[i]['heading']}" for i in range(len(CARDS)) if i not in used]
    print("notes cards not placed:", missing or "none")
