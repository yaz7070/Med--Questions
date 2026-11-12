---
title: "Block 3: Hematology"
tags:
  - block-3
description: "Weeks 9 to 12. Anemia, bleeding, myeloid disorders, lymphadenopathy and lymphoid disorders."
---

<p class="block-about">Weeks 9 to 12. Anemia, bleeding, myeloid disorders, lymphadenopathy and lymphoid disorders.</p>

<p class="block-total"><span class="pg-bar wide" aria-hidden="true"><i data-sum-bar="3"></i></span><span data-sum="3"></span><a id="resume" class="resume" hidden></a></p>

<h2 class="section-title">Weekly question banks</h2>
<ul class="sets">
<li><a class="set" href="/fom/block-3/question-bank/week-9-question-bank" data-quiz="week-9-question-bank"><span class="set-name">Week 9</span><span class="set-desc">Microcytic, normocytic, macrocytic and hemolytic anemia, MDS, quality improvement.</span><span class="set-pg"><span class="pg-txt">50 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-3/question-bank/week-10-question-bank" data-quiz="week-10-question-bank"><span class="set-name">Week 10</span><span class="set-desc">Bleeding disorders, Thrombocytopenia, Coagulation tests.</span><span class="set-pg"><span class="pg-txt">59 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-3/question-bank/week-11-question-bank" data-quiz="week-11-question-bank"><span class="set-name">Week 11</span><span class="set-desc">Leukemias, myeloproliferative neoplasms, emergencies, chemotherapy, trial design.</span><span class="set-pg"><span class="pg-txt">50 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-3/question-bank/week-12-question-bank" data-quiz="week-12-question-bank"><span class="set-name">Week 12</span><span class="set-desc">Lymphadenopathy, lymphoma, myeloma, mediastinal mass, radiation therapy.</span><span class="set-pg"><span class="pg-txt">50 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
</ul>

<h2 class="section-title">Flowcharts</h2>
<ul class="sets">
<li><a class="set flow" href="/fom/block-3/flowcharts/anemia-workup-map"><span class="set-name">Anemia Workup Map</span><span class="set-desc">Full Week 9 workup from CBC to diagnosis.</span><span class="set-go">Open</span></a></li>
<li><a class="set flow" href="/fom/block-3/flowcharts/hemostasis-workup-map"><span class="set-name">Hemostasis Workup Map</span><span class="set-desc">Week 10: bleeding, platelets, VTE, anticoagulants, transfusion.</span><span class="set-go">Open</span></a></li>
<li><a class="set flow" href="/fom/block-3/flowcharts/myeloid-disorders-map"><span class="set-name">Myeloid Disorders Map</span><span class="set-desc">Week 11: high and low counts, MPNs, leukemias and emergencies.</span><span class="set-go">Open</span></a></li>
</ul>

<script>
(function(){
  const Q = [{"s": "week-9-question-bank", "n": 50, "b": 3, "t": "Week 9 Question Bank", "h": "fom/block-3/question-bank/week-9-question-bank"}, {"s": "week-10-question-bank", "n": 59, "b": 3, "t": "Week 10 Question Bank", "h": "fom/block-3/question-bank/week-10-question-bank"}, {"s": "week-11-question-bank", "n": 50, "b": 3, "t": "Week 11 Question Bank", "h": "fom/block-3/question-bank/week-11-question-bank"}, {"s": "week-12-question-bank", "n": 50, "b": 3, "t": "Week 12 Question Bank", "h": "fom/block-3/question-bank/week-12-question-bank"}];
  function stat(q){
    let d = null;
    try { d = JSON.parse(localStorage.getItem("differential-" + q.s) || "null"); } catch(e) {}
    let a = 0, c = 0;
    if (d && d.answers) for (const k in d.answers) {
      const r = d.answers[k];
      if (r && r.pick !== null && r.pick !== undefined) { a++; if (r.ok) c++; }
    }
    return {a: Math.min(a, q.n), c: c, u: (d && d.updatedAt) || ""};
  }
  function each(sel, fn){ document.querySelectorAll(sel).forEach(fn); }
  function run(){
    const sums = {all: {a: 0, n: 0}};
    let last = null;
    for (const q of Q) {
      const s = stat(q);
      sums[q.b] = sums[q.b] || {a: 0, n: 0};
      sums[q.b].a += s.a; sums[q.b].n += q.n; sums.all.a += s.a; sums.all.n += q.n;
      if (s.a && s.a < q.n && (!last || s.u > last.u)) last = {q: q, u: s.u};
      const row = document.querySelector('[data-quiz="' + q.s + '"]');
      if (!row) continue;
      q.href = row.getAttribute("href");
      row.querySelector(".pg-txt").textContent = !s.a ? q.n + " questions"
        : s.a < q.n ? s.a + " of " + q.n + " answered"
        : s.c + " of " + q.n + " correct";
      row.querySelector(".pg-bar i").style.width = (100 * s.a / q.n) + "%";
      row.querySelector(".set-go").textContent = !s.a ? "Start" : s.a < q.n ? "Continue" : "Review";
      row.classList.toggle("done", s.a >= q.n);
    }
    for (const k in sums) {
      const v = sums[k];
      each('[data-sum="' + k + '"]', el => { el.textContent = v.a ? v.a + " of " + v.n + " questions answered" : v.n + " questions, none answered yet"; });
      each('[data-sum-bar="' + k + '"]', el => { el.style.width = (v.n ? 100 * v.a / v.n : 0) + "%"; });
    }
    const el = document.getElementById("resume");
    if (el && last) { el.hidden = false; el.textContent = "Continue " + last.q.t; el.setAttribute("href", last.q.href || last.q.h); el.dataset.b = last.q.b; }
  }
  run();
  window.addEventListener("storage", run);
  window.addEventListener("pageshow", run);
})();
</script>
