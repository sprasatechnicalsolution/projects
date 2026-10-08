# Sprasa WordPress Themes & Plugins

**Our own WordPress themes and plugins, built for Nepali sites and professionals**

![WordPress products overview](overview.jpg)

| | |
|---|---|
| **Client** | Our own products, used on client sites |
| **Type** | 2 WordPress themes and 5 plugins |
| **Year** | 2026 |
| **Status** | Products, running on the Sprasa Media news site |
| **Platform** | WordPress 6.4+ (tested up to 7.0), PHP 7.4 to 8.1 depending on product |

## Why we built them

Most WordPress sites in Nepal run a heavy theme plus a dozen plugins from different authors. They load slowly, break on updates, and handle Devanagari text badly. We built a small set of products that work together, load fast and handle Nepali properly.

Every product follows the same rules:

- **No upsell banners, no account, no phoning home.** Nothing contacts an outside server unless the site owner switches it on.
- **Sensible defaults.** The settings an expert would choose on day one are already set.
- **Nepali first.** Devanagari text is counted, trimmed and typeset correctly, and Bikram Sambat dates are supported.
- **Works on ordinary shared hosting.** No build step, no Composer and no extra PHP extensions are needed on the server.
- **Content outlives the theme.** Data lives in plugins, so changing the design never loses content.

| Product | Type | Version |
|---|---|---|
| [Sprasa News](#sprasa-news-theme) | News and magazine theme | 3.10 |
| [Sprasa Portfolio](#sprasa-portfolio-theme) | Multipurpose portfolio theme | 1.0 |
| [Sprasa Portfolio Core](#sprasa-portfolio-core-plugin) | Content plugin for the portfolio theme | 1.0 |
| [Sprasa SEO](#sprasa-seo-plugin) | SEO plugin, with Pro licence | 2.0 |
| [SprasaAds and SprasaAds Pro](#sprasaads-and-sprasaads-pro-plugins) | Ad manager plugin and add-on | 2.1 / 1.1 |
| [Sprasa Maintenance](#sprasa-maintenance-plugin) | Maintenance and coming-soon plugin | 1.0 |

---

## Sprasa News (theme)

A newspaper and magazine theme for busy Nepali and international news portals. It currently runs the Sprasa Media news site.

| Homepage | Article |
|---|---|
| ![Sprasa News homepage](screenshots/01-sprasa-news-home.jpg) | ![Sprasa News article page](screenshots/02-sprasa-news-article.jpg) |

| Category page | Mobile |
|---|---|
| ![Sprasa News category page](screenshots/03-sprasa-news-category.jpg) | ![Sprasa News on mobile](screenshots/04-sprasa-news-mobile.jpg) |

**For readers**
- Breaking news ticker and featured slider, both usable from the keyboard
- Mega menu that works by keyboard, not just mouse hover
- Live Ajax search, plus infinite scroll or a load-more button
- Reading progress bar, table of contents, author box and related posts
- Dark mode that does not flash white when the page loads
- Nepali (Devanagari) typography, a Bikram Sambat date in the header, and full right-to-left support

**For the newsroom**
- Magazine homepage builder: choose a hero layout and how each category block looks (lead, grid, list or carousel)
- Article layout screen: pick the article header style and switch sections on or off and reorder them
- Unlimited ad placements, managed from a built-in Ad Manager
- Several header and footer layouts, sticky header and sticky sidebar
- Newsletter sign-up with spam protection
- One-click demo content to start a new site fast

**Under the hood**
- Theme options built on WordPress's own Settings API, with no third-party framework
- theme.json v3 design system with classic PHP templates, so block patterns and page builders both work
- Schema.org structured data for news articles
- Built to meet Core Web Vitals and WCAG 2.2 accessibility from the start
- Optional Nepali Patro calendar and Nepali Unicode converter integrations, each with its own on/off switch, endpoint and cache setting
- Works with Gutenberg, Classic Editor, Elementor, WooCommerce, Yoast, Rank Math, AIOSEO, SEOPress, WPML, Polylang, AMP and the major cache plugins

| Homepage blocks | Article layout |
|---|---|
| ![Homepage block layouts](screenshots/05-sprasa-news-homepage-blocks.jpg) | ![Article layout settings](screenshots/06-sprasa-news-article-layout.jpg) |

| Theme options | API integrations |
|---|---|
| ![Theme options panel](screenshots/07-sprasa-news-theme-options.jpg) | ![Nepali Patro and Unicode integrations](screenshots/08-sprasa-news-api-integrations.jpg) |

---

## Sprasa Portfolio (theme)

One theme for any professional: developer, engineer, designer, doctor, teacher, student, freelancer, consultant or agency. The whole site is built from the WordPress admin, with no PHP, CSS or JavaScript to edit.

| Projects | Project page |
|---|---|
| ![Portfolio projects page](screenshots/09-sprasa-portfolio-projects.jpg) | ![Single project page](screenshots/10-sprasa-portfolio-project-page.jpg) |

- 13 homepage sections you can switch on, drag into order and rename
- 7 design presets, each with matched light and dark colours
- Light, dark and follow-the-device colour modes
- 8 font stacks, with separate heading and body fonts, or no web fonts at all
- Profile type (engineer, doctor, teacher and so on) sets suitable labels, and a business mode turns "About me" into "About us"
- Built-in contact form that works even without JavaScript, with spam protection and optional reCAPTCHA v3
- Settings export, import and reset, plus demo content that can be removed in one click
- Accessibility: skip link, visible focus, keyboard navigation and reduced-motion support
- SEO: Open Graph, Twitter cards, Person and Organization schema and breadcrumbs, and it steps aside automatically when Yoast, Rank Math, AIOSEO or SEOPress is active

| Dashboard and setup checklist | Tools |
|---|---|
| ![Portfolio admin dashboard](screenshots/11-sprasa-portfolio-dashboard.jpg) | ![Export, import and demo content](screenshots/12-sprasa-portfolio-tools.jpg) |

## Sprasa Portfolio Core (plugin)

The companion plugin that holds the content, while the theme holds the design. Because projects and profile data live in a plugin, switching themes never makes them disappear.

![Projects managed by Portfolio Core](screenshots/13-portfolio-core-projects.jpg)

- **Projects** with categories, technologies, gallery, client, dates, live link and source link
- **Services** with categories, icon, price and link
- **Experience** and **Education** with date ranges and institutions
- **Testimonials** with position, company and star rating
- **Certifications** with issuer, credential ID and verification link
- **Achievements** with a number, suffix and icon

---

## Sprasa SEO (plugin)

Everything a site actually needs for SEO, with the defaults an SEO consultant would set on day one. The site owner answers four setup questions and rarely needs the settings again.

| Content report | Search appearance |
|---|---|
| ![SEO content report](screenshots/14-sprasa-seo-content-report.jpg) | ![Title and description templates](screenshots/15-sprasa-seo-search-appearance.jpg) |

![Sitemap, schema and analytics settings](screenshots/16-sprasa-seo-sitemap-schema.jpg)

**Free**
- Titles and meta descriptions with templates, per-page overrides and a live Google preview
- Facebook, X, LinkedIn and WhatsApp share previews, with a warning when the image will break
- One clean Schema.org (JSON-LD) graph per page: Organization or Person, WebSite, WebPage, Article and breadcrumbs
- XML sitemap at `/sitemap.xml` with images, a readable stylesheet and every noindex setting respected
- Ten content checks that each name a real problem
- Content report that lists pages missing a description or share image, or that are too short, worst first
- Breadcrumbs, a robots.txt editor and Google Analytics 4 (your own visits excluded)
- Import from Yoast SEO, Rank Math or All in One SEO without deleting anything
- Tells you plainly when a page will not appear in Google, and why
- Counts and trims Nepali and Hindi text correctly

**Pro (licence key)**
- Redirect manager with CSV import
- 404 monitoring
- Local SEO
- If our licence server is unreachable, Pro keeps working for 14 days, so a customer's redirects never switch off because of our outage

---

## SprasaAds and SprasaAds Pro (plugins)

Simple image ads for editors: pick an image, choose where it goes, see how it performs.

| All ads | Add new ad |
|---|---|
| ![SprasaAds ad list](screenshots/17-sprasaads-all-ads.jpg) | ![Create an ad](screenshots/18-sprasaads-new-ad.jpg) |

| Analytics | Import / export |
|---|---|
| ![Impressions, clicks and CTR](screenshots/19-sprasaads-analytics.jpg) | ![Import and export ads as JSON](screenshots/20-sprasaads-import-export.jpg) |

**SprasaAds**
- Image ads from the Media Library, image rows (2 to 4 side by side), or AdSense / HTML code
- Placements: site header, before / inside / after the article, sidebar, footer, or manual only
- Place ads anywhere with a block or a shortcode
- Impressions, clicks and CTR for 7, 30 or 90 days with a daily chart
- Weighting when several ads share one spot, and pause / publish / duplicate in one click
- Fast: one database query per page instead of one per ad spot, and scripts only load on pages that show an ad
- Private: stores two numbers per ad per day, with no cookies, IP addresses or personal data
- Covered by automated tests (PHPUnit) and static analysis (PHPStan)

**SprasaAds Pro**
- Target by device (desktop, tablet, mobile), logged-in state, user role, post type and category or tag
- A/B testing with weighted variants and click-through rate for each variant
- Rules stack: an ad shows only when every rule passes

---

## Sprasa Maintenance (plugin)

Closes a site to the public while work is done, without hurting search rankings and without locking the owner out.

| Dashboard | Access control |
|---|---|
| ![Maintenance dashboard](screenshots/21-maintenance-dashboard.jpg) | ![Who can see the live site](screenshots/22-maintenance-access-control.jpg) |

![Design settings](screenshots/23-maintenance-design.jpg)

**Five templates, all fully editable**

| Classic | Countdown | Split screen |
|---|---|---|
| ![Classic template](screenshots/24-maintenance-template-classic.jpg) | ![Countdown template](screenshots/25-maintenance-template-countdown.jpg) | ![Split screen template](screenshots/26-maintenance-template-split.jpg) |

| Aurora glass | Terminal |
|---|---|
| ![Aurora glass template](screenshots/27-maintenance-template-aurora.jpg) | ![Terminal template](screenshots/28-maintenance-template-terminal.jpg) |

- Edit colours, fonts, sizes, background image or gradient, logo, overlay and custom CSS on every template
- Correct search engine handling: "503 with Retry-After" for maintenance, normal "200" for a coming-soon launch page
- Countdown timer, progress bar, subscribe form, contact block and social links, each optional
- Email sign-ups saved to their own table, with CSV export
- Scheduling, with automatic switch-off when the window ends
- Access by role, user, IP address or IP range, plus a secret bypass link for clients and testers
- Exclude paths with wildcards, and keep REST, AJAX and feeds open if needed
- Works even when the active theme is broken

---

## Also on WordPress

- [AdForge and SprasaSocial](../media-advertising-tools/): an enterprise ad manager for high-traffic news sites on the tagDiv Newspaper theme, and a Facebook comments plugin
- [Fastkhabar Online and Nepal Sandes](../nepali-news-websites/) news portals
- [Nepali Unicode Converter](../unicode-nepali/) as a WordPress shortcode, with English URL slugs for Nepali titles

## Technology

WordPress 6.4+, PHP 7.4 to 8.1, theme.json v3, WordPress Settings API and REST API, Gutenberg blocks, Schema.org JSON-LD, PHPUnit and PHPStan.

---

**Built by Pradip Subedi · Sprasa Technical Solution**
Need a WordPress site, theme or plugin? [Get in touch](../README.md#contact).
