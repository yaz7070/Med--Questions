import { PageFrame, PageFrameProps } from "./types"
import HeaderConstructor from "../Header"

const Header = HeaderConstructor()

/**
 * Differential site frame: no sidebars, a top bar for navigation, search and
 * theme toggle, full-width content, and a site footer with credits and a
 * disclaimer.
 */
export const DifferentialFrame: PageFrame = {
  name: "differential",
  render({ componentData, header, beforeBody, pageBody: Content, afterBody, footer }: PageFrameProps) {
    const year = new Date().getFullYear()
    return (
      <>
        <div class="center full-width differential">
          <div class="page-header">
            <Header {...componentData}>
              {header.map((HeaderComponent) => (
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
              Differential was built by <strong>Yazdaan Ahmad</strong>, Schulich School of Medicine
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
