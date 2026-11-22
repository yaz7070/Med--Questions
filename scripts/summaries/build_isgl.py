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
            "Introduced by <b>Clance and Imes in 1978</b>. High-achieving women credited their success to luck, not their talents or qualifications.",
            "About <b>70%</b> of men and women feel it at some point.",
            "A form of <b>inaccurate self-assessment</b>, linked to <b>perfectionism</b>.",
            "Common in medicine because of its high-stakes, evaluative culture.",
        )),
        card("Triggers and why medicine is at risk", ul(
            "<b>Triggers:</b> poor performance or errors, followed by guilt, anxiety and self-doubt.",
            "The profession does a poor job of preparing physicians to manage errors or seek support.",
        )),
        card("Consequences", ul(
            "Psychological wellbeing", "Burnout", "Clinical performance", "Career advancement",
            "Effectiveness as a teacher", "Support for learners and peers",
        )),
        card("How to recognize it", sub("Signs") + ul(
            "Credits success to luck, not ability.",
            "Fears peers will find out they are not good enough.",
            "Anxious about every assessment, even low-stakes or formative ones.",
            "Withdraws from peers and goes quiet.",
            "Deflects compliments and discounts praise.",
        ) + sub("Risk factors") + ul(
            "A non-traditional path into medicine or a prior rejection",
            "Feeling different from peers (age, school, background)",
            "Comparing yourself to peers who seem to answer easily",
            "Big transitions, such as starting medical school",
        )),
        card("The imposter cycle", '<ol class="cycle"><li>Task</li><li>Anxiety</li><li>Over-prepare or procrastinate</li><li>Success</li><li>Credit goes to luck or effort</li><li>Praise discounted</li><li class="loop">Fraud feeling grows, repeat</li></ol>', OUT),
        card("Reducing its effects", ol(
            "Check in on a peer privately and casually.",
            "Listen first. Don't rush to fix it.",
            "Normalize it by sharing your own self-doubt.",
            "Point to concrete evidence of competence.",
            "Point to supports. Escalate for signs of depression or safety concerns.",
        ) + pairs(
            ("Students", "Schulich Learner Experience Office personal counselling."),
            ("Physicians", "CMA Physician Wellness Hub."),
        ), OUT),
        card("Likely test angles", ul(
            "Imposter syndrome is an <b>inaccurate</b> self-assessment. Low confidence that matches real performance is not imposter syndrome.",
            "It is not a diagnosis. Burnout is one of its consequences. Depression or safety concerns need escalation, not just reassurance.",
            "Errors are the classic trigger, so healthy error disclosure and support-seeking protect against it.",
            "It affects how you teach and support others, not only you.",
        ), OUT),
    ],
    recall=[
        ("What kind of self-assessment is imposter syndrome?", "An inaccurate one, linked to perfectionism."),
        ("What triggers it during medical school?", "Poor performance or errors, with guilt, anxiety and self-doubt."),
        ("About what share of people feel it at some point?", "About 70% of men and women."),
        ("Name three consequences for physicians.", "Any three of: worse wellbeing, burnout, weaker clinical performance, slower career advancement, less effective teaching, less support for learners and peers."),
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
            "Privilege is largely a function of luck. Many opportunities come from the context we were born into, not hard work.",
            "Know your patient's context and meet them where they are, so the plan is one they can follow.",
        )),
        card("Implicit bias", ul(
            "<b>Unconscious</b>, and shaped by all your past experiences. Everyone has it.",
            "The space between the biased thought and your reaction is where you have a choice.",
            "<b>Mindfulness:</b> focusing awareness on the present moment while calmly acknowledging feelings, thoughts and bodily sensations.",
            "<b>Sleep restriction increases implicit bias</b> and influences explicit decisions. You resist bias best when rested, fed and hydrated.",
            "The Harvard <b>Implicit Association Test (IAT)</b> helps identify your biases.",
            "Under stress, practise self-compassion and remember most patients are doing what they think is reasonable.",
        )),
        card("When bias acts: System 1 and System 2", pairs(
            ("System 1", "Fast, automatic. Steers most behaviour. Where bias lives."),
            ("System 2", "Slow, deliberate. Can override System 1 when you have the resources."),
        ) + p("Bias acts most under fatigue, stress, hunger, time pressure and heavy cognitive load."), READ),
        card("Reducing bias: 3 strategies", pairs(
            ("Perspective-taking", "Picture the visit from the patient's side, then check it with them."),
            ("Partnership-building", "Use \"we\" and \"let's\", and name shared goals."),
            ("Protect cognitive resources", "Sleep, eat, manage stress, and fix system pressures."),
        ), READ),
        card("What bias does to care", ul(
            "Women are 3 times less likely to be referred for knee replacement when it is indicated.",
            "Black and Hispanic patients get less pain medication despite higher pain scores.",
            "COPD is underdiagnosed in women.",
            "Patients sense bias, so trust, adherence and follow-up drop.",
        ), READ),
        card("SDH: why a good plan fails", ul(
            "<b>SDH</b> are the social and economic conditions that shape health: income, employment and working conditions, caregiving, access to care, transportation, social support, health behaviours.",
            "OHIP covers much of the immediate evaluation, but often not the plan: drugs, physio and other services.",
            "A plan fails when the patient can't afford it, has no benefits, can't take time off work, or can't get to appointments. Ask before you prescribe.",
        )),
        card("Income and coverage supports", ul(
            "Income sources: employment, <b>Ontario Works (OW)</b>, <b>ODSP</b>, <b>CPP Disability</b>, CPP and <b>Employment Insurance (EI)</b>. Some come with drug and health coverage.",
            "<b>WSIB:</b> work injuries. Covers wages, drugs and physio.",
            "<b>Ontario Drug Benefit:</b> 65 and over, under 25 without a private plan (OHIP+), OW or ODSP, long-term care, home care, Trillium.",
            "<b>Trillium:</b> high drug costs relative to income, with an income-based deductible.",
            "<b>OHIP physio:</b> 19 and under, 65 and over, a hospital stay or day surgery in the last 12 months, or OW or ODSP.",
        ), OUT),
        card("Likely test angles: adapting the plan", pairs(
            ("Newcomer, limited English", "Professional interpreter, not family. Plain language and teach-back."),
            ("Substance use disorder", "Avoid diagnostic overshadowing. Non-opioid care first."),
            ("Serious mental illness", "Avoid diagnostic overshadowing. NSAIDs raise lithium levels. Ask about ODSP."),
            ("Older adult with cognitive impairment", "Presume capacity and speak to them directly. Avoid oral NSAIDs. Screen for falls."),
            ("No benefits, can't miss work", "Lower-cost options, check coverage programs, flexible follow-up."),
        ), OUT),
    ],
    recall=[
        ("Where do you have a choice when implicit bias kicks in?", "In the space between the biased thought and your reaction."),
        ("What does sleep restriction do to implicit bias?", "Increases it and influences explicit decisions."),
        ("Name the three strategies to reduce bias.", "Perspective-taking, partnership-building, protecting cognitive resources."),
        ("Which drug program covers work injuries, including wages and physio?", "WSIB."),
    ],
)

# =====================================================================
# Week 12: Environmental impact on health (Block 3)
# =====================================================================
W12 = dict(
    id="w12", tab="Week 12", short="Environment", title="Environment and health",
    goal="Describe how environmental and climate concerns contribute to or trigger illness, identify vulnerable patient groups, and prescribe healthy choices that help both patient and local environment.",
    cards=[
        card("Core idea", ul(
            "Climate change is causing unprecedented impacts on human health.",
            "Physicians are at the front line of assessing and managing the direct and indirect effects of planetary health on patients.",
        )),
        card("Climate and vector-borne disease", ul(
            "Warmer temperatures expand the range and season of vectors such as ticks and mosquitoes.",
            "<b>Lyme disease</b> (tick-borne) is the classic Canadian example. Think of it with fever, myalgias, arthralgias and a large expanding circular rash (<b>erythema migrans</b>) after time outdoors in a tick area.",
            "Other climate-linked infections in Canada include West Nile virus.",
            "Temperature extremes also cause heat illness and worsen chronic disease.",
        ), OUT),
        card("Environmental and occupational exposures", pairs(
            ("Ultraviolet light", "Skin cancer, including melanoma. Sun protection counselling."),
            ("Herbicides and pesticides", "Linked to some cancers and other illness. Ask about agricultural and occupational exposure."),
            ("Solvents", "Occupational exposure in labs and industry. Linked to some cancers."),
        ) + p("Take an occupational and environmental history: where the patient works, lives and spends time."), OUT),
        card("Who is most vulnerable", ul(
            "Older adults and young children",
            "People with chronic disease (heart, lung, kidney)",
            "Outdoor and agricultural workers",
            "People with low income or unstable housing",
            "Pregnant people",
        ), OUT),
        card("Diseases of public health significance", ul(
            "Certain diseases must be reported to public health by law. Lyme disease is one.",
            "Reporting drives surveillance and lets public health act.",
        ), OUT),
        card("What you can do", sub("With patients: climate resilience") + ul(
            "Heat warnings, hydration and cooling plans for high-risk patients.",
            "Tick checks, repellent and sun protection.",
            "Healthy choices that also help the environment: active transport (walking, cycling), a plant-rich diet.",
        ) + sub("Your clinic or hospital") + ul(
            "Cut waste and energy use. Choose lower-carbon options, such as inhalers with a lower carbon footprint where suitable.",
        ) + sub("Advocacy") + ul(
            "Speak up for policies that protect your patients' current and future health.",
        ), OUT),
        card("Likely test angles", ul(
            "Fever, lymphadenopathy and a large circular rash after camping: Lyme disease, reportable to public health.",
            "Differential for fever with lymphadenopathy in a young adult: mono, cat scratch disease, STIs, lymphoma, local skin infection.",
            "Link a disease to its environmental driver: temperature to vectors, UV to skin cancer, pesticides and solvents to cancer.",
            "Name a vulnerable group and a prescription that helps both patient and planet.",
        ), OUT),
    ],
    recall=[
        ("How does climate change affect tick-borne disease?", "Warmer temperatures expand tick range and season, raising Lyme disease risk."),
        ("What rash suggests Lyme disease?", "Erythema migrans: a large, expanding, red circular rash."),
        ("Name the three exposures the module highlights.", "UV light, herbicides and pesticides, and solvents."),
        ("Give one healthy choice that helps both patient and environment.", "Active transport (walking, cycling) or a plant-rich diet."),
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
            "<b>Disability is not a tragedy, but a difference.</b>",
            "Disability, stigma and system barriers affect access to safe, equitable, patient-centred care.",
        )),
        card("Communication", ul(
            "Greet with respect, attend to comfort and the need for an interpreter, and orient the patient to the interview.",
            "Use communication aids: communication boards and books, social stories, interpreters, American Sign Language.",
            "Bring in health care navigators and patient advocates for other barriers.",
            "<b>Speak to the patient first.</b> Include support workers with the patient's permission.",
            "Use appropriate nonverbal communication: positioning, posture, facial expression.",
            "Use clear language, check understanding, and clarify.",
            "Build a shared plan with the patient, family and other professionals.",
        )),
        card("Agitation and challenging behaviour", ul(
            "Treat it as communication. It may reflect communication barriers, <b>pain</b>, fear, sensory overload, environmental stressors, unmet needs or underlying illness.",
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
            "Capacity is <b>specific to each treatment decision</b> and can change over time.",
        )),
        card("Bias and anti-oppressive care", ul(
            "Reflect on your assumptions about people with disabilities, and how your values shape your communication.",
            "Recognize the effects of stigma and discrimination on groups facing health inequities: race, ethnicity, immigration, income, religion, disability, gender identity, sexual orientation, weight and substance use.",
            "Know your limits of competence.",
        )),
        card("Likely test angles", ul(
            "A patient with a disability arrives with a support worker. Who do you address first? The patient.",
            "A non-verbal patient becomes agitated. First think pain or another unmet need, not \"behaviour\".",
            "Disability does not mean incapacity. Assess capacity for each decision.",
            "Diagnostic overshadowing: don't blame new symptoms on the disability.",
            "Screening and prevention still apply, and abuse and neglect risk is higher.",
        ), OUT),
    ],
    recall=[
        ("Name four things agitation may reflect.", "Any four of: communication barriers, pain, fear, sensory overload, environmental stressors, unmet needs, underlying illness."),
        ("Who do you speak to first, the patient or the support worker?", "The patient."),
        ("Is capacity global or decision-specific?", "Decision-specific, and patients are presumed capable."),
        ("Name the two critical findings for adults with developmental disabilities.", "Level of intellectual and adaptive functioning, and risk factors for abuse and neglect."),
    ],
)

# =====================================================================
# Week 14: Vaccination and public health (Block 4)
# =====================================================================
W14 = dict(
    id="w14", tab="Week 14", short="Vaccines", title="Vaccination and public health",
    goal="Counsel patients and families about vaccines and hesitancy, using patient-centred communication, informed consent, advocacy and public health principles.",
    cards=[
        card("What the module expects you to do", ul(
            "Assess immunization status and recommend a schedule, including catch-up.",
            "Get an immunization history, including precautions and contraindications.",
            "Explain how vaccines work and obtain informed consent.",
            "Tell patients and families about possible reactions.",
            "Counsel those who refuse.",
            "Find patients who would benefit but don't come for routine visits.",
            "Report and manage adverse reactions.",
        )),
        card("Vaccine hesitancy", ul(
            "<b>Delay in accepting, or refusing, vaccines despite available services.</b>",
            "Most hesitant parents under-immunize. <b>3%</b> of parents refuse outright.",
        ) + sub("Common causes") + ul(
            "Safety concerns", "Misinformation on social media and online", "Mistrust of institutions",
            "Prior negative health care experiences", "Cultural beliefs", "Trouble accessing care",
        ), NOTES),
        card("Counselling approach", ul(
            "Prepare before the visit and set aside extra time.",
            "Use presumptive and motivational interviewing techniques to find the specific concern.",
            "Use simple, clear language for disease risks and vaccine benefits and risks.",
            "Address pain and needle fear head on.",
            "<b>Don't dismiss vaccine refusers</b> from your practice.",
            "Herd immunity does not guarantee personal protection.",
        ), NOTES),
        card("Adverse events (AEFI)", ul(
            "An unwanted or unexpected health effect within <b>6 weeks</b> of immunization. It may or may not be caused by the vaccine.",
            "Causes: a vaccine component (allergy), a defective product, the vaccination process (error or anxiety, such as syncope), or something unrelated.",
            "Expected effects: sore arm, mild fever, fatigue.",
            "Frequency scale: very common 10% or more, common 1 to 10%, uncommon 0.1 to 1%, rare 1 to 10 per 10,000, very rare under 1 per 10,000.",
            "<b>MMR:</b> febrile seizures 3 to 9 per 10,000, thrombocytopenia 2 to 3 per 100,000, anaphylaxis 3 to 10 per million.",
        ) + sub("Reporting") + ul(
            "<b>Mandatory</b> for providers who give vaccines, under s.38 of the Health Protection and Promotion Act.",
            "Send the AEFI form to the <b>local public health unit</b>.",
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
            "Health Canada approves vaccines that are safe, work, meet manufacturing standards and have benefits that outweigh risks.",
            "Trials: phase I (tens of volunteers), II (hundreds), III (tens of thousands).",
            "Governments coordinate purchase and distribution. Monitoring continues after approval.",
        ), NOTES),
        card("Outbreak steps", ol(
            "Verify the outbreak", "Confirm the diagnosis", "Assemble the team", "Define and find cases",
            "Orient the data by person, place and time", "Generate hypotheses", "Test hypotheses",
            "Implement prevention and control", "Communicate the findings", "Debrief the team",
        ), NOTES),
        card("Ontario funding, schools and consent", ul(
            "Routine vaccines are publicly funded through Ontario's immunization schedule.",
            "Public health units run Grade 7 school clinics for HPV, meningococcal and hepatitis B.",
            "School attendance requires certain vaccines, with medical or conscience exemptions. Exempt students can be excluded during outbreaks.",
            "Ontario has no fixed age of consent for treatment. A capable child can consent to their own vaccines.",
        ), OUT),
        card("Likely test angles", ul(
            "Hesitant versus refusing: most hesitant parents under-immunize, only 3% refuse.",
            "Mild fever and a sore arm the day after a vaccine: expected, reassure. Anaphylaxis within minutes: epinephrine.",
            "An AEFI is reported on a temporal link. You don't need proof the vaccine caused it.",
            "Measles contact: vaccine within 72 hours, or immune globulin within 4 to 6 days for high-risk contacts.",
            "Delayed vaccines (pandemic, moving, poor access): plan catch-up, don't restart the series.",
        ), OUT),
    ],
    recall=[
        ("What is the time window for an AEFI?", "Within 6 weeks of immunization."),
        ("Measles contact, immunocompetent, over 6 months. What and by when?", "MMR vaccine within 72 hours."),
        ("Who do you send an AEFI report to?", "The local public health unit."),
        ("Can a capable 11-year-old consent to their own vaccine in Ontario?", "Yes. Ontario has no fixed age of consent for treatment."),
    ],
)


# One ISGL summary per block, holding that block's weeks.
PAGES = {
    2: dict(weeks=[W8], intro="Key points from the Block 2 ISGL sessions on file."),
    3: dict(weeks=[W9, W10, W12], intro="Core concepts and likely test angles from the Block 3 ISGL sessions. No Week 11 module is on file yet."),
    4: dict(weeks=[W13, W14], intro="Core concepts and likely test angles from the Block 4 ISGL sessions."),
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
.tabs.many{display:grid;grid-template-columns:repeat(3,minmax(0,1fr))}
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
        out.append(f'<div class="tabs{" many" if len(weeks) > 3 else ""}" role="tablist" aria-label="Weeks">' + "".join(
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
