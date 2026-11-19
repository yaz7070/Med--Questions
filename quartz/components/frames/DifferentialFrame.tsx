import { PageFrame, PageFrameProps } from "./types"
import HeaderConstructor from "../Header"
import { pathToRoot } from "../../util/path"

const Header = HeaderConstructor()

// Top navigation: one link per block. Paths are relative to the site root,
// so links work at any address (GitHub Pages subpath, a custom domain, or localhost).
const NAV: [string, string, number][] = [
  ["Block 1", "fom/block-1/", 1],
  ["Block 2", "fom/block-2/", 2],
  ["Block 3", "fom/block-3/", 3],
  ["Block 4", "fom/block-4/", 4],
]

// The Flagged tab shows how many questions are flagged. Quizzes write the list to
// localStorage ("differential-anki"), so the count updates as soon as you flag one.
const ANKI_COUNT = `(function(){
  function n(){ try{ var d=JSON.parse(localStorage.getItem("differential-anki")||"null"); return d&&d.cards?d.cards.length:0; }catch(e){ return 0; } }
  function show(){ var el=document.getElementById("anki-count"); if(!el) return; var k=n(); el.textContent=k?String(k):""; el.hidden=!k; }
  show(); addEventListener("storage", show); addEventListener("pageshow", show);
})();`

// The block you are in is highlighted, including on its quiz and flowchart pages.
function activeTab(slug: string): string | undefined {
  if (slug.startsWith("flagged/")) return "flagged/"
  return NAV.find(([, path]) => slug.startsWith(path))?.[1]
}

/**
 * Nexus site frame: no sidebars, a top bar for navigation, search and
 * theme toggle, full-width content, and a site footer with credits and a
 * disclaimer.
 */
export const DifferentialFrame: PageFrame = {
  name: "differential",
  render({ componentData, header, beforeBody, pageBody: Content, afterBody, footer }: PageFrameProps) {
    const year = new Date().getFullYear()
    const root = pathToRoot(componentData.fileData.slug!)
    const [First, ...rest] = header
    const current = activeTab(componentData.fileData.slug ?? "")
    return (
      <>
        <div class="center full-width differential">
          <div class="page-header">
            <Header {...componentData}>
              {First && <First {...componentData} />}
              <nav class="site-nav" aria-label="Main">
                <ul>
                  {NAV.map(([, path, b]) => (
                    <li>
                      <a
                        href={`${root}/${path}`}
                        data-b={b}
                        aria-label={`Block ${b}`}
                        class={path === current ? "active" : undefined}
                        aria-current={path === current ? "page" : undefined}
                      >
                        <span class="nav-word">Block </span>
                        {b}
                      </a>
                    </li>
                  ))}
                  <li>
                    <a
                      href={`${root}/flagged/`}
                      class={current === "flagged/" ? "anki active" : "anki"}
                      aria-current={current === "flagged/" ? "page" : undefined}
                    >
                      Flagged<span class="anki-count" id="anki-count" hidden></span>
                    </a>
                  </li>
                </ul>
              </nav>
              {rest.map((HeaderComponent) => (
                <HeaderComponent {...componentData} />
              ))}
            </Header>
            <div class="popover-hint">
              {beforeBody.map((BodyComponent) => (
                <BodyComponent {...componentData} />
              ))}
            </div>
          </div>
          <Content {...componentData} />
          <div class="page-footer">
            {afterBody.map((BodyComponent) => (
              <BodyComponent {...componentData} />
            ))}
          </div>
          {footer.map((FooterComponent) => (
            <FooterComponent {...componentData} />
          ))}
          <script dangerouslySetInnerHTML={{ __html: ANKI_COUNT }} />
          <footer class="site-footer">
            <p class="credit">
              Built by <strong>Yazdaan Ahmad</strong> and <strong>Mohammad Essa</strong>, Schulich School of Medicine
              &amp; Dentistry, MD Class of 2030. © {year}
            </p>
            <p class="disclaimer">
              For study use only. This site is not medical advice and is not an official Schulich or
              Western University resource. Questions and notes come from student summaries and practice
              quizzes and may contain errors. Always check against your lectures, course materials and
              current guidelines.
            </p>
          </footer>
        </div>
      </>
    )
  },
}
