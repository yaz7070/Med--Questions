---
title: "Block 1: Early life and foundations"
tags:
  - block-1
description: "Weeks 1 to 4. Tasks of a physician, the human body, early life, the well child and adolescent."
---

<p class="block-about">Weeks 1 to 4. Tasks of a physician, the human body, early life, the well child and adolescent.</p>

<p class="block-total"><span class="pg-bar wide" aria-hidden="true"><i data-sum-bar="1"></i></span><span data-sum="1"></span><a id="resume" class="resume" hidden></a></p>

<h2 class="section-title">Weekly question banks</h2>
<ul class="sets">
<li><a class="set" href="/fom/block-1/question-bank/week-1-question-bank" data-quiz="week-1-question-bank"><span class="set-name">Week 1</span><span class="set-desc">Ethical frameworks, Physician-patient models, Bias and equity.</span><span class="set-pg"><span class="pg-txt">17 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-1/question-bank/week-2-question-bank" data-quiz="week-2-question-bank"><span class="set-name">Week 2</span><span class="set-desc">Cells, tissues, physiology, NMJ, anatomy, imaging and study design.</span><span class="set-pg"><span class="pg-txt">165 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-1/question-bank/week-3-question-bank" data-quiz="week-3-question-bank"><span class="set-name">Week 3</span><span class="set-desc">Genetics &amp; Prenatal, Development &amp; Milestones, Attachment &amp; Theory.</span><span class="set-pg"><span class="pg-txt">98 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-1/question-bank/week-4-question-bank" data-quiz="week-4-question-bank"><span class="set-name">Week 4</span><span class="set-desc">Immunology &amp; Vaccines, Childhood Behaviour &amp; ADHD, Genetic &amp; Medical Conditions.</span><span class="set-pg"><span class="pg-txt">80 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
</ul>

<h2 class="section-title">Practice tests</h2>
<ul class="sets">
<li><a class="set" href="/fom/block-1/practice-tests/block-1-practice-test-1" data-quiz="block-1-practice-test-1"><span class="set-name">Practice Test 1</span><span class="set-desc">Mixed questions from Weeks 1 to 4, exam style.</span><span class="set-pg"><span class="pg-txt">50 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-1/practice-tests/block-1-practice-test-2" data-quiz="block-1-practice-test-2"><span class="set-name">Practice Test 2</span><span class="set-desc">Mixed questions from Weeks 1 to 4, exam style.</span><span class="set-pg"><span class="pg-txt">50 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
<li><a class="set" href="/fom/block-1/practice-tests/block-1-practice-test-3" data-quiz="block-1-practice-test-3"><span class="set-name">Practice Test 3</span><span class="set-desc">Mixed questions from Weeks 1 to 4, exam style.</span><span class="set-pg"><span class="pg-txt">50 questions</span><span class="pg-bar" aria-hidden="true"><i></i></span></span><span class="set-go">Start</span></a></li>
</ul>

<script>
(function(){
  const Q = [{"s": "week-1-question-bank", "n": 17, "b": 1, "t": "Week 1 Question Bank", "h": "fom/block-1/question-bank/week-1-question-bank"}, {"s": "week-2-question-bank", "n": 165, "b": 1, "t": "Week 2 Question Bank", "h": "fom/block-1/question-bank/week-2-question-bank"}, {"s": "week-3-question-bank", "n": 98, "b": 1, "t": "Week 3 Question Bank", "h": "fom/block-1/question-bank/week-3-question-bank"}, {"s": "week-4-question-bank", "n": 80, "b": 1, "t": "Week 4 Question Bank", "h": "fom/block-1/question-bank/week-4-question-bank"}, {"s": "block-1-practice-test-1", "n": 50, "b": 1, "t": "Block 1 Practice Test 1", "h": "fom/block-1/practice-tests/block-1-practice-test-1"}, {"s": "block-1-practice-test-2", "n": 50, "b": 1, "t": "Block 1 Practice Test 2", "h": "fom/block-1/practice-tests/block-1-practice-test-2"}, {"s": "block-1-practice-test-3", "n": 50, "b": 1, "t": "Block 1 Practice Test 3", "h": "fom/block-1/practice-tests/block-1-practice-test-3"}];
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
