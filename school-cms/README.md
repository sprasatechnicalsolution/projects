# School & College CMS

**Website, content management and admissions CRM for schools and colleges in Nepal**

![School CMS overview](overview.jpg)

| | |
|---|---|
| **Client** | Schools and colleges in Nepal |
| **Type** | Institutional website + CMS + lightweight CRM |
| **Year** | 2026 |
| **Status** | Research, requirements, architecture and database design complete; build in progress |
| **Platform** | Web, runs on cPanel shared hosting |

## The problem

We studied many school and college websites. The same gaps came up again and again: notices buried or outdated, no real search, galleries left to a Facebook embed, and admissions enquiries lost in phone calls. Staff also struggle with hosting space once photos and PDFs pile up.

## What we're building

A system that lets non-technical staff publish everything a school needs, while the public website updates itself.

## Key features

**Notices (top priority)**
- Title in English and Nepali, category, image, PDF and multiple attachments
- Publish, effective and expiry dates; pinned and urgent flags
- Expired notices drop off the website automatically; urgent ones get a badge
- Short notices open in a pop-up; longer ones get their own page
- Categories: Admission, Examination, Holiday, Scholarship, Result, Academic, Tender, Vacancy and more

**Content**
- News with scheduling and SEO fields
- Events that show only upcoming dates and update their own status
- Gallery albums with lightbox, lazy loading and filters
- Academic programmes, faculty with department filter, and a downloads centre

**Admissions CRM**
- An "Apply" or "Inquire" button on every admission page feeds the CRM
- Lead stages: New → Contacted → Interested → Application started → Submitted → Admitted / Rejected
- Follow-up dates, reminders, notes and assigned staff
- General enquiries inbox

**Platform**
- Roles: Super Admin, Administrator, Editor, Admission Officer, Staff, with permissions stored in the database
- English and Nepali stored as real fields, not machine translation
- Optional Google Drive storage for photos, PDFs and videos, without visitors ever seeing a Drive link
- Built to load fast on shared hosting and on 3G phones

## Technology

| Area | Used |
|---|---|
| Backend | PHP 8.2+, no build step in production |
| Database | MySQL |
| Storage | Local or Google Drive |
| Hosting | Upload to cPanel and import one SQL file |

---

**Built by Pradip Subedi · Sprasa Technical Solution**
Want this for your school or college? [Get in touch](../README.md#contact).
