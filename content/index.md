---
title: "Nexus"
description: "Practice questions and flowcharts for Schulich Foundations of Medicine."
---

<section class="home-top">
<h1>Nexus</h1>
<p class="lede">New questions, generated with Claude for the class of 2030</p>
<p class="home-total"><span class="pg-bar wide" aria-hidden="true"><i data-sum-bar="all"></i></span><span data-sum="all"></span><a id="resume" class="resume" hidden></a></p>
</section>

<ul class="blocks">
<li><a class="block" data-b="1" href="/fom/block-1/"><span class="block-tag">Block 1</span><span class="block-main"><strong>Early life and foundations</strong><span>Weeks 1 to 4. 4 weekly banks, 3 practice tests</span></span><span class="block-pg"><span data-sum="1"></span><span class="pg-bar" aria-hidden="true"><i data-sum-bar="1"></i></span></span></a></li>
<li><a class="block" data-b="2" href="/fom/block-2/"><span class="block-tag">Block 2</span><span class="block-main"><strong>Screening, cancer, aging and prescribing</strong><span>Weeks 5 to 8. 4 weekly banks, 1 practice test, 1 flowchart</span></span><span class="block-pg"><span data-sum="2"></span><span class="pg-bar" aria-hidden="true"><i data-sum-bar="2"></i></span></span></a></li>
<li><a class="block" data-b="3" href="/fom/block-3/"><span class="block-tag">Block 3</span><span class="block-main"><strong>Hematology</strong><span>Weeks 9 to 12. 4 weekly banks, 3 flowcharts</span></span><span class="block-pg"><span data-sum="3"></span><span class="pg-bar" aria-hidden="true"><i data-sum-bar="3"></i></span></span></a></li>
<li><a class="block" data-b="4" href="/fom/block-4/"><span class="block-tag">Block 4</span><span class="block-main"><strong>Infection and immunity</strong><span>Weeks 13 to 15</span></span><span class="block-pg"><span>Coming soon</span></span></a></li>
</ul>

<script>
(function(){
  const Q = [{"s": "week-1-question-bank", "n": 17, "b": 1, "t": "Week 1 Question Bank", "h": "fom/block-1/question-bank/week-1-question-bank"}, {"s": "week-2-question-bank", "n": 165, "b": 1, "t": "Week 2 Question Bank", "h": "fom/block-1/question-bank/week-2-question-bank"}, {"s": "week-3-question-bank", "n": 98, "b": 1, "t": "Week 3 Question Bank", "h": "fom/block-1/question-bank/week-3-question-bank"}, {"s": "week-4-question-bank", "n": 80, "b": 1, "t": "Week 4 Question Bank", "h": "fom/block-1/question-bank/week-4-question-bank"}, {"s": "block-1-practice-test-1", "n": 50, "b": 1, "t": "Block 1 Practice Test 1", "h": "fom/block-1/practice-tests/block-1-practice-test-1"}, {"s": "block-1-practice-test-2", "n": 50, "b": 1, "t": "Block 1 Practice Test 2", "h": "fom/block-1/practice-tests/block-1-practice-test-2"}, {"s": "block-1-practice-test-3", "n": 50, "b": 1, "t": "Block 1 Practice Test 3", "h": "fom/block-1/practice-tests/block-1-practice-test-3"}, {"s": "week-5-question-bank", "n": 46, "b": 2, "t": "Week 5 Question Bank", "h": "fom/block-2/question-bank/week-5-question-bank"}, {"s": "week-6-question-bank", "n": 32, "b": 2, "t": "Week 6 Question Bank", "h": "fom/block-2/question-bank/week-6-question-bank"}, {"s": "week-7-question-bank", "n": 53, "b": 2, "t": "Week 7 Question Bank", "h": "fom/block-2/question-bank/week-7-question-bank"}, {"s": "week-8-question-bank", "n": 39, "b": 2, "t": "Week 8 Question Bank", "h": "fom/block-2/question-bank/week-8-question-bank"}, {"s": "block-2-practice-exam", "n": 40, "b": 2, "t": "Block 2 Practice Exam", "h": "fom/block-2/practice-tests/block-2-practice-exam"}, {"s": "week-9-question-bank", "n": 50, "b": 3, "t": "Week 9 Question Bank", "h": "fom/block-3/question-bank/week-9-question-bank"}, {"s": "week-10-question-bank", "n": 59, "b": 3, "t": "Week 10 Question Bank", "h": "fom/block-3/question-bank/week-10-question-bank"}, {"s": "week-11-question-bank", "n": 50, "b": 3, "t": "Week 11 Question Bank", "h": "fom/block-3/question-bank/week-11-question-bank"}, {"s": "week-12-question-bank", "n": 50, "b": 3, "t": "Week 12 Question Bank", "h": "fom/block-3/question-bank/week-12-question-bank"}];
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
