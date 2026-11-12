---
title: "Block 2: Screening, cancer, aging and prescribing"
tags:
  - block-2
description: "Weeks 5 to 8. Adult screening, cancer, aging, therapeutics and prescribing."
---

<p class="block-about">Weeks 5 to 8. Adult screening, cancer, aging, therapeutics and prescribing.</p>

<p class="block-total"><span class="pg-bar wide" aria-hidden="true"><i data-sum-bar="2"></i></span><span data-sum="2"></span><a id="resume" class="resume" hidden></a></p>

<h2 class="section-title">Weekly question banks</h2>
<ul class="sets">
<li><a class="set" href="/fom/block-2/question-bank/week-5-question-bank" data-quiz="week-5-question-bank"><span class="set-name">Week 5</span><span class="set-desc">Autonomic pathways, Test performance.</span><span class="set-pg"><span class="pg-txt">46 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-2/question-bank/week-6-question-bank" data-quiz="week-6-question-bank"><span class="set-name">Week 6</span><span class="set-desc">Pathology reports, Cancer screening.</span><span class="set-pg"><span class="pg-txt">32 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-2/question-bank/week-7-question-bank" data-quiz="week-7-question-bank"><span class="set-name">Week 7</span><span class="set-desc">Localization, Lobes and grey matter.</span><span class="set-pg"><span class="pg-txt">53 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-2/question-bank/week-8-question-bank" data-quiz="week-8-question-bank"><span class="set-name">Week 8</span><span class="set-desc">Enzyme induction and inhibition, Drug interactions.</span><span class="set-pg"><span class="pg-txt">39 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
</ul>

<h2 class="section-title">Practice tests</h2>
<ul class="sets">
<li><a class="set" href="/fom/block-2/practice-tests/block-2-practice-exam" data-quiz="block-2-practice-exam"><span class="set-name">Practice Exam</span><span class="set-desc">Mixed questions from Weeks 5 to 8, exam style.</span><span class="set-pg"><span class="pg-txt">40 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
</ul>

<h2 class="section-title">Flowcharts</h2>
<ul class="sets">
<li><a class="set flow" href="/fom/block-2/flowcharts/cancer-workup-map"><span class="set-name">Cancer Workup Map</span><span class="set-desc">Week 6: breast mass, screening, pathology report, treatment, hereditary cancer, carcinogenesis.</span><span class="set-go">Open</span></a></li>
</ul>

<script>
(function(){
  const Q = [{"s": "week-5-question-bank", "n": 46, "b": 2, "t": "Week 5 Question Bank", "h": "fom/block-2/question-bank/week-5-question-bank"}, {"s": "week-6-question-bank", "n": 32, "b": 2, "t": "Week 6 Question Bank", "h": "fom/block-2/question-bank/week-6-question-bank"}, {"s": "week-7-question-bank", "n": 53, "b": 2, "t": "Week 7 Question Bank", "h": "fom/block-2/question-bank/week-7-question-bank"}, {"s": "week-8-question-bank", "n": 39, "b": 2, "t": "Week 8 Question Bank", "h": "fom/block-2/question-bank/week-8-question-bank"}, {"s": "block-2-practice-exam", "n": 40, "b": 2, "t": "Block 2 Practice Exam", "h": "fom/block-2/practice-tests/block-2-practice-exam"}];
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
