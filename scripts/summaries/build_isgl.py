"""Build the ISGL summary pages (quartz/static/pages/block-N-isgl-summary.html).

Sources: the ISGL student modules (Weeks 8, 9, 10, 12, 13, 14). Untagged lines come from
the module text itself. Tags mark everything else:
  READ = an assigned reading (HCCA, CPSO, van Ryn and so on)
  NOTES = Nicole's Notes
  OUT = outside the module and its readings (Ontario government pages, general knowledge)
Run: python3 scripts/summaries/build_isgl.py
"""
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
OUT_DIR = ROOT / "quartz" / "static" / "pages"

READ, NOTES, OUT = "read", "notes", "out"
TAG_TEXT = {READ: "Assigned reading", NOTES: "Nicole's Notes", OUT: "Outside the module"}


def tag(kind):
    return f'<span class="tag t-{kind}">{TAG_TEXT[kind]}</span>'


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def pairs(*rows):
    return '<dl class="pairs">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows) + "</dl>"


def p(t, cls=""):
    return f'<p class="{cls}">{t}</p>' if cls else f"<p>{t}</p>"


def sub(t):
    return f'<p class="sub">{t}</p>'


def card(title, body, src=None):
    cls = f"card c-{src}" if src else "card"
    t = f"{title} {tag(src)}" if src else title
    return {"cls": cls, "title": t, "body": body}


# =====================================================================
# Week 8: Capacity and consent (Block 2)
# =====================================================================
W8 = dict(
    id="w8", tab="Week 8", short="Consent", title="Capacity and consent",
    goal="Apply the Health Care Consent Act (HCCA): when consent is needed, how to judge capacity, what makes consent valid, and who decides when the patient can't.",
    cards=[
        card("The case: Doris, 83", ul(
            "Alzheimer's disease. Her daughter Maria, a high school principal, comes to visits.",
            "<b>Clinic:</b> pain since a fall. Ibuprofen was increased and Tylenol #3 added. Bloodwork shows type 2 diabetes, so you prescribe metformin, suggest stopping Tylenol #3 and offer physio. Maria says Doris dislikes appointments and Maria has little time to drive her.",
            "<b>Hospital:</b> floridly delirious, with fluctuating cognition. Wants to go home and refuses treatment. The team thinks she may need the ICU for urgent dialysis.",
            "The EMR lists her other daughter, Lisa, as Power of Attorney for Personal Care. No other documentation exists.",
            "Doris has told everyone she would not want ICU care or dialysis in hospital.",
        )),
        card("When consent applies (s.2)", ul(
            "<b>Treatment</b> is anything done for a therapeutic, preventive, palliative, diagnostic, cosmetic or other health-related purpose. It includes a plan of treatment.",
            "<b>Not treatment:</b> assessing capacity, taking a history, examining, sharing an assessment or diagnosis, hospital admission, personal assistance, and treatment that poses little or no risk.",
            "In the case: bloodwork, metformin, stopping Tylenol #3, physio, and ICU with dialysis each need consent.",
        ), READ),
        card("Capacity (s.4 and s.15)", ul(
            "Two parts. The person can <b>understand</b> the information relevant to the decision, and <b>appreciate</b> the reasonably foreseeable consequences of deciding or not deciding.",
            "<b>Presume capacity</b> unless you have reasonable grounds to think otherwise.",
            "Capacity is specific to each treatment and can change over time. Delirium fluctuates, so reassess.",
        ), READ),
        card("When family does the talking", ul(
            "Seek consent from a capable patient before involving family.",
            "Keep the patient's wishes as the priority while you work with family. Protect confidentiality and autonomy.",
            "Include the patient and family in the care team, with shared decision-making where it fits.",
        )),
        card("Valid consent (s.11)", ul(
            "Four elements: it relates to the treatment, it is <b>informed</b>, it is <b>voluntary</b>, and it is not obtained through misrepresentation or fraud.",
            "<b>Informed</b> means the patient gets the nature of the treatment, expected benefits, material risks, material side effects, alternatives, and the likely consequences of no treatment, and gets answers to their questions.",
            "Consent can be express or implied.",
        ), READ),
        card("Substitute decision-makers (s.20)", ol(
            "Guardian of the person",
            "Attorney for personal care (POA)",
            "Representative appointed by the Consent and Capacity Board (CCB)",
            "Spouse or partner",
            "Child or parent",
            "Parent with right of access only",
            "Brother or sister",
            "Any other relative",
        ) + ul(
            "The SDM must be capable, at least 16 (unless they are the patient's parent), available and willing, and not barred by a court order.",
            "The Public Guardian and Trustee decides when no one qualifies, or when equal-ranked SDMs disagree.",
        ), READ),
        card("How the SDM decides (s.21)", ol(
            "Follow a <b>prior capable wish</b> that applies to the situation, expressed when the patient was 16 or older.",
            "If there is none, or it can't be followed, decide in the patient's <b>best interests</b>: their values and beliefs, current wishes, and whether the benefit outweighs the risk.",
        ) + ul(
            "Prior wishes come before best interests. In the case, Doris's wish against ICU care and dialysis guides her SDM.",
            "If an SDM ignores a prior wish, the health practitioner can apply to the CCB.",
        ), READ),
        card("Emergencies (s.25)", ul(
            "You may treat without consent when a delay would prolong severe suffering or risk serious bodily harm.",
            "Not if you know the person refused that treatment while capable.",
        ), READ),
        card("POA documentation", ul(
            "A power of attorney for personal care must be in writing, signed and witnessed. An EMR entry alone is not proof, so ask to see the document.",
        ), OUT),
    ],
    recall=[
        ("What are the two parts of the capacity test?", "Understanding the relevant information, and appreciating the reasonably foreseeable consequences of the decision."),
        ("What comes first for an SDM: prior capable wishes or best interests?", "Prior capable wishes that apply to the situation. Best interests only when there are none."),
        ("Two equal-ranked SDMs can't agree. Who decides?", "The Public Guardian and Trustee."),
    ],
)

# =====================================================================
# Week 9: Imposter syndrome (Block 3)
# =====================================================================
W9 = dict(
    id="w9", tab="Week 9", short="Imposters", title="Imposter syndrome",
    goal="Explain imposter syndrome, see its relevance to your career, identify and reduce its effects, and know the supports.",
    cards=[
        card("What it is", ul(
            "Introduced by Clance and Imes in 1978. Many high-achieving women credited their success to luck, not their talents or qualifications.",
            "About 70% of men and women feel it at some point.",
            "A form of <b>inaccurate self-assessment</b>, linked to perfectionism.",
            "Common in medicine because of its high-stakes, evaluative culture.",
            "<b>Triggers:</b> poor performance or errors, with guilt, anxiety and self-doubt.",
            "The profession does a poor job of preparing physicians to manage errors or seek support.",
        )),
        card("Consequences", ul(
            "Psychological wellbeing", "Burnout", "Clinical performance", "Career advancement",
            "Effectiveness as a teacher", "Support for learners and peers",
        )),
        card("The case: Samantha", sub("Evidence of imposter syndrome") + ul(
            "Felt relieved and lucky to pass her first exam.",
            "Spent winter break exhausted, worrying about how she did.",
            "Afraid her peers would find out she wasn't good enough.",
            "Grew more reserved and pulled away from peers.",
            "Anxious about every assignment and quiz, formative or not.",
        ) + sub("Risk factors") + ul(
            "Rejected on her first application with no interviews, and no Master's spot.",
            "Worked as a data entry clerk and banquet server before getting in.",
            "Hard transition back to school.",
            "Older than her peers, from a smaller university outside Ontario.",
            "Felt she couldn't fit in, and compared herself to peers who answered easily.",
        )),
        card("The imposter cycle", '<ol class="cycle"><li>Task</li><li>Anxiety</li><li>Over-prepare or procrastinate</li><li>Success</li><li>Credit goes to luck or effort</li><li>Praise discounted</li><li class="loop">Fraud feeling grows, repeat</li></ol>', OUT),
        card("Helping a peer", sub("Signs") + p("Goes quiet in small group, skips social events, puts themselves down, deflects compliments, gets anxious over low-stakes tasks.") + ol(
            "Check in privately and casually.",
            "Listen first. Don't rush to fix it.",
            "Normalize it by sharing your own self-doubt.",
            "Point to evidence of their competence.",
            "Point them to supports. Escalate to the Learner Experience Office (LEO) or faculty for signs of depression or safety concerns.",
        ), OUT),
        card("Supports", pairs(
            ("Students", "Schulich Learner Experience Office personal counselling (listed in the module)."),
            ("Physicians", "CMA Physician Wellness Hub (listed in the module)."),
        ) + p(f"{tag(OUT)} Also: Western Wellness and mentors for students, the PARO 24/7 helpline for residents, and the OMA Physician Health Program for physicians.")),
        card("In the session", ul(
            "Give a classmate a genuine, specific compliment, and notice how hard it is to accept one.",
            "Share past experiences of imposter syndrome.",
            "Privately write down 3 things you are great at.",
        )),
    ],
    recall=[
        ("What kind of self-assessment is imposter syndrome?", "An inaccurate one, linked to perfectionism."),
        ("What triggers it during medical school?", "Poor performance or errors, with guilt, anxiety and self-doubt."),
        ("Name three consequences for physicians.", "Any three of: worse psychological wellbeing, burnout, weaker clinical performance, slower career advancement, less effective teaching, less support for learners and peers."),
    ],
)

# =====================================================================
# Week 10: SDH, implicit bias and medical management (Block 3)
# =====================================================================
W10 = dict(
    id="w10", tab="Week 10", short="Bias and SDH", title="Implicit bias and SDH",
    goal="Reduce the impact of implicit bias, use the social determinants of health (SDH) and financial supports to plan care, and lower barriers for underrepresented groups.",
    cards=[
        card("Why it matters", ul(
            "The privilege we experience is largely a function of luck. Many opportunities come from the context we were born into, not hard work.",
            "Know your patient's context and meet them where they are, so the plan is one they can follow.",
        )),
        card("Implicit bias", ul(
            "Unconscious, and informed by all of your past experiences. Don't feel bad about having it. It can't be helped.",
            "The space between the biased thought and your reaction is where you have a choice.",
            "<b>Mindfulness:</b> focusing your awareness on the present moment while calmly acknowledging your feelings, thoughts and bodily sensations.",
            "<b>Sleep matters.</b> Alkozei and colleagues showed sleep restriction increased implicit bias and influenced explicit decisions.",
            "You are least likely to fall victim to bias when well rested, fed and hydrated.",
            "The Harvard <b>Implicit Association Test (IAT)</b> helps identify your biases and guides what to explore next.",
            "Under stress, practise self-compassion and remember most patients are doing what they think is reasonable.",
        )),
        card("The case: Andrea", sub("Your state") + p("Poor sleep, little breakfast, no lunch by 1:30 pm.") + sub("First impressions") + p("Smells of cigarettes, staring at her phone, obese, poor hygiene. Has a family doctor but came to a walk-in for 1 month of low back pain.") + sub("What the history showed") + ul(
            "Feels judged and dismissed by her family doctor, waits 3 to 4 months for 5-minute visits.",
            "No reliable transportation, and the walk-in is closer to home.",
            "Cut down to half a pack a day.",
            "PSW in long-term care, working overtime after staffing cuts, came straight from a shift.",
            "Single mom. Her son had a fever, so she was checking her phone.",
        ) + sub("The plan that failed") + p("Heating pad, NSAIDs and a physio referral. She came back unimproved because she couldn't afford the NSAIDs or physio. She is on probation at work, worried about missing time, and has no health benefits yet.")),
        card("Reducing bias", sub("van Ryn's 3 strategies") + pairs(
            ("Perspective-taking", "Picture the visit from the patient's side, then check it with them."),
            ("Partnership-building", "Use \"we\" and \"let's\", and name shared goals."),
            ("Protect cognitive resources", "Sleep, eat, manage stress, and fix system pressures."),
        ) + sub("System 1 and System 2") + ul(
            "System 1 is fast and automatic and steers most behaviour. System 2 is slow and deliberate.",
            "Bias acts most under fatigue, stress, hunger, time pressure and heavy cognitive load.",
        ), READ),
        card("Bias in care (CPSO examples)", ul(
            "Women are 3 times less likely to be referred for knee replacement when it is indicated.",
            "Black and Hispanic patients get less pain medication despite higher pain scores.",
            "COPD is underdiagnosed in women.",
            "Patients sense bias, so trust, adherence and follow-up drop.",
        ), READ),
        card("SDH and money", ul(
            "OHIP covers much of the immediate evaluation, but often less of the plan.",
            "Income sources to know: employment, Ontario Works (OW), ODSP, CPP Disability (CPPD), CPP and Employment Insurance (EI). Some come with drug and health service coverage.",
        )),
        card("SDH and coverage details", ul(
            "<b>SDH</b> are the social and economic conditions that shape health. In Andrea's case: income, employment and working conditions, caregiving, access to care, social support and smoking.",
            "<b>WSIB:</b> work injuries. Covers wages, drugs and physio.",
            "<b>Ontario Drug Benefit:</b> age 65 and over, under 25 without a private plan (OHIP+), OW or ODSP, long-term care, home care, Trillium.",
            "<b>Trillium:</b> high drug costs relative to income, with an income-based deductible.",
            "<b>OHIP physio:</b> age 19 and under, 65 and over, a hospital stay or day surgery in the last 12 months, or OW or ODSP.",
        ) + p("Ontario government pages, checked Nov 4, 2026.", "note"), OUT),
        card("Changing the patient", p("The module asks how your plan changes for each patient. Suggested answers:") + pairs(
            ("Newcomer, limited English", "Professional interpreter, not family. Plain language and teach-back."),
            ("Opioid use disorder", "Avoid diagnostic overshadowing. Non-opioid care first. Check the Narcotics Monitoring System."),
            ("Schizophrenia or bipolar", "Avoid diagnostic overshadowing. NSAIDs raise lithium levels. Ask about ODSP."),
            ("Age 75 with mild cognitive impairment", "Presume capacity and speak to her directly. Avoid oral NSAIDs. Screen for falls."),
        ), OUT),
    ],
    recall=[
        ("Where do you have a choice when implicit bias kicks in?", "In the space between the biased thought and your reaction."),
        ("What did Alkozei show about sleep restriction?", "It increased implicit bias and influenced explicit decisions."),
        ("Why did Andrea's first plan fail?", "She couldn't afford NSAIDs or physio, had no benefits yet, and was on probation at work."),
    ],
)

# =====================================================================
# Week 12: Environmental impact on health (Block 3)
# =====================================================================
W12 = dict(
    id="w12", tab="Week 12", short="Environment", title="Environment and health",
    goal="Describe how environmental and climate concerns contribute to or trigger illness, identify vulnerable patient groups, and prescribe healthy choices that help both patient and local environment.",
    cards=[
        card("The case: Sarah, 21", ul(
            "University student in the ER with right groin swelling, fatigue and a temperature of 39°C.",
            "Unwell for a week. The lump grew from grape-sized to multiple small strawberry-sized masses. Fevers on and off for 3 days.",
            "Mild headaches, myalgias and arthralgias. Lower appetite.",
            "Summer in a chemistry lab and playing ultimate frisbee. Camped at Pinery Provincial Park 2 weeks ago.",
            "Father had colon cancer in his early 50s. Mother has hypertension and lupus.",
            "<b>Exam:</b> BP 96/60, HR 115, T 38.6°C. Possible mild splenomegaly. Multiple tender, soft, rubbery right groin nodes of 1 to 2 cm, not very mobile. A 5 to 6 cm red, circular rash on the back of her upper leg.",
            "No neck or armpit nodes.",
        )),
        card("Reading the case", ul(
            "<b>Lyme disease</b> fits best. A large circular rash after camping, with fever, is erythema migrans.",
            "<b>Climate link:</b> Pinery is a tick area, and warmer temperatures expand tick range.",
            "<b>Disease of public health significance:</b> Lyme is one, so it must be reported to public health.",
            "<b>Differential:</b> mono, cat scratch disease, STIs, lymphoma, local skin infection.",
            "The lab solvents don't explain her illness.",
        ), OUT),
        card("What the module asks you to discuss", ul(
            "Temperature extremes and changes, and their effect on vector-borne infections.",
            "Environmental and occupational exposure to UV light, certain herbicides and pesticides, and solvents.",
            "Measures in primary care to improve a patient's climate resilience.",
            "How your hospital or clinic can cut its environmental footprint.",
            "How you can advocate for your patients' current and future health.",
        )),
        card("Readings", ul(
            "McCally: environment and health overview",
            "Galanis and Ogden: climate change and emerging diseases",
            "Chekuri and Harper: climate-smart health care and the family physician",
            "Clapp: environment and cancer",
        )),
    ],
    recall=[
        ("Which findings point to a tick-borne cause?", "Camping at Pinery 2 weeks earlier and a large circular rash, with fever, arthralgias and myalgias."),
        ("Which two environmental exposure groups does the module name?", "Temperature changes affecting vector-borne infections, and exposure to UV, herbicides, pesticides and solvents."),
    ],
)

# =====================================================================
# Week 13: People with disabilities (Block 4)
# =====================================================================
W13 = dict(
    id="w13", tab="Week 13", short="Disabilities", title="People with disabilities",
    goal="Give respectful, inclusive, patient-centred care by adapting communication, supporting autonomy and recognizing barriers to equitable care.",
    cards=[
        card("Core idea", ul(
            "Disability is not a tragedy, but a difference.",
            "<b>Gord, 42:</b> cerebral palsy. Uses a custom communication board. Support worker Ryan.",
            "<b>Brandy:</b> cri-du-chat syndrome. Came to the ED after a fall with a suspected head injury. Support worker Denise.",
            "Disability, stigma and system barriers affect access to safe, equitable, patient-centred care.",
        )),
        card("Communication", ul(
            "Greet with respect, attend to comfort and the need for an interpreter, and orient the patient to the interview.",
            "Use communication aids: communication boards and books, social stories, interpreters, American Sign Language.",
            "Bring in health care navigators and patient advocates for other barriers.",
            "Speak to the patient first. Include support workers, with the patient's permission.",
            "Use appropriate nonverbal communication: positioning, posture, facial expression.",
            "Use clear language, check for understanding, and clarify.",
            "Build a shared plan with the patient, family and other professionals.",
        )),
        card("Agitation and challenging behaviour", ul(
            "It may reflect communication barriers, pain, fear, sensory overload, environmental stressors, unmet needs or underlying illness.",
            "Many people with intellectual disabilities find it harder to regulate emotions or say what is wrong.",
            "Long ED waits create extra challenges for people with intellectual and developmental disabilities (IDD).",
        )),
        card("Care for adults with developmental disabilities", sub("Critical findings") + ul(
            "Level of intellectual and adaptive functioning",
            "Risk factors for abuse and neglect",
        ) + sub("Initial management") + ul(
            "Assess ability to give voluntary, informed consent.",
            "Get input and help from caregivers and support workers.",
            "Start interdisciplinary care if needed.",
            "Do screening and prevention, such as for infectious diseases and cancer.",
            "Anticipate medium and long-term complications, such as psychosocial effects and safety.",
        )),
        card("Capacity", ul(
            "Patients are <b>presumed capable</b>.",
            "Capacity is <b>specific to each treatment decision</b>.",
        )),
        card("Bias and anti-oppressive care", ul(
            "Reflect on your assumptions about people with disabilities, and how your values shape your communication.",
            "Recognize the effects of stigma and discrimination on groups facing health inequities, including by race, ethnicity, immigration, income, religion, disability, gender identity, sexual orientation, weight and substance use.",
            "Know your limits of competence.",
        )),
    ],
    recall=[
        ("Name four things agitation may reflect.", "Any four of: communication barriers, pain, fear, sensory overload, environmental stressors, unmet needs, underlying illness."),
        ("Who do you speak to first, the patient or the support worker?", "The patient."),
        ("Is capacity global or decision-specific?", "Decision-specific, and patients are presumed capable."),
    ],
)

# =====================================================================
# Week 14: Vaccination and public health (Block 4)
# =====================================================================
W14 = dict(
    id="w14", tab="Week 14", short="Vaccines", title="Vaccination and public health",
    goal="Counsel patients and families about vaccines and hesitancy, using patient-centred communication, informed consent, advocacy and public health principles.",
    cards=[
        card("The case: Sophie, 11", ul(
            "Due for HPV, a meningococcal booster and catch-up MMR. Vaccines were delayed by COVID-19, and the family moved from a rural area with poor access.",
            "Her mother read online that vaccines cause infertility and developmental problems, thinks HPV is \"too new\" and that kids get \"too many vaccines too early\". A friend's child got fever and fatigue after vaccines.",
            "Sophie is unsure, scared of needles and worried about side effects. Friends told her \"these diseases do not exist anymore\".",
            "<b>Part 2:</b> a measles exposure at school, with possible exclusion for under-vaccinated students. After catch-up shots, Sophie has mild fever, fatigue and a sore arm the next day.",
        )),
        card("Vaccine hesitancy", ul(
            "Delay in accepting, or refusing, vaccines despite available services.",
            "Most hesitant parents under-immunize. 3% of parents refuse outright.",
        ) + sub("Causes named in the module") + ul(
            "Safety concerns", "Misinformation on social media and online", "Mistrust of institutions",
            "Prior negative health care experiences", "Cultural beliefs", "Trouble accessing care",
        ) + sub("Approach") + ul(
            "Prepare before the visit and set aside extra time.",
            "Use presumptive and motivational interviewing techniques to find the specific concern.",
            "Use simple, clear language for disease risks and vaccine benefits and risks.",
            "Address pain head on.",
            "Don't dismiss vaccine refusers from your practice.",
            "Herd immunity does not guarantee personal protection.",
        ), NOTES),
        card("What the module expects you to do", ul(
            "Assess immunization status and recommend a schedule, including catch-up.",
            "Get an immunization history, including precautions and contraindications.",
            "Explain how vaccines work and obtain informed consent.",
            "Tell patients and families about possible reactions.",
            "Counsel those who refuse.",
            "Find patients who would benefit but don't come for routine visits.",
            "Report and manage adverse reactions.",
        )),
        card("Adverse events (AEFI)", ul(
            "An unwanted or unexpected health effect within <b>6 weeks</b> of immunization. It may or may not be caused by the vaccine.",
            "Causes: a vaccine component (allergy), a defective product, the vaccination process (error or anxiety, such as syncope), or something unrelated.",
            "Frequency scale: very common 10% or more, common 1 to 10%, uncommon 0.1 to 1%, rare 1 to 10 per 10,000, very rare under 1 per 10,000.",
            "<b>MMR:</b> febrile seizures 3 to 9 per 10,000, thrombocytopenia 2 to 3 per 100,000, anaphylaxis 3 to 10 per million.",
            "<b>HPV and meningococcal ACYW:</b> no adverse events listed.",
        ) + sub("Reporting") + ul(
            "Mandatory for providers who give vaccines, under s.38 of the Health Protection and Promotion Act.",
            "Fill out the AEFI form and send it to the local public health unit.",
            "Local review, then provincial, then national (PHAC), then WHO. Manufacturers report serious events to Health Canada.",
            "The Vaccine Injury Support Program supports people with serious, permanent injury from a vaccine.",
        ), NOTES),
        card("Measles exposure", ul(
            "<b>Vaccine within 72 hours</b> for immunocompetent contacts over 6 months.",
            "<b>Immune globulin within 4 to 6 days</b> for immunocompromised contacts, pregnant women and infants.",
            "Measles needs airborne precautions in a negative pressure room.",
            "Reportable diseases place legal obligations on clinicians.",
        ), NOTES),
        card("Who regulates vaccines", ul(
            "Health Canada reviews and approves vaccines that are safe, work, meet manufacturing standards and have benefits that outweigh risks.",
            "Trials run in phases: I (tens of volunteers), II (hundreds), III (tens of thousands).",
            "Governments coordinate purchase and distribution. Monitoring continues after approval.",
        ), NOTES),
        card("Outbreak steps", ol(
            "Verify the outbreak", "Confirm the diagnosis", "Assemble the team", "Define and find cases",
            "Orient the data by person, place and time", "Generate hypotheses", "Test hypotheses",
            "Implement prevention and control", "Communicate the findings", "Debrief the team",
        ), NOTES),
        card("Ontario funding and school rules", ul(
            "Routine vaccines are publicly funded through Ontario's immunization schedule.",
            "Public health units run Grade 7 school clinics for HPV, meningococcal and hepatitis B.",
            "School attendance requires certain vaccines, with medical or conscience exemptions. Exempt students can be excluded during outbreaks.",
            "Ontario has no fixed age of consent for treatment. A capable child can consent.",
        ), OUT),
    ],
    recall=[
        ("What is the time window for an AEFI?", "Within 6 weeks of immunization."),
        ("Measles contact, immunocompetent, over 6 months. What and by when?", "MMR vaccine within 72 hours."),
        ("Who do you send an AEFI report to?", "The local public health unit."),
    ],
)


PAGES = {
    2: dict(weeks=[W8], intro="Key points from the Block 2 ISGL sessions on file."),
    3: dict(weeks=[W9, W10, W12], intro="Key points from the Block 3 ISGL sessions. No Week 11 module is on file yet."),
    4: dict(weeks=[W13, W14], intro="Key points from the Block 4 ISGL sessions on file."),
}
COLOURS = {2: ("#4f46c8", "#ecebfb", "#a49df6", "#1e1c38"),
           3: ("#a3246b", "#f8e9f1", "#ef8ec0", "#2c1722"),
           4: ("#a35f08", "#f8eedf", "#e3a548", "#2a2110")}

CSS = """
:root{--bg:#f5f6f8;--surface:#fff;--ink:#15181d;--muted:#4d5560;--faint:#6b7380;--line:#d5dae1;--soft:#eef0f3;
  --c:%s;--cbg:%s;--read:#245b9a;--read-bg:#e6eef8;--notes:#0b6f6a;--notes-bg:#e3f3f1;--out:#9a3412;--out-bg:#fbe9df;
  --font:"Atkinson Hyperlegible Next","Segoe UI",system-ui,-apple-system,sans-serif}
:root[data-theme="dark"]{--bg:#14161a;--surface:#1b1e24;--ink:#eceef2;--muted:#b3bac5;--faint:#8d95a1;--line:#353b45;--soft:#23272e;
  --c:%s;--cbg:%s;--read:#93b9ec;--read-bg:#16212f;--notes:#6fd0c7;--notes-bg:#12292a;--out:#f4a37a;--out-bg:#33201a;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);font-size:16px;line-height:1.5;
  padding:20px max(16px,env(safe-area-inset-right,0px)) 48px max(16px,env(safe-area-inset-left,0px))}
.wrap{max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:18px}
h1,h2,h3,p,ul,ol,dl{margin:0}
header h1{font-size:clamp(26px,4vw,32px);line-height:1.15}
header p{color:var(--muted);margin-top:6px}
.legend{display:flex;flex-wrap:wrap;gap:6px 12px;margin-top:8px;font-size:14px;color:var(--muted);align-items:center}
.tag{display:inline-block;font-size:12px;font-weight:700;border-radius:4px;padding:1px 6px;vertical-align:2px;white-space:nowrap}
.t-read{color:var(--read);background:var(--read-bg)}.t-notes{color:var(--notes);background:var(--notes-bg)}.t-out{color:var(--out);background:var(--out-bg)}
.tabs{position:sticky;top:0;z-index:5;background:var(--bg);display:flex;gap:6px;padding:8px 0;border-bottom:1px solid var(--line)}
.tabs button{flex:1;min-width:0;font:inherit;font-size:14px;font-weight:700;color:var(--muted);background:var(--surface);border:1.5px solid var(--line);border-radius:8px;padding:7px 8px;cursor:pointer;line-height:1.25}
.tabs button span{display:block;font-weight:400;font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tabs button[aria-selected="true"]{color:var(--c);border-color:var(--c);background:var(--cbg)}
button:focus-visible,summary:focus-visible{outline:2px solid var(--c);outline-offset:2px}
.week{display:flex;flex-direction:column;gap:10px}.week[hidden]{display:none}
.week-head{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
.week-head h2{font-size:22px;color:var(--c)}
.goal{color:var(--muted);font-size:15px}
.linkbtn{font:inherit;font-size:14px;font-weight:700;color:var(--c);background:none;border:0;padding:0;cursor:pointer;text-decoration:underline;text-underline-offset:3px}
details.card{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--c);border-radius:8px}
details.c-read{border-left-color:var(--read)}details.c-notes{border-left-color:var(--notes)}details.c-out{border-left-color:var(--out)}
details.card>summary{list-style:none;cursor:pointer;padding:12px 14px;display:flex;align-items:center;flex-wrap:wrap;gap:4px 10px;font-weight:700;font-size:16.5px;padding-right:36px;position:relative}
details.card>summary::-webkit-details-marker{display:none}
details.card>summary::after{content:"";position:absolute;right:16px;top:18px;width:8px;height:8px;border-right:2px solid var(--faint);border-bottom:2px solid var(--faint);transform:rotate(45deg);transition:transform .15s}
details.card[open]>summary::after{transform:rotate(-135deg)}
.body{padding:0 14px 14px;display:flex;flex-direction:column;gap:8px}
.body ul,.body ol{padding-left:20px;display:flex;flex-direction:column;gap:4px}
.sub{font-size:13.5px;font-weight:700;color:var(--muted);margin-top:4px}
.note{font-size:14px;color:var(--muted)}
.cycle{list-style:none;padding:0 !important;display:flex !important;flex-direction:row !important;flex-wrap:wrap;gap:6px 4px !important}
.cycle li{background:var(--soft);border-radius:6px;padding:4px 9px;font-size:14.5px}
.cycle li:not(:last-child)::after{content:"\\2192";margin-left:8px;color:var(--faint)}
.cycle li.loop{background:var(--cbg);color:var(--c);font-weight:700}
.pairs{display:grid;grid-template-columns:minmax(0,11rem) minmax(0,1fr);gap:8px 14px}
.pairs dt{font-weight:700}.pairs dd{margin:0}
@media (max-width:520px){.pairs{grid-template-columns:1fr;gap:2px}.pairs dd{margin-bottom:8px}}
.recall{background:var(--surface);border:1px dashed var(--line);border-radius:8px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.recall h3{font-size:16px}.recall .hint{font-size:14px;color:var(--muted)}
.qa{border-top:1px solid var(--line);padding-top:8px}
.qa button{font:inherit;font-size:15px;text-align:left;width:100%%;color:var(--ink);background:none;border:0;padding:0;cursor:pointer;display:flex;gap:10px;align-items:flex-start}
.qa button::before{content:"Show";flex:none;font-size:12px;font-weight:700;color:var(--c);border:1.5px solid var(--c);border-radius:5px;padding:1px 6px;margin-top:2px}
.qa button[aria-expanded="true"]::before{content:"Hide"}
.qa .ans{margin-top:6px;padding:8px 10px;background:var(--cbg);border-radius:6px;font-size:15px}
.qa .ans[hidden]{display:none}
@media (prefers-reduced-motion:reduce){details.card>summary::after{transition:none}}
"""

JS = """
(function(){
  const tabs=[...document.querySelectorAll('[role="tab"]')], KEY="differential-isgl-tab-"+document.body.dataset.b;
  function show(t,focus){ tabs.forEach(x=>{ const on=x===t; x.setAttribute("aria-selected",on); x.tabIndex=on?0:-1;
    document.getElementById(x.getAttribute("aria-controls")).hidden=!on; }); if(focus) t.focus();
    try{ localStorage.setItem(KEY,t.id); }catch(e){} }
  tabs.forEach((t,i)=>{ t.onclick=()=>{ show(t); window.scrollTo({top:0}); };
    t.onkeydown=e=>{ const d=e.key==="ArrowRight"?1:e.key==="ArrowLeft"?-1:0; if(d){ e.preventDefault(); show(tabs[(i+d+tabs.length)%tabs.length],true); } }; });
  try{ const s=document.getElementById(localStorage.getItem(KEY)); if(s && tabs.includes(s)) show(s); }catch(e){}
  document.querySelectorAll("[data-all]").forEach(b=>{ const cards=[...b.closest(".week").querySelectorAll("details.card")];
    const sync=()=>{ b.textContent=cards.every(c=>c.open)?"Close all":"Open all"; };
    b.onclick=()=>{ const open=!cards.every(c=>c.open); cards.forEach(c=>c.open=open); sync(); };
    cards.forEach(c=>c.addEventListener("toggle",sync)); sync(); });
  document.querySelectorAll(".qa button").forEach(b=>{ b.onclick=()=>{ const a=b.nextElementSibling, open=a.hidden; a.hidden=!open; b.setAttribute("aria-expanded",open); }; });
})();
"""

THEME = """(function(){const r=document.documentElement;function theme(){let t=null;try{t=localStorage.getItem("theme");}catch(e){}
r.dataset.theme=t||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light");}theme();addEventListener("storage",theme);})();"""


def render(b, page):
    weeks = page["weeks"]
    used = {c["cls"].split("c-")[-1] for w in weeks for c in w["cards"] if "c-" in c["cls"]}
    legend = "".join(f"<span>{tag(k)}</span>" for k in (READ, NOTES, OUT) if k in used)
    out = [f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
           f"<title>Block {b} ISGL Summary</title>",
           '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:wght@400;600;700&display=swap">',
           "<!-- Generated by scripts/summaries/build_isgl.py. Edit that file, not this one. -->",
           f"<style>{CSS % COLOURS[b]}</style></head><body data-b=\"{b}\">", f"<script>{THEME}</script>", '<div class="wrap">',
           f'<header><h1>ISGL Summary</h1><p>{page["intro"]} Tap a card to open it. Untagged lines come from the ISGL modules.</p>'
           f'<div class="legend">{legend}</div></header>']
    if len(weeks) > 1:
        out.append('<div class="tabs" role="tablist" aria-label="Weeks">' + "".join(
            f'<button role="tab" id="t{w["id"]}" aria-controls="{w["id"]}" aria-selected="{str(i == 0).lower()}"{"" if i == 0 else " tabindex=\"-1\""}>{w["tab"]}<span>{w["short"]}</span></button>'
            for i, w in enumerate(weeks)) + "</div>")
    for i, w in enumerate(weeks):
        hidden = "" if i == 0 else " hidden"
        role = f' role="tabpanel" aria-labelledby="t{w["id"]}"' if len(weeks) > 1 else ""
        out.append(f'<section class="week" id="{w["id"]}"{role}{hidden}>')
        out.append(f'<div class="week-head"><h2>{w["tab"]}: {w["title"]}</h2><button class="linkbtn" data-all>Open all</button></div>')
        out.append(f'<p class="goal">{w["goal"]}</p>')
        for j, c in enumerate(w["cards"]):
            out.append(f'<details class="{c["cls"]}"{" open" if j == 0 else ""}><summary>{c["title"]}</summary><div class="body">{c["body"]}</div></details>')
        out.append('<div class="recall"><h3>Quick recall</h3><p class="hint">Answer in your head, then check.</p>' + "".join(
            f'<div class="qa"><button aria-expanded="false">{q}</button><p class="ans" hidden>{a}</p></div>' for q, a in w["recall"]) + "</div>")
        out.append("</section>")
    out.append(f"</div><script>{JS}</script></body></html>\n")
    return "\n".join(out)


for b, page in PAGES.items():
    f = OUT_DIR / f"block-{b}-isgl-summary.html"
    f.write_text(render(b, page))
    print("wrote", f.name)
