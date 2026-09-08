# CampusPulse requirements

Name or team: Sana Al Ali

Date: 8/9/2026

Status: working draft

Use the source IDs `S1` to `S6` from the lab handout. Keep every requirement
short enough to test and trace.

## 1. Release scope

### In scope

List at least three capabilities that belong in the first release.

- University sign-in (SSO) for all students and group officers
- Verified group profiles, announcements, and events, with follow, RSVP, and audience visibility (public vs. members-only)
- Corrections to published event/announcement details, with notification to attendees
- Reporting, moderation (including immediate hide), and appeals

### Out of scope

List at least two explicit exclusions.

- Direct messages between users
- External (non-university) users and payments
- Native mobile app, video hosting, and AI-driven recommendations

## 2. User requirements

Write at least five customer-readable needs. Use one need per line and trace it
to the stakeholder evidence.

Format: `UR-1 [Must] ... [Source: S1]`

- UR-1 [Must] Students can RSVP to an event without their name appearing on a public attendee list unless they explicitly choose to share it. [Source: S1]
- UR-2 [Must] Students can browse and RSVP to events and announcements using a screen reader and on a phone browser. [Source: S1]
- UR-3 [Must] Multiple officers of a group can draft an announcement together, but only an approved officer can publish it. [Source: S2]
- UR-4 [Must] Students who RSVP'd to an event are told if its date, time, or location changes. [Source: S2]
- UR-5 [Must] A campus moderator can hide a reported event immediately, while a record of the report and the decision is kept for any appeal. [Source: S3]
- UR-6 [Must] A group only shows an official verified badge after Student Affairs has checked and approved it. [Source: S4]
- UR-7 [Must] A student's personal RSVP/attendance data is collected only where needed and removed within 30 days after an event is cancelled. [Source: S5]

## 3. Functional requirements

Write at least six observable system behaviours. Start each one with "The
system shall" and trace it to one or more user requirements.

Format: `FR-1 [Must] The system shall ... [Source: UR-1]`

- FR-1 [Must] The system shall hide an attendee's identity from other users on an event's attendee list by default. [Source: UR-1]
- FR-2 [Must] The system shall let an attendee opt in to show their name on an event's public attendee list. [Source: UR-1]
- FR-3 [Must] The system shall present event and announcement pages with screen-reader-compatible labels and keyboard/touch navigation. [Source: UR-2]
- FR-4 [Must] The system shall let any officer of a verified group edit a draft announcement but shall only let an officer with "approved publisher" permission publish it. [Source: UR-3]
- FR-5 [Must] The system shall notify every student who RSVP'd to an event when its date, time, or location is edited. [Source: UR-4]
- FR-6 [Must]

## 4. Non-functional requirements

Write at least four measurable quality requirements. State what is measured,
the target, and the condition under which the target applies. If you introduce
a number that is not in the handout, record it as an assumption or open
question in Section 8.

Format: `NFR-1 [Must] The system shall ... [Measure: target and condition] [Source: UR-1]`

- NFR-1 [Must] The system shall support at least 5,000 registered student accounts and 200 verified group accounts. [Measure: 5,000 students / 200 groups, active without account-creation failures; condition: during the Orientation Week pilot] [Source: UR-6]
- NFR-2 [Must] The system shall remove an event's personal RSVP/attendance records after cancellation. [Measure: fully removed within 30 days of cancellation, for 100% of cancelled events; condition: applies university-wide] [Source: UR-7]
- NFR-3 [Should] The system shall make its core pages usable with a screen reader. [Measure: WCAG 2.1 AA conformance on the browse, RSVP, and follow pages; condition: assumption — no accessibility standard given in the brief] [Source: UR-2]
- NFR-4 [Must] The system shall remove a hidden event from public listings promptly after a moderator's decision. [Measure: hidden within 5 minutes of the moderator's action; condition: assumption — no response-time target given in the brief] [Source: UR-5]

## 5. User stories and acceptance criteria

Write at least three stories from different stakeholder viewpoints. Each story
needs at least two acceptance criteria. Across the set, include a failure,
permission boundary, privacy rule, or other non-happy path.

### US-1 [Source: S?, UR-?]

As a student attendee,

I want my RSVP to stay off the public attendee list by default,

so that I'm not identified publicly just for RSVPing.

Acceptance criteria:

- Given I RSVP to an event and have not opted in to be shown, when another student views the event page, then my name does not appear in the attendee list.
- Given I later choose to opt in from my RSVP settings, when another student views the event page, then my name appears in the attendee list.

### US-2 [Source: S2, S6, UR-3]

As a group officer,

I want only approved officers to be able to publish an announcement,

so that a compromised or unapproved account can't post on the group's behalf.

Acceptance criteria:

- Given a draft announcement created by any officer, when an officer without "approved publisher" permission tries to publish it, then the system blocks the action and the announcement stays unpublished.
- Given an approved officer publishes the announcement, when it goes live, then the system records which officer published it and when.

### US-3 [Source: S3, UR-5]

As a campus moderator,

I want to hide a reported event immediately while keeping the evidence,

so that harmful content stops spreading but the group can still appeal the decision.

Acceptance criteria:

- Given a report on an event is confirmed, when I choose to hide it, then the event disappears from public listings within 5 minutes.
- Given an event has been hidden, when the group requests an appeal, then I can retrieve the original report, my reasoning, and my decision.
### US-4 [Source: S4, UR-6]

As a Student Affairs staff member,

I want to verify a group before it gets an official badge,

so that students can trust which groups are genuinely affiliated with the university.

Acceptance criteria:

- Given a group applies for verification, when I approve it, then the verified badge appears on that group's profile.
- Given a group has not been approved, then no verified badge is shown on its profile, regardless of its follower count or activity.


## 6. MoSCoW summary

List requirement or story IDs in every category. The Won't category must state
what is excluded from this release.

- Must: UR-1, UR-2, UR-3, UR-4, UR-5, UR-6, UR-7, FR-1, FR-2, FR-3, FR-4, FR-5, FR-6, FR-7, FR-8, FR-9, NFR-1, NFR-2, NFR-4, US-1, US-2, US-3, US-4
- Should: NFR-3
- Could: FR-10 (if you added the "filter events by category" idea — otherwise leave blank)
- Won't this release: Direct messages between users, non-university/external user accounts, payments, native mobile app, video hosting, and AI-driven event recommendations — excluded from the first release.


## 7. Traceability

Add at least four complete paths. Every row should connect evidence to a user
requirement, a system requirement, and a user story.

| Stakeholder need | User requirement | System requirement | User story |
|---|---|---|---|
| S1: don't publicise my RSVP unless I choose to | UR-1 | FR-1, FR-2 | US-1 |
| S2 / S6: only approved officers should publish | UR-3 | FR-4 | US-2 |
| S3: hide reported content fast, but keep evidence for appeals | UR-5 | FR-6, FR-7, NFR-4 | US-3 |
| S4: official badge must mean the group was checked | UR-6 | FR-8, NFR-1 | US-4 |

## 8. Assumptions and open questions

Separate decisions your team has assumed from questions that still need an
answer.

### Assumptions

- A1: We assume WCAG 2.1 AA as the accessibility target for screen-reader support (NFR-3), since the brief mentions screen-reader users but does not name a standard.
- A2: We assume a 5-minute maximum for a hidden event to disappear from public listings (NFR-4), since the brief gives no response-time target for moderation actions.

### Open questions

- Q1: What is the expected peak concurrent traffic during Orientation Week? The brief gives account totals (5,000 students, 200 groups) but no load/throughput figure, so NFR-1 currently targets account capacity rather than peak concurrent load.
- Q2: Can a de-identified moderation record (report, reason, decision — no attendee names) be retained past the 30-day RSVP-deletion window for appeal purposes? This needs sign-off from the Data Protection Officer (S5) to fully resolve Conflict 1 in stakeholders.md.
