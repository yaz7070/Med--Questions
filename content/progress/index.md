---
title: "Progress"
description: "Your progress across every question bank and practice test."
---

Your progress across every question bank and practice test. It reads what you have answered in this browser.

<div class="prog" id="prog">
<section class="prog-hero">
<div class="prog-num"><span id="p-ans">0</span><span class="prog-of">/ 779</span></div>
<p class="prog-label">questions answered</p>
<div class="prog-bar" aria-hidden="true"><span id="p-bar"></span></div>
<p class="prog-stats" id="p-stats">Start any question bank and your progress shows here.</p>
</section>
<div id="p-blocks"></div>
</div>

<script>
(function(){
  const QUIZZES = [{"b": 1, "slug": "block-1-practice-test-1", "title": "Block 1 Practice Test 1", "n": 50, "href": "/Med-School/fom/block-1/practice-tests/block-1-practice-test-1", "kind": "test"}, {"b": 1, "slug": "block-1-practice-test-2", "title": "Block 1 Practice Test 2", "n": 50, "href": "/Med-School/fom/block-1/practice-tests/block-1-practice-test-2", "kind": "test"}, {"b": 1, "slug": "block-1-practice-test-3", "title": "Block 1 Practice Test 3", "n": 50, "href": "/Med-School/fom/block-1/practice-tests/block-1-practice-test-3", "kind": "test"}, {"b": 1, "slug": "week-1-question-bank", "title": "Week 1 Question Bank", "n": 17, "href": "/Med-School/fom/block-1/question-bank/week-1-question-bank", "kind": "quiz"}, {"b": 1, "slug": "week-2-question-bank", "title": "Week 2 Question Bank", "n": 165, "href": "/Med-School/fom/block-1/question-bank/week-2-question-bank", "kind": "quiz"}, {"b": 1, "slug": "week-3-question-bank", "title": "Week 3 Question Bank", "n": 98, "href": "/Med-School/fom/block-1/question-bank/week-3-question-bank", "kind": "quiz"}, {"b": 1, "slug": "week-4-question-bank", "title": "Week 4 Question Bank", "n": 80, "href": "/Med-School/fom/block-1/question-bank/week-4-question-bank", "kind": "quiz"}, {"b": 2, "slug": "block-2-practice-exam", "title": "Block 2 Practice Exam", "n": 40, "href": "/Med-School/fom/block-2/practice-tests/block-2-practice-exam", "kind": "test"}, {"b": 2, "slug": "week-5-question-bank", "title": "Week 5 Question Bank", "n": 46, "href": "/Med-School/fom/block-2/question-bank/week-5-question-bank", "kind": "quiz"}, {"b": 2, "slug": "week-6-question-bank", "title": "Week 6 Question Bank", "n": 32, "href": "/Med-School/fom/block-2/question-bank/week-6-question-bank", "kind": "quiz"}, {"b": 2, "slug": "week-7-question-bank", "title": "Week 7 Question Bank", "n": 53, "href": "/Med-School/fom/block-2/question-bank/week-7-question-bank", "kind": "quiz"}, {"b": 2, "slug": "week-8-question-bank", "title": "Week 8 Question Bank", "n": 39, "href": "/Med-School/fom/block-2/question-bank/week-8-question-bank", "kind": "quiz"}, {"b": 3, "slug": "week-10-question-bank", "title": "Week 10 Question Bank", "n": 59, "href": "/Med-School/fom/block-3/question-bank/week-10-question-bank", "kind": "quiz"}];
  const NAMES = {"1": "Early life and foundations", "2": "Screening, cancer, aging and prescribing", "3": "Hematology", "4": "Infection and immunity"};
  function read(slug){
    try { return JSON.parse(localStorage.getItem("differential-" + slug) || "null"); } catch(e) { return null; }
  }
  function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;"); }
  function render(){
    const root = document.getElementById("p-blocks");
    if (!root) return;
    let ans = 0, ok = 0, total = 0, started = 0;
    const byBlock = {};
    for (const q of QUIZZES) {
      const d = read(q.slug);
      let a = 0, c = 0;
      if (d && d.answers) for (const k in d.answers) {
        const r = d.answers[k];
        if (r && r.pick !== null && r.pick !== undefined) { a++; if (r.ok) c++; }
      }
      a = Math.min(a, q.n);
      ans += a; ok += c; total += q.n; if (a) started++;
      (byBlock[q.b] = byBlock[q.b] || []).push(Object.assign({a, c}, q));
    }
    document.getElementById("p-ans").textContent = ans;
    document.getElementById("p-bar").style.width = (total ? 100 * ans / total : 0) + "%";
    document.getElementById("p-stats").textContent = ans
      ? Math.round(100 * ans / total) + "% of all questions. " + ok + " correct (" + Math.round(100 * ok / ans) + "%). " + started + " of " + QUIZZES.length + " sets started."
      : "Start any question bank and your progress shows here.";
    root.innerHTML = Object.keys(byBlock).map(b => {
      const list = byBlock[b];
      const ba = list.reduce((s, x) => s + x.a, 0), bt = list.reduce((s, x) => s + x.n, 0);
      return `<h2 class="section-title">Block ${b}: ${esc(NAMES[b])} <span class="prog-sub">${ba} / ${bt}</span></h2>
        <ul class="rows">${list.map(x => `<li><a class="row prog-row" href="${x.href}"><span><strong>${esc(x.title)}</strong>
        <span class="prog-mini"><i style="width:${100 * x.a / x.n}%"></i></span>
        <span class="desc">${x.a ? x.a + " of " + x.n + " answered, " + x.c + " correct" : x.n + " questions, not started"}</span></span>
        <span class="prog-pct">${Math.round(100 * x.a / x.n)}%</span></a></li>`).join("")}</ul>`;
    }).join("");
  }
  render();
  document.addEventListener("nav", render);
  window.addEventListener("storage", render);
})();
</script>
