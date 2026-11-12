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

// The block you are in is highlighted, including on its quiz and flowchart pages.
function activeTab(slug: string): string | undefined {
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
                  {NAV.map(([label, path, b]) => (
                    <li>
                      <a
                        href={`${root}/${path}`}
                        data-b={b}
                        class={path === current ? "active" : undefined}
                        aria-current={path === current ? "page" : undefined}
                      >
                        {label}
                      </a>
                    </li>
                  ))}
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
