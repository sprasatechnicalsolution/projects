# Sprasa Travel

**Online travel agency platform: flight search, booking, payment and e-tickets, plus a full agency back office**

![Sprasa Travel overview](overview.jpg)

| | |
|---|---|
| **Client** | Sprasa Travel, Kathmandu |
| **Type** | Online travel agency (OTA) platform |
| **Year** | 2026 |
| **Status** | Built and demo-ready; airline supplier connection pending |
| **Platform** | Web (customer site, customer account, admin) |

## The client's problem

A travel agency that books flights by phone and messaging apps loses customers at night and on holidays, re-types every booking, and checks payments by hand. They wanted customers to book and pay online with the same trust as a big booking site.

## What we built

A complete booking flow, from search to ticket:

```
Search → Select → Re-check fare with airline → Passengers → Booking reference
      → Reserve seat (PNR) → Pay → Payment verified → Ticket → Email/SMS + PDF
```

### Customer site

| Home and flight search | Results with filters |
|---|---|
| ![Home](screenshots/01-home.jpg) | ![Results](screenshots/02-results.jpg) |

| Fare re-checked before booking | Passenger details |
|---|---|
| ![Fare updated](screenshots/03-fare-updated.jpg) | ![Booking](screenshots/04-booking.jpg) |

| Payment (seats held, PNR shown) | QR payment with receipt upload |
|---|---|
| ![Payment](screenshots/05-payment.jpg) | ![QR payment](screenshots/06-qr-payment.jpg) |

| Ticket issued | My Booking (guest lookup) |
|---|---|
| ![Ticket issued](screenshots/07-ticket-issued.jpg) | ![My booking](screenshots/08-my-booking.jpg) |

The e-ticket PDF:

![E-ticket](screenshots/17-e-ticket-pdf.jpg)

### Admin dashboard

| Dashboard | Bookings with PNR and profit |
|---|---|
| ![Dashboard](screenshots/09-admin-dashboard.jpg) | ![Bookings](screenshots/10-admin-bookings.jpg) |

| Booking detail | Verifying a QR payment |
|---|---|
| ![Booking detail](screenshots/11-admin-booking-detail.jpg) | ![Payment verification](screenshots/12-admin-payment-verification.jpg) |

| Flight providers | Markup rules |
|---|---|
| ![Providers](screenshots/13-admin-providers.jpg) | ![Markups](screenshots/14-admin-markups.jpg) |

| Sales and profit reports | Integration health |
|---|---|
| ![Reports](screenshots/15-admin-reports.jpg) | ![Integrations](screenshots/16-admin-integrations.jpg) |

### On a phone

| Home | Results | My booking |
|---|---|---|
| ![Mobile home](screenshots/m1-home.jpg) | ![Mobile results](screenshots/m2-results.jpg) | ![Mobile booking](screenshots/m3-my-booking.jpg) |

## Key features

- Flight search with filters and sorting, and a fare re-check with the airline before booking
- Payment by eSewa, Khalti, QR (with receipt upload and staff approval) or bank transfer
- Prices, taxes, markup and payment amounts are worked out on the server, never in the browser
- A real airline PNR is shown only when a supplier returns one; the agency's own reference is `ST-20261006-A8K92`
- E-ticket PDF sent by email and SMS
- Admin: bookings, payment verification, supplier setup, markup rules, sales/cost/profit reports
- Health checks for flights, payments, email and SMS connections
- Unpaid seat holds expire automatically

## Technology

| Area | Used |
|---|---|
| Frontend | React 19, Vite, TypeScript, Tailwind CSS |
| Backend | Laravel 12 REST API (PHP 8.3), queues and scheduler |
| Database | PostgreSQL 16, Redis |
| Payments | eSewa, Khalti, QR, bank transfer |
| Flight suppliers | Pluggable: Travelport, Sabre, Amadeus, local consolidators |
| Hosting | Docker |

---

*All bookings, PNRs and payments in the screenshots are demo data.*

**Built by Pradip Subedi · Sprasa Technical Solution**
Want something similar for your business? [Get in touch](../README.md#contact).
